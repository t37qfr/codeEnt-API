
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/postings/', include('postings.api.urls',namespace='api-postings')),
]
