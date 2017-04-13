from django.db import models

from accounts.models import User

from utils import get_file_path


class Publication(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(upload_to=get_file_path)
    author = models.ForeignKey(User)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.author, self.added.strftime('%d-%m-%Y'))

    def get_likes_count(self):
        return PublicationLike.objects.filter(publications=self).count()

class PublicationLike(models.Model):
    publications = models.ForeignKey(Publication)
    user = models.ForeignKey(User)
