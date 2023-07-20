# This File is created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    x = request.POST.get('text', 'default')
    y = request.POST.get('removepunc', 'off')
    z = request.POST.get('fullcap', 'off')
    a = request.POST.get('newlineremover', 'off')
    b = request.POST.get('erasespace', 'off')
    c = request.POST.get('charactercount', 'off')
    d = request.POST.get('remove', 'off')
    e = request.POST.get('remove2', 'off')
    count = 0
    if d=='on':
        txt = request.POST.get('remove_text', 'default')
        e = x.replace(txt, '')
        x = e
    if e=='on':
        txt2 = request.POST.get('remove_text2', 'default')
        txt3 = request.POST.get('remove_text3', 'default')
        e = x.replace(txt2, txt3)
        x = e
    if y=='on':
        e = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in x:
            if char not in punctuations:
                e = e + char
        x = e
    if z=='on':
        e = ''
        e = x.upper()
        x = e
    if a=='on':
        e = ''
        for char in x:
            if char != '\n' and char != '\r':
                e = e + char
        x = e
    if b=='on':
        e = ''
        for index, char in enumerate(x):
            if not(char==' ' and x[index+1]==' '):
                e = e + char
        x = e
    if c=='on':
        e = x
    
    if y=='off' and z=='off' and a=='off' and b=='off' and c=='off' and d=='off' and e=='off':
        return HttpResponse('Error')
    count = len(e)
    params = {'analysed_text' : e, 'character_count': count}
    return render(request, 'removepunc.html', params)