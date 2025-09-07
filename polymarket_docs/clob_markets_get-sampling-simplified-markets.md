# Get Sampling Simplified Markets
Source: https://docs.polymarket.com/developers/CLOB/markets/get-sampling-simplified-markets


Get available CLOB markets expressed in a reduced schema that have rewards enabled.

HTTP REQUEST

GET //sampling-simplified-markets?next_cursor=

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| limit | number | limit of results on a single page |
| count | number | number of results |
| next_cursor | string | pagination item to retrieve the next page base64 encoded. 'LTE=' means the end and empty (") means the beginning |
| data | SimplifiedMarket[] | list of sampling markets |

```code
resp = client.get_sampling_simplified_markets(next_cursor = "")
print(resp)
print("Done!")

```
