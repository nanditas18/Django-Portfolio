#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    current_path = Path(__file__).resolve().parent
    if str(current_path) not in sys.path:
        sys.path.insert(0, str(current_path))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordcounter_core.myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()