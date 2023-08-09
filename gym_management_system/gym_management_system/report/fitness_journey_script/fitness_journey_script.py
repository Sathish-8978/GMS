# Copyright (c) 2023, Sathish Kumar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {"label": "Gym member", "fieldname": "gym_member", "fieldtype": "Link", "options": "Gym Member", "width": 120},
        {"label": "Weight", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Calories intake", "fieldname": "calories_intake", "fieldtype": "Int", "width": 100},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100}
    ]

    data = get_filtered_data(filters)

    return columns, data

def get_filtered_data(filters):
    filtered_data = []
    gym_member=filters.get('gym_member')
    
    if gym_member is not None:
        filtered_data = frappe.get_all('Fitness metrics',filters={'gym_member':gym_member},
                                       fields=['gym_member', 'weight', 'calories_intake', 'date'])
    else:
        filtered_data = frappe.get_all('Fitness metrics',
                                       fields=['gym_member','weight','calories_intake','date'])

    return filtered_data


def call_execute_function():
    filters = {
    }
    result = frappe.call('gym_management_system.report.fitness_journey_script.execute', filters=filters)
    result = columns, data

    for record in data:
        gym_member = record.get('gym_member')
        weight = record.get('weight')
        calories_intake = record.get('calories_intake')
        date = record.get('date')

#call_execute_function()
