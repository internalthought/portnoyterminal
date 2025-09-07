# Get multiple market prices by request
Source: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request



### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |



cURL

```javascript
curl --request POST \
  --url https://clob.polymarket.com/prices \
  --header 'Content-Type: application/json' \
  --data '[
  {
    "token_id": "1234567890",
    "side": "BUY"
  },
  {
    "token_id": "0987654321",
    "side": "SELL"
  }
]'
```

200

example
