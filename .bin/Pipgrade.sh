#!/usr/bin/env bash

echo 'Updating all user installed pip packages...'
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install --user -U
