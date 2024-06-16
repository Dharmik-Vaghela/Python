from django.urls import path, include
from . import views
urlpatterns = [
    #path("",views.IndexView,name="index"),
    path("",views.htmlform,name="htmlform"),
]