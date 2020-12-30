import cv2

#wrapped everything inside a function
def detectFaceInImage(image):
	face_cascade = cv2.CascadeClassifier("Cascades\\haarcascade_frontalface_default.xml")
	img = cv2.imread(image)
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
	for x,y,w,h in faces:
		img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 1)
	return img

detect_face1 = detectFaceInImage("Images\\singleface.jpg")
detect_face2 = detectFaceInImage("Images\\multiface.jpg")

resized = cv2.resize(detect_face2, (int(detect_face2.shape[1]*2), int(detect_face2.shape[0]*2)))

cv2.imshow("Face detection1", detect_face1)
cv2.imshow("Face detection2", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


#create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#reading the image as it is
img = cv2.imread("multiface.jpg")

#reading the image as grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

#drawing the rectangle in faces
for x,y,w,h in faces:
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 1)

#resizing the image before desplaying
resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))

#displaying the image
cv2.imshow("Face detection", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()