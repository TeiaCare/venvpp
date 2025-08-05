#!/usr/bin/python
# Copyright 2025 TeiaCare
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import argparse
import subprocess

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type", choices=['Debug', 'Release', 'RelWithDebInfo'])
    parser.add_argument("--build_dir", help="Build Directory", required=False, default='./build')
    args, _ = parser.parse_known_args()
    return args
def main():
    args = parse()
    subprocess.run([
        'cmake',
        '--build', f'{args.build_dir}/{args.build_type}',
        '--parallel', str(os.cpu_count() // 2)
    ], check=True)

if __name__ == '__main__':
    if not os.getenv('VIRTUAL_ENV'):
        raise SystemError("\n========================================================"
                          "\nYou are not running inside a python virtual environment"
                          "\nConfigure and activate it as shown in the project README"
                          "\n========================================================\n")

    sys.exit(main())
