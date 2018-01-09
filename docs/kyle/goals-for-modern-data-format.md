# Goals for Modern Data Format for Medicare data

## File Format

- Must be fast
- Must be able to read a subset of columns fast
- Should be divisible into row chunks, so that you can import only a slice of the file (by rows) when file is too large for all rows -- even of a subset of columns -- to be loaded into memory.

I'll try to look through all the data formats that Pandas can read and write from. [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) contains a benchmarking [script](https://pandas.pydata.org/pandas-docs/stable/io.html#io-perf) that I modified and ran on the NBER servers (on `/agebulk1`). My modified script used generated data as well as real Medicare data. The Medicare data it used was the first 10% of the rows of the 2011 1% outpatient claims dataset. I.e. `/disk/aging/medicare/data/01pct/op/2011/opc2011.dta`. The entire script is shown at the [bottom](#full-python-io-benchmark) of this page.

### Stata (`.dta`)

Decently fast for Stata to read by column but very slow to read by row for big files, since the Stata reader must scan the entire file before importing the first row.

Python can also read Stata files, but it's not the fastest file format to read. The following python code reads the first 10% of the rows of the 2011 1% outpatient claims dataset. This is the data sample that the rest of the benchmarks use.
```ipython
path = '/disk/aging/medicare/data/01pct/op/2011/opc2011.dta'
itr = pd.read_stata(path, iterator = True)
%time df = itr.get_chunk(int(itr.nobs / 10))
# CPU times: user 17 s, sys: 7.5 s, total: 24.5 s
# Wall time: 27 s
```

### CSV (`.csv`)

Stored as text; Doesn't hold metadata about columns, therefore rather costly CPU-wise to import the data (though still better than reading `.dta` files). Python can read in a subset of the columns of a `.csv` and can loop over rows without reading in all rows at a time.
```ipython
%timeit test_csv_read()
# 2.54 s ± 50.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

### JSON (`.json`)

Also stored as text; meant for hierarchical data. Overkill for a rectangular data frame.

### Feather format (`.feather`)

Very fast file format to read and write. It's possible to import a subset of columns, but **not** a subset of rows. You must read in all rows of a column at once. It's possible to read `.feather` files from R, Python, and Julia.
```ipython
%timeit test_feather_read()
# 583 ms ± 10.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

### Parquet format (`.parquet`)

Parquet is similar to the feather format with a few differences. It's a columnar format, like Feather, which means that the data in a matrix/DataFrame is stored in each column, not in each row. That means that a column's data must be kept together. Importantly, however, Parquet files can be split into _row groups_. That means that you can write a certain number of rows in each column at a time. Say the size of your row group is 1,000,000 rows. Then you write the first 1,000,000 rows of all columns, then the next 1,000,000, and so on. This makes it fast to read 1,000,000 at a time of whatever subset (or all) of the columns you want. But you can't read the first 10 rows or the first 100; it must be the size of the row group.


```ipython
%timeit test_parquet_read_compress()
# 1.48 s ± 20.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
 
%timeit test_parquet_read()
# 1.47 s ± 22.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```bash
ls -lh
-rw-r--r-- 1 barronk dua18266  12M Jan  9 16:31 test_compress.parquet
-rw-r--r-- 1 barronk dua18266  17M Jan  9 16:32 test.parquet
-rw-rw-r-- 1 barronk dua18266  63M Jan  9 16:27 test.csv
```

### Pickle (`.pkl`)

Pickle is a Python specific format. To my knowledge, it saves objects in disk the same way they're stored in memory by Python. This makes it very fast. However you must read in the entire object; it's impossible to choose a subset of rows or columns.

```ipython
%timeit test_pickle_read()
# 1.25 s ± 47.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_read_compress()
# 2.58 s ± 669 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

### HDF5 (`.hdf`)

HDF5 is a high performance format that could work for this use case, but I don't really understand it well. From the Pandas API documentation, it's possible to read in HDF5 files by columns as well as by rows.

```ipython
%timeit test_hdf_fixed_read()
# 11.2 s ± 1.51 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_read_compress()
# 11.1 s ± 1.83 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read()
# 24.4 s ± 7.19 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read_compress()
# 25.1 s ± 7.81 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

### SQL

I've talked to Mohan and Dan and they've said that SQL isn't optimal for this kind of data processing, since we're often extracting most values of a column, rather than finding one specific row, which is helped by the index.

```ipython
%timeit test_sql_read()
# 12.8 s ± 1.86 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```


## Data Decisions

### Categorical Variables

How should categorical variables be coded?

