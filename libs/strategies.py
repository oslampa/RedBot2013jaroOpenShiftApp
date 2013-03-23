#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import path
import csv
import shutil

# Columns of stategies.csv
# | label | is_automated | name | description |

class Strategy:
  def __init__(self, strategie_name):
    self.label = strategie_name
    self.name = None
    self.is_automated = None
    self.description = None
    # TODO: support strategies which consist of many files
    assert os.path.isfile(path.data_path('strategies', self.label))
    self.file = path.data_path('strategies', self.label)
    strategies_csv = csv.reader(open(path.data_path('strategies.csv'),'r'))
    for row in strategies_csv:
      if row[0] == self.label:
        self.label = row[0]
        self.name = row[1]
        self.is_automated = int(row[2])
        self.description = row[3]
        break
    assert self.name != None
    assert self.is_automated != None
    assert self.description != None

  def deploy(self, stratdir, stratid):
    """Prepare strategy into directory 'stratdir' as 'stratid'."""
    os.mkdir(os.path.join(stratdir, stratid))
    shutil.copy(self.file, os.path.join(stratdir, stratid))
    # TODO: just do links instead of this

  def is_ready(self, stratdir, stratid, gameround):
    """Ensure next round 'gameround' of game 'stratdir' can be evaluated
    from strategy 'stratid' point of view."""
    if self.is_automated == 1:
      return True
    else:
      pass   # TODO: if this is a manual stratefy we need some code here

  def __str__(self):
    return self.file

def get_strategies():
  out = []
  strategies_csv = csv.reader(open(path.data_path('strategies.csv'),'r'))
  for row in strategies_csv:
    out.append({'label': row[0], 'name': row[1], 'is_automated': int(row[2]), 'description': row[3]})
  return out



if __name__ == '__main__':
  a = Strategy('strilej')
  print 'Strategy label', a.label
  print 'Strategy name', a.name
  print 'Strategy is automated', a.is_automated
  print 'Strategy description', a.description