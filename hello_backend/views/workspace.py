from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.pagination import StandardPagination
from hello_backend.models import Workspace, WorkspaceMember
from hello_backend.serializers.workspace import WorkspaceSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    queryset = Workspace.objects.all()
    pagination_class = StandardPagination

    def get_queryset(self):
        current_user = self.request.user
        workspaces_have_current_user = WorkspaceMember.objects.all().filter(
            user_id=current_user.id
        )

        queryset = self.queryset.filter(id__in=[
            w.workspace_id for w in workspaces_have_current_user
        ])
        return queryset

    serializer_class = WorkspaceSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        workspace = serializer.save(creator_id=current_user.id)
        WorkspaceMember.objects.create(user_id=workspace.creator_id, workspace_id=workspace.id)
