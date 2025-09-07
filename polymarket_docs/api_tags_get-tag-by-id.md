# Get tag by id
Source: https://docs.polymarket.com/api-reference/tags/get-tag-by-id



### Path Parameters

| Name | Type / Notes |
| --- | --- |
| id | integer; required |

### Query Parameters

| Name | Type / Notes |
| --- | --- |
| include_template | boolean |

### Response

| Key | Value |
| --- | --- |
| Status | 200 |
| Content-Type | application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object |


cURL

```code
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/{id}
```

```javascript
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
```

Tag

The response is of type object.
