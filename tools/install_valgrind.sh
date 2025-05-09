#!/bin/bash
set -e

VALGRIND_VERSION="$1"
CACHE_DIR="$2"
COMPILER="$3"

mkdir -p "$CACHE_DIR"

# Check if valgrind is already installed from cache
if [ -f "$CACHE_DIR/bin/valgrind" ]; then
  echo "Using cached Valgrind"
  sudo cp -r "$CACHE_DIR"/* /usr/local/
else
  echo "Installing Valgrind from source"
  # Remove existing valgrind if present
  sudo apt remove --purge valgrind -y

  # Download and extract valgrind
  wget https://sourceware.org/pub/valgrind/valgrind-$VALGRIND_VERSION.tar.bz2
  tar xf valgrind-$VALGRIND_VERSION.tar.bz2

  # Build and install valgrind
  cd valgrind-$VALGRIND_VERSION
  export CC=$COMPILER
  ./configure --prefix=/usr/local
  make -j$(nproc)
  sudo make install

  # Clean up
  cd ..
  rm -rf valgrind-$VALGRIND_VERSION valgrind-$VALGRIND_VERSION.tar.bz2

  # Cache the installation
  sudo cp -r /usr/local/bin "$CACHE_DIR"/
  sudo cp -r /usr/local/lib "$CACHE_DIR"/
  sudo cp -r /usr/local/include "$CACHE_DIR"/
  sudo cp -r /usr/local/share "$CACHE_DIR"/
  sudo chown -R "$(id -u):$(id -g)" "$CACHE_DIR"/
fi

# Verify installation
# export PATH=/usr/local/bin:$PATH
echo "Valgrind version:"
valgrind --version