from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, email=None, **extra_fields):
        """
        Создает и возвращает пользователя с номером телефона.
        """
        if not phone_number:
            raise ValueError('Поле phone_number должно быть заполнено')
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, email=None, **extra_fields):
        """
        Создает и возвращает суперпользователя с номером телефона.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Если email не передан, можно задать его значение по умолчанию
        if not email:
            email = f'{phone_number}@example.com'  # Задаем значение по умолчанию для email

        return self.create_user(phone_number, password, email=email, **extra_fields)
