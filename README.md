# Django Toolkit

A collection of utilities to streamline Django development with enhanced testing, optimized database operations, and flexible queryset exporting.

## Quality
[![CI](https://github.com/Occy88/django-toolkit/actions/workflow/status/CI.yml?branch=main)](https://github.com/Occy88/django-toolkit/actions)
[![Coverage](https://codecov.io/gh/Occy88/django-toolkit/branch/main/graph/badge.svg)](https://codecov.io/gh/Occy88/django-toolkit)

## Pytest Enhancements

- Python-based database management avoids rebuilding migrations on every test run.
- Directory-level model setup decouples test models from production models for abstract model testing.

## django_toolkit.db

- **bulk_update_queryset**  
  Optimized function for batch updating fields based on annotations.

- **UpdatableModel**  
  Enables direct model instance updates without needing to call `.save()`.

## django_toolkit.exporter

- Export app for converting querysets into various formats.

*Refer to additional documentation for installation and detailed usage instructions.*
