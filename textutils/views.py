# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
 
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    counter = 0

    # Check which checkbox is on
    if removepunc == 'on':
        counter = 1
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        counter = 1
        analyzed = ""
        for i in djtext:
            analyzed = analyzed + i.upper()
        params = {'purpose': 'Full Capitalize', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        counter = 1
        analyzed = ""
        for i in djtext:
            if i != '\n' and i!='\r':
                analyzed = analyzed + i
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        counter = 1
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        counter = 1
        k=0
        for i in djtext:
            if i.isalpha():
                k = k+1
        params = {'purpose': 'Count Characters', 'analyzed_text': 'The No. of Characters is : '+str(k)}
        djtext = analyzed

    if counter == 1:
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse(" <br> <h1> Please select any Operation and try again !!!! </h1> <br> <h1> <a href = '/'> Home Page </a> </h1>")
