#!/usr/bin/python3

import glob
from os import path, remove
from collections import defaultdict

MOD_DIRECTORY = "/home/santeri/.factorio/mods"


def get_name_and_version(f):
    args = f.split("_")
    name = path.basename(args[0])
    version = args[1][:-4]
    return name, version


def compare_versions(v1, v2):
    args1 = [int(v) for v in v1.split(".")]
    args2 = [int(v) for v in v2.split(".")]

    if len(args1) > len(args2):
        return True

    for a, b in zip(args1, args2):
        if a > b:
            return True

    return False


mod_files = [
    get_name_and_version(f) for f in glob.glob(path.join(MOD_DIRECTORY, "*.zip"))
]
mods = defaultdict(list)

for name, version in mod_files:
    mods[name].append(version)

for name, versions in mods.items():
    if len(versions) > 1:
        lower_versions = []
        highest = None
        for v in versions:
            if highest:
                if compare_versions(v, highest):
                    lower_versions.append(highest)
                else:
                    lower_versions.append(v)
                    continue

            highest = v

        print(
            f"Duplicate mod found: {name}. Highest version: {highest}. Others: {lower_versions}"
        )

        for v in lower_versions:
            filename = path.join(MOD_DIRECTORY, f"{name}_{v}.zip")
            print(f"Deleting {filename}")
            remove(filename)
