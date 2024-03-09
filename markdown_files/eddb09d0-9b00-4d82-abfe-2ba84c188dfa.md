---
uuid: eddb09d0-9b00-4d82-abfe-2ba84c188dfa
share: true
title: Caddy
---
#### Background

[Caddy - The Ultimate Server with Automatic HTTPS](https://caddyserver.com/)

#### Outline

* Caddy Install and Setup
* Static [HTML](../272babbb-b019-4290-941a-01ae25d07fe1) Hosting
* [HTTP](../2093e831-34f9-470e-a7de-efd00b084063) and [HTTPS](../1ec39053-a1f2-47e3-b951-e46c209273a5) Proxies
* Securing Caddy's API
* Examples using Caddy's API
* Using a Hostname on Local Network
* Deploying to VPS
* Setting DNS
* Use API to setup Server
* Static Site Hosting Script
* [Cloudflare](../0795ae4a-3e15-47e2-bc40-8ac275081ca6) tutorial


#### Caddy Install and Setup

[Debian](../e5892695-48a8-4b08-b405-d70790407a4a)/[Ubuntu](../a55f9e87-3627-4503-ad12-9e0748b12a50) Install
``` bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl


curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg


curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list

sudo apt update


sudo apt install caddy
```
For other systems check out, [Install — Caddy Documentation](https://caddyserver.com/docs/install)

Try not to use docker, it's a bitch with Caddy, plus Caddy can proxy into your docker containers anyways.

#### Caddy Config Files

[Getting Started — Caddy Documentation](https://caddyserver.com/docs/getting-started)

#### Static [HTML](../272babbb-b019-4290-941a-01ae25d07fe1) Hosting

``` bash

caddy file-server --root ~/mysite

```



* [Specific Docs](https://caddyserver.com/docs/quick-starts/static-files)
* [Enable HTTP on different port other than 80](https://caddy.community/t/caddy-localhost-https-this-site-can-t-provide-a-secure-connection/7483/5)


#### [HTTP](../2093e831-34f9-470e-a7de-efd00b084063) and [HTTPS](../1ec39053-a1f2-47e3-b951-e46c209273a5) Proxies

HTTPS, signed and unsigned, is the default for Caddy. To enable HTTP you need to make sure the `http_port` setting is set in the correct part of the config.

* apps
	* $APP_NAME
		* http_port : $PORT_NUMBER_1
		* servers 
			* Server Name
				* listen [":$PORT_NUMBER_1", ":$PORT_NUMBER_2"]

Below is an example where port 8080 is http and 4443 is https.

``` JSON

{
  "apps": {
    "http": {
      "http_port": 8080,
      "servers": {
        "srv0": {
          "listen": [
            ":4443",
            ":8080"
          ],
          ...
        }
      }
    }
  }
}
			  

```

#### Securing Caddy's API
* Examples using Caddy's API
* Using a Hostname on Local Network
* Deploying to VPS
* Setting DNS
* Use API to setup Server
* Static Site Hosting Script
* [Cloudflare](../0795ae4a-3e15-47e2-bc40-8ac275081ca6) tutorial

#### Forward port 80 to 8080 and 443 to 4443

``` bash

iptables -t nat -A OUTPUT -o lo -p tcp --dport 80 -j REDIRECT --to-port 8080

```


#### TODO Links

* [API Tutorial — Caddy Documentation](https://caddyserver.com/docs/api-tutorial)
* [API — Caddy Documentation](https://caddyserver.com/docs/api)
* [How correctly use the admin API endpoint from other host - Help - Caddy Community](https://caddy.community/t/how-correctly-use-the-admin-api-endpoint-from-other-host/19933)
* [How to remotely configure Caddy 2 - Help - Caddy Community](https://caddy.community/t/how-to-remotely-configure-caddy-2/8063/3)
* [admin - JSON Config Structure - Caddy Documentation](https://caddyserver.com/docs/json/admin/)
* [How to configure the API interface via a Caddyfile? - Help - Caddy Community](https://caddy.community/t/how-to-configure-the-api-interface-via-a-caddyfile/7669)
* [API Tutorial — Caddy Documentation](https://caddyserver.com/docs/api-tutorial)
* [How to reset caddy to a blank config state? - Help - Caddy Community](https://caddy.community/t/how-to-reset-caddy-to-a-blank-config-state/7698)