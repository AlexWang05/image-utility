import os
import pydicom
import png
import skimage
import matplotlib.pyplot as plt
import nibabel as nib
from PIL import Image

'''
Convert input formats to desired output format
'''
class FormatConverter:
    def __init__(self, input_folder='./', output_folder='./'):
        self.input_folder = input_folder
        self.output_folder = output_folder
    
    '''
    Converts DICOM files in folder to PNG
    '''
    def dicom_to_png(self):
        # loop through all files in input folder
        for filename in os.listdir(self.input_folder):
            # check if file is a DICOM file
            if filename.endswith('.dcm'):
                new_name = filename.replace('.dcm', '.png')
                
                dicom_file = open(os.path.join(self.input_folder, filename), 'rb')
                png_file = open(os.path.join(self.output_folder, new_name), 'wb')
                
                # Extracting data from the mri file
                plan = pydicom.read_file(dicom_file)
                shape = plan.pixel_array.shape

                image_2d = []
                max_val = 0
                for row in plan.pixel_array:
                    pixels = []
                    for col in row:
                        pixels.append(col)
                        if col > max_val: max_val = col
                    image_2d.append(pixels)

                # Rescaling grey scale between 0-255
                image_2d_scaled = []
                for row in image_2d:
                    row_scaled = []
                    for col in row:
                        col_scaled = int((float(col) / float(max_val)) * 255.0)
                        row_scaled.append(col_scaled)
                    image_2d_scaled.append(row_scaled)

                # Writing the PNG file
                w = png.Writer(shape[1], shape[0], greyscale=True)
                w.write(png_file, image_2d_scaled)

                print('Converted ' + filename + ' to ' + new_name)

                png_file.close()
    
    '''
    Converts MHA files in folder to PNG
    '''
    def mha_to_png(self):
        # loop through all files in input folder
        for filename in os.listdir(self.input_folder):
            # check if file is a MHA file
            if filename.endswith('.mha'):
                mha_path = os.path.join(self.input_folder, filename)
                new_name = filename.replace('.mha', '')

                # mha is a 3D image, so saving 2D slices to directory
                out_path = os.path.join(self.output_folder, new_name)
                if not os.path.exists(out_path):
                    os.mkdir(out_path)

                img = skimage.io.imread(fname=mha_path, plugin='simpleitk')
                
                
                for slicer in range(0, img.shape[0]):
                    plt.imsave(out_path + '/' + filename+ '_' + str(slicer) + '.png', img[slicer], cmap='gray',format='png')

                print('Converted ' + filename + ' to PNG slices at ' + self.output_folder)

    def nifti_to_png(self):
        # loop through all files in input folder
        for filename in os.listdir(self.input_folder):
            # check if file is a NIFTI file
            if filename.endswith('.nii.gz'):
                nifti_path = os.path.join(self.input_folder, filename)
                new_name = filename.replace('.nii.gz', '')

                # print(nifti_path, new_name)

                img = nib.load(os.path.join(self.input_folder, filename))
                data = img.get_fdata()

                out_path = os.path.join(self.output_folder, new_name)
                if not os.path.exists(out_path):
                    os.mkdir(out_path)

                # nifti is a 3D image, so saving 2D slices to directory
                for i in range(data.shape[2]): #x is the sequence of images
                    slice = data[:, :, i]

                    plt.imsave(out_path + '/' + filename+ '_' + str(i) + '.png', slice, cmap='gray',format='png')

                print('Converted ' + filename + ' to PNG slices at ' + out_path)

    def jpg_to_png(self):
        # loop through all files in input folder
        for filename in os.listdir(self.input_folder):
            # check if file is a JPG file
            if filename.endswith('.jpg'):
                new_name = filename.replace('.jpg', '.png')

                img = Image.open(os.path.join(self.input_folder, filename))
                img.save(os.path.join(self.output_folder, new_name))

                print('Converted ' + filename + ' to ' + new_name)

if __name__ == '__main__':
    # format: (input_dir, output_dir)
    # converter = FormatConverter('./MHA', './PNG')
    # converter = FormatConverter('./NIFTI', './PNG')
    converter = FormatConverter('./JPG', './PNG')
    
    # converter.dicom_to_png()
    # converter.mha_to_png()
    # converter.nifti_to_png()
    converter.jpg_to_png()
