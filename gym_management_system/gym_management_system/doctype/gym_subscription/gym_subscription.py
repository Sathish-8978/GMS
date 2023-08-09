# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Gymsubscription(Document):
	pass

# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class Gymsubscription(Document):
#  def get_remaining_days_in_subscription(gym_member):
#     current_date = today()

#     active_membership = frappe.get_value(
#         "Gym Membership",
#         {"gym_member":gym_member: ("<=", current_date), "end_date": (">=", current_date)},
#         ["start_date", "end_date"]
#     )
  
#     if active_membership:
#         start_date = getdate(active_membership[0])
#         end_date = getdate(active_membership[1])
#         remaining_days = (end_date - current_date).days
#         return remaining_days

#     return None
