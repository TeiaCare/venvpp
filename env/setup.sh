#!/bin/bash
# Copyright 2024 TeiaCare
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

# Upgrade pip
python3 -m pip install --upgrade pip

# Create a virtual environment
python3 -m venv .venv

# Set CONAN_USER_HOME environment variable in the activate script
echo "export CONAN_USER_HOME=\$PWD" >> .venv/bin/activate

# Activate the virtual environment
source .venv/bin/activate

# Install the required packages
pip install -r scripts/requirements.txt

# Install pre-commit hooks
pre-commit install

echo "=========================================="
echo "Virtual environment '.venv' is now active."
echo "=========================================="
exec "$SHELL"

# chmod +x scripts/env/setup.sh
# ./scripts/env/setup.sh
