#!/usr/bin/env python3

import os
from quickScanPackage.cmdModule import execute

class Nmap():
    def scan(self, ipRange):
        cmd = 'sudo nmap -sn ' + ipRange + ' -oG -'
        # -sn ping scan
        # -O --osscan-limit
        # -n # Turns off reverse name resolution, the slowest step.
        sysRes = execute(cmd)
        return sysRes

    def run(self, ipRangeList):
        print('\nEnter root password for OS detection.')
        for ipRange in ipRangeList:
            scanResult = self.scan(ipRange)
        return scanResult
