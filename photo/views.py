from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from .models import Image
from .email import send_welcome_email
from .models import Article,NewsLetterRecipients
from django.http  import HttpResponse,Http404,HttpResponseRedirect
@login_required(login_url='/accounts/login/')

# Create your views here.
def Instagram(request):
    return render(request, 'instagram.html')
  

def photo_of_day(request):
      date = dt.date.today()
      photos = Image.objects.all()
      return render(request, 'all-photo/todays-photo.html', {"date": date,"photo":photos})


def request,image_id):
    try:image(
        photo = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/image.html", {"image":photo})

