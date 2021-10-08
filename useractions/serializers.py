from rest_framework import serializers

from useractions.models import Problem, ProblemDetail


# This is the serializer for adding of problems by user
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(default='In progress')
    title = serializers.CharField()

    class Meta:
        model = Problem
        fields = ['id', 'title', 'owner', 'status']


# This is the serializer for adding of questions by user
class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    user_question = serializers.CharField()
    support_answer = serializers.ReadOnlyField(default='')
    title = serializers.ReadOnlyField()
    title_id = serializers.CharField()

    class Meta:
        model = ProblemDetail
        fields = ['id', 'title', 'user_question', 'support_answer', 'title_id', 'owner']
        ordering = ['id']


# This is the serializer for adding of status by staff
class PostSerializerStaff(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.CharField(default='In progress')
    title = serializers.ReadOnlyField()

    # Model Problem, Problem in detail was created in useractions part
    class Meta:
        model = Problem
        fields = ['id', 'title', 'owner', 'status']


# This is the serializer for adding of answer by staff
class PostDetailSerializerStaff(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.ReadOnlyField()
    user_question = serializers.ReadOnlyField()
    support_answer = serializers.CharField(default='')
    title_id = serializers.ReadOnlyField()

    class Meta:
        model = ProblemDetail
        fields = ['id', 'title_id', 'title', 'user_question', 'support_answer', 'owner']
        ordering = ['title_id']
