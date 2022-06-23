var main_data
frappe.ui.form.on("Purchase Invoice",{
	refresh:function(frm,cdt,cdn){
		main_data=locals[cdt][cdn]
	}
})
frappe.db.get_single_value("Core Accounting Settings","ts_tax_fetching").then(value =>{
    if(value==1){
		var tax_category
		var tax_and_charges
		frappe.ui.form.on("Purchase Invoice Item",{
			item_code:function(frm,cdt,cdn){
				var data = locals[cdt][cdn]
				var item_code=data.item_code
				if(item_code!=""){
					var company=main_data.company
					var transaction_type="Purchase"
					tax_category=main_data.tax_category
					tax_and_charges=main_data.taxes_and_charges
					frappe.call({
						method:"core_accounting.patches.py.tax.tax_template_filtering",
						args:{company,item_code,tax_category,transaction_type},
						callback(r){
							if(r.message===0){
								frappe.model.set_value(cdt,cdn,"item_code","")
							}
							else if(r.message===1){
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
			}
		})
	}
})
