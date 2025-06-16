from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Создает суперпользователя с кастомной моделью'

    def handle(self, *args, **options):
        username = input('Введите username: ')
        email = input('Введите email: ')
        password = input('Введите пароль: ')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('Пользователь с таким username уже существует.'))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Суперпользователь {username} успешно создан.'))
