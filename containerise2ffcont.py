#!/usr/bin/env python3

import argparse
import json


def main():
    desc_str = 'Convert export of Containerise'
    parser = argparse.ArgumentParser(description=desc_str)
    parser.add_argument('infile', help='Containerise storage.js file')
    parser.add_argument('inconts', nargs='?', default='containers.json',
                        help='Containerise containers defintions')
    parser.add_argument('outfile', help='Input file for ffcontainers.sh')

    args = parser.parse_args()

    with open(args.inconts, encoding='utf8') as inf:
        in_conts_data = json.load(inf)
        containers_defs = {}
        for cont in in_conts_data['identities']:
            # l10nID
            if 'name' in cont:
                if not cont['name'].startswith('userContextIdInternal'):
                    containers_defs[cont['name']] = cont['userContextId']
        # {'Banking': 3,
        #  'Facebook': 14,
        #  'Google': 11,
        #  'News': 15,
        #  'Wikipedia': 16,
        #  'Work': 2,
        #  'YouTube': 13}

    with open(args.infile, encoding='utf8') as inf:
        in_data = json.load(inf)
        for key in in_data:
            print(f'{key}:\t{in_data[key]}\n')
            # map=hubmaier.ceplovi.cz:  {'containerName': 'Personal',
            # 'cookieStoreId': 'firefox-container-17', 'enabled': True,
            # 'host': 'hubmaier.ceplovi.cz'}


if __name__ == "__main__":
    main()
