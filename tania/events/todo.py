import frappe
from frappe.share import add, remove


def validate(doc, method=None):
    if doc.reference_type == 'Task':
        add(doc.reference_type, doc.reference_name, doc.owner, read=1, write=1, share=1)
        frappe.msgprint(f"Document shared with {doc.owner} (Read, Write & Share).")


def on_trash(doc, method=None):
    if doc.reference_type == 'Task':
        remove(doc.reference_type, doc.reference_name, doc.owner, flags=None)
        frappe.msgprint(f"{doc.owner} shared permissions remove successfully")
