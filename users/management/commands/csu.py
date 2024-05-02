from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='zakirov.alexey@gmail.com',
            first_name='Admin',
            last_name='Administrator',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123123qwerty')
        user.save()
