from .models import Problem, ProblemDetail

from rest_framework.generics import ListCreateAPIView

from .serializers import PostSerializer, PostDetailSerializer

from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthenticatedAndOwner

from rest_framework.response import Response

from .renderers import UserJSONRenderer


class PostList(ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        problem = request.data.get('problem', {})
        serializer = self.serializer_class(data=problem)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user, status="In progress")
        return Response(serializer.data)


class PostDetailList(ListCreateAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedAndOwner,)
    renderer_classes = (UserJSONRenderer,)

    def get_queryset(self):
        number = self.kwargs.get('pk')
        queryset = ProblemDetail.objects.filter(title_id=number)
        return queryset

    def perform_create(self, serializer):
        head_id = self.kwargs.get('pk')
        data_problem = Problem.objects.get(pk=head_id)
        serializer.save(owner=self.request.user, title=data_problem.title, title_id=data_problem.id)
