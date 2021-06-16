import cv2 
import numpy as np 
import matplotlib.pyplot as plt
 
def edge_detection(image): 
    edges_detected = cv2.Canny(image , 100, 200) #playaround with these values, change 100 to 50,70 etc and 200 to 150,250 etc
    images = [image , edges_detected]
    location = [121, 122] 
    for loc, edge_image in zip(location, images): 
        plt.subplot(loc) 
        plt.imshow(edge_image, cmap='gray')
        plt.show()

    

img = cv2.imread('''Put Image name here''', 0)

# call edge_detection using img from above line as parameter
edge_detection(img)
 
