import frappe
@frappe.whitelist()
def property_creator():
    ts_new_tax_category=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Item Tax Template",
        'property':"reqd",
        'field_name':"tax_category",
        "value":0
    })
    ts_new_tax_category.insert()
    ts_new_tax_category.save()

    ts_new_transaction_type=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Item Tax Template",
        'property':"reqd",
        'field_name':"transaction_type",
        "value":0
    })
    ts_new_transaction_type.insert()
    ts_new_transaction_type.save()
    return ts_new_tax_category.name, ts_new_transaction_type.name
@frappe.whitelist()
def property_terminator(ts_property_cdn):
    ts_property_cdn=eval(ts_property_cdn)
    for cdn in ts_property_cdn:
        frappe.delete_doc("Property Setter",cdn)