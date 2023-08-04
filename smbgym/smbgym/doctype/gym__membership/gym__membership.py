import datetime
import frappe
from frappe.model.document import Document
from frappe.utils import add_days

class GymMembership(Document):
    def calculate_end_date(self):
        if self.start_date and self.valid_number_of_days:
            # Calculate the end_date based on the valid_number_of_days
            end_date = add_days(self.start_date, self.valid_number_of_days)

            # Set the end_date value in the Membership document
            frappe.db.set_value("Gym Membership", self.name, "end_date", end_date)

    def on_submit(self):
        try:
            # Call the function to calculate and set the End Date before submitting the Membership
            self.calculate_end_date()
        except Exception as e:
            frappe.log_error(title="Error in Gym Membership Script", message=e)

