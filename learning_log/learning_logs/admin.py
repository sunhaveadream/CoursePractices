from django.contrib import admin

from .models import Topic,Entry,Teacher,TeacherMessage

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Teacher)
admin.site.register(TeacherMessage)