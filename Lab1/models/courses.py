
from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses'
    _description = 'Courses System'

    name = fields.Char(string="Course Name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    cost = fields.Float()


