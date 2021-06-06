from django.conf.urls import url
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):

    # the best way for user model used from setting.AUTH_USER_MODEL instead
    # of get_user_model()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    # A short label that contains only letters, numbers, underscores,
    # or hyphens to be used for building beautiful SEO-friendly URLs.
    slug = models.SlugField(max_length=200, blank=True)

    # The original URL for this image.
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)

    # You use db_index=True so that Django createsanindex in the database for this field.
    created = models.DateField(auto_now_add=True, db_index=True)

    """
    Next, you will add another field to the Image model to store the users who like an image.
    You will need a many-to-many relationship in this case
    because a user might like multiple images and each image can be liked by multiple users.
    """
    # When you define a ManyToManyField, Django creates an intermediary join table
    # using the primary keys of both models.
    """
     The ManyToManyField fields provide a many-to-many manager that allows you to retrieve related objects, 
     such as image.users_like.all(),
     or get them from auserobject, such as user.images_liked.all().
    """
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        """
        You will override the save() method of the Image model
        to automatically generate the slug field based on the value of the title field.
        Import the slugify() function and add asave() method to the Image model.
        """
        if not self.slug:
            # you use the slugify() function provided by Django
            # to automatically generate the image slug
            # for the given title when no slug is provided.
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
