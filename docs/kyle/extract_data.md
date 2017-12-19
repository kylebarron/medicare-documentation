
# Extracting Data

**What's the best, fastest way to import data?**

## Stata

Stata is what I use most, and I'm really comfortable with it, but its big limitation is that it needs everything to be in memory. Therefore, it's logical to want to try to break up analyzing a big dataset into smaller pieces. If a dataset is 50 GB in size, I wanted to be able to read in the dataset 5GB at a time. However, apparently Stata is really slow at importing data from a `.dta` file by row. Just importing the first row from an 82 GB file took **18 minutes**.

```stata
. local filename "/disk/aging/medicare/data/limited_variables/raw_harmonized/100pct/op/op100_clms_raw_2010.dta"

. set rmsg on
r; t=0.00 16:38:28

. use "`filename'" in 1, clear
r; t=1106.30 16:57:09

. di 1100/60
18.333333
```

This means that:

- It could be more time consuming to prototype data extracts with Stata or
- I could have to change code between prototyping and the actual extract on the 100% sample

I don't want to have to change code between prototyping and the actual extract because it wouldn't be difficult to introduce a simple mistake that I wouldn't find out about for a long time.

## Python

My current (December 2017) solution is to use Python. Python is able to read Stata files (i.e. `.dta` format). Helpfully, Python is also able to read only a given subset of columns, and it's able to iterate over the entire dataset, reading only chunks of data in at a time.

You can read in an entire Stata file with
```python
import pandas as pd
df = pd.read_stata('filename.dta')
```

You can read in a selection of variables from a Stata dataset with
```python
import pandas as pd
df = pd.read_stata('filename.dta', columns = ['var1', 'var2', 'var3'])
```

To read in a number of rows at a time, you create an _iterator_, and then make a for loop with commands to do to each chunk of a given number of rows. For example, the following imports 10,000 rows at a time, and will do all the commands in `do_something(chunk)`
```python
itr = pandas.read_stata('filename.dta', chunksize = 10000)
for chunk in itr:
    do_something(chunk)
```

When prototyping, it helps to code interactively, so you can run
```python
itr = pd.read_stata(file, chunksize = 1000)
for chunk in itr:
    df = chunk
    break
```
This puts the first 1,000 rows in `df`. Then you can work interactively with `df`, and just move the code inside the loop once you're ready to run it on the entire dataset iteratively.

### Official Documentation
Pandas' documentation on reading files from Stata is [here](https://pandas.pydata.org/pandas-docs/stable/io.html#io-stata-reader) and [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_stata.html).


See [here](https://pandas.pydata.org/pandas-docs/stable/io.html#io-perf) for benchmarks for writing and reading with Pandas in an array of formats.

## SAS

SAS is meant for

## R

### R from .dta


## Other file formats




