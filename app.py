#!/usr/bin/env python3

import datetime

def do_magic():
    now = datetime.datetime.now()
    return "Hello! {0}".format(now)

if __name__ == "__main__":
    print("Content-type: text/html\n\n")
    print(do_magic())
