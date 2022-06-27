frappe.ui.form.on('Item', {
    add: function(frm){
    if (frm.doc.item_tax){
        let tax=[]
        if (frm.doc.taxes){
                for(let row=0;row<frm.doc.taxes.length;row++){
                        tax.push(frm.doc.taxes[row].item_tax_template)
                }
            }
            
            frappe.call({
            method: "core_accounting.patches.py.item.item_template_tax",
            args: {
                item_tax: frm.doc.item_tax,
                tax:tax
            },
            callback(r){
               
                
                    if(r.message.length){
                        r.message.forEach((data)=>{
                            if (!(data['name'] in tax))
                            var child=frm.add_child('taxes')
                            child.item_tax_template=data['name']
                            child.tax_category=data['tax_category']
                        })
                        frm.refresh()
                    }
                
            }
            })
        }  
    },
    remove_row: function(frm){
        if (frm.doc.item_tax){
            let tax=[]
            frappe.call({
                method:"core_accounting.patches.py.item.item_template_remove",
                args:{
                    item_tax: frm.doc.item_tax,
                    tax:frm.doc.taxes
                },
                callback(r){
                    console.log(r.message)
                    frm.set_value('taxes',[])
                    frm.set_value('taxes', r.message)
                    frm.refresh()
                }
            })

        }
    }

 });