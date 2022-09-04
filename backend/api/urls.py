from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IngredientsViewSet, RecipesViewSet,
                    SetPasswordAndSubscriptionUserViewSet, TagsViewSet)

app_name = "api"

router = DefaultRouter()
router.register("users", SetPasswordAndSubscriptionUserViewSet, basename="users")
router.register(r"tags", TagsViewSet, basename="tags")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients")
router.register(r"recipes", RecipesViewSet, basename="recipes")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
