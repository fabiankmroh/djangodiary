from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    pub_date = models.DateTimeField('date written')

    def __str__(self):
        return self.title