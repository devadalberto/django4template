from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views import defaults as default_views
from django.conf.urls.static import static
from .views import home_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('admin/', admin.site.urls)
]

# admin site Headers and Index titles
admin.site.site_header = 'Change your Admin Site Header (urls.py)'
admin.site.index_title = 'Change your Admin Site Index'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
