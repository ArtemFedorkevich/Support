from useractions.models import Problem, ProblemDetail

from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import PostSerializerStaff, PostDetailSerializerStaff

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .renderers import UserJSONRenderer


class PostListStaff(RetrieveUpdateAPIView):
    queryset = Problem.objects.all()
    serializer_class = PostSerializerStaff
    permission_classes = (IsAdminUser, IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)

    # Method to add title when we change status (see PostSerializeStaff)
    def perform_update(self, serializer):
        title_id = self.kwargs.get('pk')
        data_problem = Problem.objects.get(pk=title_id)
        print(data_problem.title)
        serializer.save(title=data_problem.title)


class PostDetailListStaff(RetrieveUpdateAPIView):
    serializer_class = PostDetailSerializerStaff
    permission_classes = (IsAdminUser, IsAuthenticated)
    renderer_classes = (UserJSONRenderer,)

    def get_queryset(self):
        queryset = ProblemDetail.objects.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('pk')
        data_problem = ProblemDetail.objects.get(pk=title_id)
        serializer.save(owner=self.request.user, title=data_problem.title,
                        title_id=data_problem.title_id, user_question=data_problem.user_question
                        )
