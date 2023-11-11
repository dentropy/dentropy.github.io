---
uuid: c71bada1-ae88-4a99-bfec-84efafe8fed9
share: true
title: What discord user has the longest average message length?
---
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