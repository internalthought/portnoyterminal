# List comments
Source: https://docs.polymarket.com/api-reference/comments/list-comments


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


cURL

```code
curl --request GET \
  --url https://gamma-api.polymarket.com/comments
```

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
