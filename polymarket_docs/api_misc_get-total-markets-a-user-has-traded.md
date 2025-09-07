# Get total markets a user has traded
Source: https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded



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
| The response is of type | object |


cURL

```code
curl --request GET \
  --url https://data-api.polymarket.com/traded
```

```javascript
{
  "user": 8.992731955465627e+47,
  "traded": 123
}
```

User Profile Address (0x-prefixed, 40 hex chars)

8.992731955465627e+47

Success

The response is of type object.
