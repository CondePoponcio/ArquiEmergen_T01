FROM containernet/containernet

RUN apt update

RUN apt install -y x11-xserver-utils

RUN apt install -y ifupdown net-tools

RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf
RUN echo "nameserver 8.8.4.4" >> /etc/resolv.conf

#RUN xhost +si:localuser:root
