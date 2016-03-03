from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .model import SessionMaker, StreamGage
from tethys_gizmos.gizmo_options import MapView, MVLayer, MVView, TextInput


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)

def map(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/map.html', context)