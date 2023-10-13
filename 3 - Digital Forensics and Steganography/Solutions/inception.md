# Solution
```
> binwalk wtfisthis.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1640 x 924, 8-bit/color RGBA, non-interlaced
75            0x4B            Zlib compressed data, default compression
1533028       0x176464        JPEG image data, JFIF standard 1.01

> binwalk --dd=".*" wtfisthis.png
```


```
> file *
0:      PNG image data, 1640 x 924, 8-bit/color RGBA, non-interlaced
176464: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, baseline, precision 8, 1416x672, components 3
4B:     empty
4B-0:   zlib compressed data
> mv 176464 176464.jpg
```

![Flag](_wtfisthis.png.extracted/176464.jpg)