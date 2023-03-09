from django.shortcuts import render
from urllib import request
from activity1.models import Profile

# Create your views here.

def profile_view(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'profile.html', context)