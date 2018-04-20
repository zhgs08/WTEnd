from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100, blank=True)
	body = models.CharField(max_length=300, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title


