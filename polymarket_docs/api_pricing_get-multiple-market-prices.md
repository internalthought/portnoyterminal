# Get multiple market prices
Source: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices



### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |


Retrieves market prices for multiple tokens and sides

cURL

```code
curl --request GET \
  --url https://clob.polymarket.com/prices
```

```javascript
{
  "1234567890": {
    "BUY": "1800.50",
    "SELL": "1801.00"
  },
  "0987654321": {
    "BUY": "50.25",
    "SELL": "50.30"
  }
}
```

Successful response

Map of token_id to side to price
