#!/usr/bin/env python

"""
Script Name: blockchain_init.py
Script Desc: ( A script that will define the foundation of a block chain for future use. )
Script Date: 04 October 2018
Script Author: Xenonheat

__author__ = "Olufemi Adesina"
__copyright__ = "Copyright 2018, XenonIgnition"
__credits__ = ["Olufemi Adesina"]
__license__ = "Xenon"
__version__ = "0.0.1"
__maintainer__ = "Xenonheat"
__email__ = "femiadesina@live.co.uk"
__status__ = "Development"

"""

import json

class XenonBlock:

  def __init__(self, index, data, timestamp, block_hash, previous_block = None):
    """
    """
    self.index = index
    self.data = data
    self.timestamp = timestamp
    self.block_hash = block_hash
    self.previous_block = self.determine_priorBlock(previous_block)

  def determine_priorBlock(self, previous_block):
    """
    """
    if(previous_block is None):
      previous_block = "genesis"

class XenonBlockChain:

  def __init__(self);
    """
    """

  def __str__(self):
    """
    """

