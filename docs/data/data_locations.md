
# Data

There are multiple locations for data on the file system. You can get to the top-level folder for all of these by going to `/disk/aging/medicare/data`.

!!! note
    Make sure you go to `/disk/aging/medicare/data` and not `/disk/agedisk1/medicare/`. The former location contains links that take you to all the folders you could want. However, the second location has no links that take you to the harmonized data, so if you only go to `/disk/agedisk1/medicare`, you might not discover that the harmonized data exist.

At this folder, you'll see folder choices like
```
barronk at age1 in /disk/aging/medicare/data
> tree -C -l -L 1
.
├── 0001pct
├── 01pct
├── 05pct
├── 100pct
├── 20pct
├── limited_variables
├── README
└── sas
```

The folders `{0001,01,05,20,100}pct` contain all the medicare data in Stata and SAS format. For example, within the `01pct` folder, we see
```
barronk at age1 in /disk/aging/medicare/data/01pct
> tree -C -l -L 1
.
├── bsf
├── bsfcc -> bsf  [recursive, not followed]
├── bsfcu -> bsf  [recursive, not followed]
├── car
├── den
├── dme
├── hha
├── hos
├── hsk
├── inst
├── ip
├── med
├── op
├── op01_1995_17.sas7bdat.bz2
├── snf
└── xw
```




# Tree structure



