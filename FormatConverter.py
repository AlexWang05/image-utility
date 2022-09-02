import os
import pydicom
import png

'''
Convert input formats to desired output format
'''
class FormatConverter:
    def __init__(self, input_folder='./', output_folder='./'):
        self.input_folder = input_folder
        self.output_folder = output_folder
    
    '''
    Converts a single DICOM file to PNG
    '''
    def dicom_to_png(self):
        # loop through all files in input folder
        for filename in os.listdir(self.input_folder):
            # check if file is a DICOM file
            if filename.endswith('.dcm'):
                dicom_file = open(os.path.join(self.input_folder, filename), 'rb')
                png_file = open(os.path.join(self.output_folder, filename), 'wb')

                # mri_to_png(mri_file, png_file)
                
                # Extracting data from the mri file
                # plan = pydicom.read_file(dicom_file)
                # shape = plan.pixel_array.shape

                # image_2d = []
                # max_val = 0
                # for row in plan.pixel_array:
                #     pixels = []
                #     for col in row:
                #         pixels.append(col)
                #         if col > max_val: max_val = col
                #     image_2d.append(pixels)

                # # Rescaling grey scale between 0-255
                # image_2d_scaled = []
                # for row in image_2d:
                #     row_scaled = []
                #     for col in row:
                #         col_scaled = int((float(col) / float(max_val)) * 255.0)
                #         row_scaled.append(col_scaled)
                #     image_2d_scaled.append(row_scaled)

                # # Writing the PNG file
                # w = png.Writer(shape[1], shape[0], greyscale=True)
                # w.write(png_file, image_2d_scaled)

                # png_file.close()



if __name__ == '__main__':
    converter = FormatConverter('./DICOM', './PNG')  # input_dir, output_dir
    converter.dicom_to_png()
