from django.contrib import admin
from .models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')