import csv
import os

'''
Annotates CSV file given folders of images and corresponding labels (input folder)

Label: 0 = normal, 1 = COVID-19, 2 = non-COVID-19 infections

Precondition: all images in directory are under one label
'''
class Annotator:
    def __init__(self, csv_path='./annotations.csv'):
        self.csv_path = csv_path
        
        if not os.path.isfile(csv_path):
            with open(csv_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['filename', 'label'])
    
    # append labels for all images in directory
    def append_files(self, input_dir, label_num):
        with open(self.csv_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # loop through all files in input folder
            for filename in os.listdir(input_dir):
                    # write filename and label to csv
                    writer.writerow([filename, label_num])
                    print('Annotated ' + filename + ' with label ' + str(label_num))
        print('Finished annotating ' + input_dir)
    
if __name__ == '__main__':
    annotator = Annotator()
    annotator.append_files('./JPG', 1)  # appends all images in JPG folder with label 1 (COVID)
