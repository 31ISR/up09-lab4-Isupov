from django.shortcuts import render
from .models import Communities

def communities(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities.html', {'communities': communities});