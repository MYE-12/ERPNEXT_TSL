
from frappe import _


def get_data():
	return {
		'fieldname': 'prevdoc_docname',
		'non_standard_fieldnames': {
			'Auto Repeat': 'reference_document',
			'Sales Invoice' : 'quotation',
			'Supplier Quotation':'quotation'
		},
		'transactions': [
			{
				'label': _('Sales Order'),
				'items': ['Sales Order']
			},
			{
				'label': _('Subscription'),
				'items': ['Auto Repeat']
			},
			{
				'label': _('Sales Invoice'),
				'items': ['Sales Invoice']
			},
			{
				'label': _('Supplier Quotation'),
				'items': ['Supplier Quotation']
			}
		]
	}
