# Get Simplified Markets
Source: https://docs.polymarket.com/developers/CLOB/markets/get-simplified-markets


Get available CLOB markets expressed in a simplified schema.

HTTP REQUEST

GET //simplified-markets?next_cursor=

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| limit | number | limit of results on a single page |
| count | number | number of results |
| next_cursor | string | pagination item to retrieve the next page base64 encoded. 'LTE=' means the end and empty (") means the beginning |
| data | SimplifiedMarket[] | list of markets |

A SimplifiedMarket object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| condition_id | string | id of market which is also the CTF condition ID |
| tokens | Token[2] | binary token pair for market |
| rewards | Rewards | rewards related data |
| min_incentive_size | string | minimum resting order size for incentive qualification |
| max_incentive_spread | string | max spread up to which orders are qualified for incentives (in cents) |
| active | boolean | boolean indicating whether market is active/live |
| closed | boolean | boolean indicating whether market is closed/open |

```code
resp = client.get_simplified_markets(next_cursor = "")
print(resp)
print("Done!")

```
