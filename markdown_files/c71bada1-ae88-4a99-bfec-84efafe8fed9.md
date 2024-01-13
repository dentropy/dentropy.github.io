---
uuid: c71bada1-ae88-4a99-bfec-84efafe8fed9
share: true
title: What discord user has the longest average message length?
---
## SQL Query

``` sql

select 
	authors_t.author_name,
	authors_t.nickname,
	avg_content_length_t.content_length,
	avg_content_length_t.content_count,
	authors_t.id
from 
(
	select 
		author_guild_id, 
		count(content_length) as content_count,
		AVG(content_length) as content_length
	from
		messages_t
	where isbot = false
	group by author_guild_id
) as avg_content_length_t
join authors_t
on authors_t.id = avg_content_length_t.author_guild_id
order by avg_content_length_t.content_length desc;

```

## Specific Queries

**Minimum of 20 messages sent from real person**

``` sql


select authors_t.name, authors_t.nickname, authors_t.id, avg_content_length_t.content_length, avg_content_length_t.content_count  from 
(
	select 
		author_id, 
		count(content_length) as content_count,
		AVG(content_length) as content_length
	from
		messages_t
	where isbot = false
	group by author_id
) as avg_content_length_t
join authors_t
on authors_t.id = avg_content_length_t.author_id
where avg_content_length_t.content_count >= 20
order by avg_content_length_t.content_length desc;

```

## Development Queries

``` sql

select * from
(
	select * from messages_t limit 10000
) as msg_t;



select authors_t.name, authors_t.nickname, avg_content_length_t.content_length  from 
(
	select author_id, AVG(content_length) as content_length from
	(
		select * from messages_t limit 10000
	) as msg_t
	group by author_id
) as avg_content_length_t
join authors_t
on authors_t.id = avg_content_length_t.author_id
order by avg_content_length_t.content_length desc;
```

#### Backlinks

* [What discord user has the longest average message length in a particular guild?](/2f4fd09e-24a3-4359-81b2-049742a03610)
* [ETL to QE, Update 17, Readjusting Goal Posts](/d14bd990-0628-4152-9bea-0c588dc707e8)
* [Discord Author Specific Queries](/f6c57d06-6240-41fc-9174-7a6b18362030)