from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Entry, Comment

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
    comment_list = entry.comment_set.order_by('-like')
    
    return render(request, 'diary/detail.html', {
        'entry':entry,
        'entry_id':entry_id,
        'comment_list':comment_list
   })

def new(request):
    return render(request, 'diary/new.html')

def save(request):
    title = request.POST['title']
    rating = int(request.POST['rating'])
    body = request.POST['body']
    pub_date = timezone.now()

    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(image, uploaded_file)

    Entry.objects.create(title=title, rating=rating, body=body, pub_date=pub_date)

    return HttpResponseRedirect(reverse('index'))

def commentsave(request, entry_id):
    ctxt = request.POST['ctxt']
    like = 0
    pub_date = timezone.now()

    entry = get_object_or_404(Entry, pk=entry_id)
    entry.comment_set.create(ctxt=ctxt, like=like, pub_date=pub_date)

    return HttpResponseRedirect(reverse('detail', args=(entry_id,)))