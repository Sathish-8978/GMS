# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt
# Import the required module

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, nowdate
from datetime import date

class Gymmembership(Document):
     pass
 
def calculate_remaining_days(doc,method):
        if doc.end_of_subscription:
            end_date = getdate(doc.end_of_subscription)
            current_date = getdate(nowdate())
            remaining_days = (end_date - current_date).days
            doc.remaining_days = remaining_days
            
            
# import frappe
# from frappe.model.document import Document
# from frappe.utils import getdate, nowdate
# from datetime import date

# class Gymmembership(Document):
#      pass
 
# def calculate_remaining_days(doc,method):
#         if doc.end_of_subscription:
#             end_date = getdate(doc.end_of_subscription)
#             current_date = getdate(nowdate())
#             remaining_days = (end_date - current_date).days
#             doc.remaining_days = remaining_days


# def create_gym_membership(data):
#     membership = frappe.new_doc("Gym membership")

#     membership.membership_plan_name = data.get("membership_plan_name")
#     membership.benefits = data.get("benefits")
#     membership.gym_member = data.get("gym_member")
#     membership.active_plan = data.get("active_plan")
#     membership.duration = data.get("duration")
#     membership.date_of_subscription = "5-7-23"
#     membership.end_of_subscription = "5-8-23"
#     membership.trainer = data.get("trainer")
#     membership.amount = data.get("amount")
#     membership.status = data.get("status")
#     membership.trainer_contact = data.get("trainer_contact")
    
#     membership.save()
#     membership.insert()
  

#     return membership.name


            



