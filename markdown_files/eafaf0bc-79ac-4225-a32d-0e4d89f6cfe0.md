---
share: true
uuid: eafaf0bc-79ac-4225-a32d-0e4d89f6cfe0
title: schema
---
---
id: cQqHHjds5vsBu1QnkdIsp
title: Keybase Schema
desc: ''
updated: 1644024570737
created: 1639441946130
---

* Message Contents 
  * msg.content.type = "text" // or edit
  * msg.content.text.body
* User
  * msg.sender.username
* Topics
  * msg.channel.topic_name
* Teams
  * msg.channel.name
* Topic Mentions
  * msg.channel_mention (Either none, here or all)
  * msg.channel_name_mentions
* Team Mentions
  * msg.content.text.teamMentions
* User Mentions
  * msg.content.type = "text"
  * msg.at_mention_usernames
* Replied
  * msg.content.type = "text"
  * msg.content.text.replyTo
* Reactions
  * msg.reactions.{{Reaction Name}}

``` json
PUT keybase-*/_mapping
{
  "properties": {
    "msg.channel.topic_name": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.content.type": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.sender.username": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.content.reaction.b": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.channel.name": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.content.text.body": { 
      "type":     "text",
      "fielddata": true
    },
    "msg.conversation_id": { 
      "type":     "text",
      "fielddata": true
    }
  }
}
```


``` json
PUT keybase-*
{
  "mappings": {
    "properties": {
      "msg.content.text.body": { "type": "text" }
    }
  }
}
```