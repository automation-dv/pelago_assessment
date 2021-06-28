#QUERIES
VALID_PRODUCT_QUERY = "query product($productId: String!) { product(productId: $productId){ ... on Product { productId " \
                "productName productUri destinationId kfEarnMilesPromoText shortDescription currency duration " \
                "cancellationType cancellationWindow cancellationWindowText openDateTicket collectPhysicalTicket " \
                "confirmationType confirmationTypeText voucherType redemptionType priceRangeFrom priceRangeTo latitude " \
                "longitude address availabilityStartDate availabilityEndDate status __typename } ... on PelagoError { " \
                "errorMessage code __typename } __typename }}"
INVALID_PRODUCT_QUERY = "query product($productId: String!)  { product(productId: $productId) }"
PKB3V_GOKART_VALID_QUERY = "query product($productId: String!) { product(productId: $productId){ ... on Product { productId " \
                "productName productUri destinationId kfEarnMilesPromoText shortDescription currency duration " \
                "cancellationType cancellationWindow cancellationWindowText openDateTicket collectPhysicalTicket " \
                "confirmationType confirmationTypeText voucherType redemptionType latitude " \
                "longitude address availabilityStartDate availabilityEndDate status __typename } ... on PelagoError { " \
                "errorMessage code __typename } __typename } productOptions(productId: $productId) {  ... on ProductOption { " \
                "optionId optionName minimumQuantity maximumQuantity allSelectors selectorMetaData optionPriceFrom" \
                " __typename } ... on PelagoListError {  errorMessage  code  __typename } __typename }}"

#PRODUCT ID
GOKART_PRODUCT_ID = "pkb3v"
VALID_PRODUCT_ID = "pkb3v"
INVALID_PRODUCT_ID = "abcde"

#HTTP STATUS
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404