from django.urls import path
from .views import PostList, PostDetail

app_name = 'api'

urlpatterns = [
  path('', PostList.as_view(), name='list'),
  path('<int:pk>/', PostDetail.as_view(), name='detail'),
]