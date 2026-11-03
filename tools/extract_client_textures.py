#!/usr/bin/env python3
"""Extract versioned Minecraft client texture resources from a client JAR.

Usage:
  python tools/extract_client_textures.py path/to/client.jar --version 26.3

Output is written under assets/<version>/textures/minecraft/ so the website can
reference a pinned resource snapshot instead of a third-party image host.
"""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("client_jar", type=Path)
    parser.add_argument("--version", required=True, help="Minecraft version label, e.g. 26.3")
    parser.add_argument("--output", type=Path, default=Path("assets"))
    args = parser.parse_args()

    if not args.client_jar.is_file():
        parser.error(f"client JAR not found: {args.client_jar}")

    prefix = "assets/minecraft/textures/"
    destination = args.output / args.version / "textures" / "minecraft"
    count = 0
    with ZipFile(args.client_jar) as archive:
        for entry in archive.infolist():
            name = entry.filename
            if not name.startswith(prefix) or entry.is_dir():
                continue
            relative = PurePosixPath(name[len(prefix):])
            if relative.is_absolute() or ".." in relative.parts:
                continue
            target = destination.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(entry))
            count += 1

    print(f"Extracted {count} textures to {destination}")


if __name__ == "__main__":
    main()
