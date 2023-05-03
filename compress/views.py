from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import io
import base64

def index(request):
    return render(request, 'index.html')

def compress(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = Image.open(image_file)
        image = image.resize((800, 600))
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG', quality=70)
        compressed_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return render(request, 'index.html', {'compressed_image': compressed_image})
    else:
        return render(request, 'index.html')