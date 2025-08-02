from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from userauths.models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        '''those extra fields you add in get_token() become part of the JWT’s payload. 
        They’re not sent back as separate top-level JSON properties (unless you also add them in validate()), 
        so you won’t see them in your API response body by default. Instead they’re embedded inside the token itself.'''
        token = super().get_token(user)
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["username"] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    '''
    data:
        {
        "full_name": "name",
        "email": "name@example.com",
        "phone": "9876543210",
        "password": "StrongPass123",
        "password2": "StrongPass123"
        }
    '''
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "phone", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password does not match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data["full_name"],
            email=validated_data["email"],
            phone=validated_data["phone"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = UserSerializer(instance.user).data
        return response
