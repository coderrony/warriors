from django.shortcuts import render
from .models import Parts
# Create your views here.


def spareParts(request):
    parts = Parts.objects.all()
    return render(request, 'parts.html', context={'parts': parts})


def PartDetails(request, pk):
    details = Parts.objects.get(id=pk)
    return render(request, 'partsDetails.html', context={'details': details})
