from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from main.models import Event, News, Teacher, Executive, Profile


class EventForm(forms.ModelForm):
    event_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format = '%d-%m-%y'))
    class Meta:
        model = Event
        fields = [
            'event_title', 'event_description', 'event_image',
            'event_details', 'event_date', 'event_time',
        ]


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = [
            'news_title', 'news_description',
            'news_image_1', 'news_image_2', 'news_image_3', 'news_detail',
        ]


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['teacher_status']


class ExecutiveForm(forms.ModelForm):

    class Meta:
        model = Executive
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['birth_date', 'picture', 'location', 'website', 'phone', 'occupation']