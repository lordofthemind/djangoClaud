from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=85)
    content = models.CharField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
    

class Review(models.Model):
    reviewer_name = models.CharField(max_length=85)
    review_title = models.CharField(max_length=85)
    created = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.review_title