from django.conf.urls import include, url
from board import urls as appurls
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'message_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(appurls)),
    url(r'^admin/', admin.site.urls),
]
