from django.urls import path

from .views import blog_home, article_detail, article_create, article_delete, \
                   article_update


urlpatterns = [
    path('', blog_home, name="blog-home"),
    path('<int:pk>/', article_detail, name="article-detail"),

    path('create/', article_create, name="article-create"),
    path('delete/<int:pk>/', article_delete, name="article-delete"),
    path('update/<int:pk>/', article_update, name="article-update"),
]
