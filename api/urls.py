from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('we',views.we),
    path('time/<str:date>/',views.time)
]
