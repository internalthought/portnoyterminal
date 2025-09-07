# Get Spread(s)
Source: https://docs.polymarket.com/developers/CLOB/prices-books/get-spread


Get the spread for a market.

HTTP REQUEST

GET //spread

### Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| token_id | yes | string | token ID to get the spread for |

### Response

{"spread": ".513"}

```code
print(
    client.get_spread(
        "71321045679252212594626385532706912750332728571942532289631379312455583992563"
    )
)

```

# Get Spreads

Get the spreads for a set of markets.

HTTP REQUEST

GET //spreads

### Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| params | yes | BookParams | search params for books |

A BookParams object is of the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| token_id | yes | string | token ID of market to get book for |

### Response

{[asset_id]: spread}

```code
resp = client.get_spreads(
    params=[
        BookParams(
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563"
        ),
        BookParams(
            token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426"
        ),
    ]
)
print(resp)

```
