# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DailyTask(models.Model):
    _name = "daily.task"
    _description = "Employees daily tasks"

    task_name = fields.Char(string='Task Name', required=True)
    task_description = fields.Text(string='Task Description', required=True)
    task_owner = fields.Char(string='Task owner')
    task_type = fields.Selection([
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('home', 'Home'),
    ], required=True) #default='Morning')
    task_startTime = fields.Date(index=True, help="Starting time")
    task_endTime = fields.Date(index=True, help="Ending time")