# NoteSMP Resources

Shared static assets and tools used by the NoteSMP website and related projects.

## Repository contents

| Path | Purpose |
|---|---|
| `cursors/note.png` | Default NoteSMP cursor artwork. |
| `cursors/arrow.png` | Pointer cursor for interactive elements. |
| `cursors/TextSelector.png` | Text-selection cursor. |
| `cursors/barrier.png` | Disabled/unavailable cursor. |
| `logos/disk13_x64.png` | Shared logo/graphic asset. |
| `tools/extract_client_textures.py` | Extracts Minecraft client textures from a version-matched client JAR. |

The website can reference these assets from the repository's raw/CDN hosting URL. Keep paths stable when assets are already used by the website.

## Extracting Minecraft client textures

The texture extraction utility is available for version-pinned client assets. Download the official Minecraft Java client JAR for the target version, then run:

```bash
python tools/extract_client_textures.py /path/to/client.jar --version 26.3
```

The script extracts the JAR's `assets/minecraft/textures/` tree into the corresponding versioned asset directory. Review the output before committing it. Keep each game version in its own folder so updates do not silently replace older textures.

## Asset guidelines

- Use descriptive, stable filenames and preserve case-sensitive paths.
- Prefer optimized image formats and sensible dimensions for web delivery.
- Do not commit generated archives, unrelated client files or credentials.
- Update consuming website paths when an asset is intentionally renamed or removed.

## Minecraft intellectual property

Minecraft assets are Mojang/Microsoft property. Use and redistribute them only in accordance with the applicable Minecraft terms and policies.

## Theme 2 interface frames

The reusable Minecraft Dungeons-inspired menu frame assets live in `ui/theme-2/`:

| Asset | Purpose |
|---|---|
| `frame-border.svg` | Bright ivory selected/hover frame with stepped pixel corners. |
| `frame-border-muted.svg` | Muted blue-grey inactive frame. |
| `frame-notch.svg` | Small centered top-frame ornament. |

The website uses the border SVG as a CSS nine-slice border so the corner artwork remains intact while panels resize.
