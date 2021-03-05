#!/usr/bin/env python3

import os
import json
from quickScanPackage.cmdModule import execute

class Ip():
    def parseJson(self, jsonToParse):
        output = json.loads(jsonToParse)
        print("Found " + str(len(output)) + " interfaces.")
        return output

    def getIpRangeList(self, jsonParsed):
        res = []
        for interface in jsonParsed:
            addr_info_key = 'addr_info'
            if (addr_info_key not in interface):
                continue
            addr_info = interface[addr_info_key]
            if len(addr_info) <= 1:
                continue
            addr_info_ipv4 = addr_info[0]
            addr_info_ipv6 = addr_info[1]
            scope = addr_info_ipv4['scope']
            if scope == 'host':
                continue
            local = addr_info_ipv4['local']
            prefixlen = addr_info_ipv4['prefixlen']
            minPrefixlen = min(24, prefixlen)
            ipRange = local + '/' + str(minPrefixlen)
            res.append(ipRange)
        return res

    def printIpRangeList(self, ipRangeList):
        print("Found " + str(len(ipRangeList)) + " ip ranges :\n")
        for ipRange in ipRangeList:
            print(ipRange)

    def run(self):
        cmd = 'ip -s -d -h -j -p addr show'
        sysRes = execute(cmd)
        jsonParsed = self.parseJson(sysRes)
        ipRangeList = self.getIpRangeList(jsonParsed)
        self.printIpRangeList(ipRangeList)
        return ipRangeList
