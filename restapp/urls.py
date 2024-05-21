from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ShowRoom_view ,ShowRoom_details

router = DefaultRouter()
router.register('showroom',views.ShowRoom_viewset,basename='showroom')

urlpatterns = [
    path('',views.home,name='home'),
    path('h1/',views.hello_world,name='home1'),
    path('v1/',views.view,name='view'),
    path('carlist/',views.car_list,name='car_list'),
    path('carlist/<int:pk>/',views.car_detail_view,name='car_detail'),
    path('',include(router.urls)),
    # path('showroom/',ShowRoom_view.as_view(),name='showroomview'),
    # path('showroom/<int:pk>',ShowRoom_details.as_view(),name='showroomdetails'),
    path('review',views.Reviewlist.as_view(),name='ReviewList'),
    # path('review/<int:pk>',views.ReviewList_detail.as_view(),name='ReviewListdetails'),
    path('carlist/<int:pk>/review-create',views.Reviewcreate.as_view(),name="review_create"),
    path('carlist/<int:pk>/review',views.ReviewList.as_view(),name="review_list"),
    path('carlist/review/<int:pk>',views.ReviewList_detail.as_view(),name="review_detail"),


 
]
