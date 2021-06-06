from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':

        # Instantiate the form with the submitted data with form.
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # This method takes the request object, the username,
            # and the password parameters and returns the User object
            # if the user has been successfully authenticated
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:

                # If the user was successfully authenticated, you check whether the user is active.
                if user.is_active:

                    # Set the user in the session
                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        # When the user_login view is called with a GET request.
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


@login_required
# The login_required decorator checks whether the current user is authenticated.
# If the user is authenticated, it executes the decorated view; if the user is not authenticated,
# it redirects the user to the login URL with the originally requested URL as a GET parameter named next.
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()

            # When users register on your site,
            # you will create an empty profile associated with them.
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
# You use the login_required decorator because users have to be
# authenticated to edit their profile.
def edit(request):
    if request.method == 'POST':

        # Return a user with post information
        user_form = UserEditForm(
            instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        # if those forms that now a model is valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # Use default message option on django
            messages.success(request, 'Profile updated '
                             'successfully')
        else:
            messages.error(request, 'Error updating your profile')

    else:
        # Fill fields with that 2 model from user and user.profile
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
