import cv2
import cv2.cv as cv

if __name__ == '__main__':
    import sys

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    cam = cv2.VideoCapture(0)

    while True:
        ret, img = cam.read()
        rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30,30), flags=cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) != 0:
            rects[:,2:] += rects[:,:2]

        copy = img.copy()
        for x1,y1,x2,y2 in rects:
            cv2.rectangle(copy, (x1,y1), (x2,y2), (0, 150, 222), 3)


        cv2.imshow('la fache', copy)

        if 0xFF & cv2.waitKey(5) == 27: #exit on 'Esc'
            break

    cv2.destroyAllWindows()

