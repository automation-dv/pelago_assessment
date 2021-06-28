import json
from jsonschema import validate

from helpers.features.travel_product.product_actions import TravelProductActions
from testdata.expected_data.travel_products_details import TravelProductsDetails
from testdata.expected_data.travel_products_schemas import PKB3V_GOKART_VALID_SCHEMA
from tests.constants import *

class TestTravelProduct():

    @classmethod
    def setup_class(cls):
        cls.product_actions = TravelProductActions()

    def test_validate_gokart_schema(self):
        """
            Validate Go Kart Schema with custom query  .
        """
        response = self.product_actions.get_product_details(PKB3V_GOKART_VALID_QUERY, GOKART_PRODUCT_ID)
        validate(json.loads(response.text), PKB3V_GOKART_VALID_SCHEMA)

    def test_validate_gokart_product_is_published(self):
        """
            Validate Go Kart Product is published
        """
        response = self.product_actions.get_product_details(PKB3V_GOKART_VALID_QUERY, GOKART_PRODUCT_ID)
        response_json = json.loads(response.text)
        status = response_json['data']['product']['status']

        assert status == 'PUBLISHED', "Go Kart Product is published, current status: " + str(status)


    def test_valid_product_ids_product_details(self):
        """
            Verify product details of product ids list in class TravelProductsData.
        """

        products = TravelProductsDetails().product_ids
        for product in products:
            for product_id, product_details in product.items():
                response = self.product_actions.get_product_details(VALID_PRODUCT_QUERY, product_id)
                response_status_code = response.status_code
                assert response_status_code == HTTP_OK, "Invalid Response code : " + str(response_status_code)
                response_json = json.loads(response.text)
                assert response_json['data']['product']['productName'] == product_details[
                    'productName'], "productName doesn't match."
                assert response_json['data']['product']['productUri'] == product_details[
                    'productUri'], " productUri doesn't match."
                assert response_json['data']['product']['destinationId'] == product_details[
                    'destinationId'], "destinationId doesn't match."
                assert response_json['data']['product']['shortDescription'] == product_details[
                    'shortDescription'], "shortDescription doesn't match."
                assert response_json['data']['product']['currency'] == product_details[
                    'currency'], "currency doesn't match."
                assert response_json['data']['product']['duration'] == product_details[
                    'duration'], "duration doesn't match."
                assert response_json['data']['product']['cancellationType'] == product_details[
                    'cancellationType'], "cancellationType doesn't match."
                assert response_json['data']['product']['confirmationType'] == product_details[
                    'confirmationType'], "confirmationType doesn't match."
                assert response_json['data']['product']['voucherType'] == product_details[
                    'voucherType'], "voucherType doesn't match."
                assert response_json['data']['product']['address'] == product_details[
                    'address'], "address doesn't match."
                assert response_json['data']['product']['status'] == product_details[
                    'status'], "status doesn't match."


    def test_valid_query_valid_product_id(self):
        """
            Verify status code with valid query and valid product id
        """
        response = self.product_actions.get_product_details(VALID_PRODUCT_QUERY, VALID_PRODUCT_ID)
        assert response.status_code == HTTP_OK, "Invalid Response code : " + str(response.status_code)


    def test_valid_query_invalid_product_id(self):
        """
            Verify status code with valid query and invalid product id
        """

        response = self.product_actions.get_product_details(VALID_PRODUCT_QUERY, INVALID_PRODUCT_ID)
        response_json = json.loads(response.text)

        status_code = response_json['data']['product']['code']
        error_message = response_json['data']['product']['errorMessage']

        assert status_code == HTTP_NOT_FOUND, 'Invalid Response code : ' + str(status_code)
        assert error_message == INVALID_PRODUCT_ID + ' product not found', "Unexpected error message thrown for invalid product id"


    def test_invalid_query(self):
        """
            Verify status code with invalid query
        """

        response = self.product_actions.get_product_details(INVALID_PRODUCT_QUERY, VALID_PRODUCT_ID)
        assert response.status_code == HTTP_BAD_REQUEST, "Invalid Response code : " + str(response.status_code)


    def test_invalid_data_type_product_id(self):
        """
            Verify data type of product id, i.e. other than String
        """
        INVALID_DATA_TYPE_PRODUCT_ID = 000
        response = self.product_actions.get_product_details(VALID_PRODUCT_QUERY, INVALID_DATA_TYPE_PRODUCT_ID)
        response_json = json.loads(response.text)

        status_code = response_json['data']['product']['code']
        error_message = response_json['data']['product']['errorMessage']

        assert status_code == HTTP_NOT_FOUND, 'Invalid Response code : ' + str(status_code)
        assert error_message == str(INVALID_DATA_TYPE_PRODUCT_ID) + ' product not found', "Unexpected error message thrown for invalid product id"