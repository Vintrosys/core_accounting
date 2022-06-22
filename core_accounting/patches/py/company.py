import frappe

@frappe.whitelist()
def property_terminator(ts_property_cdn):
    ts_property_cdn=eval(ts_property_cdn)
    for cdn in ts_property_cdn:
        frappe.delete_doc("Property Setter",cdn)