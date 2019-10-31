from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^setup_hood$', views.setup_hood, name='setup_hood'),
    url(r'^setup_profile', views.setup_profile, name='setup_profile'),
    url(r'^setup_hood', views.setup_hood, name='setup_profile_hood'),
    url(r'^home/(\d+)$', views.index, name="index"),
    url(r'^profile/(\d+)$', views.user_profile, name='profile'),
    url(r'^profile_update/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^business/(\d+)$', views.business, name='business'),
    url(r'^leave_hood$', views.leave_hood, name='leave_hood'),
    url('accounts/', include('django.contrib.auth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
