# Copyright (c) 2023, Sathish Kumar and Contributors
# See license.txt

import unittest
from frappe.tests.utils import FrappeTestCase
from frappe.utils import getdate, nowdate
# from datetime import date
import frappe
from gym_management_system.gym_management_system.doctype.gym_membership.gym_membership import Gymmembership

class TestGymmembership(FrappeTestCase):
    def test_remaining_days_calculation(self):
        print('testcal-----------')
        gym_member = frappe.new_doc('Gym member')
        gym_member.first_name = "Naveen"
        gym_member.last_name = "kumar"
        gym_member.date_of_birth = "2000-01-14"
        gym_member.gender = "Male"
        gym_member.contact_number = "9159988978"
        gym_member.email_address = "naveen@gmail.com"
        gym_member.address = "Bangalore"
        gym_member.insert()
        
        gym_member_doc=frappe.get_doc('Gym member',gym_member.name)
        doc = frappe.new_doc("Gym membership")
        doc.membership_plan_name = "Silver plan"
        doc.gym_member = gym_member_doc.name
        doc.date_of_subscription = "2023-07-25"
        doc.end_of_subscription = "2023-08-25"
        doc.insert()

        doc = frappe.get_doc("Gym membership", doc.name)

        # expected_remaining_days = (getdate("2023-08-25") - nowdate()).days
        expected_remaining_days = (getdate(doc.end_of_subscription) - getdate(nowdate())).days
        doc_remaining_days = int(doc.remaining_days)
        self.assertEqual(doc_remaining_days, expected_remaining_days)
        
# def validate(doc,method):
#     doc = frappe.new_doc("Gym membership")
#     doc.membership_plan_name = "Silver plan"
#     doc.gym_member = "AlexHales-0001"
#     doc.date_of_subscription = "25-07-2023"
#     doc.end_of_subscription = "25-08-2023"
#     doc.insert()








