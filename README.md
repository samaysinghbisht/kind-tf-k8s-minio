<h3>Task:</h3>

1. Setup two clusters locally using Kind and Terraform
2. Deploy minio object storages in one cluster
3. Deploy an application which fetches  images from a bucket in minio running in another cluster and display it on the frontend.


<h3>Pre-Requisites:</h3>
Required Tools:

 - Kind 
 - Terraform
 - Docker
 - Kubernetes


<h3>Steps to deploy locally:</h3>

1. Clone the repo
2. Change Directory to infra and run:
    - terraform fmt
    - terraform init
    - terraform plan
    - terraform apply
    This should create two kind clusters with names "kind-infrastructure" and "kind-application"
3. Goto root directory and run command to change context to kind-infrastructure
    - kubectl config use-context kind-infrastructure
4. Change Directory to metallb and run:
    - kubectl apply -f metallb-native.yaml
    - kubectl wait --namespace metallb-system \
                --for=condition=ready pod \
                --selector=app=metallb \
                --timeout=90s
    - kubectl apply -f metallb-config.yaml
5. Goto Root Directory again and now deploy minio by running command:
    - kubectl apply -f minio-deployment.yaml
6. List out the svc in minio namespace, and note down the External IP, and update the jw-scaler-deplpyment.yaml line 22 and 33 with that IP:9000

7. We need to change the context to another cluster now and for that run command:
    - kubectl config use-context kind-application
8. Now, we can go ahead and deploy the application which would create the bucket in minio and then displays those images in our frontend, for that run command:
    - kubectl apply -f jw-scaler-deployment.yaml
9. Now port forward your jw-scaler service to desired port and access it on your localhost.