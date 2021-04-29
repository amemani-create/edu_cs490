from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from newsapi import NewsApiClient

from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
def newsPaper(request):
    newsapi = NewsApiClient(api_key='573dab4634604cb0a5bc4a55de0f9e50')
    source = 'new-scientist'
    #changed .get_top_headlines to everthing
   # topic = newsapi.get_top_headlines(sources=source)
    topic = newsapi.get_everything(sources=source)
    articles = topic['articles']
    description = []
    newsTitle = []
    img = []
    url = []
    #new scientist source
    for i in range(len(articles)):
        newsInfo = articles[i]
        newsTitle.append(newsInfo['title'])
        description.append(newsInfo['description'])
        img.append(newsInfo['urlToImage'])
        url.append(newsInfo['url'])



    Newslist = zip(newsTitle, description, url, img)

    return render(request, 'news.html', context={"Newslist": Newslist})
