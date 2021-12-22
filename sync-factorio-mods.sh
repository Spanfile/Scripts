#!/bin/bash
rsync -avh $HOME/.factorio/mods/ factorio.int.spans.me:/opt/factorio/mods/ --delete --exclude "debugadapter*" --include "*.zip" --include "mod-settings.dat" --include "mod-list.json" --exclude "*"
