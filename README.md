# Sample headless turntable render in blender

## Dependencies

[EasyBpy](https://github.com/curtisjamesholt/EasyBPY) - follow installation instructions

## Usage example

```sh
blender ./scenes/preset_0.blend \
--background \
--python ./scripts/preset_0.py \
--render-anim \
-- ak47
```

### Convert to mp4

```sh
ffmpeg -framerate 30 \
-pattern_type glob -i './output/*.png' \
-c:v libx264 -pix_fmt yuv420p \
output/out.mp4

```

## Args

Argument passed to script placed after `--`:

```sh
-- weapon_name_as_it_named_in_folder
```
