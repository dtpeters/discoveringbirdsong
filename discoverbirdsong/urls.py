from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from accounts.views import user_rating_form



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',  TemplateView.as_view(template_name="index.html")),
    # url(r'^discoverbirdsong/', include('discoverbirdsong.foo.urls')),
    (r'^rating-for-recording/', ''),
                       

    # Uncomment the next line to enable the admin:
    url(r'^notsomuch/', include(admin.site.urls)),
)
