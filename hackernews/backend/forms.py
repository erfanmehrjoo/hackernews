from django.forms import ModelForm
from .models import Links , Message , UserWithPhoto
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

class MessagesForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
    

class UserWithPhotoForm(ModelForm):
    class Meta:
        model = UserWithPhoto
        fields = "__all__"