import cv2
import numpy as np

# Görüntüyü yükle (image klasöründeki bir görüntü)
image_path = 'image/girdi_goruntu.jpg'
image = cv2.imread(image_path)

# Görüntüyü gri tonlamalı hale getir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenarları tespit et
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Hough Dönüşümünü uygulayarak doğruları tespit et
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Tespit edilen doğruları çiz
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Sonuç görüntüsünü göster
cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
