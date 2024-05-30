FROM registry.suse.com/bci/python:3.11

MAINTAINER mail@maltewildt.de

WORKDIR /usr/src/app

ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD podman-kube-secrets.py ./

ENTRYPOINT ["python3", "podman-kube-secrets.py" ]



