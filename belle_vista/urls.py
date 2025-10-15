from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from belle_vista.sitemaps import BlogSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from core.views import serve_media
from django.conf.urls import handler404

sitemaps = {
    "blog": BlogSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("user/", include("userauths.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    re_path(r"^media/(?P<path>.*)$", serve_media),
]

handler404 = 'core.views.error'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)