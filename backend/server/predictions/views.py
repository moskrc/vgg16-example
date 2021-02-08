from django.shortcuts import render

from .apps import PredictionsConfig
from .forms import UploadImageForm


def predict(request):
    uploaded_image = predictions = None

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES.get('image')

            predictions = PredictionsConfig.prediction.predict(uploaded_image)
    else:
        form = UploadImageForm()

    return render(request, 'predictions/index.html', {
        'form': form,
        'predictions': predictions,
        'uploaded_image': uploaded_image
    })
