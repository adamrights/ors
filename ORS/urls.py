from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/exportdata', 'ORS.old_patient_reg.views.exportdata', name='admin'),
    # url(r'^ORS/', include('ORS.foo.urls')),
    url(r'^report/', include('report.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
