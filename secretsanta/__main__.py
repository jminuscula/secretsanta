#!/usr/bin/env python3.4

import sys
import argparse
import json

from .participant import read_participants_csv
from .manager import SecretSantaDebugManager, SecretSantaDefaultManager


def get_arguments(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--email', '-e', metavar='PATH',
        dest='email_config', help='Email json config',
    )

    parser.add_argument(
        '--template', '-t',
        dest='template', help='Message template'
    )

    parser.add_argument(
        '--seed', '-s', type=int, metavar='N',
        dest='seed',
        required=True, help='Seed value',
    )

    parser.add_argument(
        '--debug', '-d', action='store_true',
        dest='debug',
        default=False, help='Debug mode',
    )

    parser.add_argument(
        '--participants', '-p', metavar='PATH',
        dest='participants_csv_path',
        required=True, help='Participants CSV (name,email) path'
    )

    return parser.parse_args(args)


manager = None
args = get_arguments(sys.argv[1:])
participants = read_participants_csv(args.participants_csv_path)

if args.debug:
    manager = SecretSantaDebugManager(
        participants,
        seed=args.seed,
        template="{sfrom.name} ({sfrom.email}) -> {sto.name} ({sto.email})",
    )

elif not args.debug and args.email_config:
    config = {}
    with open(args.email_config) as ec:
        config = json.load(ec)

    manager = SecretSantaDefaultManager(
        participants,
        seed=args.seed,
        template_file=args.template,
        email_config=config
    )

if manager:
    manager.run()
