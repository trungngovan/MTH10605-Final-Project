from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class CRUDViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """CRUD viewset for api views."""


class ReadOnlyViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """Read only viewset for api views."""


class CreateOnlyViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    """Create only viewset for api views."""