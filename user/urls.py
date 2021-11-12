from django.urls import path
from . import views
from .views import IndexView,PostDetailView,PostCreateView ,PostUpdateView,PostDeleteView

urlpatterns = [
    # path('',views.index, name='home-page'),
    path('',IndexView.as_view(), name='home-page'),
    # path('detail/<int:id>/', views.detail, name="post-details"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="details"),
    path('post/create/', PostCreateView.as_view(), name="create"),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name="updates"),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name="delete")
]