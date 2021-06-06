from django.db import models
from django.conf import settings


class Profile(models.Model):
    # When you have to deal with user accounts,
    # you will find that the user model of the Django authentication framework is suitable for common cases.
    # However, the user model comes with very basic fields.
    # You may wish to extend it to include additional data.
    # The best way to do this is by creating a profile model that contains all additional fields
    # and a one-to-one relationship with the Django User model.

    # The user one-to-one field allows you to associate profiles with users.

    # A one-to-one relationship is similar to a ForeignKey field with the parameter unique=True. 
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return f'Profile for user {self.user.username}'
