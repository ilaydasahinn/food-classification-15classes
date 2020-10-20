# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jLQ4Pz-cWpPxnLVfoMuqgQ0n6ch7n7_2
"""

!pip install tflite-model-maker

import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tensorflow_examples.lite.model_maker.core.data_util.image_dataloader import ImageClassifierDataLoader
from tensorflow_examples.lite.model_maker.core.task import image_classifier
from tensorflow_examples.lite.model_maker.core.task.model_spec import mobilenet_v2_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec import ImageModelSpec

import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

image_path = '/content/drive/My Drive/DietApp/Resized'

data = ImageClassifierDataLoader.from_folder(image_path)

train_data, test_data = data.split(0.8)

model = image_classifier.create(train_data)

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='.', with_metadata=True)

