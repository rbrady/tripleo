#!/bin/bash

set -eux

mkdir -p ~/extra
cd ~/extra
git clone https://github.com/rbrady/tripleo-heat-templates.git
git clone https://github.com/rbrady/flaming-octo-tyrion.git

