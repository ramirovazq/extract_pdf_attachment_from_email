#!/usr/bin/env python

import sys

output = open('/home/ramirovaz/adjuntos/script.out', 'a')
output.write(sys.stdin.read())
output.close()

