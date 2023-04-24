from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Override default User model fields
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)

    # Add custom fields
    age = models.PositiveIntegerField(null=True, blank=True)

    # Override related name for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_user_permissions'
    )

    def __str__(self):
        return self.email


from django.apps import AppConfig
from django.db.models import BigAutoField

class App(AppConfig):
    name = 'App'
    default_auto_field = 'django.db.models.BigAutoField'



class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    FILE_TYPES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music_files')
    file_type = models.CharField(max_length=20, choices=FILE_TYPES, default=PUBLIC)
    allowed_users = models.ManyToManyField(CustomUser, related_name='allowed_files', blank=True)

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2
    def __str__(self):
        return self.title

