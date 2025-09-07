# Get Midpoint(s)
Source: https://docs.polymarket.com/developers/CLOB/prices-books/get-midpoint


Get the midpoint price for a market (halfway between best bid or best ask).

HTTP REQUEST

GET //midpoint

### Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| token_id | yes | string | token ID market to get price for |

### Response

{"mid": "0.55"}

```code
resp = client.get_midpoint(
    "71321045679252212594626385532706912750332728571942532289631379312455583992563"
)
print(resp)
print("Done!")

```

# Get Midpoints

Get the midpoint prices for a set of market (halfway between best bid or best ask).

HTTP REQUEST

POST //midpoints

### Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| params | yes | BookParams | search params for books |

A BookParams object is of the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| token_id | yes | string | token ID of market to get book for |

### Response

{[asset_id]: mid_price}

```code
resp = client.get_midpoints(
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
