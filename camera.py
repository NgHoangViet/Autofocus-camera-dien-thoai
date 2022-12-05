import numpy as np
import cv2
import matplotlib.pyplot as plt

pictures = []
sums = []

for i in range(5, 6):
    pictures.append(i)
    img = cv2.imread("p" + str(i) + ".jpg", 0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    # cv2.imwrite('sobelx.jpg', sobelx)
    # cv2.imwrite('sobely.jpg', sobely)
    # sobel = sobelx + sobely
    # cv2.imwrite('sobel.jpg', sobel)

    gvals = np.sqrt(sobelx * sobelx + sobely * sobely)
    gvals = gvals.flatten()
    # Lấy phần tử khác 0
    gvals = gvals[gvals != 0]

    median = np.median(gvals)
    print(str(i) + " - MEDIAN = ","%.2f" % median)

    gvals = gvals[gvals > median]

    print("    SUM    = ", "%.2f" % np.sum(gvals))
    sums.append(np.sum(gvals))


pictures = np.array(pictures)
sums = np.array(sums)

print("pictures: ", pictures)
print("sums: ", sums)
print("Ảnh ", sums.argmax()+1, " có độ nét cao nhất.", )

plt.plot(pictures, sums)
plt.yscale('linear')
plt.xlabel("Ảnh thứ i")
plt.ylabel("Giá trị tổng")
plt.title("Kết quả")
plt.show()