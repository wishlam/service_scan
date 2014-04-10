service_scan
============

Really shitty code, but logs into a CIDR block using a user name and SSH key of your choosing and checks if a process is running or setup via three methods:

 - chkconfig --list | grep \<pidname\>
 - ps axflww | grep -i \<pidname\>
 - ls /etc/init.d/ | grep -i \<pidname\>

TODO
============

Configure it to take in command line input, i.e. scan.py --ssh=<ssh_key> --pid=<pidname> --user=<user>
