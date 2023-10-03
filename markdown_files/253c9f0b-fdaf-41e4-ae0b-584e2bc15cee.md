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