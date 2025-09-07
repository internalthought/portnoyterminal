# Get current positions for a user
Source: https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user


```javascript
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "asset": "",
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "size": 123,
    "avgPrice": 123,
    "initialValue": 123,
    "currentValue": 123,
    "cashPnl": 123,
    "percentPnl": 123,
    "totalBought": 123,
    "realizedPnl": 123,
    "percentRealizedPnl": 123,
    "curPrice": 123,
    "redeemable": true,
    "mergeable": true,
    "title": "",
    "slug": "",
    "icon": "",
    "eventSlug": "",
    "outcome": "",
    "outcomeIndex": 123,
    "oppositeOutcome": "",
    "oppositeAsset": "",
    "endDate": "",
    "negativeRisk": true
  }
]
```

### Query Parameters

| Name | Type / Notes |
| --- | --- |
| user | string; required; User address (required) |
| Example | string[] |
| Comma-separated list of condition IDs. Mutually exclusive with eventId. | 0x-prefixed 64-hex string |
| eventId | integer[] |
| Comma-separated list of event IDs. Mutually exclusive with market. | number |
| default: | Required range: |
| redeemable | boolean |
| offset | integer |
| sortBy | enum |
| CURRENT | , |
| INITIAL | , |
| TOKENS | , |
| CASHPNL | , |
| PERCENTPNL | , |
| TITLE | , |
| RESOLVING | , |
| PRICE | enum |
| ASC | string |
| 100 |  |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |
