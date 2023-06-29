#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    import os
    import sys

    # local_settings.py faylini import qiling
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.local_settings')

    # serverning o'zgaruvchilarni sozlang
    os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')
    os.environ.setdefault('RUN_MAIN', 'true')

    # serverni ishga tushirish
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)