from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from main.models import Event, News, Teacher, Executive, Profile

class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'news_title', 'news_description', 'news_author', 'news_detail', 'news_status',
        'date_added', 'date_modified',
    ]


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'event_title', 'event_date', 'event_time', 'event_status'
    ]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teachers_title', 'first_name', 'last_name', 'teachers_phone', 'teachers_email']


class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ['executive_title', 'first_name', 'last_name', 'executive_phone', 'executive_email']


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(Event, EventAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)