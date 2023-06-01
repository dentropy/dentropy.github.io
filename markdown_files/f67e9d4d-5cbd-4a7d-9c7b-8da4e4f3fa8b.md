---
share: true
uuid: f67e9d4d-5cbd-4a7d-9c7b-8da4e4f3fa8b
---
---
id: VjZ1GvlmjjFXXfa97opDc
title: lvm - logical volume manager
desc: ''
updated: 1630509835751
created: 1628449250426
---
# lvm - logical volume manager
Chapter 7, Paritions, Filesystems, and LVM for Noobs
----------------------------------------------------

Make me some LVM
----------------

Linux LVM
---------

Make me some LVM
----------------

    # LVM let's you create super large disks by creating file paritions that span multiple disks
    
    # First we need a physical volume groult
    pvcreate /dev/sdb1
    
    # To see existing physical volumes
    pvdisplay
    
    # Now we need a volume group based on physical volumes
    vgcreate {volume_group_name}} /dev/{device}}
    
    # After we have a volume group we need a logical volume for our system to actually use
    lvcreate -n {logical_volume_name}} -L {Size}G {volume_group_name}}
    
    # Now we can put a file system on the logical volume
    mkfs -t xfs /dev/{name}}/{new name}}
    

LVM needs modifications FUCK
----------------------------

`=====`

LVM needs modifications FUCK
----------------------------

\>>>>>>> 7a8abfaa064042981fb745a54b60262bb1ebedcf

Create and Remove Physical Volumes, Assign Physical VOlumes to Volume
---------------------------------------------------------------------

Groups and Create and Delete Logical Volumes

LVM (Logical Volume Manager)

Use gdisk but use LVM GUID label

Volume Groups?

*   `vgcreate {name}} /dev/WHATEVER1 /dev/WHATEVER2`
*   `lvcreate -n {name}} -L 10G {name volumegroup, from above}}`

One can create and edit file systems on LVM

*   Some file systems can not be edited

`lvremove`

`lvdisplay`

Remove volume group

`vgremove`

`pvremove`

Add New Patitions and Logical Volumes and Swap to a System
----------------------------------------------------------

Non-Destructively

    free -m # Can see Swap, 2-2.5 times free memory
    # Swap is LVM type partition
    # Create LVM, with vgcreate and lvcreate
    mkswap /dev/{lvm name}}/{name partition}}
    
    # Enable swap
    swapon /dev/{lvm name}}/{name partition}}
    free- -n # Check if it works
    
    # Edit /etc/fstab
    /dev/{lvm name}}/{name partition}} swap swap 0 0
    
    # Switch on fstab without reboot
    swapon -a
    free -a # Check if it works
    
    # Can have multiple swap disks and linux will use the total storage of all of them
    
    blkid
    
    # Edit /etc/fstab
    UUID={UUID}} swap swap 0 0
    
    swapoff /dev/WHATEVER
    swapoff -a
    
    swapon -a # Apply swap from /etc/fstab
    
    cat /proc/swaps
    

Extend Existing Logical Volumes
-------------------------------

    cd /dev
    # Should see a bunch of aditional devices
    fdisk /dev/{device}}
    # Make sure to label device LVM
    pvcreate /dev/{device}}
    pvdisplay
    vsgreate {name}} /dev/{device}}
    lvcreate -n {new name}} -L {Size}G {name}}
    mkfs -t xfs /dev/{name}}/{new name}}
    mount /dev/{name}}/{new name}} {Mount Location}}
    df -h
    # With logical volumes you can add and remove phyiscal volumes without interupting the data on the volume
    gdisk /dev/{new device}}
    # Use linux LVM code
    vsextend {name}} /dev/{new device}}
    
    # Copy from one thing to another
    pvmove /dev/{device}} # To remove data from
    
    # Remove Phyiscal device
    vgreduce {name}} /dev/{device}} # Device you want to remove
    
    # Congradualtions you just did a live data migration
    
    # Now to actually extend
    
    lvextend -L {Size}}G /dev/{name}}/{new name}}  # Change size
    lvextend -L +{Size}}G /dev/{name}}/{new name}} # Add
    # Wait the file system is still fucked
    
    xfs_growfs {Mount Point}}
    # For ext4 resize2fs
    
    lvextend -l +50%FREE /dev/{name}}/{new name}} # Take up 50% of aditional space
