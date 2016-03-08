# -*- coding:Utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
import json
import django_filters
from rest_framework import viewsets, filters
from .models import Team
from .accountSerializer import TeamSerializer

# Create your views here.
class JSONResponse(HttpResponse):
        """
        An HttpResponse that renders its content into JSON.
        """
        def __init__(self, data, code, message, token, **kwargs):
            content =json.dumps({'status':{'code':code ,'message': message},'data':[data] },ensure_ascii=False,indent=2)
            kwargs['content_type'] = 'application/json'
            super(JSONResponse, self).__init__(content = content)
            super(JSONResponse, self).__setitem__('X-TWISK-AUTH-TOKEN', token)
            super(JSONResponse, self).__setitem__('X-Content-Type-Options', 'nosniff')
#{'status':{'code':code ,'message': message}, 

@csrf_exempt
def signin(request):
    try:
        data = JSONParser().parse(request)
        user = authenticate(username=data['username'], password=data['password'])
    except:
        return JSONResponse({},'LOGIN0001','error','',status=400)
    if user is not None and user.is_active:
        login(request, user)
        token=Token.objects.get_or_create(user=user)
        return JSONResponse({},'LOGIN0002','success',token[0],status=200)
    else:
        return JSONResponse({},'LOGIN0003','error','',status=400)

@login_required
def signout(request):
    try:
        Token.objects.get(user=request.user).delete()
        ID=request.user.id
        logout(request)
    except:
        return JSONResponse({},'LOGOUT0001','error','',status=400)
    return JSONResponse({"user_id":ID},'LOGOUT0002','success','',status=200)

class TeamViewSet(viewsets.ModelViewSet):
        queryset = Team.objects.all()
        serializer_class = TeamSerializer


