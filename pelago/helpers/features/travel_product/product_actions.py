import logging
import requests
import urllib3
from helpers.base import Base


class TravelProductActions(Base):

    def get_product_details(self, query, product_id):
        # disabling ssl warnings due to verify=False in request API calls
        urllib3.disable_warnings()
        headers = {
            "content-type": "application/json",
            "Host": "traveller-core.pelago.co",
        }
        payload = {"query": query, "variables": {"productId": product_id}, "operationName": "product"}
        # print('Payload : %s' % str(payload)) # These statements shall be replaced by log statements
        response = requests.post(self.url, json=payload, verify=False, headers=headers)

        return response
