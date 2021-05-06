from django import forms
from .models import Todos , User

class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["title","description","finished","date"]

class ListUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","password"]

        