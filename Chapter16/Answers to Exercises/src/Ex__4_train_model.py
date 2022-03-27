#!/usr/bin/env python

"""Ex__4_train_model.py: Answer to Ch 16 Ex 4."""

from tensorflow.keras import datasets, layers, models, optimizers, losses
import matplotlib.pyplot as plt

def load_dataset():
    (train_images, train_labels), \
        (test_images, test_labels) = \
        datasets.cifar10.load_data()

    # Normalize pixel values to the range 0-1
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return train_images, train_labels, \
           test_images, test_labels
    
def create_model():
    # Each image is 32x32 pixels with 3 RGB color planes
    image_shape = (32, 32, 3)

    # The convolutional filter kernel size is 3x3 pixels
    conv_filter_size = (3, 3)

    # Number of convolutional filters in each layer
    filters_layer1 = 32
    filters_layer2 = 64
    filters_layer3 = 64

    # Perform max pooling over 2x2 pixel regions
    pooling_size = (2, 2)

    # Number of neurons in each of the dense layers
    hidden_neurons = 64
    output_neurons = 10

    model = models.Sequential([
        # First convolutional layer followed by max pooling
        layers.Conv2D(filters_layer1, conv_filter_size,
            activation='relu', input_shape=image_shape),
        layers.MaxPooling2D(pooling_size),

        # Second convolutional layer followed by max pooling
        layers.Conv2D(filters_layer2, conv_filter_size,
            activation='relu'),
        layers.MaxPooling2D(pooling_size),

        # Third convolutional layer followed by flattening
        layers.Conv2D(filters_layer3, conv_filter_size,
            activation='relu'),
        layers.Flatten(),

        # Dense layer followed by the output layer
        layers.Dense(hidden_neurons, activation='relu'),
        layers.Dense(output_neurons)
    ])

    model.compile(optimizer=optimizers.Adam(),
        loss=losses.SparseCategoricalCrossentropy(
            from_logits=True), metrics=['accuracy'])

    return model

def train_model(train_images, train_labels, \
                test_images, test_labels, model):
    history = model.fit(train_images, train_labels,
        epochs=10, validation_data=(test_images, test_labels))

    test_loss, test_acc = model.evaluate(test_images,
        test_labels, verbose=2)

    return history, test_acc

def plot_model_accuracy(history):
    plt.figure()
    plt.plot(history.history['accuracy'], label='Accuracy')
    plt.plot(history.history['val_accuracy'],
        label = 'Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    train_images, train_labels, test_images, \
        test_labels = load_dataset()
    model = create_model()
    history, test_acc = train_model(train_images, \
        train_labels, test_images, test_labels, model)
    print()
    print('='*31)
    print('| Validation accuracy: {:.2f}% |'.
          format(100*test_acc))
    print('='*31)
    plot_model_accuracy(history)
