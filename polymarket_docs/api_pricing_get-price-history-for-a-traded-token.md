# Get price history for a traded token
Source: https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| market | string; required |
| startTs | number |
| endTs | number |
| interval | enum; A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs |
| 1m | , |
| 1w | , |
| 1d | , |
| 6h | , |
| 1h | number |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object |


Fetches historical price data for a specified market token

cURL

```code
curl --request GET \
  --url https://clob.polymarket.com/prices-history
```

```javascript
{
  "history": [
    {
      "t": 1697875200,
      "p": 1800.75
    }
  ]
}
```

The CLOB token ID for which to fetch price history

The start time, a Unix timestamp in UTC

The end time, a Unix timestamp in UTC

A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs

The resolution of the data, in minutes

A list of timestamp/price pairs

The response is of type object.
