from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='page1-home'),
    path("about/", views.about,name='page1-about'),
    path("branch/",views.Branch,name = 'page1-Branch.html'),
    path("yearwise/",views.YearWise,name = 'page1-YearWise.html'),
    path('roundwise/',views.Roundwise,name = 'page1-Roundwise.html'),

]