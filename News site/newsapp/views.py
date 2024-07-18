from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    local_url = requests.get("https://inshortsapi.vercel.app/news?category=hatke")
    local_data = local_url.json()
    print(local_data['data'][0]['author'])

    world_url = requests.get("https://inshortsapi.vercel.app/news?category=world")
    world_data = world_url.json()
    print(world_data['data'][0]['author'])

    entertainment_url = requests.get("https://inshortsapi.vercel.app/news?category=entertainment")
    entertainment_data = entertainment_url.json()
    print(entertainment_data['data'][0]['author'])

    context = {
        'localnewsdata': local_data['data'],
        'worldnewsdata': world_data['data'],
        'entertainmentnewsdata': entertainment_data['data']
    }

    return render(request, 'index.html', context)

def sports(request):
    url=requests.get("https://inshortsapi.vercel.app/news?category=sports")
    mydata=url.json()
    print(mydata['data'][0]['author'])
    context={
        'sportsdata':mydata['data']
    }
    return render(request, 'sports.html',context)

def search(request):
    category=request.GET.get("query")
    response = requests.get("https://inshortsapi.vercel.app/news?category=" + category)
    mydata = response.json()
    print(mydata['data'][0]['author'])
    context={
        'newsdata':mydata['data']
    }
    return render(request, 'search.html',context)

def technology(request):
    url=requests.get("https://inshortsapi.vercel.app/news?category=technology")
    mydata=url.json()
    print(mydata['data'][0]['author'])
    context={
        'techdata':mydata['data']
    }
    return render(request, 'technology.html',context)

def politics(request):
    url=requests.get("https://inshortsapi.vercel.app/news?category=politics")
    mydata=url.json()
    print(mydata['data'][0]['author'])
    context={
        'politicsdata':mydata['data']
    }
    return render(request, 'politics.html',context)
