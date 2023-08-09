# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Cardiomachine(Document):
	def validate(self):
		if self.machine_availability:
			self.status= "Working"
		else:
			self.status= "Not working"