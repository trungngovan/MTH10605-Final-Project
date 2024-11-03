from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path

router = DefaultRouter()
router.register(
    r"keyword",
    views.KeywordViewSet,
    basename="keyword",
)
router.register(
    r"result",
    views.ResultViewSet,
    basename="result",
)



urlpatterns = [
    path(
        "predict/",
        views.PredictAPIView.as_view(),
        name="predict",
    ),
    *router.urls,
]