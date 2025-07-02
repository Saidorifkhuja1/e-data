from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer, FileCreateSerializer

class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileRetrieveView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'


class FileUpdateView(generics.UpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'
    parser_classes = [MultiPartParser, FormParser]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class FileDeleteView(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'


class FileListByUserAPIView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_uid = self.kwargs['uid']
        return File.objects.filter(user__uid=user_uid).order_by('-uploaded_at')


class MyFileListAPIView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(user=self.request.user).order_by('-uploaded_at')


class AllFileListAPIView(generics.ListAPIView):
    queryset = File.objects.all().order_by('-uploaded_at')
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]




class SearchFileAPIView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return File.objects.all().order_by('-uploaded_at')


