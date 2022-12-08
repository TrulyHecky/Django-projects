from django.shortcuts import render
from .forms import ConverterForm
from .models import Converter

def index(request):
    form = ConverterForm()
    context = {
        "form": form
    }
    return render(request, "app/index.html", context)
