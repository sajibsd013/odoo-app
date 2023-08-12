from odoo import api, fields, models 

class Patient(models.Model):
    _name = "patient.paitent"
    _description = "Patients Records"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    is_child = fields.Boolean(string="Is Child?", required=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([("male","male"),("female","female"),("others","others")], string="Gender")