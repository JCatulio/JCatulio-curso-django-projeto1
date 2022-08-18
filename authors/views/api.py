from rest_framework.viewsets import ReadOnlyModelViewSet
from ..serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class AuthorViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.filter(username=self.request.user.username)
        return qs
