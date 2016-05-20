from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^top/', include('top.urls')),
    url(r'^article/', include('article.urls', namespace='article')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'top.views.top', name='root'),
    url(r'^account/', include('account.urls')),
    url(r'^upload/', include('upload.urls',namespace='upload')),

]
# okie the url has been changed and now working well
# the next step is configure and see what is working
# you still have 20 mins for working with it
# i believe you can done this night.
# it should be done ...

# urlpatterns = patterns('',
#     (r'^', include('upload.urls',namespace='upload')),
#     url(r'^top/', include('top.urls')),
#     url(r'^account/', include('account.urls')),
#
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
