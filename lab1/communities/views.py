from django.shortcuts import render
from .models import Communities
from django.contrib.auth.decorators import login_required

def communities(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities.html', {'communities': communities})

def communities_page(request, slug):
    communitie = Communities.objects.get(slug=slug)  
    return render(request, 'communities/communities_page.html', {'communitie': communitie})



@login_required(login_url="/users/login/")
def communities_new(request):
    return render(request, 'communities/communities_new.html')
