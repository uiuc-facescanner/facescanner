import cv2
import os

# args: imgpath, output imgpath, cascPath
#TODO scanned_originals
def numfaces(imagePath):
    #imagePath = "static/photos_orig/face1.jpg"
    #cascPath = sys.argv[2]

    faceCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    scale = 1.2 #smaller scale, smaller face

    faces = faceCascade.detectMultiScale(gray,scaleFactor=scale,minNeighbors=5,minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

    #count faces!
    count = 0;
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h), (0, 255, 0), 2)
        count = count + 1
    print "faces detected:",count

    #if file exists, append/increment number
    fileCount = 1
    while os.path.exists("static/photos_scanned/result%s.jpg" % fileCount):
        fileCount += 1

    #save processed image
    cv2.imwrite("static/photos_scanned/result%s.jpg" % fileCount, image);
    return count
