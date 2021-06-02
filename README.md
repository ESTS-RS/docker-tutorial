# Docker & Kubernetes

## Exemplo

É necessário editar o ip da base na aplicação.

        docker build -t app .
        kubectl apply -f persistent-volume.yml
        kubectl apply -f persistent-volume-claim.yml
        kubectl apply -f statefulset.yml
        kubectl apply -f statefulset-service.yml
        kubectl apply -f deployment.yml
        kubectl apply -f load-balancer.yml

## Notas

Ver o estado do cluster:

        kubectl get all

Acompanhar o output de um pod:

        kubectl logs <pod-name> -f

Descrever um pod:

        kubectl describe <pod-name>
