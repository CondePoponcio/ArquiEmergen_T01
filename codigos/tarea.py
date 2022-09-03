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
h1 = net.addDocker('h1', ip='10.0.0.251', dimage="robertxie/ubuntu-nettools")
h2 = net.addDocker('h2', ip='10.0.0.252', dimage="robertxie/ubuntu-nettools")
h3 = net.addDocker('h3', ip='10.0.0.253', dimage="robertxie/ubuntu-nettools")
h4 = net.addDocker('h4', ip='10.0.0.254', dimage="robertxie/ubuntu-nettools")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
info('*** Creating links\n')
net.addLink(s2, s1)
net.addLink(s2, s3, delay='15ms', bw=10)
net.addLink(s3, s4, delay='30ms', bw=10, loss=10)
net.addLink(s1, h1)
net.addLink(s1, h2)
net.addLink(s3, h3)
net.addLink(s4, h4)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([h1, h2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
