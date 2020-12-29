import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import cv2


K=4
img=plt.imread("kmean_image.jpg")
img=cv2.resize(img,(160,160),interpolation = cv2.INTER_AREA)
print(type(img))
print(img.shape)
width=img.shape[0]
height=img.shape[1]
img=img.reshape(width*height,3)
kmeans=KMeans(n_clusters=K).fit(img)
labels=kmeans.predict(img)
clusters=kmeans.cluster_centers_

img_init=np.zeros_like(img)
for i in range(len(img_init)):
	img_init[i]=clusters[labels[i]]

img_after=img_init.reshape(width,height,3)

print(type(img_after))

plt.imshow(img_after)
plt.show()