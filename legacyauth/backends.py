import logging
logger = logging.getLogger(__name__)

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a username/password pair.

    Warning: by default, Django's User model has no index on email. Perhaps
    monkey-patch this onto the User model?

    Ref: http://www.micahcarrick.com/django-email-authentication.html
    """

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None
