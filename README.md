![An animated film strip of a running horse](./docs/racehorse12.gif)

A CLI for generating a filmstrip effect from any video, using ffmpeg-python and Click.

example:
```
pipenv run main.py --count 12 --delay 8 --width 838 --out output.mp4 input.mp4
```

help:
```
pipenv run main.py --help
Usage: main.py [OPTIONS] INPUT

Options:
  --count INTEGER     number of tiles
  --delay INTEGER     number of frames between tiles
  --out TEXT          output file name
  --width INTEGER     width of output
  --info / --no-info  prints ffprobe information
  --help              Show this message and exit.
```

requirements: ffmpeg, python