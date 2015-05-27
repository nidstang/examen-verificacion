from django.conf.urls import patterns, include, url

from blog.views import home, create_post, get_posts

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen.views.home', name='home'),
    # url(r'^examen/', include('examen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^home/$', home, name="home"),
    url(r'^create/$', create_post, name="create"),
    url(r'^posts/$', get_posts, name="posts"),
)
