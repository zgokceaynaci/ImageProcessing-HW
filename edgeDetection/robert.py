
import numpy as np
import cv2

def roberts_edge_detection(image):
    # Gri tonlamalı görüntüyü elde etme
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Robert çekirdeklerini tanımlama
    roberts_kernel_x = np.array([[1, 0],
                                  [0, -1]])
    
    roberts_kernel_y = np.array([[0, 1],
                                  [-1, 0]])
    
    # Görüntüyü x ve y yönlerinde türevleme
    gradient_x = cv2.filter2D(gray_image, -1, roberts_kernel_x)
    gradient_y = cv2.filter2D(gray_image, -1, roberts_kernel_y)
    
    # Kenar yoğunluğunu ve yönünü hesapla
    edge_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))
    edge_direction = np.arctan2(gradient_y, gradient_x)
    
    return edge_magnitude, edge_direction

# Görüntüyü yükleme
image = cv2.imread('/image/picture.png')

# Roberts kenar belirleme algoritmasını uygulama
edges, direction = roberts_edge_detection(image)

# Sonucu gösterme
cv2.imshow('Roberts Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()