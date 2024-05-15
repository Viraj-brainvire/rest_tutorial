from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('h1/',views.hello_world,name='home1'),
    path('v1/',views.view,name='view'),
    path('list/',views.car_list,name='car_list'),
    path('list/<int:pk>',views.car_detail_view,name='car_detail')
]
