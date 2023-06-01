---
share: true
uuid: fa93aadb-7ded-4bda-be1b-59bbd9bf9af6
---
---
id: DPUQM04b4dqQzUOfBHzro
title: Setup
desc: ''
updated: 1628449250321
created: 1628449250321
---
# setup
Setup of stuff
--------------

docker
------

    wget https://get.docker.com -O docker.sh
    sudo bash docker.sh
    rm docker.sh
    sudo usermod -aG docker USERNAME
    

kubectl
-------

    curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x ./kubectl
    sudo mv ./kubectl /usr/local/bin/kubectl
    

minikube
--------

*   Kubernetes documentation [https://kubernetes.io/docs/tasks/tools/install-minikube/](https://kubernetes.io/docs/tasks/tools/install-minikube/)
*   Minikube documentation [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
*   Kubectl for docker users [https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/](https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/)

    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
    && chmod +x minikube
    sudo mv minikube /usr/bin
    

Run it

    minikube start --driver=docker
    minikube addons enable ingress
    

*   [Ingress Minikube](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
*   [hello-minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)

Helm
----

[https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)

    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    helm repo add stable https://kubernetes-charts.storage.googleapis.com/
    rm get_helm.sh
    

kompose
-------

[https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/)

    curl -L https://github.com/kubernetes/kompose/releases/download/v1.21.0/kompose-linux-amd64 -o kompose
    sudo mv kompose /usr/bin/kompose
    sudo chmod +x /usr/bin/kompose
    

Open Shift
----------

[https://github.com/openshift/origin/releases](https://github.com/openshift/origin/releases)

[https://developers.redhat.com/products/codeready-containers/overview](https://developers.redhat.com/products/codeready-containers/overview)

[https://developers.redhat.com/blog/2019/09/05/red-hat-openshift-4-on-your-laptop-introducing-red-hat-codeready-containers/](https://developers.redhat.com/blog/2019/09/05/red-hat-openshift-4-on-your-laptop-introducing-red-hat-codeready-containers/)
