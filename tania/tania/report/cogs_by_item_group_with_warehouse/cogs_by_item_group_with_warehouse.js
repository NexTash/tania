// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["COGS By Item Group With Warehouse"] = {
	filters: [
		{
		  label: __("Company"),
		  fieldname: "company",
		  fieldtype: "Link",
		  options: "Company",
		  mandatory: true,
		  default: frappe.defaults.get_user_default("Company"),
		},
		{
		  label: __("From Date"),
		  fieldname: "from_date",
		  fieldtype: "Date",
		  mandatory: true,
		  default: frappe.datetime.year_start(),
		},
		{
		  label: __("To Date"),
		  fieldname: "to_date",
		  fieldtype: "Date",
		  mandatory: true,
		  default: frappe.datetime.get_today(),
		},
		]
};
