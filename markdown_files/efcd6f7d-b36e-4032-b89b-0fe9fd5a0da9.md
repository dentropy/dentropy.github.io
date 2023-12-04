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