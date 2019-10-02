from rest_framework import serializers
from .models import Transaction
from django.db.models import Sum, Q

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Transaction
		fields 	=  ('id','amount','parent_id','t_type')


class TransactionTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Transaction
		fields 	=  ('id',)


class TransactionSumSerializer(serializers.ModelSerializer):
	sum	= serializers.SerializerMethodField()
	
	def get_sum(self, obj):
		list_categories = [obj.id]
		total_sum = 0.0
		parent_ids = Transaction.objects.filter(parent_id=obj.id)

		while parent_ids:
			parent_ids = [int(p_id.id) for p_id in parent_ids]
			for c_id in parent_ids:
				list_categories.append(c_id)

			child_category = Transaction.objects.filter(parent_id__in=parent_ids)
			if len(child_category):
				parent_ids = child_category
			else:
				parent_ids = []
		
		# print("final",list_categories)
		for i in list_categories:
			queryset 	= Transaction.objects.filter(id=i)
			totals 		= queryset.aggregate(total_sum=Sum('amount'))
			total_sum 	= total_sum + totals['total_sum']
		
		return total_sum

	class Meta:
		model 	= Transaction
		exclude = ('id','amount','parent_id','t_type','created_at','updated_at')
