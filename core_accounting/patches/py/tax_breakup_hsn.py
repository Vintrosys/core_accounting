import frappe
from erpnext.controllers.taxes_and_totals import get_itemised_tax_breakup_data
def ts_tax_breakup_separater(ts_document,action):
    ts_value=frappe.get_doc("Core Accounting Settings")
    if ts_value.ts_hsn==1 and ts_document.docstatus == 0:
        if ts_document:
            ts_document.update({"ts_tax_breakup_gst_table":[]})
            if ts_document.tax_category:
                ts_main_tax_category=ts_document.tax_category
                ts_tax_type=[]
                ts_tax_description=ts_document.taxes
                for tax in ts_tax_description:
                    ts_tax_type.append(tax.description)
                ts_tax_hsn=[]
                ts_hsn=ts_document.items
                for hsn in ts_hsn:
                    if hsn.gst_hsn_code:
                        ts_tax_hsn.append(hsn.gst_hsn_code)
                    else:
                        ts_tax_hsn.append("")
                itemised_tax, itemised_taxable_amount = get_itemised_tax_breakup_data(ts_document)
                itemised_taxable_amount=list(itemised_taxable_amount.values())
                ts_tax_item=list(itemised_tax.keys())
                ts_tax_details=list(itemised_tax.values())
                ts_hsn_checking_completed=[]
                for ts_in in range(0,len(ts_tax_item),1):
                    ts_count=0
                    ts_same_hsn_item=[]
                    ts_same_hsn_details=[]
                    ts_tax_details_separated=[]
                    ts_final_valuable_amount=0
                    if(ts_tax_hsn[ts_in] not in ts_hsn_checking_completed):
                        for ts_ih in range(ts_in,len(ts_tax_hsn),1):
                                if(ts_tax_hsn[ts_in]==ts_tax_hsn[ts_ih]):
                                    ts_hsn_checking_completed.append(ts_tax_hsn[ts_ih])
                                    if(ts_count==0):
                                        ts_count=1
                                        ts_same_hsn_item.append(ts_tax_item[ts_in])
                                        ts_same_hsn_details.append(ts_tax_hsn[ts_in])
                                        ts_tax_details_separated.append(ts_tax_details[ts_in])
                                        ts_final_valuable_amount=ts_final_valuable_amount+itemised_taxable_amount[ts_in]

                                    else:
                                        ts_same_hsn_item.append(ts_tax_item[ts_in])
                                        ts_same_hsn_details.append(ts_tax_hsn[ts_ih])
                                        ts_tax_details_separated.append(ts_tax_details[ts_in])
                                        ts_final_valuable_amount=ts_final_valuable_amount+itemised_taxable_amount[ts_in]
                                else:
                                    if(ts_count==0):
                                        ts_count=1
                                        ts_same_hsn_item.append(ts_tax_item[ts_in])
                                        ts_same_hsn_details.append(ts_tax_hsn[ts_in])
                                        ts_tax_details_separated.append(ts_tax_details[ts_in])
                                        ts_final_valuable_amount=ts_final_valuable_amount+itemised_taxable_amount[ts_in]
                        ts_tax_category=[]
                        ts_tax_percentage_amount=[]
                        ts_cgst_tax=[]
                        ts_final_cgst_tax=[]
                        ts_final_cgst_amount=[]
                        ts_sgst_tax=[]
                        ts_igst_tax=[]
                        ts_final_sgst_tax=[]
                        ts_final_sgst_amount=[]
                        ts_final_total_tax=[]
                        ts_final_total_tax_amount=[]
                        ts_final_igst_tax=[]
                        ts_final_igst_amount=[]
                        ts_cgst_checking_completed=[]
                        ts_igst_checking_completed=[]
                        ts_sgst_checking_completed=[]
                        for ts_i in range(0,len(ts_tax_details_separated),1):
                            ts_tax_category.append(list(ts_tax_details_separated[ts_i].keys()))
                            ts_tax_percentage_amount.append(list(ts_tax_details_separated[ts_i].values()))
                        for ts_j in range(0,len(ts_tax_category),1):
                            ts_separate_tax_category=ts_tax_category[ts_j]
                            for ts_x in range(0,len(ts_separate_tax_category),1):
                                if(len(ts_tax_type)==2):
                                    if(ts_separate_tax_category[ts_x] == ts_tax_type[0]):
                                        ts_cgst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                                    if(ts_separate_tax_category[ts_x] == ts_tax_type[1]):
                                        ts_sgst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                                if(len(ts_tax_type)==1):
                                    if(ts_separate_tax_category[ts_x] == ts_tax_type[0]):
                                        ts_igst_tax.append(ts_tax_percentage_amount[ts_j][ts_x])
                        if(ts_main_tax_category=="In-State" or ts_main_tax_category=="Tamil Nadu"):
                            for ts_loop in ts_cgst_tax:
                                for ts_y in range(0,len(ts_cgst_tax),1):
                                    if(ts_cgst_tax[ts_y]["tax_rate"] not in ts_cgst_checking_completed):
                                        ts_cgst_checking_completed.append(ts_cgst_tax[ts_y]["tax_rate"])
                                        ts_flag=0
                                        ts_cgst_amount=0
                                        for ts_z in range(ts_y,len(ts_cgst_tax),1):
                                            if(ts_cgst_tax[ts_y]["tax_rate"]==ts_cgst_tax[ts_z]["tax_rate"]):
                                                if(ts_flag==0):
                                                    ts_flag=1
                                                    ts_cgst_amount=ts_cgst_amount+ts_cgst_tax[ts_y]["tax_amount"]
                                                else:
                                                    ts_cgst_amount=ts_cgst_amount+ts_cgst_tax[ts_z]["tax_amount"]
                                            else:
                                                if(ts_flag==0):
                                                    ts_flag=1
                                                    ts_cgst_amount=ts_cgst_amount+ts_cgst_tax[ts_y]["tax_amount"]
                                        ts_final_cgst_tax.append(ts_cgst_tax[ts_y]["tax_rate"])
                                        ts_final_cgst_amount.append(ts_cgst_amount)

                                for ts_a in range(0,len(ts_sgst_tax),1):
                                    if(ts_sgst_tax[ts_a]["tax_rate"] not in ts_sgst_checking_completed):
                                        ts_sgst_checking_completed.append(ts_sgst_tax[ts_a]["tax_rate"])
                                        ts_flag=0
                                        ts_sgst_amount=0
                                        for ts_b in range(ts_a,len(ts_sgst_tax),1):
                                            if(ts_sgst_tax[ts_a]["tax_rate"]==ts_sgst_tax[ts_b]["tax_rate"]):
                                                if(ts_flag==0):
                                                    ts_flag=1
                                                    ts_sgst_amount=ts_sgst_amount+ts_sgst_tax[ts_a]["tax_amount"]
                                                else:
                                                    ts_sgst_amount=ts_sgst_amount+ts_sgst_tax[ts_b]["tax_amount"]
                                            else:
                                                if(ts_flag==0):
                                                    ts_flag=1
                                                    ts_sgst_amount=ts_sgst_amount+ts_sgst_tax[ts_a]["tax_amount"]
                                        ts_final_sgst_tax.append(ts_sgst_tax[ts_a]["tax_rate"])
                                        ts_final_sgst_amount.append(ts_sgst_amount)
                            for ts_tc in range(0,len(ts_final_cgst_tax),1):
                                ts_final_total_tax_amt=0
                                for ts_ts in range(0,len(ts_final_sgst_tax),1):
                                    if(ts_final_cgst_tax[ts_tc]==ts_final_sgst_tax[ts_ts]):
                                        ts_final_total_tax_amt=ts_final_total_tax_amt+(ts_final_cgst_amount[ts_tc]+ts_final_sgst_amount[ts_ts])
                                        ts_final_total_tax.append(ts_final_cgst_tax[ts_tc])
                                        ts_final_total_tax_amount.append(ts_final_total_tax_amt)
                            for ts_i in range(0,len(ts_final_cgst_tax),1):
                                ts_document.append("ts_tax_breakup_gst_table",{
                                    "ts_hsn_code":ts_tax_hsn[ts_in],
                                    "ts_gst_rate":(ts_final_cgst_tax[ts_i]*2),
                                    "ts_taxable_values":ts_final_valuable_amount,
                                    "ts_central_tax":ts_final_cgst_tax[ts_i],
                                    "ts_central_amount":ts_final_cgst_amount[ts_i],
                                    "ts_state_tax":ts_final_sgst_tax[ts_i],
                                    "ts_state_amount":ts_final_sgst_amount[ts_i],
                                    "ts_total_tax_amount":ts_final_total_tax_amount[ts_i]
                                })

                        if(ts_main_tax_category=="Out-State" or ts_main_tax_category == "Export Sales" or ts_main_tax_category == "0% SEZ"):
                            for ts_i in range(0,len(ts_igst_tax),1):
                                if(ts_igst_tax[ts_i]["tax_rate"] not in ts_igst_checking_completed):
                                    ts_igst_checking_completed.append(ts_igst_tax[ts_i]["tax_rate"])
                                    ts_flag=0
                                    ts_igst_amount=0
                                    for ts_j in range(ts_i,len(ts_igst_tax),1):
                                        if(ts_igst_tax[ts_i]["tax_rate"]==ts_igst_tax[ts_j]["tax_rate"]):
                                            if(ts_flag==0):
                                                ts_flag=1
                                                ts_igst_amount=ts_igst_amount+ts_igst_tax[ts_i]["tax_amount"]
                                            else:
                                                ts_igst_amount=ts_igst_amount+ts_igst_tax[ts_j]["tax_amount"]
                                        else:
                                            if(ts_flag==0):
                                                ts_flag=1
                                                ts_igst_amount=ts_igst_amount+ts_igst_tax[ts_i]["tax_amount"]
                                    ts_final_igst_tax.append(ts_igst_tax[ts_i]["tax_rate"])
                                    ts_final_igst_amount.append(ts_igst_amount)
                            for ts_i in range(0,len(ts_final_igst_tax),1):
                                ts_document.append("ts_tax_breakup_gst_table",{
                                    "ts_hsn_code":ts_tax_hsn[ts_in],
                                    "ts_igst_tax":ts_final_igst_tax[ts_i],
                                    "ts_igst_amount":ts_final_igst_amount[ts_i],
                                    "ts_taxable_values":ts_final_valuable_amount,
                                    "ts_total_tax_amount":ts_final_igst_amount[ts_i]
                                })