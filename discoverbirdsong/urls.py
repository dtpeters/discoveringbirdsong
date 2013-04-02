from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',  TemplateView.as_view(template_name="index.html")),
    # url(r'^discoverbirdsong/', include('discoverbirdsong.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^notsomuch/', include(admin.site.urls)),
)
