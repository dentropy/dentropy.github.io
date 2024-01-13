---
share: true
uuid: 627cbfea-af5a-4dbf-b92a-b760c2d98d37
title: HTTP Basic Auth
---
* [dentropydaemon-wiki/Software/List/Traefik](/dentropydaemon-wiki/Software/List/Traefik)
	* [Traefik BasicAuth Documentation - Traefik](https://doc.traefik.io/traefik/middlewares/http/basicauth/)


``` yaml
# Declaring the user list
#
# Note: when used in docker-compose.yml all dollar signs in the hash need to be doubled for escaping.
# To create a user:password pair, the following command can be used:
# echo $(htpasswd -nb user password) | sed -e s/\\$/\\$\\$/g
#
# Also note that dollar signs should NOT be doubled when they not evaluated (e.g. Ansible docker_container module).
labels:
  - "traefik.http.middlewares.test-auth.basicauth.users=test:$$apr1$$H6uskkkW$$IgXLP6ewTrSuBkTrqE8wj/,test2:$$apr1$$d9hr9HBB$$4HxwgUir3HP4EsggP/QNo0"
```

#### Backlinks

* [Supported App List - DentropyCloud](/f738f680-95a2-46e5-bb4c-57b67687e36a)