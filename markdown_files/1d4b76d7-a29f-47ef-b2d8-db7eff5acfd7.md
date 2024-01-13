---
share: true
uuid: 1d4b76d7-a29f-47ef-b2d8-db7eff5acfd7
title: Inital Design Doc - DentropyCloud
---
## More detailed plan

The first step of building a dead simple automated kubernetes / docker deployment that stands on the shoulders of open source projects which I am working on [here](https://gitlab.com/dentropy/DentropyCloud).

The second step is to write a piece of software that centralizes all useful metadata one can gather from ones devices and organize it to give users meaningful analytics. Location + All conversations with timestamps

*   keyboard and mouse movements + All social media interactions + music

and shows watched + entire browsing history + how long each application was use and how how long.

The third step is to create a decentralized AI marketplace where people can choose how much information to share with AI systems that try to help them live their lives.

Somewhere is the middle of this is decentralized spotify and netflix and youtube ;-) Aaron Schwartz is the first Martyr of Dataisim and I will learn from his death. I know this is too abstract to do anything with but that is why I am trying to build a team of cofounders, consultants and advisors so I can have a proper design meeting in person. [https://deseng.ryerson.ca/dokuwiki/design:kickoff\_meeting](https://deseng.ryerson.ca/dokuwiki/design:kickoff_meeting) I took a course in this stuff so I think I know what I am talking about

## Project Goals

* Dentropy Daemon allows individuals to gather all their metadata into a single querriable API that they control AND run their own applications.


## Technical Problems

* Choice of container orchestration software
* Storage
	* Applications should support multiple stroage backends including NFS, CIFS, and the host itself.
* Backup and Restore
  * Labeling of storage backups
* VPN
  * Internal VPN
  * External VPS
* The system should be able to route to other applications not using docker on the network
* DNS
  * Internal
  * External
  * Dynamic

## User Flow

**For MVP**

* User gets VPS
* User forwards Domain Name to VPS
* User SSH into VPS
* User install ddaemon
  * ddaemon asks for
    * DNS
    * Storage Options
* User log into ddaemon web gui
* User can install apps
* Wireguard into network and configure application at APPNAME.local
* Once application is configured go to ddaemon web UI and and open it to the public inerwebs
* Apps are available at APPNAME.DOMAIN_NAME.TLD

**Ideally**

* User goes to dentropydaemon.io and signs up for a subscription
* As part of the subscription process the user can buy a domain name or use a subdomain on dentropydaemon.io
* Once user has account they log into portal.dentropydaemon.io where they can install apps via gui, each app can be completely configued from the portal.dentropydaemon.io site without having to connect to the internal network.

## Sprints TODO

### Step 1, An App Store For Cloud

Installing applications in the cloud should be as easy as installing apps from an app store. The key difference here is that all meta data generates will be accessable to them. Censorship is a radically different problem compared to today's social media platforms. A User can be as private or public as they like.

- *Ordered By Priority*
- Simple modules to add
  - Stuff from [linuxserver.io](https://fleet.linuxserver.io/)
  - Emby
  - Calibre and Calibre Web
  - Wallabag
  - Booksonic
  - Torrent Client
  - NFS/Samba server
- Public Facing Modules To Add
  - Matrix Serer with Element front end
  - Pleroma
  - Mastadon
  - Ghost blogging platform
- OpenVPN / Wireguard router for exit traffic
- Nginx and wireguard manager scripts with front end on any raw server 
- LDAP module with UI and connect as many modules to it as possible
- Dynamic Interactive Install Script
- RClone backup and restore functionality with Arweave support
- Bind9 DNS server with Webmin to function as nameserver for subdomains users will use username.dentropydaemon.io
- Build and maintain our own container registry possibly using a
  decentralized protocol
- Kubernetes Migration
  - Package everything into helm charts
- Be able to get a DentropyCloud instance via smart contract

### Step 2, Integration of ones self with their Daemon

Now the infastructure for apps in the cloud exists the next step is to gather and build API's to help one generate their algorithmic reflection and modulates ones existance to the outside world.

- [Activiety Watch](https://activitywatch.net/) project and add a container to DentropyCloud to sync everything
- Automate setting up something like [this](https://beepb00p.xyz/myinfra.html)
- Automation of tasks
  - Use PyAutoGUI on desktop for automation, remote management, and help troubleshooting
  - Add functionality of tasker android application for automation on android
- Capture keystrokes and mouse movements on desktop
- Have simple to use voice changer and anonymity video changer
- Network metadata such as Mac Addresses / IP addresses nearby, wifi network and so forth
- Optionally capture eye movements via webcam on desktop
- Optionally record all video at all times
- Optionally record all audio at all times
  - Feed through speech to Text and put in database
  - Have UI to feed data through simple image classification
    algorithms
- Have API to allow one to easily query and do custom analytics
- Voice assistant integration, [mycroft.ai](https://mycroft.ai/)

### Step 3, Finish Tim May's Blacknet

- Generalized Messaging Schema API
- Bootstrap ones daemon using blockchain and a decentralized name system
- Launch a DAO to federate daemons
  - Research the best arbitration systems
- Create gitcoin with blackjack and hookers


# Dentropy Cloud Manic Plan
If users could pay for a service in the cloud that was as easy to install apps on as a smartphone could lead people off of centralized platforms and give users back control of their data. The general idea was to have a Homelab as a service managed using urbit. This approach is flawed for many reasons.

*   Import facebook friends to urbit

## DentropyCloud


*   Kubernetes Migration
*   Package everything into helm charts
*   RClone backup and restore functionality with Arweave support
*   Bind9 DNS server with Webmin to function as nameserver for subdomains, users will use username.dentropydaemon.io
*   Nginx and wireguard manager scripts with front end
*   Dynamic Interactive python install script so project can be installed on any raw server with python3/ansible
*   Simple modules to add
    *   Emby
    *   Matrix Serer with Element front end
    *   Pleroma
    *   Ghost blogging platform
    *   Wallabag
    *   Calibre Web
    *   Booksonic
    *   Torrent Client
    *   Samba server
*   LDAP module with UI and connect as many modules to it as possible
*   OpenVPN / Wireguard router for exit traffic
*   Migrate from docker to kubernetes
*   Create a Helm package or packages
*   Build and maintain our own container registry possibly using a decentralized protocol

## DentropyDaemon

*   Finish up the Synchronization feature for the \[[https://activitywatch.net/](https://activitywatch.net/) Activity Watch\] project and add a container to DentropyCloud to sync everything
    *   Work with the activity watch team on a fork of activity watch with the following features
    *   Responsible for wireguard connection
    *   Use PyAutoGUI on desktop for automation, remote management, and help troubleshooting
    *   Add functionality of tasker android application for automation on android
    *   Capture keystrokes and mouse movements on desktop
    *   Optionally capture eye movements via webcam on desktop
    *   Have simple to use voice changer and anonymity video changer
    *   Network metadata such as Mac Addresses / IP addresses nearby, wifi network and so forth
    *   Optionally record all audio at all times
        *   Feed through speech to Text and put in database
    *   Optionally record all video at all times
        *   Have UI to feed data through simple image classification algorithms
    *   Have API to allow one to easily query and do custom analytics
    *   Mycroft integration
*   Be able to get a DentropyDaemon instance via smart contract

## Finish Tim May's Blacknet using Urbit or better alternative

*   Import ones friend list from facebook to Urbit and be able to message them through the Urbit UI
*   Connect Urbit + ENS + Handshake Identities to a Activitypub + Matrix social network
*   Launch a DAO using Aragon or better alternative
*   Research the best arbitration systems
*   Create gitcoin with blackjack and hookers


#### Backlinks

* [Design Doc - DentropyCloud](/6c1ccc56-5584-4ec8-9208-34fcdd2a97a5)
* [Backlog - DentropyCloud](/4e71511d-083c-4683-adb1-617be0f9f5be)