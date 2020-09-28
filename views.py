# I have created this file - SWATI
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'Name':'Swati', 'place':'Mars'}
    return render(request, 'index.html')

    # return HttpResponse('''<h1><a href="https://pixabay.com/">Home</a>''')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')

    #check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # if djtext[index] == " " and djtext[index+1] == " ":
            #     pass
            # else:
            #     analyzed = analyzed + char
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(charcounter == "on"):
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed+1
        params = {'purpose': 'Counted Characters', 'analyzed_text': analyzed}

    if(charcounter != "on" and removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please select atleast any one operation and try again.")

    return  render(request, 'analyze.html', params)