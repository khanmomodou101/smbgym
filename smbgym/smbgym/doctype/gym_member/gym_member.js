// Copyright (c) 2023, royalsmb and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	refresh: function(frm) {
		frm.events.set_full_name(frm)
	},

	first_name: function(frm){
		frm.events.set_full_name(frm)
	},

	last_name: function(frm){
		frm.events.set_full_name(frm)
	},


	set_full_name: function(frm){
		var full_name = '';
		var first_name = frm.doc.first_name;
		var last_name = frm.doc.last_name;

		full_name = first_name + " " + last_name;

		frm.set_value('full_name', full_name)

	}
});
