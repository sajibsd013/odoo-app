from odoo import fields, models

class TestModel(models.Model):
    _name = "todo.app"
    _description = "This is a todo app..."

    task = fields.Char(string="Task", required=True)
    description = fields.Text(string="Task description", required=True)
    deadline = fields.Date(string="Task Deadline", required=True)
    is_done = fields.Boolean(string="Is Done ?", required=True)