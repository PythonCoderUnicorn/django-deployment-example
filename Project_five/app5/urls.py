from django.conf.urls import url 
from app5 import views 

# TEMPLATE URLS
app_name = 'app5'

urlpatterns = [
    url('register/',views.register,name='register'),
    url('user_login', views.user_login, name='user_login'),
]