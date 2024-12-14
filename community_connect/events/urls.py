from django.urls import path
from . import views

urlpatterns = [
#    path('', views.home, name='home'),
    path('', views.event_list, name='event_list'),
    path('events/<int:event_id>/signup/', views.event_signup, name='event_signup'),
    path('participation/', views.my_participation, name='my_participation'),
    path('organizer/create/', views.EventCreateView.as_view(), name='event_create'),
    path('organizer/edit/<int:pk>/', views.EventUpdateView.as_view(), name='event_edit'),
    path('organizer/delete/<int:pk>/', views.EventDeleteView.as_view(), name='event_delete'),
    path('organizer/<int:event_id>/signups/', views.view_signups, name='view_signups'),
]
