# Get Markets
Source: https://docs.polymarket.com/developers/CLOB/markets/get-markets


Get available CLOB markets (paginated).

HTTP REQUEST

GET //markets?next_cursor=

### Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| next_cursor | no | string | cursor to start with, used for traversing paginated response |

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| limit | number | limit of results in a single page |
| count | number | number of results |
| next_cursor | string | pagination item to retrieve the next page base64 encoded. 'LTE=' means the end and empty (") means the beginning |
| data | Market[] | list of markets |

A Market object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| condition_id | string | id of market which is also the CTF condition ID |
| question_id | string | question id of market which is the CTF question ID which is used to derive the condition_id |
| tokens | Token[2] | binary token pair for market |
| rewards | Rewards | rewards related data |
| minimum_order_size | string | minimum limit order size |
| minimum_tick_size | string | minimum tick size in units of implied probability (max price resolution) |
| category | string | market category |
| end_date_iso | string | iso string of market end date |
| game_start_time | string | iso string of game start time which is used to trigger delay |
| question | string | question |
| market_slug | string | slug of market |
| min_incentive_size | string | minimum resting order size for incentive qualification |
| max_incentive_spread | string | max spread up to which orders are qualified for incentives (in cents) |
| active | boolean | boolean indicating whether market is active/live |
| closed | boolean | boolean indicating whether market is closed/open |
| seconds_delay | integer | seconds of match delay for in-game trade |
| icon | string | reference to the market icon image |
| fpmm | string | address of associated fixed product market maker on Polygon network |

Where the Token object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| token_id | string | erc1155 token id |
| outcome | string | human readable outcome |

Where the Rewards object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| min_size | number | min size of an order to score |
| max_spread | number | max spread from the midpoint until an order scores |
| event_start_date | string | string date when the event starts |
| event_end_date | string | string date when the event ends |
| in_game_multiplier | number | reward multiplier while the game has started |
| reward_epoch | number | current reward epoch |

```code
resp = client.get_markets(next_cursor = "")
print(resp)
print("Done!")

```
