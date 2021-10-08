from django.db import models

from django.conf import settings


# Model for creation of problems
class Problem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="problems", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='In progress')

    class Meta:
        ordering = ['created']


# Model for adding of questions
class ProblemDetail(models.Model):
    title_id = models.IntegerField(default=1)
    title = models.CharField(max_length=100, default='')
    user_question = models.CharField(max_length=100, blank=True, default='')
    support_answer = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="detail_problems", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
