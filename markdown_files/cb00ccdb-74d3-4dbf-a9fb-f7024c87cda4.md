---
share: true
uuid: cb00ccdb-74d3-4dbf-a9fb-f7024c87cda4
---
---
id: gc7cc9ndr6jz76n6ukgp6u8
title: Docs
desc: ''
updated: 1641486548217
created: 1640737198013
---

* [ddaemon.monorepo.datapipelines](/undefined)

## Adding a data visualization

1. Write down the name of the data visualization...
  * reducer value, to get and set:
  * file / component name:
  * title:
1. Add button to press
  * DiscordSideBarLeft.js for discord
  * KeybaseQuerySelect.js for keybase
1. Run reducer function when button is called to update context
  * DATA_VIZ_SELECT for discord
  * GRAPH_CONTROLS for keybase
1. Create component
  * Copy the template component
  * Rename the file
  * Set the correct name of the component function
1. Import component and add if statement to render the component
  * DiscordRenderDataViz.js function renderDataViz for Discord
  * KeybaseRoot.js function renderGraph for keybase


## Files with DataViz names

* DiscordSidebarLeft.js and KeybaseQuerySelect.js

## backend_api

``` javascript
{
  dataset : "STRING",
  query_name : "STRING",
  inputs : {
    NAME_1 : "OBJECT DATA",
    NAME_2 : "OBJECT DATA",
    NAME_3 : "OBJECT DATA"
  }
}
```

**dataset**

* discord
* keybase
* git

**query_name**

* discord
  * most_messages_per_user
* keybase
* git
