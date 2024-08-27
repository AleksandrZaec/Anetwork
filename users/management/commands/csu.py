from django.core.management import BaseCommand
from users.models import User
import os
from dotenv import load_dotenv
from config.settings import BASE_DIR

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    """
        Команда для создания суперпользователя.
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('SUPERUSER_EMAIL'),
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password(os.getenv('SUPERUSER_PASSWORD'))
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Суперпользователь успешно создан.'))
