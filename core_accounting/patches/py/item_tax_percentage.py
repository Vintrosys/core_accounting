import frappe
@frappe.whitelist()
def item_tax_percentage(item_tax_percentage):
    tax_template = frappe.get_doc("Item Tax Template",item_tax_percentage)
    tax_templates= tax_template.taxes
    tax_total = 0
    if tax_templates:
        for tax in tax_templates:
            tax_total+=tax.tax_rate 
        
    return tax_total
