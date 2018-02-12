##############################
## 2018
## maildraw.py -h HOST [-p PORT} -l USER:PASS LIST
##
##
#############################

import sys
import telnetlib
import argparse

print "hello world"
parse = argparse.ArgumentParser()
args = parse.parse_args()

try:
    parse.add_argument("-h", "--hostname", help="host")
    parse.add_argument("-p", "--port", help="port (default 110)")
    parse.add_argument("-l", "--loginlist", help="user:pass list")

    print ("Accessing {}:{} with {}".format(
        args.hostname,
        args.port,
        args.loginlist
    ))
except:
    print "usage: maildraw.py -h HOST [-p PORT -l USER:PASS LIST"


print "goodbye world"
