# List tags
Source: https://docs.polymarket.com/api-reference/tags/list-tags



### Query Parameters

| Name | Type / Notes |
| --- | --- |
| limit | integer; Required range: |
| offset | integer; Required range: |
| order | string |
| Comma-separated list of fields to order by | boolean |
| include_template | boolean |
| is_carousel | boolean |

### Response

| Key | Value |
| --- | --- |
| Status |  |
| Content-Type | 200 - application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |


cURL

```code
curl --request GET \
  --url https://gamma-api.polymarket.com/tags
```

```javascript
[
  {
    "id": "",
    "label": "",
    "slug": "",
    "forceShow": true,
    "publishedAt": "",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

Comma-separated list of fields to order by

List of tags

The response is of type object[].
