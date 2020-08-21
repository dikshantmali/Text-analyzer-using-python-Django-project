from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    #all the checkbox value
    removepunc=request.POST.get('removepunc','off')

    uprcase =request.POST.get('uprcasetxt','off')

    nlrmv =request.POST.get('nlremover','off')
    spcrmv =request.POST.get('extraspcremover','off')
    flag = 0
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        flag = 1

    if uprcase =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        flag = 1

    if spcrmv=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        flag = 1

    if nlrmv == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        flag = 1
    if flag == 0:
    	return render(request,'error.html')
    else:
    	return render(request, 'analyze.html', params) 

