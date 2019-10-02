from django.db import models

# Create your models here.
class Transaction(models.Model):
	t_type		   	= models.CharField(max_length=255)
	amount		   	= models.FloatField()
	parent_id  		= models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
	created_at		= models.DateTimeField(auto_now_add=True)
	updated_at		= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'transaction'

	def __str__(self):
		return self.t_type