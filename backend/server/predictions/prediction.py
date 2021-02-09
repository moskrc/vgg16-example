from typing import List

import numpy as np
from PIL import Image
from django.core.files.uploadedfile import TemporaryUploadedFile
from keras.preprocessing.image import img_to_array, smart_resize
from keras.applications.nasnet import NASNetLarge, decode_predictions, preprocess_input


class Predictor:
    def __init__(self):
        self.model = NASNetLarge()

    def labels_to_percents(self, labels) -> List:
        """
        Attach percents to labels
        """
        return [[x[1], round(x[2] * 100, 2)] for x in labels[0]]

    def predict(self, uploaded_image: TemporaryUploadedFile) -> (List, Image):
        """
        Read image and predict category
        """
        # convert the image pixels to a numpy array
        image = img_to_array(Image.open(uploaded_image))

        # resize (crop) to vgg16 size (331, 331, 3)
        image = smart_resize(image, (331, 331))

        # grab a RGB preview for frontend
        rgb_preview = Image.fromarray(np.uint8(image)).convert('RGB')

        # reshape data for the model, add new axis (1, 224, 224, 3)
        image = np.expand_dims(image, axis=0)

        # prepare the image for the VGG model (subtracts the mean RGB channels)
        image = preprocess_input(image)

        # predict the probability across all output classes
        what = self.model.predict(image)

        # convert the probabilities to class labels
        labels = decode_predictions(what, top=3)

        # make it readable
        labels = self.labels_to_percents(labels)

        return labels, rgb_preview
