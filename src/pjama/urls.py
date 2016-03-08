"""pjama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pjama.account.urls import router as accountRouter
from pjama.log.urls import router as logRouter
from pjama.problem.urls import router as problemRouter

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'pjama.account.views.signin'),
    url(r'^logout/$', 'pjama.account.views.signout'),
    url(r'^api/', include(accountRouter.urls)),
    url(r'^api/', include(logRouter.urls)),
    url(r'^api/', include(problemRouter.urls)),
]

