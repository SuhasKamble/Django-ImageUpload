from django.contrib import admin
from myApp.models import Image
# Register your models here.
@admin.register(Image)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']