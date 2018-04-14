import sys
import pandas as pd
import numpy as np

from keras.models import load_model
from keras.preprocessing import image

model = load_model('model.h5')

X_test = pd.read_csv("./data/train.csv")

X_test = X_test.drop(labels=["label"], axis=1)
X_test = X_test / 255.0

# Reshape the 1D array into 4D
reshaped_data = X_test.values.reshape(-1,28,28,1)

image_index = int(sys.argv[1])

image_data = np.array(reshaped_data[image_index])

prediction = model.predict_classes(image_data.reshape(1,28,28,1))[0]

print("The number is most likely a {}".format(prediction))