# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_column(), get_data(filters)
	return columns, data


def get_column():
	columns = [
		{
			"fieldname": "agent",
			"fieldtype": "Link",
			"label": "Agent Name",
			"options": "Agent",
			"width": 300
		},
		{
			"fieldname": "full_name",
			"fieldtype": "Data",
			"label": "Agent Full Name",
			"width": 300
		},
		{
			"fieldname": "total_messages",
			"fieldtype": "Int",
			"label": "Total Messages"
		},
		{
			"fieldname": "read_messages",
			"fieldtype": "Int",
			"label": "Read Messages"
		},
		{
			"fieldname": "not_read_messages",
			"fieldtype": "Int",
			"label": "Unread Messages"
		},
	]

	return columns

def get_data(filters):
	data = []
	agent_filters ={}

	if filters.get("agent_name"):
		agent_filters["name"] = filters.get("agent_name")

	agents = frappe.get_list("Agent", agent_filters, ["full_name", "name"])
	for agent in agents:
		agency_records = frappe.get_list("Agency View", { "agent_name": agent.name }, ["is_read"])
		total_messages = len(agency_records)

		readed_records = 0
		for row in agency_records:
			if row.is_read:
				readed_records = readed_records + 1
		
		if not total_messages:
			continue

		if filters.get("unread") and total_messages == readed_records:
			continue

		if filters.get("readed") and total_messages != readed_records:
			continue
			
		data.append({
			"agent": agent.name,
			"full_name": agent.full_name,
			"total_messages": total_messages,
			"read_messages": readed_records,
			"not_read_messages": total_messages - readed_records
		})

	return data