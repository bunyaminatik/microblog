from django.conf.urls import patterns, include, url
from django.contrib import admin
import myblog.views
import profiles.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # register process
    # url(r'^register', profiles.views.register, name='register'),
    # url(r'^login', profiles.views.login, name='login'),
    # url(r'^logout', profiles.views.logout, name='logout'),
    # posts
    url(r'^newpost', myblog.views.newpost, name='newpost'),
    url(r'^editpost/(?P<pk>[\d]+)$', myblog.views.editpost, name='editpost'),
    url(r'^deletepost/(?P<pk>[\d]+)$', myblog.views.deletepost, name='deletepost'),
    url(r'^post/(?P<pk>[\d]+)$', myblog.views.detailpost, name='detailpost'),
    # comments
    url(r'^newcomment/(?P<pk>[\d]+)$', myblog.views.newcomment, name='newcomment'),
    url(r'^deletecomment/(?P<pk>[\d]+)$', myblog.views.deletecomment, name='deletecomment'),
	# other
    url(r'^$', myblog.views.home, name='home'),
)
