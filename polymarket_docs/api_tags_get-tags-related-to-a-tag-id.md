# Get tags related to a tag id
Source: https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id



### Path Parameters

| Name | Type / Notes |
| --- | --- |
| id | integer; required |

### Query Parameters

| Name | Type / Notes |
| --- | --- |
| omit_empty | boolean |
| status | enum |
| active | , |
| closed | , |
| all |  |

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
  --url https://gamma-api.polymarket.com/tags/{id}/related-tags/tags
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

Related tags

The response is of type object[].
