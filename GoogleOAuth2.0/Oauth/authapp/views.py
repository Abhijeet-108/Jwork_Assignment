import requests
from django.conf import settings
from django.shortcuts import redirect, render
from urllib.parse import urlencode

# Show a simple login page
def login_view(request):
    return render(request, 'login.html')


# Redirect to Google's OAuth 2.0 authorization endpoint
def authorize(request):
    base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    params = {
        'client_id': settings.GOOGLE_CLIENT_ID,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'response_type': 'code',
        'scope': 'openid email profile https://www.googleapis.com/auth/userinfo.email',
        'access_type': 'offline',  # ensures refresh token is returned
        'prompt': 'consent',       # always ask for permission
    }
    return redirect(f"{base_url}?{urlencode(params)}")


# Callback handler: exchange code for token
def oauth2callback(request):
    code = request.GET.get('code')

    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }

    # Get access + refresh token
    response = requests.post(token_url, data=data)
    tokens = response.json()

    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token')

    return render(request, 'login.html', {
        'access_token': access_token,
        'refresh_token': refresh_token
    })

def refresh_access_token(refresh_token):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post(token_url, data=data)
    token_data = response.json()
    return token_data.get('access_token')
