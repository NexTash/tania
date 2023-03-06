# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_column(), get_data(filters)
	return columns, data


def get_column():
	columns = [
			{
			"fieldname": "full_name",
			"fieldtype": "Data",
			"label": "Full Name",
			"width": 160
		},
		{
			"fieldname": "employee",
			"fieldtype": "Data",
			"label": "Employee",
			"width": 300
		},
		{
			"fieldname": "total_tasks",
			"fieldtype": "Data",
			"label": "Total Tasks",
			"width": 160
		},
		{
			"fieldname": "completed",
			"fieldtype": "Data",
			"label": "Completed Tasks",
			"width": 160
		},
		{
			"fieldname": "overdue",
			"fieldtype": "Data",
			"label": "Overdue Tasks",
			"width": 160
		},

		
	]

	return columns


def get_data(filters):
	data = []
	employee_filters ={}

	todo_filter = {"reference_type":"Task"}
	if filters.get("employee_name"):
		user_id = frappe.get_value("Employee", filters.get("employee_name"), "user_id")
		todo_filter["owner"] = user_id

	todos = frappe.db.get_all("ToDo", todo_filter , ["reference_name", "owner"])

	employee_wise_task = {}

	for row in todos:
		employee_wise_task[row.owner] = {
			"full_name":"",
			"total": 0,
			"overdue": 0,
			"completed": 0,
			
		}

	for row in todos:
		full_name = frappe.get_value("User", row.owner, "full_name")
		employee_wise_task[row.owner]["full_name"] = full_name
		if filters.get("employee_name") and full_name == full_name:
			continue

	for row in todos:
		employee_wise_task[row.owner]["total"] += 1
		status = frappe.get_value("Task", row.reference_name, "status")

		if status == "Completed":
			employee_wise_task[row.owner]["completed"] += 1
		elif status == "Overdue":
			employee_wise_task[row.owner]["overdue"] += 1
			
	
	for (key, val) in employee_wise_task.items():
		row = {
			"full_name":val.get("full_name"),
			"employee": key,
			"total_tasks": val.get("total"),
			"completed": val.get("completed"),
			"overdue":val.get("overdue"),
			
		}

		data.append(row)

	return data