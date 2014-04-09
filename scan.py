#!/usr/bin/env python

import iptools.ipv4
import netaddr
import re

hosts = []

print ('\nThis is a quick script used to ssh into a range of \nip addresses to check for an existence service.\n')
ip = raw_input('Input block of IP addresses (CIDR notation, i.e. 10.0.0.0/24): ')

# Validate if true CIDR notation
if iptools.ipv4.validate_cidr(ip):
  print('True, valid cidr:\n')

  # Okay, true, so let's put the valid hosts somewhere. Any subnet <= 4 IPs is an empty list
  for i in netaddr.IPNetwork(ip).iter_hosts():
    # Turn i into type string
    hosts = str(i)

  print ('done')

else:
  print('Nope not valid cidr, input something useful.')
