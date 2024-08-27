from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
         Команда для создания пользователя.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Введите email\n'),
            is_active=True,
        )

        user.set_password(input('Введите пароль\n'))
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Пользователь успешно создан.'))