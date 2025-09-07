# Get top holders for markets
Source: https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| limit | integer |
| default: | Required range: |
| market | string[]; required |
| Comma-separated list of condition IDs. | 0x-prefixed 64-hex string |
| minBalance | integer |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |
