from django.urls import path
from . import views
from .views import showRoom_view ,showRoom_details

urlpatterns = [
    path('',views.home,name='home'),
    path('h1/',views.hello_world,name='home1'),
    path('v1/',views.view,name='view'),
    path('list/',views.car_list,name='car_list'),
    path('list/<int:pk>',views.car_detail_view,name='car_detail'),
    path('showroom/',showRoom_view.as_view(),name='showroomview'),
    path('showroom/<int:pk>',showRoom_details.as_view(),name='showroomdetails')

 
]
