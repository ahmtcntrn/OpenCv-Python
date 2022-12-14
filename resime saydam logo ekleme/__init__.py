import cv2
import numpy as np
img1=cv2.imread("messi.jpg")
img2=cv2.imread("logo.jpg")
satir,sutun,kanal=img2.shape
roi=img1[0:satir,0:sutun]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,25,255,cv2.THRESH_BINARY)#25-255 arasını resimden sil sildiği yerleri beyaz yapar
mask_inv=cv2.bitwise_not(mask)#0-25 arasını resimden sil
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
son_resim=cv2.addWeighted(img1_bg,img2_fg)
img1[0:satir,0:sutun]=son_resim
cv2.imshow("gri",img2gray)
cv2.imshow("sonresim",son_resim)
cv2.imshow("mask",mask)
cv2.imshow("mask_inv",mask_inv)
cv2.imshow("img1_bg",img1_bg)
cv2.imshow("img2_fg",img2_fg)
cv2.imshow("montaj",img1)
cv2.waitKey()
cv2.destroyAllWindows()