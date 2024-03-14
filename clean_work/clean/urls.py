from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('about-us/', views.about_us, name='about-us'),
      path('contact/', views.contact, name='contact'),
      path('<int:service_id>/', views.service_detail, name='service_detail'),
      path('service/', views.service, name='service'),
      path('privacy_policy/', views.policy, name='policy')
]