from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import Registration_view , logout_view

urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',Registration_view.as_view(),name='login'),
    path('logout/',logout_view,name='logout')
]
