# Get total value of a user's positions
Source: https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| user | string; required |
| User Profile Address (0x-prefixed, 40 hex chars) | Example |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |


cURL

```code
curl --request GET \
  --url https://data-api.polymarket.com/value
```

```javascript
[
  {
    "user": 8.992731955465627e+47,
    "value": 123
  }
]
```

User Profile Address (0x-prefixed, 40 hex chars)

8.992731955465627e+47

0x-prefixed 64-hex string

Success

The response is of type object[].
