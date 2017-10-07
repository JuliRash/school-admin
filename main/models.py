from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

qualification_choices = (
        ('OND', 'OND'),
        ('Bsc', 'Bsc'),
        ('Msc', 'Msc'),
        ('NCE', 'NCE'),
    )

gender_choices = (
        ('male', 'male'),
        ('female', 'female'),
    )

status_choices = (
        ('draft', 'draft'),
        ('published', 'published'),
    )

title_choices = (
    ('Mr', 'Mr'),
    ('Miss', 'Miss'),
    ('Mrs', 'Mrs'),
    ('Dr', 'Dr'),
    ('Prof', 'Prof'),
)

religion_choices = (
    ('Christianity', 'Christianity'),
    ('Islam', 'Islam'),
    ('Traditional', 'Traditional'),
)


class Event(models.Model):
    event_title = models.CharField(max_length=300, unique=True)
    event_description = models.CharField(max_length=400)
    event_image = models.ImageField()
    event_author = models.ForeignKey(User, on_delete=models.CASCADE)
    event_details = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    event_status = models.CharField(
        max_length=12, choices=status_choices, default='draft'
        )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '' + self.event_title



class News(models.Model):
    news_title = models.CharField(max_length=300, unique=True)
    news_description = models.CharField(max_length=400)
    news_author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_image_1 = models.ImageField()
    news_image_2 = models.ImageField(blank=True)
    news_image_3 = models.ImageField(blank=True)
    news_detail = models.TextField()
    news_status = models.CharField(
        max_length=12, choices=status_choices, default='draft'
        )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '' + self.news_title

    class Meta:
        verbose_name_plural = 'News'


class Setting(models.Model):
    school_name = models.CharField(max_length=200)
    school_logo = models.ImageField()
    school_description = models.CharField(max_length=500)
    school_address = models.CharField(max_length=400)
    school_vision = models.TextField()
    school_mission = models.TextField()
    school_core_values = models.TextField()
    phone_number_1 = models.CharField(max_length=12)
    phone_number_2 = models.CharField(max_length=12)
    email_address = models.EmailField()
    email_address_2 = models.EmailField(blank=True)
    settings_status = models.CharField(
        max_length=12, choices=status_choices, default='draft'
        )
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return '' + self.school_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    teachers_bio = models.CharField(max_length=500)
    teachers_picture = models.ImageField(blank=True)
    teachers_qualification = models.CharField(max_length=10, choices=qualification_choices)
    teachers_course = models.CharField(max_length=300)
    teachers_religion = models.CharField(max_length=17, choices=religion_choices)
    teachers_title = models.CharField(max_length=7, choices=title_choices)
    teachers_gender = models.CharField(max_length=7, choices=gender_choices)
    teachers_email = models.EmailField(unique=True)
    teachers_phone = models.CharField(max_length=13)

    def __str__(self):
        return '' + self.first_name + ', ' + self.last_name


class Executive(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    executive_bio = models.CharField(max_length=500)
    executive_picture = models.ImageField()
    executive_position = models.CharField(max_length=200)
    executive_qualification = models.CharField(max_length=10, choices=qualification_choices)
    executive_gender = models.CharField(max_length=7, choices=gender_choices)
    executive_religion = models.CharField(max_length=20, choices=religion_choices)
    executive_title = models.CharField(max_length=7, choices=title_choices)
    executive_email = models.EmailField(unique=True)
    executive_phone = models.CharField(max_length=12)


    def __str__(self):
        return '' + self.first_name + ', ' + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)
    picture = models.ImageField(blank=True)
    location = models.CharField(max_length=300, blank=True)
    birth_date = models.DateField()
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=12)
    occupation = models.CharField(max_length=300)

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
