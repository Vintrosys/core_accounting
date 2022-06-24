import frappe

def tax_fixing(company,item_code,tax_category,transaction_type,ts_condition):
	separate_item_tax=[]
	total_item_tax=[]
	total_tax_category=[]
	item_data=frappe.get_doc("Item",item_code)
	total_item_tax_details=item_data.__dict__["taxes"]
	if(total_item_tax_details):
		for i in range(0,len(total_item_tax_details),1):
			total_item_tax.append(total_item_tax_details[i].__dict__["item_tax_template"])
			total_tax_category.append(total_item_tax_details[i].__dict__["tax_category"])
		for i in range(0,len(total_item_tax),1):
			if(total_tax_category[i]==tax_category):
				separate_item_tax.append(total_item_tax[i])
		if(separate_item_tax):
			for item_tax_name in separate_item_tax:
				tax_details=frappe.get_doc("Item Tax Template",item_tax_name)
				if(tax_details.__dict__["company"]==company):
					if(tax_details.__dict__["transaction_type"]==""):
						frappe.msgprint("There Is No Transaction Type For Item Tax Template : "+item_tax_name)
						if(ts_condition==1):
							return 0
					else:
						if(tax_details.__dict__["transaction_type"]==transaction_type):
							break
						else:
							item_tax_name=""
				else:
					item_tax_name=""
			if(item_tax_name==""):
				if(ts_condition==0):
					return item_tax_name,2
				else:
					frappe.msgprint("There Is No Tax Template For Item : "+item_code)
					return 0
			else:
				return item_tax_name
		else:
			if(ts_condition==0):
				return 2
			else:
				frappe.msgprint("There Is No Tax Template For Item : "+item_code)
				return 0
	else:
		if(ts_condition==0):
			return 2
		else:
			frappe.msgprint("There Is No Tax Template For Item : "+item_code)
			return 0

@frappe.whitelist()
def tax_template_filtering(company,item_code,tax_category=None,transaction_type=None):
	enable_tax_company=frappe.get_doc("Company",company)
	if(enable_tax_company.__dict__["enable_mulltiple_item_tax_templates"]==1):
		if(tax_category==None or tax_category==""):
			if(enable_tax_company.__dict__["ts_allow_only_tax_applied"]==1):
				frappe.msgprint("Please Select The Tax Category")
				return 0
			if(enable_tax_company.__dict__["ts_allow_tax_with_message"]==1):
				return 1
		else:
			ts_condition=enable_tax_company.__dict__["ts_allow_only_tax_applied"]		
			item_tax_name=tax_fixing(company,item_code,tax_category,transaction_type,ts_condition)
			print(item_tax_name)
			return(item_tax_name)