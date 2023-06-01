---
share: true
uuid: 38fd56a5-a10e-492c-9bbc-8b1ff8deec0a
---
* What are you trying to do? Articulate your objectives using absolutely no jargon.
  * tl;dr The goal of DentropyCloud is to allow one to easily deploy, maintain, and secure any of a set of self hosted applications.
  * We live in a new application paradime where our applications actually run on and require servers far away, the cloud. Rather than running apps on someone elses server the goal of DentropyCloud allows individuals to setup and manage their own server to run their applications on that can be accessed from any device over the internet.
* How is it done today, and what are the limits of current practice?
  * Infrastructure
    * Bare Metal, applications are installed directly on top of the operating system that is installed on the computer hardware. This way can lead to lots of complexity because there can be additional applications installed on the hardware consuming resources that should be going towards other applications. Installing on bare metal can also makes it harder to perform backups, reinstall, and restore when hardware dies.
    * Virtual Machine with choice of [wiki.concepts.list.Hypervisor](/d8de751b-0b11-4076-b9e5-a020a31038a3). Hypervisor allow one to install virtual machines on top of a operating system installed on bare metal hardware. Virtual machines only have access to a limited set of the bare metal hardware in the form of RAM, Storage, and CPU Cores. It is normal to see a virtual machine installed for each application though this can require a lot of additional compute and storage resources that would be better managed with bare metal or containers.
    * Use [wiki.concepts.list.Containerization](/2b328daa-25f6-48a6-846c-bc8be17fb3ee) technologies. Containers are similar to Virtual Machines but rather than creating hard barriers in terms of compute resources containers share resources but operate in separate environments. Below the Operating System there is a piece of software called a Kernel, containers can run abstractly run different operating systems on top of the Kernel rather than having each virtual machine run their own kernel reducing wasted compute resources.
    * Many self hosted applications can also be purchased as IaaS (Infrastructure as a Service) or SaaS (Software as a Service) packages. [Linode App Marketplace](https://www.linode.com/marketplace/) is a good example of this. These IaaS and SaaS models all use IAS(Infrastructure as Code) to deploy, manage, update, backup, and restore these application's so you don't have to. One down side to using IaaS/SaaS offerings is scale. When managing your own applications you can scale the compute resources up or down depending on how you plan to use your applications rather than the default size IaaS and SaaS offers.
  * Deployment
    * Manually
    * [Infrastructure as Code - IAC](/18a9ad29-6aa9-40a6-be0a-ab3883d5d7df)
* What is new in your approach and why do you think it will be successful?
  * For my approach I did everything manually myself therefore I know how all moving parts work
  * I have not found an approach out there that automatically managed DNS with HTTPs in an easy to operate way. I hope to accomplish this using a script or Terraform. This needs to be scoped out #TODO
  * I am trying to keep things as simple as possible, taking the default docker-compose scripts, storing all envrionment variables in a single file, storing all volumes in a single directory for easy backup
* Who cares? If you are successful, what difference will it make?
  * I am doing this primarily for myself to run software in the cloud easily and extendable so I can easily deploy applications I write myself
  * I will be able to run my software easily and hopefully other people will use it
* What are the risks?
  * This project may be a waste of time because there are already so many mature tools to help managed self hosted applications out there
* How much will it cost?
  * $20 USD a month for VPS
  * $5 USD a month for VPS Backups
  * Free-$5 USD a month for additional backups
  * $10-$100 USD a year for Domain Name
* How long will it take?
  * Already have working application, need to scope out future features and marketing plan
* What are the mid-term and final “exams” to check for success?
  * Is dentropycloud actually deployed somewhere
  * Can you delete the server and restore from backup
  * Can passwords be set and reset programmatically?
  * Can it deal with Dynamic DNS?
  * Can you put apps behind a authentication service?
  * Can you run a VPN and access separate apps behind it?

## Sources

* [Catechism](/474cf7d6-0c55-489d-90d0-cf4edce33b3a)