#!/usr/bin/env python


import sys
import os
import errno
import socket

import iptools.ipv4
import netaddr
import paramiko
import getpass

hosts = []

default_user = getpass.getuser()
default_ssh_key = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')

print '\nThis is a quick script used to ssh into a range of \nip addresses to check for an existence service.\n'
ip = raw_input('Input block of IP addresses\n(CIDR notation, i.e. 10.0.0.0/24): ')
user = raw_input('Specify user, or hit enter for current user: ')
# Default input
if user == '':
  user = default_user
ssh_key = raw_input('Specify your path for your ssh key, or\nhit enter for default home dir: ')
# Default input
if ssh_key == '':
  ssh_key = default_ssh_key

# Validate if true CIDR notation
if iptools.ipv4.validate_cidr(ip):
  print 'True, valid cidr:\n'
  print 'Scanning ' + ip + ' for your service...' 

  # Okay, true, so let's put the valid hosts somewhere. Any subnet <= 4 IPs is an empty list
  for i in netaddr.IPNetwork(ip).iter_hosts():
    # Turn i into type string
    hosts.append(str(i))

else:
  print 'Nope not valid cidr, input something useful.'

for k in hosts: 
  print '\nTrying ' + k +'...' 
  try:
    client = paramiko.SSHClient()
    client.connect(k, username=user, key_filename=ssh_key, look_for_keys=False, allow_agent=False, timeout=10)
    stdin, stdout, stderr = client.exec_command('ls')
    for line in stdout:
      print '... ' + line.strip('\n')
    client.close()
  except socket.timeout:
    print 'Ruh roh, ' + k + ' has timed out.'
    continue
  except socket.error, v:
    if 'Connection refused' in v:
      print 'Ruh roh, ' + k + ' refused.'
    continue
