"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),

    # Include authentication backends for Facebook, Twitter, and Google.
    path('social-auth/', include('social_django.urls', namespace='social')),
]

# In this way, the Django development server will be in charge of serving the media files during development
# (that is when the DEBUG setting is set to True)
if settings.DEBUG:
    # The static() helper function is suitable for development, but not for production use.
    # Django is very inefficient at serving static files.
    # Never serve your static files with Django in a production environment.
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
