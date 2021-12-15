__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 16, Exercise 4

Create a program using the TensorFlow library that trains the CNN developed in [Exercise 3](Ex__3_create_network.md) and test the resulting model using the CIFAR-10 test images. Determine the percentage of test images that the CNN classifies correctly.

# Answer
See the python file [Ex__4_train_model.py](src/Ex__4_train_model.py) for the code to create, train, and test the CNN model.

To execute the program, assuming **python** is installed and is in your path, execute the command **python Ex__4_train_model.py**

**Note:** You can ignore any warning messages about not having a GPU present if your system doesn't have one. The code will execute on the system processor if a GPU is not configured for use with TensorFlow.

Your results should indicate an accuracy of approximately 70%. For such a simple CNN, this is a tremendous improvement over the accuracy of random guessing, which would be 10%.

This is the output of a test run:
```C:\>Ex__4_train_model.py
2021-12-12 17:55:19.402677: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-12-12 17:55:19.802026: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1525] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 3617 MB memory:  -> device: 0, name: Quadro P2200, pci bus id: 0000:01:00.0, compute capability: 6.1
Epoch 1/10
2021-12-12 17:55:21.475358: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8301
1563/1563 [==============================] - 9s 5ms/step - loss: 1.5032 - accuracy: 0.4521 - val_loss: 1.2326 - val_accuracy: 0.5559
Epoch 2/10
1563/1563 [==============================] - 7s 5ms/step - loss: 1.1306 - accuracy: 0.5996 - val_loss: 1.0361 - val_accuracy: 0.6318
Epoch 3/10
1563/1563 [==============================] - 8s 5ms/step - loss: 0.9704 - accuracy: 0.6589 - val_loss: 1.0053 - val_accuracy: 0.6517
Epoch 4/10
1563/1563 [==============================] - 7s 5ms/step - loss: 0.8831 - accuracy: 0.6904 - val_loss: 0.8999 - val_accuracy: 0.6883
Epoch 5/10
1563/1563 [==============================] - 7s 5ms/step - loss: 0.8036 - accuracy: 0.7177 - val_loss: 0.8924 - val_accuracy: 0.6956
Epoch 6/10
1563/1563 [==============================] - 7s 5ms/step - loss: 0.7514 - accuracy: 0.7374 - val_loss: 0.9180 - val_accuracy: 0.6903
Epoch 7/10
1563/1563 [==============================] - 7s 5ms/step - loss: 0.7020 - accuracy: 0.7548 - val_loss: 0.8755 - val_accuracy: 0.7074
Epoch 8/10
1563/1563 [==============================] - 7s 5ms/step - loss: 0.6599 - accuracy: 0.7694 - val_loss: 0.8505 - val_accuracy: 0.7116
Epoch 9/10
1563/1563 [==============================] - 8s 5ms/step - loss: 0.6180 - accuracy: 0.7842 - val_loss: 0.8850 - val_accuracy: 0.7058
Epoch 10/10
1563/1563 [==============================] - 8s 5ms/step - loss: 0.5825 - accuracy: 0.7943 - val_loss: 0.8740 - val_accuracy: 0.7128
313/313 - 1s - loss: 0.8740 - accuracy: 0.7128 - 648ms/epoch - 2ms/step

===============================
| Validation accuracy: 71.28% |
===============================
```