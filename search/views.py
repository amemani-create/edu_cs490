from django.shortcuts import render
import requests


# Create your views here.
def customSearch(request):
    listForSearch = []
    if request.method =='POST':
        customSearch_url = 'https://www.googleapis.com/customsearch/v1'
        for_customSearch = {

            'q': request.POST['search'],
            'title': 'title',
            'snippet': 'snippet',
            'key': 'AIzaSyCrhQKutOoqcaKJdbvbCJA9LEj0XezVj20',
            'cx': '58809daec6b6edb20',
            'num': 5,
            'link' : 'link'

        }
        request_for_customSearch = requests.get(customSearch_url, params=for_customSearch)
        results = request_for_customSearch.json()['items']

        for result in results:
            Information_For_Search = {
                'title': result['title'],
                'snippet': result['snippet'],
                'link': result['link']


            }
            listForSearch.append(Information_For_Search)
    context = {

        'SearchList': listForSearch

    }

    return render(request, 'search/index.html',context)