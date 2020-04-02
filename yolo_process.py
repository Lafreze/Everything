import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_images = '/datas/images/'
path_labels = 'O/data/labels/'
path_data = '/data_wafer/datas/'
# Percentage of images to be used for the test set
percentage_test = 15;

# Create and/or truncate train.txt and test.txt
file_train = open(path_data + 'train.txt', 'w')
file_test = open(path_data + 'test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(path_images, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(path_images + title + '.jpg' + "\n")
        #file_test.write(path_labels + title + '.txt' + "\n")
    else:
        file_train.write(path_images + title + '.jpg' + "\n")
        #file_train.write(path_labels + title + '.txt' + "\n")
        counter = counter + 1

print("ok")
