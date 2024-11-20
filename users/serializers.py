from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password', 'password2', 'balance']

    def validate(self, attrs):
        # Проверка совпадения паролей
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        # Убираем поле password2
        validated_data.pop('password2')
        # Создание нового пользователя
        user = CustomUser.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            balance=validated_data.get('balance', 0)  # Если баланс не передан, по умолчанию 0
        )
        return user
