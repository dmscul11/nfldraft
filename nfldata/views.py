from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create views
def index(request):
    return render(request, 'nfldata/homepage.html')

# adds stats to table
def add_nfldata(request):
    return HttpResponse('No data added')

# runs fantasy draft
def begin_draft(request):
    return HttpResponse('Not started')