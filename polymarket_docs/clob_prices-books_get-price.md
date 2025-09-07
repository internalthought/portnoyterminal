# Get Price
Source: https://docs.polymarket.com/developers/CLOB/prices-books/get-price


```code
resp = client.get_prices(
    params=[
        BookParams(
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
            side="BUY",
        ),
        BookParams(
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
            side="SELL",
        ),
        BookParams(
            token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426",
            side="BUY",
        ),
        BookParams(
            token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426",
            side="SELL",
        ),
    ]
)
print(resp)

```
