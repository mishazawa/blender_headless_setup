# Sample headless turntable render in blender

## Dependencies

[EasyBpy](https://github.com/curtisjamesholt/EasyBPY) - follow installation instructions

## Usage example

```sh
blender ./scenes/preset_0.blend \
--background \
--python ./scripts/preset_0.py \
--render-anim \
-- 1 15 180
```

## Args

Argument passed to script placed after `--`:

```sh
-- first_frame last_frame rotation_in_degrees
```
