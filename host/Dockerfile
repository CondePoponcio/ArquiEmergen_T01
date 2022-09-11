FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
    libc6 \
    libpcap0.8 \
    apparmor \
    libssl1.0.0 \
    libssl-dev \
    net-tools \
    traceroute \
    iptables \
    arping \
    ipcalc \
    inetutils-ping \
    curl dnsutils wget  vim ethtool tcpdump \
    iperf \
    telnet \
    && apt clean
CMD ["bash"]