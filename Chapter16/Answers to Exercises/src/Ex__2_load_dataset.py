#!/usr/bin/env python

"""Ex__2_load_dataset.py: Answer to Ch 16 Ex 2."""

from tensorflow.keras import datasets
import matplotlib.pyplot as plt

def load_dataset():
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

    # Normalize pixel values to the range 0-1
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return train_images, train_labels, test_images, test_labels
    
def plot_samples(train_images, train_labels):
    class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
                   'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    plt.figure(figsize=(14,7))
    for i in range(60):
        plt.subplot(5,12,i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(train_images[i])
        plt.xlabel(class_names[train_labels[i][0]])
        
    plt.show()

if __name__ == '__main__':
    train_images, train_labels, test_images, test_labels = load_dataset()
    plot_samples(train_images, train_labels)
