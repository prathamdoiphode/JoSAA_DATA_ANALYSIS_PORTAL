from django.urls import path
from . import views

urlpatterns = [
    # for headers url ....
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('more/',views.more,name='more'),
    path('service/',views.service,name='service'),

    # for questions url ....
    path('innerpage/',views.innerpage),

]