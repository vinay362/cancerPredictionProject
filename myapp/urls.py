from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='homepage'),
    path('form/',views.cancerForm,name='cancer_form'),
    path('result/',views.prediction,name='result'),
]