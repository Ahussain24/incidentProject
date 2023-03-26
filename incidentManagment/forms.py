from django import forms
from .models import Incident
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_details', 'priority', 'status']

    def __init__(self, user, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['incident_details'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['reporter'].initial = user

    def clean(self):
        cleaned_data = super(IncidentForm, self).clean()
        status = cleaned_data.get('status')
        if status == Incident.INCIDENT_STATUS_CLOSED:
            raise forms.ValidationError("Cannot modify a closed incident.")
        return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data.get("username"):
            user.username = None
        if commit:
            user.save()
        return user


