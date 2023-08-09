// Copyright (c) 2023, Sathish Kumar and contributors
// For license information, please see license.txt
frappe.ui.form.on('Gym member', {
    before_save: function(frm) {
        frm.add_custom_button(__('Create New Gym member'), function() {
            var first_name = frm.doc.first_name;
            var last_name = frm.doc.last_name;
            var date_of_birth = frm.doc.date_of_birth;
            var gender = frm.doc.gender;
            var contact_number = frm.doc.contact_number;
            var email_address = frm.doc.email_address;
            var address = frm.doc.address;

            frappe.call({
                method: "gym_management_system.gym_management_system.doctype.gym_member.gym_member.create_gym_member",
                args: {
                    first_name: first_name,
                    last_name: last_name,
                    date_of_birth: date_of_birth,
                    gender: gender,
                    contact_number: contact_number,
                    email_address: email_address,
                    address: address
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint('New Gym member created: ' + response.message);
                    }
                }
            });
        });
    }
});

