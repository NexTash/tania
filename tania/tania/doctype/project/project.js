// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project', {
	refresh: function(frm) {
		frm.add_custom_button("Create", () => {
			frm.call("create_task")
		})
	}
});
