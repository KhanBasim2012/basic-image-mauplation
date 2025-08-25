import cv2
import matplotlib.pyplot as plt

image = cv2.imread("closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.title("BGR Image")
plt.show()

grey_image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
plt.imshow(grey_image)
plt.title("Grey Image", cmap='grey')
plt.title("Grayscale Image")
plt.show()