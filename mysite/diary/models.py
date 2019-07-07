from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date written')

    def __str__(self):
        return self.title + str(self.rating) + self.pub_date