# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AgentView(Document):
	@frappe.whitelist()
	def delete_operation(self):
		# deleting this document
		# @Delete
		self.delete()
		
		# deleting Agency View
		# @Delete
		frappe.delete_doc('Agency View', self.agency_reference)