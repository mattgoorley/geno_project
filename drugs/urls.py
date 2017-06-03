from django.conf.urls import url
from drugs.views import *

urlpatterns = [
    url(r'^mechanisms/$', GetMechanism.as_view(), name='mechanisms'),
    url(r'^drugs/$', GetDrug.as_view(), name='getdrug'),
    url(r'^entitylookup/$', EntityLookup.as_view(), name='entitylookup'),
    # url(r'^seed$', SeedDB.as_view(), name='seed'),
    url(r'^$', IndexView.as_view(), name='index'),
]
