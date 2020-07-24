#!/usr/bin/env python3

"""Main."""

import sys
from CPU import *

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()
