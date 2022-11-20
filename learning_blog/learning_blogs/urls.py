"""定义learning_blogs的URL模式"""

from django.urls import path

from . import views

app_name = 'learning_blogs'
urlpatterns = [
	# 主页
    path('', views.index, name='index'),
	# 显示所有的博客标题
    path('blogposts/', views.blogposts, name='blogposts'),
	# 显示特定博客的博文内容
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
	# 用于添加新博客的页面
    path('new_blogpost/', views.new_blogpost, name='new_blogpost'),
	# 用于添加新博文的页面
    path('new_blogartical/<int:blogpost_id>/', views.new_blogartical, name='new_blogartical'),
	# 用于编辑博文的页面
    path('edit_blogartical/<int:blogartical_id>/', views.edit_blogartical, name='edit_blogartical'),
]
