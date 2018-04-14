# Number reader

Playing around with MNIST and CNN networks.

Based on the work of [Yassine Ghouzam](https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)

To download training and validation data run `kaggle competitions download -c digit-recognizer -p ./data`

Train the model using `train.py` optionally pass the numbers of epochs as the first arguments, e.g. `python3 train.py 5` (train using epochs=5). Default is 2.

The model achieves accuracy of .984 after 2 epochs.

```
Epoch 1/2
 - 159s - loss: 0.4434 - acc: 0.8570 - val_loss: 0.0631 - val_acc: 0.9793
Epoch 2/2
 - 162s - loss: 0.1282 - acc: 0.9623 - val_loss: 0.0516 - val_acc: 0.9848
```

## Utils

*Show image*

You can open the image representation of a number using `show_image.py [row_index]`, e.g. `python3 show_image.py 5` will open the 5th row in the dataset and convert it into its image representation

*Predict*

You can predict the number of a data row using `predict.py [row_index]`, e.g. `python3 predict.py 5` will predict what number the 5th row in the dataset is