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

import subprocess
import argparse
import pathlib
import sys
import os

def setup_conan_home():
    if os.getenv('CONAN_USER_HOME') != None:
        print("CONAN_USER_HOME already set to:", os.getenv('CONAN_USER_HOME'))
        return
    
    current_working_directory = pathlib.Path().resolve()
    os.environ['CONAN_USER_HOME'] = str(current_working_directory.absolute())
    print("CONAN_USER_HOME:", os.getenv('CONAN_USER_HOME'))

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("remote_name", help="Conan remote name")
    parser.add_argument("artifactory_url", help="Artifactory server address")
    parser.add_argument("username", help="Remote username")
    parser.add_argument("password", help="Remote password")
    return parser.parse_args()

def conan_configure_remote(remote_name, artifactory_url, username, password):
    subprocess.run(['conan', 'config', 'set', 'general.revisions_enabled=0'], check=True)
    subprocess.run(['conan', 'remote', 'add', remote_name, f'{artifactory_url}/{remote_name}', '--force'], check=True)
    subprocess.run(['conan', 'user', username, '-p', password, '-r', remote_name], check=True)

def conan_upload(remote_name):
    subprocess.run(['conan', 'upload', '--all', '--confirm', '--parallel', '--check', '--force', '--remote', remote_name, "*"], check=True)

def get_profile_path(profile_name):
    profile_path = pathlib.Path(os.getenv('CONAN_USER_HOME'), ".conan", "profiles", profile_name)
    return profile_path

def main():
    setup_conan_home()
    args = parse()
    conan_configure_remote(args.remote_name, args.artifactory_url, args.username, args.password)
    conan_upload(args.remote_name)

if __name__ == '__main__':
    sys.exit(main())
