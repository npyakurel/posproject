from django.db import models

class Book(models.Model):
	title=models.CharField(max_length=100)
	pages=models.IntegerField()

	def __str__(self):
		return self.title

def get_absolute_url(self):
	return reverse('bookdetail',kwargs={'pk':str(self.pk)})