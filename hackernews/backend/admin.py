from django.contrib import admin
from .models import Links , Message , UserWithPhoto
# Register your models here.
admin.site.register(Links)
admin.site.register(Message)
admin.site.register(UserWithPhoto)