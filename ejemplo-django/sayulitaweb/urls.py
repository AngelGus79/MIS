from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from views import SayulitaView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SayulitaView.as_view(), name='home')
] + static(settings.STATIC_URL)
