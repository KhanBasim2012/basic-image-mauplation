import cv2
import matplotlib.pyplot as plt

image = cv2.imread("vertical-shot-some-beautiful-trees-sun-setting-background.jpg")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap="grey")
plt.title("Grey Image")
plt.title("grey Scale Image")
plt.show()

cropped_image = image[100:800, 200:1000]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()