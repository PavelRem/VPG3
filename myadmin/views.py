from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
import datetime
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from PIL import Image
from news.models import NewsData, Aboutus, Team, Reference, Images, Partners, Contacts
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import json
import os
from bs4 import BeautifulSoup


def upload(request):
    if request.FILES.get('file', ''):
        obj = Images.objects.create()
        obj.img = request.FILES.get('file', '')
        obj.save()
        compres_img("/home/shostatscky.andriy/myproject/media/news/"+request.FILES['file'].name)
        return HttpResponse(obj.img_url)
    else:
        return HttpResponse("Error in Sending Email")

def login_user(request):
    logout(request)
    username = password = ''
    wrong_input = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/admin/news')
                #return redirect(request.GET('next')
        wrong_input = True
    return render(request, 'form.html',  {'wrong_input': wrong_input})

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/admin/login/')
def image(request):
    return render(request, 'image.html',  {'images': Images.objects.all()})

@login_required(login_url='/admin/login/')
def image_add(request):
    if request.method == "POST":
        obj = Images.objects.create()
        if request.FILES.get('image', ''):
            obj.img = request.FILES.get('image', '')
            obj.save()
        if request.FILES.get('image', ''):
            compres_img("/home/shostatscky.andriy/myproject/media/news/"+request.FILES['image'].name)
        return redirect('/admin/image/')

    return render(request, 'image_add.html',  {})

@login_required(login_url='/admin/login/')
def image_change(request, id):
    if request.method == "POST":
        obj = Images.objects.get(pk=id)
        if request.FILES.get('image', ''):
            obj.img = request.FILES.get('image', '')
        obj.save()
        if request.FILES.get('image', ''):
            compres_img("/home/shostatscky.andriy/myproject/media/news/"+request.FILES['image'].name)
        return redirect('/admin/image/')
    return render(request, 'image_change.html',  {'image': Team.objects.get(pk=id)})

@login_required(login_url='/admin/login/')
def image_delete(request, id):
    Images.objects.get(pk=id).delete()
    return redirect('/admin/image/')

@login_required(login_url='/admin/login/')
def activ(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.activity = False if obj.activity else True
        obj.save()
        print("activity ", obj.activity)
        return HttpResponse("true");
    return HttpResponse("false");

@login_required(login_url='/admin/login/')
def monitor(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.monitoring = False if obj.monitoring else True
        obj.save()
        return HttpResponse("true");
    return HttpResponse("false");

@login_required(login_url='/admin/login/')
def slider(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.slider = False if obj.slider else True
        obj.save()
    return HttpResponse("false");

@login_required(login_url='/admin/login/')
def news_update(request, id):
    return render(request, 'news_update.html',  {'news': NewsData.objects.get(pk=id)})

def compres_img(path):
    im = Image.open(path)
    im.save(path, format="JPEG", quality=35)

@login_required(login_url='/admin/login/')
def news_update_save(request, id):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=id)
        obj.title = request.POST.get('title', '')
        obj.text = request.POST.get('text', '')
        pub_date = request.POST.get('date', '')

        if '/' in pub_date:
            date_lst = pub_date.split('/')
        elif '-' in pub_date:
            date_lst = pub_date.split('-')
        else:
            date_lst = pub_date.split('.')

        if len(date_lst[0]) > 2:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])
        else:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])

        obj.pub_date = datetime.date(year, month, day)
        if request.FILES.get('photo', ''):
            obj.img = request.FILES.get('photo', '')
        obj.save()
        if request.FILES.get('photo', ''):
            compres_img("/home/shostatscky.andriy/myproject/media/news/"+request.FILES['photo'].name)
        return redirect('/admin/news')
    return render(request, 'news_update.html',  {'news': NewsData.objects.all()})

@login_required(login_url='/admin/login/')
def news_delete(request, id):
    obj = NewsData.objects.get(pk=id)
    soup = BeautifulSoup(obj.text)
    imgs = soup.findAll('img').get('src')
    for img in images:
        os.remove("/home/shostatscky.andriy/myproject" + img)
    obj.delete()
    return redirect('/admin/news')

