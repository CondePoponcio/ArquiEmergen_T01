FROM ubuntu:16.04
RUN apt-get update 

RUN apt-get install -y libc6 libpcap0.8 \ 
    apparmor libssl1.0.0 libssl-dev net-tools 
RUN apt-get install -y traceroute iptables \
    arping ipcalc inetutils-ping
RUN apt-get install -y curl dnsutils wget vim \
    ethtool tcpdump \
    iperf \
    telnet \
    && apt clean
CMD ["bash"]