from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(request, 'mainsite/home.html',{'title' : 'Song Lyric Search'} )


def albums(request):
    return render(request, 'mainsite/albums.html', {'title', 'Albums and songs'})


def redirect_view(request):
    response = redirect('/redirect-sucess/')
    return response
