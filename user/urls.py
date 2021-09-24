from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home-page'),
    path('detail/<int:id>/', views.detail, name="post-details"),
    path('create/', views.create, name="create")
]