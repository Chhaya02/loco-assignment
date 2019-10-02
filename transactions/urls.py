from django.conf.urls import url
from . import views

urlpatterns = [
	# Api's
	url(r'^transaction/types/(?P<t_type>\w+)/$',views.TransactionType.as_view(),name='meetup-detail-slug'),
	url(r'^transaction/add/$', views.Transaction.as_view(), name='transaction-create'),
	url(r'^transaction/sum/(?P<pk>[0-9]+)/$', views.TransactionSum.as_view(), name='transaction-sum'),
	url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view(), name='transaction-update'),


]