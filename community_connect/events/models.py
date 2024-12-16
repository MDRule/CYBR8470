from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=[('Volunteer', 'Volunteer'), ('Organizer', 'Organizer'), ('Admin', 'Admin')],
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Ensure this field exists

    def __str__(self):
        return f"{self.user.username} ({self.role})"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


    

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    organizer = models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name="organized_events",
                                default=1  # Replace with the `id` of a default user
                                )
    created_at = models.DateTimeField(auto_now_add=True)  # Add this field

    def __str__(self):
        return self.name


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} signed up for {self.event}"
    
class Feedback(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)  # Relation to Event
    feedback = models.TextField()

    def __str__(self):
        return f"{self.event.name} - Feedback"