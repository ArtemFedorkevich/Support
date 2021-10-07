from rest_framework import serializers

from .models import Problem, ProblemDetail


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(default='In progress')
    title = serializers.CharField()

    class Meta:
        model = Problem
        fields = ['id', 'title', 'owner', 'status']


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    user_question = serializers.CharField()
    support_answer = serializers.ReadOnlyField(default='')
    title = serializers.ReadOnlyField()
    title_id = serializers.ReadOnlyField()

    class Meta:
        model = ProblemDetail
        fields = ['id', 'title', 'user_question', 'support_answer', 'title_id', 'owner']
        ordering = ['id']