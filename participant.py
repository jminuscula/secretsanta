#!/usr/bin/env python3.4

import csv
from collections import namedtuple

Participant = namedtuple('Participant', ['name', 'email'])


def read_participants_csv(path):
    with open(path) as data:
        return map(lambda p: Participant(*p), csv.reader(data.readlines()))
