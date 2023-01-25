# Copyright (c) 2023, nextash.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import base64

class AgencyView(Document):
	@frappe.whitelist()
	def create_agent_doc(self):
		agency_msg = self.message
		
		# decode the text
		# # converting string to byte_object so we can perform base64 operations
		agency_msg = agency_msg.encode('ascii')

		# # decoding base64 encoded text to string
		agent_msg = base64.b64decode(agency_msg)


		# Check if already exist
		# @Read
		if_exist = frappe.db.exists("Agent View", {"agency_reference": self.name})

		
		if not if_exist:
			# Creating agent view document
			# @Create Operation
			doc = frappe.get_doc({
				'doctype': 'Agent View',
				'message': agent_msg,
				"agency_reference": self.name
			})
			doc.insert()

			frappe.msgprint("Message on the way")
		else:
			# Updating agent view document with new message
			# @Read
			agent_views = frappe.db.get_list('Agent View', filters = { 'agency_reference': self.name }, fields= ["name"])
			
			for row in agent_views:
				# getting specific agent view document for updation
				# @Read
				doc = frappe.get_doc("Agent View", row.name)
				
				# updating
				# @Update
				doc.message = agent_msg
				doc.save()