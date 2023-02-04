from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from auction.views import *


urlpatterns = [
    path('', home.as_view(), name="home"),
    path('login/', loginView.as_view(), name="logIn"),
    path('logout/',logoutView.as_view(), name="logOut"),
    path('index/', home.as_view(), name="home"),
    path('bought/', bought.as_view(), name="bought"),
    path('bidItem/', bidItem.as_view(), name="bidItem"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
