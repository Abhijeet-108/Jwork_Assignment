from django.urls import path
from .views import AddEntryView, RetrieveEntriesView

urlpatterns = [
    path('add/', AddEntryView.as_view(), name='add-entry'),
    path('entries/', RetrieveEntriesView.as_view(), name='retrieve-entries'),
]
