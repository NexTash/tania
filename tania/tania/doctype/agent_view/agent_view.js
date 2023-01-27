// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agent View", {
  refresh: function (frm) {
    setTimeout(() => {
      frm.call("read_operation");
    }, 2000);

    setTimeout(() => {
      frappe.set_route("List", "Agent View");
    }, 10000);
  },
});
