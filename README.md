# n5mrc

Script to export N5 subvolumes to MRC files.

Install with `pip install git+https://github.com/clbarnes/n5mrc.git`

```_n5mrc
usage: n5mrc [-h] [-f] [-s SUBVOLUME] container dataset outfile

positional arguments:
  container             path to N5 root
  dataset               path from N5 root to dataset
  outfile               path to MRC file

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           overwrite existing output file
  -s SUBVOLUME, --subvolume SUBVOLUME
                        subvolume bounds (left-inclusive) as a string like
                        '0:100,20:60,1000:20000'
```
