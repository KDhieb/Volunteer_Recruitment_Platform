from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def volunteer_required(function=None, redirect_field_name= REDIRECT_FIELD_NAME, login_url = 'login'):
    ''' Decorator for views to check that logged in user is a volunteer'''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_volunteer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def npo_required(function=None, redirect_field_name= REDIRECT_FIELD_NAME, login_url = 'login'):
    ''' Decorator for views to check that logged in user is an npo'''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_npo,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
