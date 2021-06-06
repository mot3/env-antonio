from django.contrib.auth.models import  User

class EmailAuthBackend(object):
    """
    Authenticate using e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        """
        You try to retrieve a user with the given email address 
        and check the password using the built-in check_password() method of the user model. 
        This method handles the password hashing to compare the given password 
        with the password stored in the database.
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        You get a user through the ID provided in the user_idparameter. 
        Django uses the backend that authenticated the user 
        to retrieve the User object for the duration of the user session
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None