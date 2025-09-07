# Get user activity
Source: https://docs.polymarket.com/api-reference/core/get-user-activity



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| limit | integer |
| default: | Required range: |
| offset | integer |
| user | string; required |
| User Profile Address (0x-prefixed, 40 hex chars) | Example |
| Comma-separated list of condition IDs. Mutually exclusive with eventId. | 0x-prefixed 64-hex string |
| eventId | integer[] |
| Comma-separated list of event IDs. Mutually exclusive with market. | enum[] |
| Show | integer; Required range: |
| end | integer; Required range: |
| sortBy | enum |
| TIMESTAMP | , |
| TOKENS | enum |
| ASC | enum |
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


Returns on-chain activity for a user.
