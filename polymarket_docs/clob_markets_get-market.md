# Get Single Market
Source: https://docs.polymarket.com/developers/CLOB/markets/get-market


Get a single CLOB market.

HTTP REQUEST

GET //markets/

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| market | Market | market object |

```code
resp = client.get_market(condition_id = "...")
print(resp)
print("Done!")

```
