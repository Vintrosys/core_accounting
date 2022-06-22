frappe.db.get_single_value("Core Accounting Settings","ts_tax_fetching").then(value =>{
    if(value==1){
        cur_frm.set_df_property("tax_settings","hidden",0)
        frappe.ui.form.on("Company",{
            validate:function(frm,cdt,cdn){
                var validate=0
                var data=locals[cdt][cdn]
                if(data.enable_mulltiple_item_tax_templates==1){
                    if(data.ts_allow_only_tax_applied==1){
                        validate=validate+1
                    }
                    if(data.ts_allow_tax_with_message==1){
                        validate=validate+1
                    }
                    if(validate==0){
                        frappe.throw({
                            title:("Message"),
                            message:('"Enable Mulltiple Item Tax Templates" options is enabled, So please select any one of the option in "Tax Settings"')
                        })
                    }
                }
            },
        })


        var ts_property_cdn=[]
        frappe.ui.form.on("Company",{
            before_save:function(){
                frappe.call({
                    method:"core_accounting.patches.py.company.property_terminator",
                    callback(ts_r){
                        ts_property_cdn.push(ts_r.message[0])
                        ts_property_cdn.push(ts_r.message[1])
                    }
                })
            },
            after_save:function(){
                frappe.call({
                    method:"core_accounting.patches.py.company.property_terminator",
                    args:{ts_property_cdn}
                })
            },
        })
    }
    else{
        cur_frm.set_df_property("tax_settings","hidden",1)
        var ts_property_cdn=[]
        frappe.ui.form.on("Company",{
            before_save:function(){
                frappe.call({
                    method:"core_accounting.patches.py.company.property_terminator",
                    callback(ts_r){
                        ts_property_cdn.push(ts_r.message[0])
                        ts_property_cdn.push(ts_r.message[1])
                    }
                })
            },
            after_save:function(){
                frappe.call({
                    method:"core_accounting.patches.py.company.property_terminator",
                    args:{ts_property_cdn}
                })
            },
        })
    }
})
