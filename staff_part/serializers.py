from rest_framework import serializers
from useractions.models import Problem, ProblemDetail

# This serializer works when the Problems are created.
class PostSerializerStaff(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # model Problem, Problem in detail was created in useractions part
    class Meta:
        model = Problem
        fields = ['id', 'title', 'owner', 'status']

# This serializer works when user send a question.
class PostDetailSerializerStaff(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.ReadOnlyField()
    user_question = serializers.ReadOnlyField()
    support_answer = serializers.CharField(default='')

    class Meta:
        model = ProblemDetail
        fields = ['id', 'title_id', 'title', 'user_question', 'support_answer', 'owner']
        ordering = ['title_id']
