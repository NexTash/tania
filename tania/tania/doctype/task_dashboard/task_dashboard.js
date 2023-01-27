// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Task Dashboard', {
	refresh: function(frm) {
		frm.add_custom_button("Complete", () => {
			frm.call("delete_operation")
			setTimeout(() => {
				frappe.set_route("List", "Task Dashboard");
			  }, 3000);
		})
		  
	}
});
