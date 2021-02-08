from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render

from .apps import PredictionsConfig
from .forms import UploadImageForm


def predict(request):
    preview_image = predictions = None

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES.get('image')
            print(type(uploaded_image))

            # process image
            predictions, preview_image = PredictionsConfig.prediction.predict(uploaded_image)

            file_buffer = BytesIO()
            preview_image.save(file_buffer, 'jpeg')
            preview_image = InMemoryUploadedFile(file_buffer, None, 'foo.jpg', 'image/jpeg', None, None)

    else:
        form = UploadImageForm()

    return render(request, 'predictions/index.html', {
        'form': form,
        'predictions': predictions,
        'uploaded_image': preview_image
    })
