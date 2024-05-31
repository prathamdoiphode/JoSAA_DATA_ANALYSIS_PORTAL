from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='page1-home'),
    path("about/", views.about,name='page1-about'),
    path("Branch.html/",views.Branch,name = 'page1-Branch.html'),
    path("YearWise.html/",views.YearWise,name = 'page1-YearWise.html'),
    path("Roundwise.html/",views.Roundwise,name = 'page1-Roundwise.html'),

]