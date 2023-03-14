from django import forms
from .models import Comment, Email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'whatsapp', 'body')
        widgets = {'name': forms.TextInput(attrs={ 'id':"name-id"}),
        'email': forms.EmailInput(attrs={ 'id':"email-id"}),
        'whatsapp': forms.TextInput(attrs={ 'id':"site-id"}),
        'body': forms.Textarea(attrs={ 'id':"comment"})
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('name','email_address','subject','body')
        widgets = {
            'name': forms.TextInput(attrs={ 'id':"name"}),
            'email_address': forms.EmailInput(attrs={ 'id':"email"}),
            'subject': forms.TextInput(attrs={ 'id':"subject"}),
            'body': forms.Textarea(attrs={ 'id':"message"})
        }

    