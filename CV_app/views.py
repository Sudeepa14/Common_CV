from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django.core import serializers
import json


def viewPosts(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    orderBy='-lasteditdate'
    orderByRequest=request.GET.get('orderBy',None)
    #htmlresponse
    browser=request.GET.get('browserView',False)
    print(orderByRequest)
    #stop sql injection
    if(orderByRequest=="viewCount"):
       orderBy='-viewcount'

    if(orderByRequest=="score"):
       orderBy='-score'

    post_list = Post.objects.all().order_by(orderBy)
    context = {
        'post_list': post_list,
    }
    data = serializers.serialize('json', post_list)
    if(browser):
        return render(request, 'posts/index.html', context)

    return HttpResponse(data, content_type="application/json")



def searchPosts(request):

    searchBy=request.GET.get('searchBy','body')
    query=request.GET.get('query','')
    browser=request.GET.get('browserView',False)

    print(searchBy,query)
    # try:
    if(searchBy=="body"):
       post_list = Post.objects.filter(body__contains=query)

    elif(searchBy=="title"):
        post_list = Post.objects.filter(title__contains=query)

    #return all if no search parameter is specified
    else:
        post_list = Post.objects.filter(title__contains=query)

    context = {
        'post_list': post_list,
    }

    data = serializers.serialize('json', post_list)
    #htmlresponse
    if(browser):
        return render(request, 'posts/index.html', context)

    return HttpResponse(data, content_type="application/json")


# def posts(request)
    