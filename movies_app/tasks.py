from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def calculate_amount(x):
    print("Calculate Task")
    return x * 1.0 if x <= 3 else 3.0 + (x-3) * 0.5
