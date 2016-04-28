import cv2

def numfaces():
    imagePath = sys.argv[1]
    cascPath = sys.argv[2]
    count = 0;

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    scale = 1.2 #smaller scale, smaller face

    faces = faceCascade.detectMultiScale(gray,scaleFactor=scale,minNeighbors=5,minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)


    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h), (0, 255, 0), 2)
        count = count + 1

    return count

