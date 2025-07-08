from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    score_sum = models.IntegerField(default=0)
    score_count = models.IntegerField(default=0)

    def average_score(self):
        if self.score_count == 0:
            return 0
        return self.score_sum / self.score_count

    def __str__(self):
        return self.title