from django.db import models
from Food.models import Recipe
from User.models import User

#Manager
class CommentQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Comment.PUBLISHED)

class Comment(models.Model):


    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = [(DRAFT, 'Draft'), 
                      (PUBLISHED, 'Published')]


    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='recipe_comment', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', related_name='comment_reply', on_delete=models.CASCADE, null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)    

    # intializing custom manager
    objects = CommentQuerySet.as_manager()

    class Meta:
        ordering = ('-created_at',)  