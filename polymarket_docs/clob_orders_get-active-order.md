# Get Active Orders
Source: https://docs.polymarket.com/developers/CLOB/orders/get-active-order




This endpoint requires a L2 Header.

Get active order(s) for a specific market.

HTTP REQUEST

GET //data/orders

### Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | no | string | id of order to get information about |
| market | no | string | condition id of market |
| asset_id | no | string | id of the asset/token |

### Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OpenOrder[] | list of open orders filtered by the query parameters |

```code
from py_clob_client.clob_types import OpenOrderParams

resp = client.get_orders(
    OpenOrderParams(
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    )
)
print(resp)
print("Done!")

```



```code
from py_clob_client.clob_types import OpenOrderParams

resp = client.get_orders(
    OpenOrderParams(
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    )
)
print(resp)
print("Done!")

```

### ​Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | no | string | id of order to get information about |
| market | no | string | condition id of market |
| asset_id | no | string | id of the asset/token |

### ​Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OpenOrder[] | list of open orders filtered by the query parameters |

```code
from py_clob_client.clob_types import OpenOrderParams

resp = client.get_orders(
    OpenOrderParams(
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    )
)
print(resp)
print("Done!")

```