@login_required(login_url='/admin/login/')
def news_add(request):
    if request.method == "POST":
        obj = NewsData.objects.create()
        obj.title = request.POST.get('title', '')
        obj.text = request.POST.get('text', '')
        pub_date = request.POST.get('date', '')

        if '/' in pub_date:
            date_lst = pub_date.split('/')
        elif '-' in pub_date:
            date_lst = pub_date.split('-')
        else:
            date_lst = pub_date.split('.')

        if len(date_lst[0]) > 2:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])
        else:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])

        obj.pub_date = datetime.date(year, month, day)
        obj.activity = True if request.POST.get('activ', '') else False
        obj.monitoring =  True if request.POST.get('monitor', '') else False
        obj.slider =  True if request.POST.get('slider', '') else False
        if request.FILES.get('photo', ''):
            obj.img = request.FILES.get('photo', '')
        obj.save()
        if request.FILES.get('photo', ''):
            compres_img("/home/shostatscky.andriy/myproject/media/news/"+request.FILES['photo'].name)
        return redirect('/admin/news')

    return render(request, 'news_add.html',  {'news': NewsData.objects.all(), 'images': Images.objects.all()})

@login_required(login_url='/admin/login/')
def adminindex(request):
    return redirect('/admin/news')

@login_required(login_url='/admin/login/')
def news(request):
    news_list = NewsData.objects.all().order_by('-pub_date')
    paginator = Paginator(news_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'news': news })

@login_required(login_url='/admin/login/')
def reference(request):
    reference_list = Reference.objects.all().order_by('-pub_date')
    paginator = Paginator(reference_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        references = paginator.page(paginator.num_pages)
    return render(request, 'reference.html', {'references': references })

@login_required(login_url='/admin/login/')
def reference_add(request):
    return render(request, 'ref_add.html',  {})

@login_required(login_url='/admin/login/')
def reference_add_save(request):
    if request.method == "POST":
        obj = Reference.objects.create()
        obj.title = request.POST.get('title', '')
        obj.link = request.POST.get('link', '')
        obj.source = request.POST.get('source', '')
        pub_date = request.POST.get('date', '')

        if '/' in pub_date:
            date_lst = pub_date.split('/')
        elif '-' in pub_date:
            date_lst = pub_date.split('-')
        else:
            date_lst = pub_date.split('.')

        if len(date_lst[0]) > 2:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])
        else:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])

        obj.pub_date = datetime.date(year, month, day)
        obj.save()
        return redirect('/admin/reference')
    return render(request, 'reference.html',  {'references': Reference.objects.all()})

@login_required(login_url='/admin/login/')
def reference_update(request, id):
    return render(request, 'ref_update.html',  {'ref': Reference.objects.get(pk=id)})

@login_required(login_url='/admin/login/')
def reference_update_save(request, id):
    if request.method == "POST":
        obj = Reference.objects.get(pk=id)
        obj.title = request.POST.get('title', '')
        obj.link = request.POST.get('link', '')
        obj.source = request.POST.get('source', '')
        pub_date = request.POST.get('date', '')

        if '/' in pub_date:
            date_lst = pub_date.split('/')
        elif '-' in pub_date:
            date_lst = pub_date.split('-')
        else:
            date_lst = pub_date.split('.')

        if len(date_lst[0]) > 2:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])
        else:
            year = int(date_lst[0])
            month = int(date_lst[1])
            day = int(date_lst[2])

        obj.pub_date = datetime.date(year, month, day)
        obj.save()
        return redirect('/admin/reference')
    return render(request, 'reference.html',  {'references': Reference.objects.all()})

@login_required(login_url='/admin/login/')
def reference_delete(request, id):
    Reference.objects.get(pk=id).delete()
    return redirect('/admin/reference/')

@login_required(login_url='/admin/login/')
def team(request):
    return render(request, 'team.html',  {'team': Team.objects.all()})

