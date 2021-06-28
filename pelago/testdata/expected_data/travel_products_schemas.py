#https://www.liquid-technologies.com/online-json-to-schema-converter
PKB3V_GOKART_VALID_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "product": {
          "type": "object",
          "properties": {
            "productId": {
              "type": "string"
            },
            "productName": {
              "type": "string"
            },
            "productUri": {
              "type": "string"
            },
            "destinationId": {
              "type": "string"
            },
            "kfEarnMilesPromoText": {
              "type": "string"
            },
            "shortDescription": {
              "type": "string"
            },
            "currency": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "cancellationType": {
              "type": "string"
            },
            "cancellationWindow": {
              "type": "integer"
            },
            "cancellationWindowText": {
              "type": "string"
            },
            "openDateTicket": {
              "type": "boolean"
            },
            "collectPhysicalTicket": {
              "type": "boolean"
            },
            "confirmationType": {
              "type": "string"
            },
            "confirmationTypeText": {
              "type": "string"
            },
            "voucherType": {
              "type": "string"
            },
            "redemptionType": {
              "type": "string"
            },
            "latitude": {
              "type": "string"
            },
            "longitude": {
              "type": "string"
            },
            "address": {
              "type": "string"
            },
            "availabilityStartDate": {
              "type": "string"
            },
            "availabilityEndDate": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "__typename": {
              "type": "string"
            }
          },
          "required": [
            "productId",
            "productName",
            "productUri",
            "destinationId",
            "kfEarnMilesPromoText",
            "shortDescription",
            "currency",
            "duration",
            "cancellationType",
            "cancellationWindow",
            "cancellationWindowText",
            "openDateTicket",
            "collectPhysicalTicket",
            "confirmationType",
            "confirmationTypeText",
            "voucherType",
            "redemptionType",
            "latitude",
            "longitude",
            "address",
            "availabilityStartDate",
            "availabilityEndDate",
            "status",
            "__typename"
          ]
        },
        "productOptions": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "optionId": {
                  "type": "string"
                },
                "optionName": {
                  "type": "string"
                },
                "minimumQuantity": {
                  "type": "integer"
                },
                "maximumQuantity": {
                  "type": "integer"
                },
                "allSelectors": {
                  "type": "array",
                  "items": {}
                },
                "selectorMetaData": {
                  "type": "object",
                  "properties": {
                    "all_selectors": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "all_selectors"
                  ]
                },
                "optionPriceFrom": {
                  "type": "null"
                },
                "__typename": {
                  "type": "string"
                }
              },
              "required": [
                "optionId",
                "optionName",
                "minimumQuantity",
                "maximumQuantity",
                "allSelectors",
                "selectorMetaData",
                "optionPriceFrom",
                "__typename"
              ]
            },
            {
              "type": "object",
              "properties": {
                "optionId": {
                  "type": "string"
                },
                "optionName": {
                  "type": "string"
                },
                "minimumQuantity": {
                  "type": "integer"
                },
                "maximumQuantity": {
                  "type": "integer"
                },
                "allSelectors": {
                  "type": "array",
                  "items": {}
                },
                "selectorMetaData": {
                  "type": "object",
                  "properties": {
                    "all_selectors": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "all_selectors"
                  ]
                },
                "optionPriceFrom": {
                  "type": "null"
                },
                "__typename": {
                  "type": "string"
                }
              },
              "required": [
                "optionId",
                "optionName",
                "minimumQuantity",
                "maximumQuantity",
                "allSelectors",
                "selectorMetaData",
                "optionPriceFrom",
                "__typename"
              ]
            }
          ]
        }
      },
      "required": [
        "product",
        "productOptions"
      ]
    }
  },
  "required": [
    "data"
  ]
}