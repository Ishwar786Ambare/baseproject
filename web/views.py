from django.shortcuts import render, redirect
from .context_utils import createContext

# Create your views here.


def index(request, **kwargs):
    """
    index page
    """
    context = createContext(request=request, **kwargs)

    context.update({
        'title': 'index',
    })

    return render(request, 'web/pages/index.html.j2', context)
