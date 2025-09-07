# Get Books
Source: https://docs.polymarket.com/developers/CLOB/prices-books/get-books


HTTP REQUEST

POST //books

### Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| params | yes | BookParams | search params for books |

A BookParams object is of the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| token_id | yes | string | token ID of market to get book for |

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| - | OrderBook[] | list orderbooks |

A OrderBook object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| market | string | condition id |
| asset_id | string | id of the asset/token |
| hash | string | hash summary of the orderbook content |
| timestamp | string | unix timestamp the current book generation in milliseconds (1/1,000 second) |
| bids | OrderSummary[] | list of bid levels |
| asks | OrderSummary[] | list of ask levels |

A OrderSummary object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| price | string | price |
| size | string | size |

```code
print(
    client.get_order_books(
        params=[
            BookParams(
                token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563"
            ),
            BookParams(
                token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426"
            ),
        ]
    )
)

```
