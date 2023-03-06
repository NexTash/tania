// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Task Detail"] = {
	"filters": [
		{
			"fieldname": "employee_name",
			"fieldtype": "Link",
			"label": "Employee",
			"options": "Employee"
		},
	]
};
