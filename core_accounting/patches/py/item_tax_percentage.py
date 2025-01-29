from erpnext.controllers.taxes_and_totals import get_itemised_tax_breakup_data
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

def item_tax_amount(doc,event):
    if(doc.docstatus == 1):return
    ts_value=frappe.get_doc("Core Accounting Settings")
    if ts_value.itemwise_tax_fetching==1:
        if doc:
            if doc.tax_category:
                ts_main_tax_category=doc.tax_category
                ts_tax_type=[]
                tax_desc=doc.taxes
                for tax in tax_desc:
                    ts_tax_type.append(tax.description)
                ts_tax_category=[]
                ts_tax_percentage_amount=[]
                cgst_tax=[]
                sgst_tax=[]
                igst_tax=[]
                cgst_checking_completed=[]
                igst_checking_completed=[]
                sgst_checking_completed=[]
                itemised_tax_data, itemised_tax, itemised_taxable_amount = get_itemised_tax_breakup_data(doc)
                ts_tax_details=list(itemised_tax.values())
                for ts_i in range(0,len(ts_tax_details),1):
                    ts_tax_category.append(list(ts_tax_details[ts_i].keys()))
                    ts_tax_percentage_amount.append(list(ts_tax_details[ts_i].values()))
                for ts_j in range(0,len(ts_tax_category),1):
                    ts_separate_tax_category=ts_tax_category[ts_j]
                    for ts_x in range(0,len(ts_separate_tax_category),1):
                        if(len(ts_tax_type)==2):
                            if(ts_separate_tax_category[ts_x] == ts_tax_type[0]):
                                cgst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                            if(ts_separate_tax_category[ts_x] == ts_tax_type[1]):
                                sgst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                        if(len(ts_tax_type)==1):
                            if(ts_separate_tax_category[ts_x] == ts_tax_type[0]):
                                igst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                if(ts_main_tax_category=="In-State" or ts_main_tax_category=="Tamil Nadu"):
                    cgst_amount=[]
                    sgst_amount=[]
                    for ts_loop in cgst_tax:
                        for ts_y in range(0,len(cgst_tax),1):
                            if(cgst_tax[ts_y]["tax_rate"] not in cgst_checking_completed):
                                cgst_checking_completed.append(cgst_tax[ts_y]["tax_rate"])
                                ts_flag=0
                                for ts_z in range(ts_y,len(cgst_tax),1):
                                    if(cgst_tax[ts_y]["tax_rate"]==cgst_tax[ts_z]["tax_rate"]):
                                        if(ts_flag==0):
                                            ts_flag=1
                                            cgst_amount.append(cgst_tax[ts_y]["tax_amount"])
                                        else:
                                            cgst_amount.append(cgst_tax[ts_z]["tax_amount"])
                                    else:
                                        if(ts_flag==0):
                                            ts_flag=1
                                            cgst_amount.append(cgst_tax[ts_y]["tax_amount"])
                        for ts_a in range(0,len(sgst_tax),1):
                            if(sgst_tax[ts_a]["tax_rate"] not in sgst_checking_completed):
                                sgst_checking_completed.append(sgst_tax[ts_a]["tax_rate"])
                                ts_flag=0
                                for ts_b in range(ts_a,len(sgst_tax),1):
                                    if(sgst_tax[ts_a]["tax_rate"]==sgst_tax[ts_b]["tax_rate"]):
                                        if(ts_flag==0):
                                            ts_flag=1
                                            sgst_amount.append(sgst_tax[ts_a]["tax_amount"])
                                        else:
                                            sgst_amount.append(sgst_tax[ts_b]["tax_amount"])
                                    else:
                                        if(ts_flag==0):
                                            ts_flag=1
                                            sgst_amount.append(sgst_tax[ts_a]["tax_amount"])
                        for i in range(0,len(doc.items)):
                            doc.items[i].ts_igst_amount = 0
                            doc.items[i].ts_sgst_amount = sgst_amount[i]
                            doc.items[i].ts_cgst_amount = cgst_amount[i]
                if(ts_main_tax_category=="Out-State"):
                    igst_amount=[]
                    for ts_i in range(0,len(igst_tax),1):
                        if(igst_tax[ts_i]["tax_rate"] not in igst_checking_completed):
                            igst_checking_completed.append(igst_tax[ts_i]["tax_rate"])
                            ts_flag=0
                            for ts_j in range(ts_i,len(igst_tax),1):
                                if(igst_tax[ts_i]["tax_rate"]==igst_tax[ts_j]["tax_rate"]):
                                    if(ts_flag==0):
                                        ts_flag=1
                                        igst_amount.append(igst_tax[ts_i]["tax_amount"])
                                    else:
                                        igst_amount.append(igst_tax[ts_j]["tax_amount"])
                                else:
                                    if(ts_flag==0):
                                        ts_flag=1
                                        igst_amount.append(igst_tax[ts_i]["tax_amount"])
                    for i in range(0,len(doc.items)):
                        doc.items[i].ts_igst_amount = igst_amount[i]
                        doc.items[i].ts_sgst_amount = 0
                        doc.items[i].ts_cgst_amount = 0
                
                        

                    
