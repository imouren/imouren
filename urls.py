from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'users.views.index'),
    (r'^regist/$', 'users.views.regist'),
    (r'^(index.xml)$','users.views.index_xml'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns("",
    (r"^media/(?P<path>.*)$", "django.views.static.serve", {'document_root': settings.MEDIA_ROOT})    
)