- Leave them as strings. Currently they're usually stored as strings, because any digit with a leading zero upon import isn't considered an integer. Then you have to reference them as strings and you have to look up the lookup table in ResDAC every time you want to do something with them.
- Convert them to categoricals. Could improve memory usage and performance by being able to represent these columns as integers, rather than strings.
   
    However then you wouldn't be able to reference categoricals by the numbers listed in ResDAC.
    
    Consider [`clm_type`](https://www.resdac.org/cms-data/variables/nch-claim-type-code). The codes are small values like `10` and `20`, while the code values are `HHA claim` and `Non swing bed SNF claim`. The codes are much easier to type, and existing code could be more easily adapted to use these datasets. Having to refer to `clm_type` with
    ```
    df['clm_type'] == 'Non swing bed SNF claim'
    ```
    instead of with
    ```
    df['clm_type'] == 20
    ```
    would probably get annoying.
    
    I can't keep the integer representation of the categorical the number that ResDAC uses because Python requires that there be no spaces among integers. I.e. if Male is represented with `1`, Female would have to be represented with `2`, it couldn't be represented with `3`, because there would be a gap there. Many columns have gaps, and so Python would have to re-index those keys.
- Convert columns to categoricals but leave the current string values in the data as the keys. Then you'd still refer to the data with ResDAC's code, but there would be enhanced performance by virtue of using integers instead of strings.




## Full Python I/O Benchmark

First using generated data, then using real Medicare data. All computations are taking place on the Aging servers.

(Done in the ipython kernel.)

```ipython
import os
import pandas as pd
import sqlite3
from numpy.random import randn
from pandas.io import sql
import pyarrow as pa
import pyarrow.parquet as pq

cd ~/agebulk1/pytest

real_data = True

if not real_data:
    sz = 10000000
    df = pd.DataFrame({'A': randn(sz), 'B': [1] * sz})
else:
    path = '/disk/aging/medicare/data/01pct/op/2011/opc2011.dta'
    itr = pd.read_stata(path, iterator = True)
    %time df = itr.get_chunk(int(itr.nobs / 10))

memuse = df.memory_usage().sum() / 1024 ** 2
print('Data in memory is {:.0f} MB'.format(memuse))
# Data in memory is 153 MB / 242 MB

if real_data:
    cd medicare

def test_sql_write(df):
    if os.path.exists('test.sql'):
        os.remove('test.sql')
    sql_db = sqlite3.connect('test.sql')
    df.to_sql(name='test_table', con=sql_db)
    sql_db.close()

def test_sql_read():
    sql_db = sqlite3.connect('test.sql')
    pd.read_sql_query("select * from test_table", sql_db)
    sql_db.close()

def test_hdf_fixed_write(df):
    df.to_hdf('test_fixed.hdf','test',mode='w')

def test_hdf_fixed_read():
    pd.read_hdf('test_fixed.hdf','test')

def test_hdf_fixed_write_compress(df):
    df.to_hdf('test_fixed_compress.hdf','test',mode='w',complib='blosc')

def test_hdf_fixed_read_compress():
    pd.read_hdf('test_fixed_compress.hdf','test')

def test_hdf_table_write(df):
    df.to_hdf('test_table.hdf','test',mode='w',format='table')

def test_hdf_table_read():
    pd.read_hdf('test_table.hdf','test')

def test_hdf_table_write_compress(df):
    df.to_hdf('test_table_compress.hdf','test',mode='w',complib='blosc',format='table')

def test_hdf_table_read_compress():
    pd.read_hdf('test_table_compress.hdf','test')

def test_csv_write(df):
    df.to_csv('test.csv',mode='w')

def test_csv_read():
    pd.read_csv('test.csv',index_col=0)

def test_feather_write(df):
    df.to_feather('test.feather')

def test_feather_read():
    pd.read_feather('test.feather')

def test_parquet_write(df):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'test.parquet', compression = 'none')

def test_parquet_read():
    pq.read_table('test.parquet').to_pandas()

def test_parquet_write_compress(df):
    df.to_parquet('test_compress.parquet')

def test_parquet_read_compress():
    pd.read_parquet('test_compress.parquet')

def test_stata_write(df):
    df.to_stata('test.dta')

def test_stata_read():
    pd.read_stata('test.dta')

def test_pickle_write(df):
    df.to_pickle('test.pkl')

def test_pickle_read():
    pd.read_pickle('test.pkl')

def test_pickle_write_compress(df):
    df.to_pickle('test.pkl.compress', compression='xz')

def test_pickle_read_compress():
    pd.read_pickle('test.pkl.compress', compression='xz')

#### Writes -- Fake Data

%timeit test_sql_write(df)
# 22.1 s ± 1.68 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_write(df)
# 1.06 s ± 25.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_write_compress(df)
# 1.05 s ± 7.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_write(df)
# 5.47 s ± 52.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_write_compress(df)
# 5.45 s ± 87.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_csv_write(df)
# 28.6 s ± 2.53 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_feather_write(df)
# 715 ms ± 10.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_write(df)
# 1.04 s ± 30 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_write_compress(df)
# 42.3 s ± 1.34 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_write_compress(df)
# 1.14 s ± 7.01 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_write(df)
# The slowest run took 5.13 times longer than the fastest. This could mean that an intermediate result is being cached.
# 1.78 s ± 1.56 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_stata_write(df)
# 1.74 s ± 47.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#### Reads -- Fake Data

%timeit test_parquet_read_compress()
# 493 ms ± 17.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_read()
# 429 ms ± 11.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_stata_read()
# 796 ms ± 26.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_sql_read()
# 14.1 s ± 48 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_read()
# 159 ms ± 1e+03 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit test_hdf_fixed_read_compress()
# 159 ms ± 6.04 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read()
# 390 ms ± 41.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read_compress()
# 411 ms ± 6.97 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_csv_read()
# 4.2 s ± 45 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_feather_read()
# 206 ms ± 7.98 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_read()
# 237 ms ± 15.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_read_compress()
# 5.77 s ± 63.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

! ls -lhSr
# -rw-rw-r-- 1 barronk dua18266  72M Jan  9 15:19 test.pkl.compress
# -rw-r--r-- 1 barronk dua18266 116M Jan  9 15:19 test_compress.parquet
# -rw-r--r-- 1 barronk dua18266 153M Jan  9 15:13 test.feather
# -rw-rw-r-- 1 barronk dua18266 153M Jan  9 15:20 test.dta
# -rw-rw-r-- 1 barronk dua18266 153M Jan  9 15:13 test.pkl
# -rw-r--r-- 1 barronk dua18266 154M Jan  9 15:19 test.parquet
# -rw-rw-r-- 1 barronk dua18266 229M Jan  9 15:08 test_fixed.hdf
# -rw-rw-r-- 1 barronk dua18266 229M Jan  9 15:08 test_fixed_compress.hdf
# -rw-rw-r-- 1 barronk dua18266 231M Jan  9 15:09 test_table.hdf
# -rw-rw-r-- 1 barronk dua18266 231M Jan  9 15:09 test_table_compress.hdf
# -rw-rw-r-- 1 barronk dua18266 282M Jan  9 15:13 test.csv
# -rw-r--r-- 1 barronk dua18266 346M Jan  9 15:08 test.sql



#### Writes -- Real Data

%timeit test_sql_write(df)
# 15.3 s ± 52.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_write(df)
# 5.19 s ± 553 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_write_compress(df)
# 5.63 s ± 764 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_write(df)
# 17.3 s ± 1.41 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_write_compress(df)
# 16 s ± 182 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_csv_write(df)
# 8.83 s ± 57.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_feather_write(df)
# 2.34 s ± 14.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_write(df)
# 2.65 s ± 111 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_write_compress(df)
# 23 s ± 329 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_write_compress(df)
# 2.71 s ± 183 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_write(df)
# 2.59 s ± 16.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#### Reads -- Real Data

%timeit test_parquet_read_compress()
# 1.48 s ± 20.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
 
%timeit test_parquet_read()
# 1.47 s ± 22.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_sql_read()
# 12.8 s ± 1.86 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_read()
# 11.2 s ± 1.51 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_read_compress()
# 11.1 s ± 1.83 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read()
# 24.4 s ± 7.19 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_table_read_compress()
# 25.1 s ± 7.81 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_csv_read()
# 2.54 s ± 50.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_feather_read()
# 583 ms ± 10.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_read()
# 1.25 s ± 47.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_pickle_read_compress()
# 2.58 s ± 669 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

!ls -lhSr
# -rw-rw-r-- 1 barronk dua18266 5.6M Jan  9 16:31 test.pkl.compress
# -rw-r--r-- 1 barronk dua18266  12M Jan  9 16:31 test_compress.parquet
# -rw-r--r-- 1 barronk dua18266  17M Jan  9 16:32 test.parquet
# -rw-rw-r-- 1 barronk dua18266  63M Jan  9 16:27 test.csv
# -rw-r--r-- 1 barronk dua18266  76M Jan  9 16:20 test.sql
# -rw-rw-r-- 1 barronk dua18266 116M Jan  9 16:21 test_fixed.hdf
# -rw-rw-r-- 1 barronk dua18266 116M Jan  9 16:22 test_fixed_compress.hdf
# -rw-r--r-- 1 barronk dua18266 161M Jan  9 16:28 test.feather
# -rw-rw-r-- 1 barronk dua18266 178M Jan  9 16:28 test.pkl
# -rw-rw-r-- 1 barronk dua18266 452M Jan  9 16:24 test_table.hdf
# -rw-rw-r-- 1 barronk dua18266 452M Jan  9 16:26 test_table_compress.hdf
```
