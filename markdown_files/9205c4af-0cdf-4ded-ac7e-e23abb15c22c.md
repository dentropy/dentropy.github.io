---
uuid: 9205c4af-0cdf-4ded-ac7e-e23abb15c22c
share: true
title: What discord author responds most to questions in a specific discord guild?
---
Think for a sec how many queries can you generate from this?
Work In Progress

## SQL Query

``` SQL
select
	messages_t.msg_content,
	reply_count
from
(
	select 
		count(reply_to_message_id) as reply_count,
		reply_to_message_id
	from
		messages_t
	where
		is_bot = false
		and guild_id in (  (select id from guilds_t limit 1)  )
		and msg_content like '%?%'
	group by reply_to_message_id
	order by reply_count desc
) as reply_count_t
join messages_t on reply_count_t.reply_to_message_id = messages_t.reply_to_message_id


```

## Similar Queries

* [What authors asked the most questions within a specific discord guild?](/c102ef60-4b8c-423e-8102-69578c1ec330)

#### Backlinks

* [Questions for Discord Data](/46abc67b-bbe7-4800-82f5-f08d4c457ef0)