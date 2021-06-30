from django.urls import path
from .import views

urlpatterns = [
  path('blog/', views.blog, name="Blog"),
  path('blogpost/<int:id>', views.blogpost, name="Post"),
]