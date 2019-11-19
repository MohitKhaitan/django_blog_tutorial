from django.db import models


class Article(models.Model):
    """
    To store articles for the blog
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        """
        To display the title as the object name in the admin panel
        :return: Tuple of title for the blog
        """
        return self.title

