from django.urls import path
from api.blog import views

urlpatterns = [
    path('',views.ListBlogAPIView.as_view()),
    path('create',views.CreateBlogAPIView.as_view()),
    path('<int:pk>',views.DetailBlogAPIView.as_view()),  
    path('update/<int:pk>',views.UpdateBlogAPIView.as_view()),
    
]