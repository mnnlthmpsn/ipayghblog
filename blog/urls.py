from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:blog_id>/detail/', views.blog_detail, name='detail'),
    path('admin/', views.admin, name='admin'),
    path('admin/logout', views.admin_logout, name='logout'),
    path('admin/dashboard', views.dashboard, name='admin_dashboard'),
    path('admin/add/', views.add_blog, name='add'),
    path('admin/<int:blog_id>/view/', views.view_blog, name='view'),
    path('admin/<int:blog_id>/update/', views.update_blog, name='update'),
    path('admin/<int:blog_id>/delete/', views.delete_blog, name='delete'),
]