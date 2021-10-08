from useractions.models import Problem, ProblemDetail

from useractions.serializers import (PostSerializer, PostDetailSerializer,
                                     PostSerializerStaff, PostDetailSerializerStaff
                                     )

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from useractions.permissions import IsAuthenticatedAndOwner

from rest_framework.response import Response

from rest_framework import viewsets

from django.shortcuts import get_object_or_404


class PostList(viewsets.ViewSet):
    queryset = Problem.objects.all()

    # All authenticated users can create problem, only staff can patch problems.
    def get_permissions(self):
        if self.request.method in ('GET', 'POST'):
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthenticated, IsAdminUser,)

        return super().get_permissions()

    def list(self, request):
        """
        This will return list of problems.
        """
        serializer_class = PostSerializer(self.queryset, many=True)

        return Response(serializer_class.data)

    def create(self, request):
        """
        This will create a problem.
        """
        serializer_class = PostSerializer
        problem = request.data.get('problem', {})
        serializer = serializer_class(data=problem)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user, status="In progress")

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Returns a single problem
        """
        problem = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(problem)

        return Response(serializer_class.data)

    def partial_update(self, request, pk):
        """
        Patch a status
        """
        serializer_class = PostSerializerStaff
        details = Problem.objects.get(pk=pk)
        print(dict(request.data))
        serializer = PostSerializerStaff(details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


# This class shows users questions.
class PostDetailList(viewsets.ViewSet):
    serializer_class = PostDetailSerializer
    queryset = ProblemDetail.objects.all()

    def get_permissions(self):
        if self.request.method in ('GET'):
            self.permission_classes = (IsAuthenticated,)
        elif self.request.method in ('POST'):
            self.permission_classes = (IsAuthenticatedAndOwner,)
        else:
            self.permission_classes = (IsAuthenticated, IsAdminUser,)

        return super().get_permissions()

    def list(self, request):
        serializer_class = PostDetailSerializer(self.queryset, many=True)

        return Response(serializer_class.data)

    def create(self, request):
        question = request.data.get('question', {})
        result = dict(question)
        data_problem = Problem.objects.get(pk=result['title_id'])
        serializer = self.serializer_class(data=question)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user, title=data_problem.title)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Returns a single object
        """
        problemindetail = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostDetailSerializer(problemindetail)

        return Response(serializer_class.data)

    def partial_update(self, request, pk):
        serializer_class = PostDetailSerializerStaff
        detail = ProblemDetail.objects.get(pk=pk)
        print(dict(request.data))
        serializer = PostDetailSerializerStaff(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
