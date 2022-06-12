import json
from rest_framework import viewsets
from users.models import Role, User
from users.serializers import ProfileSerializer, RoleSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
  queryset = Role.objects.all()
  serializer_class = RoleSerializer
  
class ProfileViewSet(APIView):
  permission_classes = (IsAuthenticated, )
  authentication_classes = [JWTAuthentication]
  # renderer_classes = [
  #   renderers.OpenAPIRenderer,
  #   renderers.SwaggerUIRenderer
  # ]
  
  def get(self, request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({ "success": True }, status=status.HTTP_205_RESET_CONTENT)
          #fuck
        except Exception as e:
            return Response({
              "success": False,
              "detail": 'Токен уже в черном списке'
            }, status=status.HTTP_400_BAD_REQUEST)