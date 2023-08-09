# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _

@frappe.whitelist()
def create_gym_member(first_name, last_name, date_of_birth, gender ,contact_number ,email_address ,address):
        gym_member = frappe.new_doc("Gym member")
        gym_member.first_name = "Naveen"
        gym_member.last_name = "kumar"
        gym_member.date_of_birth = "2000-01-14"
        gym_member.gender = "Male"
        gym_member.contact_number = "9159988978"
        gym_member.email_address = "naveen@gmail.com"
        gym_member.address = "Bangalore"
        gym_member.insert()
        
        return gym_member.name


# def validate(doc,method):
#     doc = frappe.new_doc("Gym membership")
#     doc.membership_plan_name = "Silver plan"
#     doc.gym_member = "Alex"
#     doc.date_of_subscription = "25-7-23"
#     doc.end_of_subscription = "25-8-23"
#     doc.insert()

# @frappe.whitelist()
# def create_user_from_Gym_member(doc, method):
    
#     first_name = doc.first_name
#     last_name = doc.last_name
#     email_address = doc.email_address
#     role = doc.role

    
#     new_user = frappe.new_doc("User")
#     new_user.update();{
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email_address,
#         "roles": [{
#             "role": role
#         }],
        
#         "send_welcome_email": True,
#     }
#     new_user.insert(ignore_permission=True)