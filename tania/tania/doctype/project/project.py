# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Project(Document):
	@frappe.whitelist()
	def create_task(self):
		title = self.title
		desc = self.description
		assign = self.assign_to
		
		if_exist = frappe.db.exists("Task Dashboard", {"project": self.name})

		
		if not if_exist:
			# Creating agent view document
			# @Create Operation
			doc = frappe.get_doc({
				'doctype': 'Task Dashboard',
				'title': title,
				'description':desc,
				'assign_to':assign,
				"admin": self.name
			})
			doc.insert()

			frappe.msgprint("New Task Has Been Created")
		else:
			# Updating agent view document with new message
			# @Read
			dashboard = frappe.db.get_list('Task Dashboard', filters = { 'project': self.name }, fields= ["name"])
			
			for row in dashboard:
				# getting specific agent view document for updation
				# @Read
				doc = frappe.get_doc("Task Dashboard", row.name)
				
				# updating
				# @Update
				doc.title = title
				doc.description=desc
				doc.assign_to=assign
				doc.save()