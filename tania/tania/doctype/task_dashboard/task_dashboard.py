# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TaskDashboard(Document):
	@frappe.whitelist()
	def delete_operation(self):
		#update project document and delete
		comment=self.comment
		status=self.status
		doc = frappe.get_doc("Project", self.admin)
		doc.comment=comment
		doc.status=status
		doc.save()
		# deleting this document
		# @Delete
		self.delete()

