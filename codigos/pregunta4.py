#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')

h1 = net.addDocker('h1', dimage="robertxie/ubuntu-nettools")
h2 = net.addDocker('h2', dimage="robertxie/ubuntu-nettools")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
info('*** Creating links\n')
net.addLink(s1, s2, cls=TCLink, delay='50ms', bw=5, loss=2)
net.addLink(s2, s3, cls=TCLink, delay='70ms', bw=10, loss=2)
net.addLink(s3, s4, cls=TCLink, delay='30ms', bw=5, loss=2)
net.addLink(s1, h1)
net.addLink(s4, h2)
info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
