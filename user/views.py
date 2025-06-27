from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .serializers import *
from .utils import unhash_token
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)



class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-uid')
    serializer_class = UserListSerializer
    # permission_classes = [permissions.IsAdminUser]




class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'
    queryset = User.objects.all()



class RetrieveProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        decoded = unhash_token(self.request.headers)
        return get_object_or_404(User, uid=decoded.get('user_id'))


class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=PasswordResetSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        decoded = unhash_token(request.headers)
        user = get_object_or_404(User, uid=decoded.get('user_id'))

        if not check_password(serializer.validated_data['old_password'], user.password):
            return Response({"error": "Incorrect old password"}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)


class DeleteUserByUIDAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'  # Get the user UID from the URL

    def perform_destroy(self, instance):
        requesting_user = self.request.user
        if instance != requesting_user and not requesting_user.is_admin:
            raise PermissionDenied("You do not have permission to delete other users.")
        instance.delete()








