from django import forms
from django.contrib.auth.models import User
from .models import Profile, Event, Feedback

class VolunteerSignupForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
            # Update the profile with role and phone number
            Profile.objects.filter(user=user).update(
                role='Volunteer',
                phone_number=self.cleaned_data['phone_number']
            )
        return user

# Add this missing EventForm class
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['event', 'feedback']  # Match the fields in the Feedback model