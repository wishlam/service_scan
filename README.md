service_scan
============

 - Requires iptools
"pip install iptools"

 - Requires netaddr
"pip install netaddr"

 - Requires paramiko
"pip install paramiko"

 - Requires getpass
"pip install getpass"

Really shitty code, but logs into a CIDR block using a user name and SSH key of your choosing and checks if a process is running or setup via three methods:

 - chkconfig --list | grep <pidname>
 - ps axflww | grep -i <pidname>
 - ls /etc/init.d/ | grep -i <pidname>
