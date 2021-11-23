from django.db import models

# Create your models here.
class Fibonacci:

    def __init__(self):
        self.data = {
            "history" :[]
        }

    def fib_response(self, order):
        self.data["history"].append(order)
        a = 0
        b = 1
        if order < 0:
            return 0
        elif order == 0:
            return 0
        elif order == 1:
            return b
        else:
            for i in range(1, order):
                c = a + b
                a = b
                b = c
            return b
    