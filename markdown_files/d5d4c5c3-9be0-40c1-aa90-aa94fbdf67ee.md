---
share: true
uuid: d5d4c5c3-9be0-40c1-aa90-aa94fbdf67ee
title: dentropycloud.research.backups
---
# Dentropy Cloud Backup Research

As they say if your data does not exist in three locations it might as well not exist. Dentropy Cloud needs automated remote backup procedures so one's data is not lost. The ability to do encrypted back ups to third party storage providers is required.

* Possible backup tools
  * [Documentation](https://rclone.org/docs/)
  * [restic](https://restic.readthedocs.io/e)
  * [duplicity: Main](http://duplicity.nongnu.org/)


### Kubernetes Backup Solutions

The defacto tool for kubernetes backup is Velero, velero plugs into most object storage providers making it pretty simple to use. Envryption is a problem it does not deal with at this time.

* Velero Links
  * [Velero Docs - Backup Reference](https://velero.io/docs/v1.5/backup-reference/)
  * [[ Kube 45 ] Velero - Backup & Restore Kubernetes Cluster - YouTube](https://www.youtube.com/watch?v=C9hzrexaIDA)
  * [Kubernetes: Backup your Stateful apps - Objectif Libre](https://www.objectif-libre.com/en/blog/2020/01/10/kubernetes-backup-stateful-apps/)
  * [Kubernetes Backups, Upgrades, Migrations - with Velero - YouTube](https://www.youtube.com/watch?v=zybLTQER0yY)