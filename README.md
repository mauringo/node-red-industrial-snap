# Modded Node-RED Snap package to be  more industrial

[![platform](https://img.shields.io/badge/platform-Node--RED-red)](https://nodered.org)
[![GitHub version](https://badge.fury.io/gh/node-red%2Fnode-red.svg)](https://badge.fury.io/gh/node-red%2Fnode-red)

The Node-RED graphical wiring tool for Low-code programming of event-driven applications.
Packaged as a Core18 based Ubuntu Snap, intended for multiple architectures.

Listens on port 1881 and runs as as service in strict mode by default.
Fully configurable on port 1882: edit **settings.js** directly from a webpage!

### Modifications

The snap by default comes with the following packages installed

 - node-red dashboard
 - CtrlX-Automation-Contrib
 - OPCUA contrib
 - MongoDB3
 - Influxdb 





#### Building
   
    sudo snap install multipass
    sudo snap install snapcraft --classic
    snapcraft
    
