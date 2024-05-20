import numpy as np
import cv2

def prewitt_edge_detection(image):
    # Gri tonlamalı görüntüyü elde et
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Prewitt çekirdeklerini tanımla
    prewitt_kernel_x = np.array([[-1, 0, 1],
                                  [-1, 0, 1],
                                  [-1, 0, 1]])
    
    prewitt_kernel_y = np.array([[-1, -1, -1],
                                  [0, 0, 0],
                                  [1, 1, 1]])
    
    # Görüntüyü x ve y yönlerinde türevle
    gradient_x = cv2.filter2D(gray_image, -1, prewitt_kernel_x)
    gradient_y = cv2.filter2D(gray_image, -1, prewitt_kernel_y)
    
    # Kenar yoğunluğunu ve yönünü hesapla
    edge_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))
    edge_direction = np.arctan2(gradient_y, gradient_x)
    
    return edge_magnitude, edge_direction

# Görüntüyü yükle
image = cv2.imread('/Users/zehragokceaynaci/Documents/VsCode Projects/imageProcessing/image/picture.png')

# Prewitt kenar belirleme algoritmasını uygula
edges, direction = prewitt_edge_detection(image)

# Sonucu göster
cv2.imshow('Prewitt Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()