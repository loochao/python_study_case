#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def main():
	print(__file__)
	print(os.path.dirname(__file__))
	print(sys.path)
	print(os.path.dirname('..'))

if __name__ == '__main__':
	main()