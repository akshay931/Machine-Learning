import cv2 as cv
img = cv.imread('charA.png',0)
row,col = img.shape
thresh, im_bw = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
cv.imwrite('binary.png',im_bw)
print('binary.png black and white image saved  \nextracted binary data from image saved as binary.txt')
with open('binary.txt','w') as output:
    for i in range(row):
        output.write('\n')
        for j in range(col):
            if(im_bw[i][j]==255):
                im_bw[i][j]=1
                output.write('1 ')
            else:
                im_bw[i][j]=0
                output.write('0 ')

cv.waitKey(0)
