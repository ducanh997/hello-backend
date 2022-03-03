from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.pagination import StandardPagination
from hello_backend.models import Board
from hello_backend.serializers.board import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    queryset = Board.objects.all()
    pagination_class = StandardPagination

    def get_queryset(self):
        return self.queryset

    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(creator_id=current_user.id)
