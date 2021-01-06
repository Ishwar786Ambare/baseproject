from django.urls import path, include
from  . import views as vs

urlpatterns = [
	path('', vs.index, name='index'),
]
