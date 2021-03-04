#!/usr/bin/env python3

from quickScanPackage.ipModule import Ip
from quickScanPackage.nmapModule import Nmap

def main():
    ip = Ip()
    ipJson = ip.run()

    nmap = Nmap()
    hosts = nmap.run(ipJson)

    print(hosts)

if __name__ == '__main__':
    main()
