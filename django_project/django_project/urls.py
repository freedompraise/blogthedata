"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_project.sitemaps import (
    PostSitemap,
    HomeSitemap,
    WorksCitedSiteMap,
    CategorySiteMap,
)
from .views import (
    works_cited_view,
    privacy_view,
    security_txt_view,
    security_pgp_key_view,
)
from users.views import (
    register_view,
    profile_view,
    MyLoginView,
    MyLogoutView,
    MyPasswordResetView,
    MyPasswordResetDoneView,
    MyPasswordResetConfirmView,
    MyPasswordResetCompleteView,
)
from siteanalytics.views import (
    leaflet_map_view,
    openlayers_map_view,
    maplibre_map_view,
    mapbox_map_view
)


sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySiteMap,
    "home page": HomeSitemap,
    "Works Cited": WorksCitedSiteMap,
}

urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("works-cited", works_cited_view, name="works-cited"),
    path("privacy", privacy_view, name="privacy"),
    path("leaflet-map", leaflet_map_view, name="leaflet-map"),
    path("openlayers-map", openlayers_map_view, name="openlayers-map"),
    path("maplibre-map", maplibre_map_view, name="maplibre-map"),
    path("mapbox-map", mapbox_map_view, name="mapbox-map"),
    path("admin/", admin.site.urls),
    path(".well-known/security.txt", security_txt_view, name="security-txt"),
    path("pgp-key.txt", security_pgp_key_view, name="security-pgp-key-txt"),
    path("robots.txt", include("robots.urls")),
    path("", include("blog.urls")),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path(
        "login/",
        MyLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        MyLogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        MyPasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        MyPasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        MyPasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        MyPasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("captcha", include("captcha.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "django_project.views.handler_404"
