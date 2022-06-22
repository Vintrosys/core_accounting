from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():

    custom_fields = {
		"Company": [
			dict(fieldname='tax_settings', label='Tax Settings',
				fieldtype='Section Break', insert_after='total_monthly_sales', read_only=0),
			dict(fieldname='enable_mulltiple_item_tax_templates', label='Enable Mulltiple Item Tax Templates',
				fieldtype='Check', description='Automatic tax template update based on item',insert_after='tax_settings', read_only=0),
			dict(fieldname='ts_allow_tax_with_message', label='Allow tax with message',
				fieldtype='Check', depends_on='eval:doc.enable_mulltiple_item_tax_templates==1 && doc.ts_allow_only_tax_applied==0',insert_after='enable_mulltiple_item_tax_templates'),
			dict(fieldname='ts_allow_only_tax_applied', label='Allow only tax applied',
				fieldtype='Check', depends_on='eval:doc.enable_mulltiple_item_tax_templates==1 && doc.ts_allow_tax_with_message==0',insert_after='ts_allow_tax_with_message', read_only=0),
		],
		"Item Tax Template":[
			dict(fieldname='tax_category', label='Tax Category',
				fieldtype='Link', options='Tax Category',Mandatory=1,insert_after='taxes', read_only=0),
			dict(fieldname='transaction_type', label='Transaction Type',
				fieldtype='Select', options='\nSales\nPurchase',Mandatory=1,insert_after='tax_category'),
		]
	}
    create_custom_fields(custom_fields)
    print('finished')