import os
import json
import cv2
from random import randint

TEST_FLAG   = False
IMAGE_DIR   = '/output/'

CLASSES = ['Car', 'Bus', 'Truck', 'Svehicle', 'Pedestrian',\
    'Motorbile', 'Bicycle', 'Train', 'Signal', 'Signs']

KEEP_CLASSES = ['Car', 'Truck', 'Pedestrian',\
    'Bicycle', 'Signal', 'Signs']
COLORS  = {key: (randint(0,256), randint(0,256), randint(0,256)) for key in KEEP_CLASSES}

def get_txts(root):
    files   = []
    for fname in os.listdir(root):
        ext = os.path.splitext(fname)[1]
        if ext == '.txt':
            files.append(os.path.join(root, fname))
    return files

def read_boxes(txt_file):
    boxes   = {}
    with open(txt_file) as fi:
        for line in fi:
            line    = line.rstrip().split()
            if len(line) == 6:
                class_num   = int(line[4])
                class_name  = CLASSES[class_num]
                left    = int(line[0])
                top     = int(line[1])
                right   = int(line[2])
                bot     = int(line[3])
                if class_name in KEEP_CLASSES:
                    if class_name not in boxes:
                        boxes[class_name]   = [[left, top, right, bot]]
                    else:
                        boxes[class_name].append([left, top, right, bot])

    if TEST_FLAG:
        fname   = os.path.split(txt_file)[1]
        img_name = os.path.splitext(fname)[0] + '.jpg'
        image   = cv2.imread(os.path.join(IMAGE_DIR, img_name))
        for class_name, boxes_ in boxes.items():
            for x1, y1, x2, y2 in boxes_:
                cv2.rectangle(image, (x1,y1), (x2,y2), COLORS[class_name])
        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('image', image)
        k = cv2.waitKey(0)
        if k == ord('q'):
            cv2.destroyAllWindows()
            exit()
    return boxes

def convert(root):
    json_string = {}
    files   = get_txts(root)
    for txt_file in files:
        fname   = os.path.split(txt_file)[1]
        img_name = os.path.splitext(fname)[0] + '.jpg'
        boxes   = read_boxes(txt_file)
        json_string[img_name]  = boxes
    json.dump(json_string, open(IMAGE_DIR+'predict_025.json','w'), indent=4)
    print('done')




if __name__ == '__main__':
    convert(IMAGE_DIR)
