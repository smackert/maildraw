##############################
## 2018
## maildraw.py -h HOST [-p PORT} -l USER:PASS LIST
##
##
#############################

import sys
import telnetlib
import argparse

print "hello world" #remove after debugging
parser = argparse.ArgumentParser()


try:
    parser.add_argument("-t", "--target", help="host")
    parser.add_argument("-p", "--port", help="port (default 110)")
    parser.add_argument("-l", "--loginlist", help="user:pass list")

    args = parser.parse_args()
    print (
        args.target,
        args.port,
        args.loginlist
        )
except:
    print "Failed"


print "goodbye world" #remove after debugging
