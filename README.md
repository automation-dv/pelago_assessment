# Pelago assessment

**Define various test cases that you want to be included in the regression test set**<br /> 
I have defined 7 tests which are specific to travel products:<br /> 
a. test_validate_gokart_schema - It validates Schema of Go Kart product with custom query <br /> 
b. test_validate_gokart_product_is_published - It validate whether Go Kart Product is published or not.<br /> 
c. test_valid_product_ids_product_details - Verify product details of product ids list in class TravelProductsData. I have listed data of only 2 products for now.<br /> 
d. test_valid_query_valid_product_id - Verify status code with valid query and valid product id<br /> 
e. test_valid_query_invalid_product_id -  Verify status code with valid query and invalid product id<br /> 
f. test_invalid_query - Verify status code with invalid query<br /> 
g. test_invalid_data_type_product_id - Verify data type of product id, i.e. other than String<br /> 
**NOTE:** 
1. Few tests are generic to products API and others are specific to Go Kart product that was mentioned as an example in assessment.
2. These tests can be further enhanced by parameterizing them to cover larger number to travel products.
3. Only product details API is covered. Other APIs such as recommended products etc. have not been considered for this assessment.

**Write an API test automation to cover some/all test cases defined in the regression test set**<br /> 
This is done. Code checked-in github covers API test automation.

**Tests to be runnable from the command line**<br /> 
- command => pytest tests<br /> 
- To generate html report => pytest --html=report.html tests<br /> 

**Tests to be configurable to run on various OSes ( Mac, Linux etc )**<br /> 
Tests are configured in such a way that they can be run on all OS.<br /> 

**Tests to be able to run in parallel**
- command => pytest -n 4 tests (here 4 shows number of workers)<br /> 
- Also, following library is needed to run tests in parallel -<br /> 
  pip install pytest-xdist<br /> 
  
**Framework overview :**<br /> 
![image](https://user-images.githubusercontent.com/53708382/123697752-e684ba80-d87a-11eb-966f-4bf883ebb80c.png)<br /> 

**Items couldn't add in this framework due to time constraints:**
- Logger<br /> 
- Allure Reporting for better reporting.<br /> 
