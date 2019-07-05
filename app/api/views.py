import requests
from requests.auth import HTTPBasicAuth
from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from .models import Payment, payments

class Register(Resource):

    def get(self):
        consumer_key = "wqtCtGKOWpXiPd4USm3DF30uTGHcSpkd"
        consumer_secret = "09r9sHq6rZvDfsk1"
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        print (r.text)


    def post(self):
        access_token = "Access-Token"
        api_url = "http://dad9396e.ngrok.io/register"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = { "ShortCode": " ",
            "ResponseType": " ",
            "ConfirmationURL": "http://dad9396e.ngrok.io/confirmation",
            "ValidationURL": "http://dad9396e.ngrok.io/validation_url"}

        response = requests.post(api_url, json = request, headers=headers)

        print (response.text)

class Simulate(Resource, Payment):

    parser = reqparse.RequestParser()

    parser.add_argument("BillRefNumber", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("ShortCode", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Amount", type=int, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Msisdn", type=int, required=True,
                        help="This field can not be left bank")
    parser.add_argument("CommandID", type=str, required=True,
                        help="This field can not be left bank")


    def __init__(self):
        self.ops = Payment()

    def post(self):
        data = Simulate.parser.parse_args()
        BillRefNumber = data['BillRefNumber']
        ShortCode = data['ShortCode']
        Amount = data['Amount']
        Msisdn = data['Msisdn']
        CommandID = data['CommandID']        
        

        result = self.ops.save(BillRefNumber, ShortCode, Amount, Msisdn, CommandID)
        payload = {
            'BillRefNumber':BillRefNumber,
            'ShortCode':ShortCode,
            'Amount':Amount,
            'Msisdn':Msisdn,
            'CommandID':CommandID,
        }
        payments.append(payload)

        return make_response(jsonify(
            {
                'Message': 'Payment created',
                'status': 'ok',
                'Data': result
            }), 201)