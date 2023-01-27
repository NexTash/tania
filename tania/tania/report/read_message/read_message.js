// Copyright (c) 2023, nextash.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Read Message"] = {
	"filters": [
		{
			"fieldname": "agent_name",
			"fieldtype": "Link",
			"label": "Agent",
			"options": "Agent"
		},
		{
			"fieldname": "readed",
			"fieldtype": "Check",
			"label": "Read Messages Only",
		},
		{
			"fieldname": "unread",
			"fieldtype": "Check",
			"label": "Unread Messages Only"
		},
		
	]
};
