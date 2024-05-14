from django.urls import path
from . import views

urlpatterns = [
    path('',views.helloworld,name='home'),
    path('h1/',views.hello_world,name='home1'),
    path('v1/',views.view,name='view')
]
