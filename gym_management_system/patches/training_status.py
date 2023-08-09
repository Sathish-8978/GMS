import frappe

def execute():
    gym_trainers = frappe.get_all("Gym trainer", fields=["name", "training_completed"])
    for gym_trainer in gym_trainers:
        if gym_trainer.training_completed:
            frappe.db.set_value("Gym trainer", gym_trainer.name, "training_status", "Completed", update_modified=False)
        else:
            frappe.db.set_value("Gym trainer", gym_trainer.name, "training_status", "Not started", update_modified=False)
