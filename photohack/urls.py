from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name='photo'),
    # path('photo', views.process_image, name='process_image'),
    path('photo', views.return_gif, name='return_gif'),
]
