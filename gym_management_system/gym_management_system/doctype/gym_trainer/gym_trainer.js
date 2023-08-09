// Copyright (c) 2023, Sathish Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym trainer', {
    after_save: function(frm) {
        showSavedNotification();
		console.log("successfulll saved")
    }
});

function showSavedNotification() {
    frappe.msgprint("Gym trainer is successfull saved");
}



