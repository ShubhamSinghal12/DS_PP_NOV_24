import cv2


img = cv2.imread("./dog.png")
# new_img = img[:,:,::-1]
# new_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# new_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)


cv2.imshow('Dog Image',img)
# cv2.imshow('Gray Dog Image',gray)

cv2.waitKey(5000) # Program will stop when any key is pressed
cv2.destroyAllWindows()