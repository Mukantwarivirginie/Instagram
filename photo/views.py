from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from .models import Image,NewArticleForm
from .email import send_welcome_email
# from .models import Article,NewsLetterRecipients
# from django.http  import HttpResponse,Http404,HttpResponseRedirect

# @login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('newsToday')

    else:
        form = NewArticleForm()
    return render(request, 'instagram.html', {"form": form})


# Create your views here.
def welcome(request):
    return render(request, 'Instagram.html')
    return HttpResponse('Welcome to the Instagram')
 
def instagram_of_day(request): 
    date = dt.date.today()
    instagram = Article.todays_news()
    if request.method == 'POST':
        form = InstgramLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstagramLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('news_today')
    else:
        form = InstagramLetterForm()
    return render(request, 'all-instagram/today-instagram.html', {"date": date,"instagram":news,"letterForm":form})






# def news_of_day(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     # return render(request, 'all-news/today-news.html', {"date": date,})
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news})







   # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
def past_days_instagram(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
     return redirect(news_of_day)
     return render(request, 'all-instagram/past-instagram.html',{"date": date,"instagram":news})
    # return render(request, 'all-news/past-news.html', {"date": date})
                                                               
# day = convert_dates(date)
# html = f'''
#         <html>
#             <body>
#                 <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
# return HttpResponse(html)

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-instagram/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-instagram/search.html',{"message":message})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-instagram/article.html", {"article":article})