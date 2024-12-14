from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from events.models import Event  # Replace with your app and model names

def setup_roles():
    # Create groups
    volunteer_group, _ = Group.objects.get_or_create(name='Volunteer')
    organizer_group, _ = Group.objects.get_or_create(name='Organizer')
    admin_group, _ = Group.objects.get_or_create(name='Admin')

    # Assign permissions
    event_content_type = ContentType.objects.get_for_model(Event)

    # Volunteer permissions
    volunteer_permissions = [
        Permission.objects.get(codename='view_event'),
    ]
    volunteer_group.permissions.set(volunteer_permissions)

    # Organizer permissions
    organizer_permissions = [
        Permission.objects.get(codename='add_event'),
        Permission.objects.get(codename='change_event'),
        Permission.objects.get(codename='delete_event'),
    ]
    organizer_group.permissions.set(organizer_permissions)

    # Admin has all permissions
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)
