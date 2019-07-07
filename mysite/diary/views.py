from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Entry

# Create your views here.
def index(request):
    latest_entry_list = Entry.objects.order_by('-pub_date')[:10]
    template = loader.get_template('diary/index.html')
    context = {
        'latest_entry_list' : latest_entry_list,
    }
    return render(request, 'diary/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'diary/detail.html', {'entry':entry})

def save(request, entry_id):
    