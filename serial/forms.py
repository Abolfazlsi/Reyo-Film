from django import forms
from serial.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", )
        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"})
        }
