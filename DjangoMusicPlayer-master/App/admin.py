from django.contrib import admin
from .models import Song
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Song)
