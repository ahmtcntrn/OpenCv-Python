import cv2

kamera=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
kayit=cv2.VideoWriter("kayit.avi",fourcc,20,(640,480))

while(kamera.isOpened()):
    ret , video=kamera.read()
    if ret==True:
        video = cv2.flip(video, 1) ##kamerayı normal ayarında açan kod sıfır yazarsan ters açar
        kayit.write(video)
        cv2.imshow("kayit",video)
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
kamera.release()
kayit.release()
cv2.destroyAllWindows()