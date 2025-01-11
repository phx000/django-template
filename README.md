### Steps

```
py -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

pip freeze > requirements.txt


npm create vite@latest frontend --template react-ts

cd frontend

npm install


docker-compose up --build -d
```

for k8s:
- add nginx ingress controller if not present
- add the monitoring bundle
- create a namespace
- change the namespace in all resources
- change the api service image name in api.yaml and worker.yaml
- change ingress host
- edit configmap and secret
- run py manage.py tests --keepdb
- change name of helm chart
- set all the secrets and vars in the gh repo (or dont, if the repo is going to be forked)
- create a dev and prod db in postgres

todos:
- review all env vars and config vars




steps:
- install py
- install helm

- inject configmap
- inject secrets

- run tests
- log into docker hub

- install doctl
- build and push docker image
- set up kubectl
- upgrade helm chart
---------------------------

- install py
- install helm

- log into docker hub
- build image

- inject configmap
- inject secrets

- run tests

- install doctl

- push image

- set up kubectl

- upgrade helm chart
----