from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Item, Service, Designer

def index(request):
    '''
    Show 'Hello world!' in the main page
    '''

    return render_to_response('hairsalon/index.html',locals())
def hairsalon(request):
    '''
    Render the indexbooking page
    '''
    return render(request, 'hairsalon/indexbooking.html')
def indexbooking(request):
    '''
    Render the indexbooking page
    '''
    return render(request, 'hairsalon/indexbooking.html')