from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import TransactionSerializer, TransactionTypeSerializer, TransactionSumSerializer
from .models import Transaction as TransactionModel


class Transaction(generics.ListCreateAPIView):
	serializer_class    = TransactionSerializer
	queryset            = TransactionModel.objects.all()


class TransactionUpdate(generics.RetrieveUpdateAPIView):
	serializer_class    = TransactionSerializer
	queryset            = TransactionModel.objects.all()

	def put(self, request, pk, format=None):
		try:
			data  		= TransactionModel.objects.get(id=pk)
			serializer 	= TransactionSerializer(data, data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return JsonResponse({"status" : "ok"}, status=status.HTTP_200_OK)
		except TransactionModel.DoesNotExist:
					return JsonResponse({"id" :["Id Does Not Exist"]}, status=status.HTTP_400_BAD_REQUEST)
			

class TransactionType(generics.ListAPIView):
	serializer_class 	= TransactionTypeSerializer
	lookup_field 		= 't_type'

	def get_queryset(self):
		t_type = self.kwargs.get(self.lookup_field)
		queryset = TransactionModel.objects.filter(t_type=t_type)
		return queryset

class TransactionSum(generics.RetrieveAPIView):
	serializer_class 	= TransactionSumSerializer
	lookup_field 		= 'pk'

	def get_queryset(self):
		pk = self.kwargs.get(self.lookup_field)
		queryset = TransactionModel.objects.filter(pk=pk)
		return queryset