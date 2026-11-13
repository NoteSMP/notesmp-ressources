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

## Website command catalogue

The website's `/commands` page loads its command groups from
[`commands/commands.json`](commands/commands.json) in this repository. Edit this
file to add, change or remove plugins and commands; no website code change is
needed for catalogue content updates.

Each entry in `groups` represents one section on the page:

- `name`: plugin or command-group name shown as the heading.
- `category`: small category label above the heading.
- `source`: short source label, such as `PLUGIN` or `NATIVE`.
- `commands`: list of command entries.
  - `command`: command syntax shown on the page.
  - `description`: explanation shown below the command.

To add a plugin, copy a group object and add it to `groups`. Add or remove
objects inside its `commands` array as needed. Keep the file valid JSON:
use double quotes, separate array items with commas, and do not add comments or
trailing commas. Changes are fetched directly from the `main` branch when the
Commands page is opened.

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

## Theme 2 interface frame

Theme 2 uses one user-supplied nine-slice PNG:

| Asset | Details |
|---|---|
| `ui/theme-2/frames/panel-9slice.png` | Exact 30×30 PNG; each of the nine slices is 10×10 pixels. |

The same asset frames the homepage hero and main section panels. Do not add alternate color variants, separate corner overlays or CSS-drawn ornaments. The website applies CSS `border-image` with a 10px slice and a 10px rendered border width.
