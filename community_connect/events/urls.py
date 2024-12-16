from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
#    path('', views.home, name='home'),
#    path('', views.event_list, name='event_list'),
#    path('events/<int:event_id>/signup/', views.event_signup, name='event_signup'),
#    path('participation/', views.my_participation, name='my_participation'),
#    path('organizer/create/', views.EventCreateView.as_view(), name='event_create'),
#    path('organizer/edit/<int:pk>/', views.EventUpdateView.as_view(), name='event_edit'),
#    path('organizer/delete/<int:pk>/', views.EventDeleteView.as_view(), name='event_delete'),
#    path('organizer/<int:event_id>/signups/', views.view_signups, name='view_signups'),
#    path('events/', views.browse_events, name='browse_events'),
#    path('events/create/', views.CreateEventView.as_view(), name='create_event'),
#    path('admin/events/', views.manage_events, name='manage_events'),
#    path('signup/volunteer/', views.volunteer_signup, name='volunteer_signup'),
    path('', views.browse_events, name='browse_events'),
    path('volunteer_signup/', views.volunteer_signup, name='volunteer_signup'),
    path('create_event/', views.create_event, name='create_event'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='browse_events'), name='logout'),

]
