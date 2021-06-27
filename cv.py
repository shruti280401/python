import cv2
# img = cv2.imread("demo-image2.png")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("output1.avi")
# while True:
#     success , img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     success , img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#     break


# import numpy as np
# img = cv2.imread("demo-image2.png")
# kernel = np.ones((5,5))
# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray,(7,7),0) #to blur image
# imgcanny = cv2.Canny(img,170,200)   #detect ages
# imgdial = cv2.dilate(imgcanny,kernel,iterations=1) #make img ages thicker
# imgerode = cv2.erode(imgdial,kernel,iterations=1) #make img ages thinner
# # cv2.imshow("gray image",imggray)
# cv2.imshow("canny image",imgcanny)
# cv2.imshow("dialation image",imgdial)
# cv2.imshow("erode image",imgerode)
# cv2.waitKey(0)

## RESIZING THE IMAGE
#img = cv2.imread("demo-image2.png")
#print(img.shape) #gives dimension of img(ht,width,bgr)
#imgresize = cv2.resize(img,(900,500)) #resizeimg(width,ht)
#cv2.imshow("image",img)
#cv2.imshow("resize img",imgresize)
#print(imgresize.shape)
#for cropping image
#imgcropped = img[0:800,200:500] #hight,width
# cv2.imshow("cropped image",imgcropped)
# cv2.waitKey(0)

## TEXT AND SHAPES
# import numpy as np
# img = np.zeros((512,512,3)) #dimensions of pixels of img
#print(img)
#cv2.imshow("img",img)
#img[200:500] = 255,0,0 #coloring image
# cv2.line(img,(0,0),(300,300),(0,250,0),3) #(start pt,end pt,color,thickness),thickness not necessary
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)#filled used to fill color not necessary
# cv2.circle(img,(400,50),30,(255,255,0),5)#centre,radius,color,thickness
# cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_DUPLEX,1,(0,225,50),1)#text,origin,font,scale,color,thickness
# cv2.imshow("img",img)
# cv2.waitKey(0)


##WARP PERSPECTIVE
# import numpy as np
# img = cv2.imread("demo-image2.png")
# wd,ht = 250,350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[wd,0],[0,ht],[wd,ht]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgoutput=cv2.warpPerspective(img,matrix,(wd,ht))
# cv2.imshow("img",imgoutput)
# cv2.waitKey(0)

##join images
# import numpy as np
# img = cv2.imread("demo-image2.png")
#
# imghor = np.hstack((img,img))
# imgver = np.vstack((img,img))
# #cv2.imshow("horizontal",imghor)
# cv2.imshow("vertical",imgver)
# cv2.waitKey(0)

##COLOR DETECTION
