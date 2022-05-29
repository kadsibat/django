<<<<<<< HEAD
from dataclasses import field
from django import forms
=======
from django import forms
from django.db.models import fields
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model =Todo
        fields= "__all__"
=======
        model = Todo
        fields = "__all__"
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
