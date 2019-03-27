from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,HttpResponseRedirect,Http404
from .models import Image
from .email import send_welcome_email
from .forms import InstagramForm,ImageForm
from django.contrib.auth.decorators import login_required






# Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    return render(request, 'instagram.html')
    # return HttpResponse('Welcome to the Instagram')


@login_required(login_url='/accounts/login/')
def photo_today(request):

    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['your_name']
            picture = form.cleaned_data['picture']
            like=models.TextFieProfileForm
            HttpResponseRedirecProfileFormtoday
    else:
        form = instagramForm()
    return render(request, 'all-photo/today-photo.html', {"photo":photo,"instagramForm":form})



@login_required(login_url='/accounts/login/')
def instagram_of_day(request):
    
    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstagramRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('photo_today')
    else:
        form = InstagramForm()
  
    return render(request, 'all-photo/todays_pictures.html', {"photo":photo,"InstagramForm":form})    

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = InstagramForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('NewsToday')

    else:
        form = InstagramForm()
    return render(request, 'new_profile.html', {"form": form})






def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})

def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/profile.html", {"profile":profile})