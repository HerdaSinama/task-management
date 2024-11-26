from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser
from typing import Any
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validator_avatar_weight(file: Any) -> Any:
    """
    Валидатор размера файла для изображений.
    Проверяет, не превышает ли размер загружаемого файла 5 МБ.

    - file: объект файла, который будет проверяться на размер.

    Исключения:
    - ValidationError: Если размер файла превышает 5 МБ.
    """
    limit = 5 * 1024 * 1024
    if file.size > limit:
        raise ValueError('File size is too big')
    

class User(AbstractUser):
    class ROLE(TextChoices):
        DEFAULT = 'default', 'Default',
        ADMIN = 'admin', 'Admin',

    class GENDER(TextChoices):
        MALE = 'male', 'Male',
        FEMALE = 'female', 'Female',
        
    gender = models.CharField(
        max_length=6,
        choices=GENDER.choices,
        default=None,
    )
    role = models.CharField(
        max_length=7,
        choices=ROLE.choices,
        default=ROLE.DEFAULT,
        )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='/media',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validator_avatar_weight,
            ],
    )
    register_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args: Any, **kwargs: Any) -> None:
        super().save(*args, **kwargs)
        if self.avatar:
            try:
                image = image.open(self.avatar.path)
                max_size = (350, 350)
                if image.height > 350 or image.width > 350:
                    image.thumbnail(max_size)
                    image.save(self.avatar.path)
            except Exception as e:
                raise ValidationError('Image size error')
                
            

