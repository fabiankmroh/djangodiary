from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date written')

    def __str__(self):
        return self.title + " " + str(self.rating) + " " + str(self.pub_date)

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    ctxt = models.CharField(max_length = 400)
    like = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date written')

