from django.conf.urls import url

from .views import Encode, Decode


urlpatterns = [
    url(r'^encode$', Encode.as_view(), name="encode"),
    url(r'^decode', Decode.as_view(), name="decode"),
]
