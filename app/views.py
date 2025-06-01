from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount, SocialToken

def home(request):
    """
    If the user is already authenticated, redirect to /profile/.
    Otherwise, show a “Sign in with Google” button.
    """
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'app/home.html')


@login_required
def profile(request):
    """
    After Google login, display the user’s access and refresh tokens.
    django-allauth stores tokens in SocialToken.
    """
    try:
        # Retrieve the SocialAccount for provider='google'
        social_account = SocialAccount.objects.get(user=request.user, provider='google')
        # Retrieve the SocialToken for that account
        token = SocialToken.objects.get(account=social_account)
    except (SocialAccount.DoesNotExist, SocialToken.DoesNotExist):
        social_account = None
        token = None

    context = {
        'user': request.user,
        'access_token': token.token if token else None,
        # allauth stores refresh_token in token.token_secret
        'refresh_token': token.token_secret if token else None,
        'expires_at': token.expires_at if token else None,
    }
    return render(request, 'app/profile.html', context)
