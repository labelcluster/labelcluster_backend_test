from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import get_object_or_404

def create_blog(request):   #2101
    if request.method == 'POST':
        data = request.POST
        newBlog = Blog()
        blog_creator = get_object_or_404(User, pk=data['user_id'])
        newBlog.user = blog_creator
        newBlog.blog_title = data['blog_title']
        newBlog.blog_content = data['blog_content']
        newBlog.save()
        
        return JsonResponse({'new_Blog_id': newBlog.id})
    
def update_blog(request): #2102
    if request.method == 'POST':
        data = request.POST
        key = data['blog_id']
        updateBlog = get_object_or_404(Blog, pk=key)
        if len(data['blog_title']) > 0:
            updateBlog.blog_title = data['blog_title']
        if len(data['blog_content']) > 0:
            updateBlog.blog_content = data['blog_content']
        # Edge case not checked yet
        updateBlog.save()
        return HttpResponse("Success")
    
    
def get_blog(request):  #2103
    if request.method == 'POST':
        key = request.POST['blog_id']
        data = Blog.objects.filter(pk=key).values()
        return JsonResponse({'blog': list(data)})
    
    
def create_comment(request):  #2104
    if request.method == 'POST':
        data = request.POST
        newComment = Comment()
        comment_creator = get_object_or_404(User, pk=data['user_id'])
        blog_commented = get_object_or_404(Blog, pk=data['blog_id'])
        newComment.user = comment_creator
        newComment.blog = blog_commented
        newComment.comment_content = data['comment_content']
        newComment.save()
        
        return JsonResponse({'new_Comment_id': newComment.id})
    

def update_comment(request):    #2105
    if request.method == 'POST':
        data = request.POST
        key = data['comment_id']
        updateComment = get_object_or_404(Comment, pk=key)
        if len(data['comment_content']) > 0:
            updateComment.comment_content = data['comment_content']
        updateComment.save()
        return HttpResponse("Success")
    

def get_comment(request):   #2106
    if request.method == 'POST':
        key = request.POST['comment_id']
        data = Comment.objects.filter(pk=key).values()
        return JsonResponse({'Comment': list(data)})
    
        
def get_all_blog_by_user(request): #2107
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = get_object_or_404(User, pk=user_id)
        
        blogs = Blog.objects.filter(user=user).values()
        return JsonResponse({'blogs': list(blogs)})


def get_all_comments_in_blog(request):  #2108
    if request.method == 'POST':
        blog_id = request.POST['blog_id']
        blog = get_object_or_404(Blog, pk=blog_id)
        
        comments = Comment.objects.filter(blog=blog).values()
        return JsonResponse({'comments': list(comments)})
    
