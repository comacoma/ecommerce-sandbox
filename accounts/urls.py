from django.conf.urls import url, include
from accounts.views import *
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registeration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]