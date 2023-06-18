---
share: true
uuid: ceddbaf7-5c37-453d-a24d-e53cd5de49f8
title: qanda
---
---
id: 4Q0S6IXaNh4Mvc66HvEov
title: Qanda
desc: ''
updated: 1628449250321
created: 1628449250321
---
# qanda
How do I port forward to localhost
----------------------------------

    kubectl port-forward html-against-humanity-6b88977966-2sfdm 5000:5000
    

How do I solve this x509 Certificate Problem
--------------------------------------------

`--insecure-skip-tls-verify`

Questions
---------

*   Generate cert to connect remotely to cluster
    
*   Forward an entire port into the cluster
    
*   ELI5 Routers and Kubernetes
    
*   How to bind ingress to a specific host
    
*   Simple way to create a kubernetes cluster
    
*   How to set up and use persistent storage
    
*   Any good tutorials
    
    *   [https://kubernetes.io/docs/tutorials/hello-minikube/](https://kubernetes.io/docs/tutorials/hello-minikube/)
*   How do I Backup and restore containers
    
    *   [Copying container files](https://kubectl.docs.kubernetes.io/pages/container_debugging/copying_container_files.html)
    *   [velero from vmware](https://github.com/vmware-tanzu/velero)

Welcome to OpenShift
--------------------

*   Troubleshooting issues
    
    *   [https://github.com/openshift/origin/issues/21650](https://github.com/openshift/origin/issues/21650)
*   Get everything from openshift
    
    *   `oc delete all --selector app=blog-django-py`
*   Delete stuff from openshift
    
    *   `oc get all -o name`

How do containers on the same pod communicate
---------------------------------------------

Each pod has a seperate port open to it so just use localhost followed by the opened port