from PIL import Image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array, smart_resize


class Predictor:
    def __init__(self):
        self.model = VGG16()

    def labels_to_percents(self, labels):
        """
        Attach percents to labels
        """
        return [[x[1], round(x[2] * 100, 2)] for x in labels[0]]

    def predict(self, uploaded_image):
        """
        Read image and predict category
        """
        image = Image.open(uploaded_image).copy()
        uploaded_image.seek(0)

        # convert the image pixels to a numpy array
        image = img_to_array(image)

        # resize for vgg16
        image = smart_resize(image, (224, 224))

        # reshape data for the model
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

        # prepare the image for the VGG model
        image = preprocess_input(image)

        # predict the probability across all output classes
        what = self.model.predict(image)

        # convert the probabilities to class labels
        labels = decode_predictions(what, top=3)

        # make it readable
        labels = self.labels_to_percents(labels)

        return labels
