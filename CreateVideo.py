import os
import cv2


path = "photosForByjus"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (size))
#out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*"mp4"), 5, size)

#for i in range(0,count-1):
for i in range(count-1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()

