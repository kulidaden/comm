from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_author_for_user(cls, user):
        try:
            author = cls.objects.get(user=user)
        except cls.DoesNotExist:
            author = cls.objects.create(user=user)
        return author

class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    comment_file = models.FileField(upload_to='comment_files/', null=True, blank=True)

    def __str__(self):
        return f'{self.author.name} - {self.content[:50]}'
