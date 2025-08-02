from rest_framework_simplejwt.views import TokenObtainPairView
from userauths.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    """
    POST request body:
        {
            "email": "test@example.com",
            "password": "yourpass"
        }

    Successful response:
        {
            "refresh": "<refresh_token>",
            "access": "<access_token>"
        }

    Error response if credentials are invalid:
        {
            "detail": "No active account found with the given credentials"
        }
    """

    serializer_class = MyTokenObtainPairSerializer


@extend_schema(
    tags=["Users"],
    request=RegisterSerializer,
    responses={
        201: OpenApiResponse(
            description=
            """
            {
                "full_name": "admin",
                "email": "admin@example.com",
                "phone": "9876543210",
            }
            """
        ),
        400: OpenApiResponse(
            description= 
            """
                "email": 
                    - This field is required.
                    - Enter a valid email address.
                    - user with this email already exists.
                "username":
                    - user with this username already exists.
                "password":
                    - This field is required.
                    - This password is too short.
                    - This password is too common.
                "password2":
                    - This field is required.
                    - Password does not match
                "phone":
                    - Ensure this field has no more than 100 characters.
                "full_name":
                    - Ensure this field has no more than 100 characters.
            """
        )
    },
    examples=[
        OpenApiExample(
            name="Basic Register",
            value={
                "full_name": "admin",
                "email": "admin@example.com",
                "phone": "9876543210",
                "password": "StrongPass123",
                "password2": "StrongPass123"
            },
            summary="Register a new user with required fields",
        )
    ]
)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()