"""定义learning_logs的URL模式"""

from django.urls import path

from . import views

app_name ='learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # 显示所有教师
    path('teachers/', views.teachers, name='teachers'),
    # 特定教师的详细页面
    path('teachers/<int:teacher_id>/', views.teacher, name='teacher'),
    # 用于添加新教师的页面
    path('new_teacher/', views.new_teacher, name='new_teacher'),
    # 用于添加新教师详情的页面
    path('new_teacherMessage/<int:teacher_id>/', views.new_teacherMessage, name='new_teacherMessage'),
    # 用于编辑教师详情的页面
    path('edit_teacherMessage/<int:teacherMessage_id>/', views.edit_teacherMessage, name='edit_teacherMessage'),
    # 用于删除教师详情的页面
    path('delete_teacherMessage/<int:teacherMessage_id>/', views.delete_teacherMessage, name='delete_teacherMessage'),
]