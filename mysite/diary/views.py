from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Entry
from django.utils import timezone

# Create your views here.
def index(request):
    latest_entry_list = Entry.objects.order_by('-pub_date')[:10]
    template = loader.get_template('diary/index.html')
    context = {
        'latest_entry_list' : latest_entry_list,
    }
    return render(request, 'diary/index.html', context)

def detail(request, entry_id):
    try:
        selected_entry = Entry.objects.get(pk=entry_id)
    except (KeyError, Entry.DoesNotExist):
        return render(request, 'diary/error.html',{'id':entry_id})
    else:
        return render(request, 'diary/detail.html', {'entry':selected_entry})

def new(request):
    return render(request, 'diary/new.html')

def save(request):
    title = request.POST['title']
    rating = int(request.POST['rating'])
    body = request.POST['body']
    pub_date = timezone.now()

    Entry.objects.create(title=title, rating=rating, body=body, pub_date=pub_date)

    return HttpResponseRedirect(reverse('index'))