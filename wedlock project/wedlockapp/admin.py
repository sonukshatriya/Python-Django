from django.contrib import admin
from .models import wedlock

# Register your models here.

class show_wedlock(admin.ModelAdmin):
    list_display = ['email','password','profile_seeking_for','first_name','last_name','gender','religion','mother_tongue']
admin.site.register(wedlock, show_wedlock)


