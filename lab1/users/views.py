from django.shortcuts import render


# Create your views here.
def register_view(req):
    return render(req, 'users/register.html', {})