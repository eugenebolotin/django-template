import os
import time

import django
from django.db import connections
from django.db.utils import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def wait_for_db(alias='default', delay=5, max_attempts=30):
    attempts = 0
    while attempts < max_attempts:
        try:
            connection = connections[alias]
            connection.ensure_connection()
            print('Database is ready!')
            return
        except OperationalError as e:
            print(f'Database not ready ({e}), waiting {delay} seconds...')
            time.sleep(delay)
            attempts += 1
    print('Max attempts reached. Database not available.')
    exit(1)


if __name__ == '__main__':
    wait_for_db()
