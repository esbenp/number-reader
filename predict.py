import pandas as pd
import numpy as np

from keras.models import load_model
from keras.preprocessing import image

model = load_model('model.h5')

X_test = pd.read_csv("./data/train.csv")

X_test = X_test.drop(labels=["label"], axis=1)
X_test = X_test / 255.0

seven = np.array(X_test.values[509])

# Reshape the 1D array into 4D
as_4d = seven.reshape(1,28,28,1)

prediction = model.predict_classes(as_4d)[0]

print("The number is most likely a {}".format(prediction))