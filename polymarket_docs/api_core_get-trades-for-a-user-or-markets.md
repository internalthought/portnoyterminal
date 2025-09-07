# Get trades for a user or markets
Source: https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| limit | integer |
| default: | Required range: |
| offset | integer |
| takerOnly | boolean |
| CASH | number |
| market | string[] |
| Comma-separated list of condition IDs. Mutually exclusive with eventId. | 0x-prefixed 64-hex string |
| eventId | integer[] |
| Comma-separated list of event IDs. Mutually exclusive with market. | string |
| User Profile Address (0x-prefixed, 40 hex chars) | Example |
| BUY | , |
| SELL |  |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |
