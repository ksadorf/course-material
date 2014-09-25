# Be creative, import math.

Introduces: pip.

Author(s): Julien Palard

## Instructions

Using the following program as a root, or not, generate the most
beautiful wallpaper your Python skils can.

You'll need a `pip3 install pycanvas` to run my ugly solution.

```python
#!/usr/bin/env python3

from pngcanvas import PNGCanvas
import math

HEIGHT = 500
WIDTH = int(HEIGHT * (16 / 9))

canvas = PNGCanvas(WIDTH, HEIGHT,
                   bgcolor=(255, 255, 255, 255),
                   color=(0, 0, 0, 255))

def get_point(x, y):
    """
    Return (Red, Green, Blue, Alpha) for the given (x, y) point.
    """
    R = (math.sin(x / 50) ** 2) * 0xFF
    G = (math.cos(y / 50) ** 2) * 0xFF
    B = (math.sin((x - y) / 50) ** 2) * 0xFF
    A = 0xFF
    return (int(R), int(G), int(B), int(A))

for x in range(WIDTH):
    for y in range(HEIGHT):
        canvas.point(x, y, get_point(x, y))
with open('solution.png', 'wb') as solution:
    solution.write(canvas.dump())
```

## Bonus

 - Generate a wallpaper far more beautiful than any other from the class.
 - Generate a different wallpaper each run, each of a more or less equal beauty, like [imagemagic](http://www.imagemagick.org/Usage/backgrounds/).
 - Accept parameters, like "--dominant-color" "--overall-luminosity", or whatever you want.
 - Use your program in a `crontab` to automatically set a new wallpaper to your desktop every hour.
 - Make your `crontab` generate an wallpaper according to the hour of the day (Dark at night, blue on the day, kind of orange for sunrises and dawns.
 - Generate a video instead of an image, needless to say, the video have to change every frame, and it have to be pretty.
 - Generate an infinite video stream.
 - Expose your video to the LAN over RTP.

## References
 - [pip](https://pip.pypa.io/en/latest/)
