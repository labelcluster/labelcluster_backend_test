from django.urls import path
from . import views


urlpatterns = [
    path('2101/', views.create_blog, name='createBlog'),
    path('2102/', views.update_blog, name="updateBlog"),
    path('2103/', views.get_blog, name="getBlog"),
    path('2104/', views.create_comment, name="createComment"),
    path('2105/', views.update_comment, name="updateComment"),
    path('2106/', views.get_comment, name="getComment"),
    path('2107/', views.get_all_blog_by_user, name="allBlogsByUser"),
    path('2108/', views.get_all_comments_in_blog, name="allCommentsInBlog"),
]