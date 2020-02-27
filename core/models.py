from django.db import models


class Note(models.Model):
  title = models.CharField(max_length=250)
  body = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Note title: {self.title} body: {self.body}"