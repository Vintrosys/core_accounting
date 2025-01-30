import frappe
import erpnext.controllers.taxes_and_totals 
from erpnext.utilities.regional import temporary_flag
from erpnext.controllers.taxes_and_totals import get_itemised_tax_breakup_header, get_rounded_tax_amount, update_itemised_tax_data, get_itemised_tax, get_itemised_taxable_amount
from india_compliance.gst_india.overrides.transaction import is_hsn_wise_breakup_needed, get_hsn_wise_breakup, get_item_wise_breakup

# from taxes_and_totals.py
def custom_get_itemised_tax_breakup_html(doc):
	if not doc.taxes:
		return

	# get headers
	tax_accounts = []
	for tax in doc.taxes:
		if getattr(tax, "category", None) and tax.category == "Valuation":
			continue
		if tax.description not in tax_accounts:
			tax_accounts.append(tax.description)

	with temporary_flag("company", doc.company):
		headers = get_itemised_tax_breakup_header(doc.doctype + " Item", tax_accounts)
		itemised_tax_data, itemised_tax, itemised_taxable_amount = custom_get_itemised_tax_breakup_data(doc)
		get_rounded_tax_amount(itemised_tax_data, doc.precision("tax_amount", "taxes"))
		update_itemised_tax_data(doc)

	return frappe.render_template(
		"templates/includes/itemised_tax_breakup.html",
		dict(
			headers=headers,
			itemised_tax_data=itemised_tax_data,
			tax_accounts=tax_accounts,
			doc=doc,
		),
	)

# from taxes_and_totals.py
def custom_get_itemised_tax_breakup_data(doc):
	
	itemised_tax = get_itemised_tax(doc.taxes)
	
	itemised_taxable_amount = get_itemised_taxable_amount(doc.items)

	itemised_tax_data = []
	for item_code, taxes in itemised_tax.items():
		itemised_tax_data.append(
			frappe._dict(
				{"item": item_code, "taxable_amount": itemised_taxable_amount.get(item_code, 0), **taxes}
			)
		)
	return itemised_tax_data, itemised_tax, itemised_taxable_amount

# from transaction.py
def get_itemised_tax_breakup_data(doc):
	itemised_tax = get_itemised_tax(doc.taxes)
	taxable_amounts = get_itemised_taxable_amount(doc.items)

	if is_hsn_wise_breakup_needed(doc.doctype + " Item"):
		return get_hsn_wise_breakup(doc, itemised_tax, taxable_amounts), itemised_tax, taxable_amounts

	return get_item_wise_breakup(itemised_tax, taxable_amounts), itemised_tax, taxable_amounts




