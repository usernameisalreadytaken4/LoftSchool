__all__ = ['Class1', 'Class2']

from django.contrib.auth import get_user_model
from django.db.models import Model

User = get_user_model()


class Class1(Model):
    pass


class Class2(Model):
    pass
