# Get comments by user address
Source: https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address


```javascript
[
  {
    "id": "",
    "body": "",
    "parentEntityType": "",
    "parentEntityID": 123,
    "parentCommentID": "",
    "userAddress": "",
    "replyAddress": "",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "profile": {
      "name": "",
      "pseudonym": "",
      "displayUsernamePublic": true,
      "bio": "",
      "isMod": true,
      "isCreator": true,
      "proxyWallet": "",
      "baseAddress": "",
      "profileImage": "",
      "profileImageOptimized": {
        "id": "",
        "imageUrlSource": "",
        "imageUrlOptimized": "",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "",
        "relID": 123,
        "field": "",
        "relname": ""
      },
      "positions": [
        {
          "tokenId": "",
          "positionSize": ""
        }
      ]
    },
    "reactions": [
      {
        "id": "",
        "commentID": 123,
        "reactionType": "",
        "icon": "",
        "userAddress": "",
        "createdAt": "2023-11-07T05:31:56Z",
        "profile": {
          "name": "",
          "pseudonym": "",
          "displayUsernamePublic": true,
          "bio": "",
          "isMod": true,
          "isCreator": true,
          "proxyWallet": "",
          "baseAddress": "",
          "profileImage": "",
          "profileImageOptimized": {
            "id": "",
            "imageUrlSource": "",
            "imageUrlOptimized": "",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "",
            "relID": 123,
            "field": "",
            "relname": ""
          },
          "positions": [
            {
              "tokenId": "",
              "positionSize": ""
            }
          ]
        }
      }
    ],
    "reportCount": 123,
    "reactionCount": 123
  }
]
```

### Path Parameters

| Name | Type / Notes |
| --- | --- |
| user_address | string; required |

### Query Parameters

| Name | Type / Notes |
| --- | --- |
| limit | integer; Required range: |
| offset | integer; Required range: |
| order | string |
| Comma-separated list of fields to order by | boolean |

### Response

| Key | Value |
| --- | --- |
| Status |  |
| Content-Type | 200 - application/json |

| Field | Type / Notes |
| --- | --- |
| The response is of type | object[] |
