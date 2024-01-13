---
share: true
uuid: 253c9f0b-fdaf-41e4-ae0b-584e2bc15cee
title: RClone
---
## Install RClone
``` bash

sudo -v ; curl https://rclone.org/install.sh | sudo bash

```

## How to List Remotes

``` bash

rclone config

```

## Where RClone Config Files

``` bash

rclone config file

```

## List contents

``` bash

rclone ls "Vultr Object Storage":/

```

## Sync folder
``` bash

rclone sync ./02-24-2023-08-14-53-umbrel.tar.gz "Vultr Object Storage":/02-24-2023-08-14-53-umbrel.tar.gz

```

## Delete everything on remote

``` bash

rclone delete "Vultr Object Storage":

```

#### Backlinks

* [ETL to QE, Update 4, Code Refactor and TrueNAS S3](/d59dbed7-08bd-462e-8f87-24a80c791f46)
* [ETL to QE, Update 2, S3 and PostGraphile](/01d14af7-0d89-4c3a-90a8-12696e01e036)
* [Backlog - Tutorials](/31f7e81a-967e-41f4-872e-91d1571df726)