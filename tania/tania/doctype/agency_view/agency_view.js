// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Agency View', {
	refresh: function(frm) {
		frm.add_custom_button("Create", () => {
			frm.call("create_agent_doc")
		})
	},
	validate(frm, dt, dn) {
		let message = frm.doc.message
		message = btoa(message)
		
		frappe.model.set_value(dt, dn, "message", message)
	}
});