@login_required(login_url='/admin/login/')
def team_add(request):
    if request.method == "POST":
        obj = Team.objects.create()
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('descrip', '')
        obj.fb = request.POST.get('fb', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/team/')

    return render(request, 'team_add.html',  {})

@login_required(login_url='/admin/login/')
def team_change(request, id):
    if request.method == "POST":
        obj = Team.objects.get(pk=id)
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('descrip', '')
        if request.FILES.get('photo', ''):
            obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/team/')
    return render(request, 'team_change.html',  {'member': Team.objects.get(pk=id)})

@login_required(login_url='/admin/login/')
def team_delete(request, id):
    Team.objects.get(pk=id).delete()
    return redirect('/admin/team/')

@login_required(login_url='/admin/login/')
def about(request):
    try:
        return render(request, 'about.html',  {'info': Aboutus.objects.all()[0].text})
    except:
        return render(request, 'about.html',  {'info': ''})

@login_required(login_url='/admin/login/')
def change_aboutus(request):
    if Aboutus.objects.all().count():
        obj = Aboutus.objects.all()[:1].get()
    else:
        obj = Aboutus.objects.create()
    obj.text = request.POST['text']
    obj.save()
    return redirect('/admin/about')

@login_required(login_url='/admin/login/')
def partners(request):
    return render(request, 'partners_adm.html',  {'partners': Partners.objects.all()})

@login_required(login_url='/admin/login/')
def partners_add(request):
    return render(request, 'partners_add.html',  {})

@login_required(login_url='/admin/login/')
def partners_add_save(request):
    if request.method == "POST":
        obj = Partners.objects.create()
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('text', '')
        obj.link = request.POST.get('ref', '')
        if request.FILES.get('photo', ''):
            obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/partners/')

    return render(request, 'partners_adm.html',  {'partners': Partners.objects.all()})

@login_required(login_url='/admin/login/')
def partners_update(request, id):
    return render(request, 'partner_update.html',  {'partner': Partners.objects.get(pk=id)})

@login_required(login_url='/admin/login/')
def partners_update_save(request, id):
    if request.method == "POST":
        obj = Partners.objects.get(pk=id)
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('text', '')
        obj.link = request.POST.get('ref', '')
        if request.FILES.get('photo', ''):
            obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/partners')
    return render(request, 'partners_admdatefrom.html',  {'partners': Partners.objects.all()})

@login_required(login_url='/admin/login/')
def partners_delete(request, id):
    Partners.objects.get(pk=id).delete()
    return redirect('/admin/partners/')

@login_required(login_url='/admin/login/')
def contacts(request):
    try:
        return render(request, 'contactsmng.html',  {'info': Contacts.objects.all()[0] })
    except:
        return render(request, 'contactsmng.html',  {})

@login_required(login_url='/admin/login/')
def change_contacts(request):
    if Contacts.objects.all().count():
        obj = Contacts.objects.all()[:1].get()
    else:
        obj = Contacts.objects.create()
    obj.number = request.POST['tel']
    obj.email = request.POST['email']
    obj.address = request.POST['address']
    obj.save()
    return redirect('/admin/contacts')

@login_required(login_url='/admin/login/')
def users(request):
    return render(request, 'users.html',  {'users': User.objects.all()})

@login_required(login_url='/admin/login/')
def user_add(request):
    return render(request, 'user_add.html', {})

@login_required(login_url='/admin/login/')
def user_update(request, id):
    return render(request, 'user_add.html',  {'prtcl_user': User.objects.get(pk=id)})

@login_required(login_url='/admin/login/')
def user_add_save(request):
    user = User.objects.create_user(
        username=request.POST.get('name', ''),
        email=request.POST.get('email', ''),
        password=request.POST.get('password', '')
    )
    user.save()
    return redirect('/admin/users')

@login_required(login_url='/admin/login/')
def user_update_save(request, id):
    user = User.objects.get(pk=id)
    if not user.check_password(request.POST.get('password', '')):
        return render(request, 'user_add.html',  {'prtcl_user': User.objects.get(pk=id), 'nomatch': 1})
    user.is_superuser = True
    user.set_password(request.POST.get('password_check', ''))
    user.username = request.POST.get('name', '')
    user.email = request.POST.get('email', '')
    user.save()
    return redirect('/admin/users')

@login_required(login_url='/admin/login/')
def user_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/admin/users')
