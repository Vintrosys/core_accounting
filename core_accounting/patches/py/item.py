
import frappe
import json
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def item_custom_fields():
    custom_fields = {
        "Item":[
            dict(
                fieldname='item_tax',  
                label='Item GST%',
                fieldtype='Link', 
                insert_after='item_tax_section_break', 
                read_only=0,
                options='TS Item Tax'
                 ),
            dict(
                fieldname='column_break_000',
                label='',
                fieldtype='Column Break',
                insert_after='item_tax', 
                read_only=0,
                 ),
            dict(
                fieldname='add',
                label='Add',
                fieldtype='Button',
                insert_after='column_break_000', 
                read_only=0,
                 ),
            dict(
                fieldname='column_break_001',
                label='',
                fieldtype='Column Break',
                insert_after='add', 
                read_only=0,
                 ),
            dict(
                fieldname='remove_row',
                label='Remove',
                fieldtype='Button',
                insert_after='column_break_001', 
                read_only=0,
                 ),
            dict(
                fieldname='section_break_000',
                label='',
                fieldtype='Section Break',
                insert_after='remove_row', 
                read_only=0,
                )
            ]
    }

    create_custom_fields(custom_fields)

@frappe.whitelist()
def item_template_tax(item_tax,tax):
    tax=json.loads(tax)
    item_template=frappe.get_all("Item Tax Template", filters={'tax_template':item_tax,'name':['not in',tax]}, fields=['tax_category','name'])
    return item_template

@frappe.whitelist()
def item_template_remove(item_tax,tax):
    item_template=[i[0] for i in frappe.db.sql(f"""select name
									from `tabItem Tax Template` 
									where tax_template='{item_tax}';
									
								""",as_list=True)]
    tax=json.loads(tax)
    taxes=[]
    for i in range(len(tax)):
        if tax[i]['item_tax_template'] not in item_template:
            taxes.append({'item_tax_template':tax[i]['item_tax_template'],'tax_category':tax[i]['tax_category']})
    return taxes


   
