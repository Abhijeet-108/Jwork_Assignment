from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Entry
from .serializers import EntrySerializer

class AddEntryView(generics.CreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveEntriesView(generics.ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Entry.objects.filter(user=self.request.user)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
