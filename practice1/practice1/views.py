#I have created this file.
from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def operations(request):
    analyze= request.POST.get('Text','Default')
    removepun=request.POST.get('removepun','off')
    newlinerem = request.POST.get('newlinerem', 'off')
    spacerem=request.POST.get('spacerem', 'off')

    if removepun =='on' or newlinerem =='on' or spacerem == 'on':
        if removepun == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            text=""
            for char in analyze:
                if char not in punctuations:
                    text+=char
            print(text)
            param = {'t1': text}
            analyze = text

        if newlinerem == 'on':
            text=""
            for char in analyze:
                if char !="\n" and char!="\r":
                    text+=char
            print(text)
            param = {'t1': text}
            analyze = text

        if spacerem=='on':
            text=""
            for index,char in enumerate(analyze):
                if not analyze[index] == " ":
                    text+=char
            print(text)
            param = {'t1': text}

    else:
        return HttpResponse("<h2>Please select any operation</h2><br><a href='/'>Back</a>")


    return render(request,'result.html',param)
