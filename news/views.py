from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate
from django.contrib.postgres.search import TrigramSimilarity
import django.contrib.postgres
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from bs4 import BeautifulSoup
from .models import NewsData, Aboutus, Reference, Team, Partners, Contacts

def index(request):
#    news_data = NewsData.objects.order_by('-pub_date')
    return redirect('/news/')

def teammembers(request):
    return render(request, 'teammembers.html',  {'team': Team.objects.all(), 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0] })

def aboutus(request):
    return render(request, 'aboutus.html',  {'aboutus': Aboutus.objects.all()[0], 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0]})

def reference(request):
    reference_list = Reference.objects.all()
    paginator = Paginator(reference_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        references = paginator.page(paginator.num_pages)
    return render(request, 'media_about.html', {'references': references, 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0]})

def news(request):
    data = {
        'news': NewsData.objects.order_by("-pub_date")[:4].all(),
        'slides': NewsData.objects.filter(slider=True).order_by("-pub_date")[:3].all(),
        'partners': Partners.objects.all(),
        'contacts':Contacts.objects.all()[0]
    }
    for x in data['news']:
        soup = BeautifulSoup(x.text)
        x.text = (soup.text)[:130] + ' ...'
        x.text = x.text.replace("&nbsp", " ");

    for x in data['slides']:
        soup = BeautifulSoup(x.text)
        x.text = (soup.text)[:130] + ' ...'
        x.text = x.text.replace("&nbsp", " ");

    return render(request, 'index.html',  data)

def activity(request):
    news_list = NewsData.objects.filter(activity=True).all()
    paginator = Paginator(news_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    for n in news:
        soup = BeautifulSoup(n.text)
        n.text = (soup.text)[:130] + ' ...'
        n.text = n.text.replace("&nbsp", " ");

    return render(request, 'activity.html', {'activity_news': news, 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0] })

def monitoring(request):
    news_list = NewsData.objects.filter(monitoring=True).all()
    paginator = Paginator(news_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    for n in news:
        soup = BeautifulSoup(n.text)
        n.text = (soup.text)[:130] + ' ...'
        n.text = n.text.replace("&nbsp", " ");

    return render(request, 'monitoring.html', {'monitoring_news': news, 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0] })

def fullread(request, id_news):
    return render(request, 'News.html',  {'news_detail': NewsData.objects.get(pk=id_news), 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0]})

def donate(request):
    return render(request, 'donate.html',  {'donate': 1, 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0]})

def contacts(request):
    return render(request, 'contacts.html',  {'contacts': Contacts.objects.all()[0], 'partners': Partners.objects.all()})

def partners(request):
    return render(request, 'partners.html', {'partners': Partners.objects.all(), 'partnerspage': [1], 'contacts':Contacts.objects.all()[0]})

def search(request):
    keywords = request.POST.get('search_input', '')
    vector = SearchVector('text', 'title')
    query = SearchQuery(keywords)
    news_list = NewsData.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.04).order_by('-rank')
    #news_list = NewsData.objects.annotate(similarity=TrigramSimilarity('text', keywords),).filter(similarity__gt=0.3).order_by('-similarity')
    paginator = Paginator(news_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    for n in news:
        soup = BeautifulSoup(n.text)
        n.text = (soup.text)[:130] + ' ...'
        n.text = n.text.replace("&nbsp", " ");

    return render(request, 'searchnews.html', {'searchnews': news, "keywords": keywords, 'partners': Partners.objects.all(), 'contacts':Contacts.objects.all()[0] })
