from django.db import models

# Create your models here.
class Poll(models.Model):
    question_text = models.CharField(max_length=255)

    def ___str__(self):
        return self.question_text


class Choice(models.Model):
    text = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
