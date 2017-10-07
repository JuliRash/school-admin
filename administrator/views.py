""" administrator/views.py file CRUD for my school information management."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView

from main.models import Event, News, Teacher, Executive
from administrator.forms import (
    EventForm, NewsForm, TeacherForm,
    ExecutiveForm, UserForm, ProfileForm
)



# ==================================================================================================================================
# News CRUD
# ==================================================================================================================================

@login_required(login_url='/administrator/login')
def index(request):
    """Dashboard for logged in user."""
    event = Event.objects.filter(
        event_status='published').order_by('-date_modified')[:3]
    news = News .objects.filter(
        news_status='published').order_by('-date_modified')[:3]
    all_news = News.objects.filter(news_status='published')
    all_events = Event.objects.filter(event_status='published')
    all_teachers = Teacher.objects.all()
    all_executives = Executive.objects.all()
    return render(
        request, 'school/dashboard.html', {
            'event': event, 'news': news,
            'events': all_events, 'all_news': all_news,
            'teachers': all_teachers, 'executives': all_executives
        }
    )

@login_required(login_url='/administrator/login')
def add_news(request):
    """function for adding news."""
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.news_author = User.objects.get(username=request.user)
            news.save()
            messages.success(
                request, 'you have successfully added an event await system administrator approval', extra_tags='alert')
            return redirect('administrator:view-events')
    else:
        form = NewsForm()

    return render(request, 'school/add-news.html', {'form': form})


@login_required(login_url='/administrator/login')
def view_news(request):
    """View all news that have been published."""
    news = News.objects.all().order_by('-date_modified')
    return render(request, 'school/view-news.html', {'news': news})


class UpdateNews(LoginRequiredMixin, UpdateView):
    form_class = NewsForm
    template_name = 'school/add-news.html'
    model = Event

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(News, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'News updated successfully', extra_tags='alert'
        )
        return redirect('administrator:view-news')



def delete_news(request, pk):
    """function to delete a single news."""
    instance = get_object_or_404(News, pk=pk)
    instance.delete()
    messages.success(request, instance.news_title +
                  ' has been deleted successfully')
    return redirect('administrator:view-events')

# ================================================================================================================================
# Events CRUD
# ==================================================================================================================================

@login_required(login_url='/administrator/login')
def add_event(request):
    """function for adding a single event."""
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_author = User.objects.get(username=request.user)
            event.save()
            messages.success9(
                request, 'you have successfully added an event await adminstrator approval', extra_tags='alert')
            return redirect('administrator:view-events')
    else:
        form = EventForm()

    return render(request, 'school/add-event.html', {'form': form})


@login_required(login_url='/administrator/login')
def view_events(request):
    """View all events that have been published."""
    events = Event.objects.filter(event_status='published')
    return render(request, 'school/view-event.html', {'events': events})


class EventUpdate(LoginRequiredMixin, UpdateView):
    form_class = EventForm
    template_name = 'school/add-event.html'
    model = Event

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Event, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
             'Event updated successfully', extra_tags='alert'
        )
        return redirect('administrator:view-events')


def delete_event(request, pk):
    instance = get_object_or_404(Event, pk=pk)
    instance.delete()
    return redirect('administrator:view-events')


# =================================================================================================================================
# Teachers CRUD
# =================================================================================================================================

@login_required(login_url='/administrator/login')
def add_teacher(request):
    """function for adding a single event."""
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.info(
                request, 'you have successfully added a teacher!', extra_tags='alert')
            return redirect('administrator:view-teachers')
    else:
        form = TeacherForm()

    return render(request, 'school/add-teacher.html', {'form': form})


@login_required(login_url='/administrator/login')
def view_teachers(request):
    """View all events that have been published."""
    teacher = Teacher.objects.all()
    return render(request, 'school/view-teachers.html', {'teacher': teacher})


class TeacherUpdate(LoginRequiredMixin, UpdateView):
    form_class = TeacherForm
    template_name = 'school/add-teacher.html'
    model = Event

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Teacher, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.info(
            self.request,
            'Event updated successfully!', extra_tags='alert'
        )
        return redirect('administrator:view-events')


def delete_teacher(request, pk):
    instance = get_object_or_404(Teacher, pk=pk)
    instance.delete()
    return redirect('administrator:view-teachers')

# ==================================================================================================================================
# Executive CRUD
# ==================================================================================================================================

@login_required(login_url='/administrator/login')
def add_executive(request):
    """function for adding a single event."""
    if request.method == 'POST':
        form = ExecutiveForm(request.POST, request.FILES)
        if form.is_valid():
            executive = form.save(commit=False)
            executive.save()
            messages.info(
                request, 'you have successfully added an executive!', extra_tags='alert')
            return redirect('administrator:view-executives')
    else:
        form = ExecutiveForm()

    return render(request, 'school/add-executive.html', {'form': form})


@login_required(login_url='/administrator/login')
def view_executives(request):
    """View all events that have been published."""
    exco = Executive.objects.all()
    return render(request, 'school/view-executives.html', {'exco': exco})


class ExecutiveUpdate(LoginRequiredMixin, UpdateView):
    form_class = ExecutiveForm
    template_name = 'school/add-executive.html'
    model = Executive

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Executive, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'Executive updated successfully', extra_tags='alert'
        )
        return redirect('administrator:view-executives')


def delete_executive(request, pk):
    instance = get_object_or_404(Executive, pk=pk)
    instance.delete()
    return redirect('administrator:view-events')

# =================================================================================================================================
# User Profile
# =================================================================================================================================

@login_required(login_url='/administrator/login')
def view_profile(request):
    return render(request, 'school/profile.html')


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Congratulations your profile was updated successfully!'))
            return redirect('administrator:profile')
        else:
            messages.danger(request, ('Unable to update correct the errors.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'school/profile-update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
