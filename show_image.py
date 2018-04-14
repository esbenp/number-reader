import sys
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

X_train = pd.read_csv("./data/train.csv")

X_train = X_train.drop(labels=["label"], axis=1)
X_train = X_train / 255.0

reshaped_data = X_train.values.reshape(-1,28,28,1)

image_index = int(sys.argv[1])

image_data = reshaped_data[image_index]

plt.imsave("tmp.jpg", image_data[:,:,0], cmap="gray")
img = Image.open("tmp.jpg")
img.show()