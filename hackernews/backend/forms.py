from dataclasses import field
from django.forms import ModelForm
from .models import Links
from django.contrib.auth.models import User
class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = "__all__"
        exclude = ['slug']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"