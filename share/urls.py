
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from products.views import (
    ProductListView,
    UserProductListView,
    ProductCreateView,
    CreateCheckoutSessionView,
    SuccessView,
    stripe_webhook
)
from users.views import UserProfileView, StripeAccountLinkView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="pages/base.html"), name="home"),
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("discover/", ProductListView.as_view(), name='discover'),
    path('products/', UserProductListView.as_view(), name='user-products'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path("create-checkout-session/<slug>/", CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('stripe/auth/', StripeAccountLinkView.as_view(), name='stripe-account-link'),
    path("p/", include('products.urls', namespace='products')),
    path('success/', SuccessView.as_view(), name='success'),
    path("webhooks/stripe/", stripe_webhook, name='stripe-webhook'),
]


# API URLS
urlpatterns += [
    # API base url
    path("api/", include("share.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)