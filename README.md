# NoteSMP resources

Version-pinned Minecraft client textures and related NoteSMP assets.

## Extracting the official client textures

Download the Minecraft Java client JAR for the exact server version (26.3) from
the official Minecraft version manifest/launcher, then run:

```bash
python tools/extract_client_textures.py /path/to/client.jar --version 26.3
```

The tool extracts the JAR's `assets/minecraft/textures/` tree to
`assets/26.3/textures/minecraft/`. Commit the resulting asset files to this
repository before switching the website to the repository-hosted paths. Keep
each Minecraft version in its own directory so textures do not drift when the
game updates.

Minecraft assets are Mojang/Microsoft property. Use and redistribute them only
in accordance with the applicable Minecraft terms and policies.
