var main_data;
	frappe.ui.form.on("Sales Order",{
		refresh:function(frm,cdt,cdn){
			main_data=locals[cdt][cdn]
		}
	})
frappe.db.get_single_value("Core Accounting Settings","ts_tax_fetching").then(value =>{
    if(value==1){
		var tax_category;
		var tax_and_charges;
		frappe.ui.form.on("Sales Order Item",{
			item_code:function(frm,cdt,cdn){
				var data = locals[cdt][cdn]
				var item_code=data.item_code
				if(item_code!=""){
					var transaction_type="Sales"
					var company=main_data.company
					tax_category=main_data.tax_category
					tax_and_charges=main_data.taxes_and_charges
					frappe.call({
						method:"core_accounting.patches.py.tax.tax_template_filtering",
						args:{company,item_code,tax_category,transaction_type},
						callback(r){
							if(r.message===0){
								frappe.model.set_value(cdt,cdn,"item_code","")
							}
							else if(r.message==1){
								frappe.show_alert({ message: __('Tax Category is not selected'), indicator: 'red' });
							}
							else if(r.message===2 || r.message[1]===2){
								frappe.show_alert({ message: __("There Is No Tax Template For Item : "+item_code), indicator: 'red' });
							}
							else{
								frappe.model.set_value(cdt,cdn,"item_tax_template",r.message)
							}
						}
					})
				}
			},
			item_tax_template:function(frm,cdt,cdn){
				var data = locals[cdt][cdn]
				var item_tax_percentage=data.item_tax_template
                if(item_tax_percentage){
                    frappe.call({
                        method:"core_accounting.patches.py.item_tax_percentage.item_tax_percentage",
                        args:{item_tax_percentage},
                        callback(r){
                            frappe.model.set_value(cdt,cdn,"ts_item_gst",r.message)
							frm.refresh()
                        }
					})
				}
			}
		})
	}
})