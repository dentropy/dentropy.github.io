---
uuid: efcd6f7d-b36e-4032-b89b-0fe9fd5a0da9
share: true
title: How much activity for a specific discord guild per month?
---
## Query Name

guild_activity_per_month

## SQL Query
``` sql

select distinct guilds_t.id , guilds_t.guild_name, month_timestamp, msg_count from (
	select
		distinct DATE_TRUNC('month', msg_timestamp)
			         AS  month_timestamp,
	    COUNT(guild_id) AS msg_count,
	    guild_id 
	FROM messages_t
	WHERE guild_id = '{}'
	GROUP BY guild_id, month_timestamp
) as month_messages_t
join guilds_t on month_messages_t.guild_id = guilds_t.id
order by guilds_t.id, month_timestamp;

```

``` sql

select distinct guilds_t.id , guilds_t.guild_name, month_timestamp, msg_count from (
	select
		distinct DATE_TRUNC('month', msg_timestamp)
			         AS  month_timestamp,
	    COUNT(guild_id) AS msg_count,
	    guild_id 
	FROM messages_t
	WHERE guild_id = (SELECT id from guilds_t limit 1 offset 1)
	GROUP BY guild_id, month_timestamp
) as month_messages_t
join guilds_t on month_messages_t.guild_id = guilds_t.id
order by guilds_t.id, month_timestamp;

```

#### Backlinks

* [What is the number of messages from a specific author from a particular discord guild aggregated by month?](/9046827c-32a0-4720-92f2-ab6b7b31bd64)
* [What is the messages per month of a specific discord guild?](/d40934f0-2831-4a55-b0ed-ec1e560db607)
* [What is the activity per month of each discord guild measured in messages per month?](/edb39918-b02f-4ee7-b2b2-d902c8370412)
* [Questions for Discord Data](/46abc67b-bbe7-4800-82f5-f08d4c457ef0)
* [Questions for Discord Data](/46abc67b-bbe7-4800-82f5-f08d4c457ef0)
* [Queries Implemented in queries.py](/3a44d50b-0280-42f8-8fa0-6c15d4ffe161)