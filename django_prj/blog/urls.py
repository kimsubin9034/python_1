from django.urls import path
from . import views


urlpatterns=[
    #localhost:8000/blog
    #path('',views.index),
    path('', views.PostList.as_view()),
    #localhost:8000/blog/4(pk)
    #path('<int:pk>/',views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),

]