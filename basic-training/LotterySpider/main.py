# _*_ coding: utf-8 _*_
__author__ = 'Kevin.Luo'

from scrapy.cmdline import execute

import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "ssq"])