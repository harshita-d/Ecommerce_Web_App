"""Views for the USER API"""

from rest_framework import generics, authentication, permissions
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.shortcuts import render


def api_endpoints(request):
    # Example of dynamically fetching registered endpoints
    from django.urls import get_resolver

    resolver = get_resolver()
    endpoints = {}
    for pattern in resolver.url_patterns:
        if hasattr(pattern, "pattern") and hasattr(pattern, "lookup_str"):
            endpoints[f"http://localhost:8000/{pattern.pattern}"] = pattern.lookup_str

    return render(request, "home.html", {"endpoints": endpoints})


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new Token for user"""

    serializer_class = AuthTokenSerializer

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""

        return self.request.user
