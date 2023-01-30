from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('product_list/', Products.as_view(), name='product_list'),
                  path('order/', create_project, name='order'),
                  path('registration/', RegisterUser.as_view(), name='registration'),
                  path('profile/', Profile.as_view(), name='profile'),
                  path('product/<pk>', DetailView.as_view(), name='product'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
              ]
