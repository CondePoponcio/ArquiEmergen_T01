FROM containernet/containernet

RUN apt update

RUN apt install -y

RUN apt install -y linux-image-amd64 linux-headers-amd64

RUN apt install --reinstall wireguard-dkms

CMD ["bash"]
