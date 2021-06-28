# pelago_assessment

**Define various test cases that you want to be included in the regression test set**
I have defined 7 tests:
a. test_validate_gokart_schema - It validates Schema of Go Kart product with custom query 
b. test_validate_gokart_product_is_published - It validate whether Go Kart Product is published or not.
c. test_valid_product_ids_product_details - Verify product details of product ids list in class TravelProductsData. I have listed data of only 2 products for now.
d. test_valid_query_valid_product_id - Verify status code with valid query and valid product id
e. test_valid_query_invalid_product_id -  Verify status code with valid query and invalid product id
f. test_invalid_query - Verify status code with invalid query
g. test_invalid_data_type_product_id - Verify data type of product id, i.e. other than String

**Write an API test automation to cover some/all test cases defined in the regression test set**
Done

**Tests to be runnable from the command line**
- command => pytest tests
- To generate html report => pytest --html=report.html tests

**Tests to be configurable to run on various OSes ( Mac, Linux etc )**
Tests are configured in such a way that they can be run on all OS.

**Tests to be able to run in parallel**
- command => pytest -n 4 tests (here 4 shows number of workers)
- Also, following library is needed to run tests in parallel -
  pip install pytest-xdist
  
**Framework overview :**
![image](https://user-images.githubusercontent.com/53708382/123697752-e684ba80-d87a-11eb-966f-4bf883ebb80c.png)

**Items couldn't add in this framework due to time constraints:**
- Logger
- Allure Reporting for better reporting.
