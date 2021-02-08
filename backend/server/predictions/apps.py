from django.apps import AppConfig

from .prediction import Predictor


class PredictionsConfig(AppConfig):
    name = 'predictions'
    prediction = Predictor()

