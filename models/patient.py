from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patients'
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string="Description")
