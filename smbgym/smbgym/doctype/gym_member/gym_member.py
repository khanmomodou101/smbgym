# # Copyright (c) 2023, royalsmb and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class GymMember(Document):
# 	def after_insert(self):
# 		self.set_full_name()
		

# 	def set_full_name(self):
# 		member = frappe.get_doc("Gym Member", self.name)
# 		first_name = member.first_name
# 		last_name = member.last_name
# 		full_name = first_name + " " + last_name
# 		member.db_set("full_name", full_name)


from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GymMember(Document):
    def validate(self):
        if not frappe.db.exists("Customer", self.email):
            customer = frappe.new_doc("Customer")
            customer.email = self.email
            customer.customer_name = self.full_name
            customer.customer_group = "Individual"
            customer.customer_type = "Individual"
            
            
            customer.insert()
            frappe.db.commit()
            
    def after_insert(self):
         self.set_full_name()

    def set_full_name(self):
        member = frappe.get_doc("Gym Member", self.name)
        first_name = member.first_name
        last_name = member.last_name
        full_name = first_name + " " + last_name
        member.db_set("full_name", full_name)

    def on_trash(self):
        customer = self.email
        if frappe.db.exists("Customer", customer):
              frappe.delete_doc("Customer", customer)
    
