import os
import sys

import django
from decouple import config
from django.contrib.auth import get_user_model

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

User = get_user_model()

username = config('DJANGO_SUPERUSER_USERNAME')
email = config('DJANGO_SUPERUSER_EMAIL')
password = config('DJANGO_SUPERUSER_PASSWORD')


if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser {username} created')
    else:
        print(f'Superuser {username} already exists')
else:
    print('Superuser credentials not provided or incomplete')
