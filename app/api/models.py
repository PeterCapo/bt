from datetime import datetime
from flask import current_app
from app.db_con import connection


payments = []


class Payment():
    def __init__(self, BillRefNumber=None):
        self.curr = connection().cursor()
        self.BillRefNumber = BillRefNumber

    def save(self, BillRefNumber, ShortCode, Amount, Msisdn, CommandID):

        payload = {
            "BillRefNumber": BillRefNumber,
            "ShortCode": ShortCode,
            "Amount": Amount,
            "Msisdn": Msisdn,
            "CommandID":CommandID
        }
        query = """INSERT INTO payments (BillRefNumber, ShortCode, Amount, Msisdn, CommandID) VALUES
                ( %(BillRefNumber)s, %(ShortCode)s, %(Amount)s, %(Msisdn)s, %(CommandID)s)"""
        self.curr.execute(query, payload)
        return payload