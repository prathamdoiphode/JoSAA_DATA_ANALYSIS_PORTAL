from django.urls import path
from . import views

urlpatterns = [
    # for headers url ....
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contributors/',views.contributors,name='contributors'),

    # for questions url ....
    path('roundwise/',views.roundwise),
    path('bestcourse/',views.bestcourse),
    path('yearwise/',views.yearwise),
    path('CourseComparison/',views.CourseComparison),
    path('BestCollege/',views.BestCollege),
    path('categorywise/',views.categorywise),

    
    

    # for dropdown url ....
    path('get-InstTypewise-Instname/', views.get_InstTypewise_Instname),
    path('get-InstNameWise-ProgrammeName/', views.get_InstNameWise_ProgrammeName),
    path('get-Programmewise-Course/', views.get_Programmewise_Course),
    path('get-Coursewise-Category/', views.get_Coursewise_Category),
    path('get-Categorywise-Gender/', views.get_Categorywise_Gender),
    path('get-RoundDropdown/', views.get_RoundDropdown),
    path('get-YearDropdown/', views.get_YearDropdown),
    path('get-only-Categorywise-Gender/', views.get_only_Categorywise_Gender),
    path('get-InstTypeWise-ProgrammeName/', views.get_InstTypeWise_ProgrammeName),
    path('get-only-Programmewise-Course/', views.get_only_Programmewise_Course),
    path('get-Instype-Coursewise-Category/', views.get_Instype_Coursewise_Category),
    path('get-InsType-Categorywise-Gender/', views.get_InsType_Categorywise_Gender),
    path('get-Coursewise-Gender/', views.get_Coursewise_Gender),
    
    
    
    
    
    # for table url ....
    path('get-Yearwise-Rank-Table/', views.get_Yearwise_Rank_Table),
    path('get-Roundwise-Rank-Table/', views.get_Roundwise_Rank_Table),
    path('get-Bestcourse-Table/', views.get_Bestcourse_Table),
    path('get-InstituteWise-Table/', views.get_InstituteWise_Table),

    # for graph url ....
    path('get-graph-CategoryWise/', views.get_graph_CategoryWise),
    path('get-graph-A-RankWise/', views.get_graph_A_RankWise),
    path('get-graph-B-RankWise/', views.get_graph_B_RankWise),
    
    

]