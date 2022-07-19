from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from core_accounting.patches.py.item import item_custom_fields
def execute():
	fields()
	# item_custom_fields()

def fields():
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
		# "Item Tax Template":[
		# 	dict(fieldname='tax_category', label='Tax Category',
		# 		fieldtype='Link', options='Tax Category',reqd=1,insert_after='taxes', read_only=0),
		# 	dict(fieldname='transaction_type', label='Transaction Type',
		# 		fieldtype='Select', options='\nSales\nPurchase',reqd=1,insert_after='tax_category'),
		# 	dict(fieldname='tax_template', label='Item GST%',
		# 		fieldtype='Link', options='TS Item Tax',insert_after='title',read_only=0),
		# ],
		"Sales Invoice":[
			dict(fieldname='ts_tax_breakup', label='Tax Breakup GST',
				fieldtype='Section Break',insert_after='total_taxes_and_charges',hidden=1),
		
			dict(fieldname='ts_tax_breakup_table', label='Tax Breakup GST Table',
				fieldtype='Table', options='TS Tax Breakup',insert_after='ts_tax_breakup',read_only=1),

			dict(fieldname='ts_tax_breakup_hsn', label='Tax Breakup HSN',
				fieldtype='Section Break', insert_after='ts_tax_breakup_table',hidden=1),
			
			dict(fieldname='ts_tax_breakup_gst_table', label='Tax Breakup HSN Table',
				fieldtype='Table', options='TS Tax Breakup HSN',insert_after='ts_tax_breakup_hsn',read_only=1),
		],
		"Sales Order":[
			
			dict(fieldname='ts_tax_breakup', label='Tax Breakup GST',
				fieldtype='Section Break',insert_after='total_taxes_and_charges',hidden=1),
		
			dict(fieldname='ts_tax_breakup_table', label='Tax Breakup GST Table',
				fieldtype='Table', options='TS Tax Breakup',insert_after='ts_tax_breakup',read_only=1),

			dict(fieldname='ts_tax_breakup_hsn', label='Tax Breakup HSN',
				fieldtype='Section Break', insert_after='ts_tax_breakup_table',hidden=1),
			
			dict(fieldname='ts_tax_breakup_gst_table', label='Tax Breakup HSN Table',
				fieldtype='Table', options='TS Tax Breakup HSN',insert_after='ts_tax_breakup_hsn',read_only=1),
		],
		"Sales Order Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"Purchase Order Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"Purchase Order": [
                    dict(fieldname='ts_tax_breakup', label='Tax Breakup GST',
				fieldtype='Section Break',insert_after='total_taxes_and_charges',hidden=1),
		
		dict(fieldname='ts_tax_breakup_table', label='Tax Breakup GST Table',
				fieldtype='Table', options='TS Tax Breakup',insert_after='ts_tax_breakup',read_only=1),

		dict(fieldname='ts_tax_breakup_hsn', label='Tax Breakup HSN',
				fieldtype='Section Break', insert_after='ts_tax_breakup_table',hidden=1),
			
		dict(fieldname='ts_tax_breakup_gst_table', label='Tax Breakup HSN Table',
				fieldtype='Table', options='TS Tax Breakup HSN',insert_after='ts_tax_breakup_hsn',read_only=1),
        ],
		"Purchase Invoice": [
                    dict(fieldname='ts_tax_breakup', label='Tax Breakup GST',
				fieldtype='Section Break',insert_after='total_taxes_and_charges',hidden=1),
		
		dict(fieldname='ts_tax_breakup_table', label='Tax Breakup GST Table',
				fieldtype='Table', options='TS Tax Breakup',insert_after='ts_tax_breakup',read_only=1),

		dict(fieldname='ts_tax_breakup_hsn', label='Tax Breakup HSN',
				fieldtype='Section Break', insert_after='ts_tax_breakup_table',hidden=1),
			
		dict(fieldname='ts_tax_breakup_gst_table', label='Tax Breakup HSN Table',
				fieldtype='Table', options='TS Tax Breakup HSN',insert_after='ts_tax_breakup_hsn',read_only=1),
        ],
		"Purchase Invoice Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"Sales Invoice Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"Delivery Note Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"Purchase Receipt Item": [
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1
                    ),
        ],
		"POS Invoice":[
			dict(fieldname='ts_tax_breakup', label='Tax Breakup GST',
				fieldtype='Section Break',insert_after='total_taxes_and_charges',hidden=1),
		
			dict(fieldname='ts_tax_breakup_table', label='Tax Breakup GST Table',
				fieldtype='Table', options='TS Tax Breakup',insert_after='ts_tax_breakup',read_only=1),

			dict(fieldname='ts_tax_breakup_hsn', label='Tax Breakup HSN',
				fieldtype='Section Break', insert_after='ts_tax_breakup_table',hidden=1),
			
			dict(fieldname='ts_tax_breakup_gst_table', label='Tax Breakup HSN Table',
				fieldtype='Table', options='TS Tax Breakup HSN',insert_after='ts_tax_breakup_hsn',read_only=1),
		],
		"POS Invoice Item":[
                    dict(
                        fieldname= "ts_item_gst",
                        fieldtype= "Data",
                        insert_after= "price_list_rate",
                        label= "Item GST",
						read_only=1,
						hidden=1
                    ),
        ]

	}
    create_custom_fields(custom_fields)
