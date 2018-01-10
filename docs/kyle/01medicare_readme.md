---
title: Readme
date: Thursday, Dec 14, 2017
---

!!! note
    This page is a slightly edited version of the `README` file written by Jean Roth and located at `/disk/aging/medicare/data/README`.


Filenames are of the form `TYPEpercent_YEAR_divisionFILE`. However, Jean Roth is moving these to filenames that include version, like `TYPEpercentVersion_YEAR_divisionFILE`. The old names will still work because they should by symbolic links pointing to the new filenames when they are added.

### Type
`TYPE` is `[bsf|car|den|dme|hha|hos|hsk|ip|med|op|snf]`.

- `bsf =` Master Beneficiary Summary File.  enrollment information.
- `car =` Carrier.  Previously known as Physician/Supplier and Part B.
- `den =` Denominator.  An abbreviated version of the enrollment database (EDB) starting 1991.
      Contains data on all medicare beneficiaries enrolled and/or entitled in a given year.
      nrol is a subdirectory with enrollment summary files
- `dme =` Durable Medical Equipment
- `hha =` Home Health Agency
- `hos =` Hospice
- `hsk =` HISKEW, Health Insurance Skeleton Eligibility Write-Off.
      An abbreviated version of the enrollment database (EDB)
      Contains data on all beneficiaries ever entitled to medicare.
      We have this for 1985-1995.
- `ip =` Inpatient
- `med =` MEDPAR, Medical Provider Analysis and Review
- `op =` Outpatient
- `snf =` Skilled Nursing Facility

### Percent
`percent` is `100`, `20`, `05`, `01`, or `0001`. See below for more detail.
The percent files have been made by request.  So if a small sample
has not made from the file you want email Jean jroth@nber.org
to request an extraction.

### Version
`Version` is a letter such as `g`, `h`, `i`, or `j`.

### Year

`YEAR` is four-digit year

### Division

`division` if applicable is

- `clms =>` claims, `revcntrs =>` revenue centers  for `HHA`, `IP`, `OP`, `SNF`
- `clms =>` claims, `lnits =>` line items for `CAR`, `DME`

`FILE`s that have been split into divisions can be merged on `EHIC` and `claimindex`.

2002-2005 DME files are split by the `RIC_CD`(Record Identification Code) variable.
In the DME files, `RIC_CD` takes two values: `M` and `O` (capital-Oh).

- `M =` Part B DMEPOS claim record (processed by DME Regional Carrier) (effective 10/93);
- `O =` Part B physician/supplier claim record (processed by local carriers, can include DMEPOS services); DME files split this way are called dmeo or dmem .

Not all `TYPES` of files are split into divisions, and not all `YEAR`s of a `TYPE` will be split into divisions.

### File

`FILE` is 1 to N .


## Sampling Method

Recent denominator, inpatient, outpatient, and medpar files are 100% files.
Jean Roth created the 20%, 5%, 1%, and 0.1% files based on digits from `EHIC`:

From start-2005:

- A  20% file has `0` or `5` in the 9th position of `EHIC`.
- A   5% file has `05`, `20`, `45`, `70`, `95` in positions 8-9 of `EHIC`.
- A   1% file has `45` in positions 8-9 of `EHIC`.
- A 0.1% file has `1545` in positions 6-9 of `EHIC`.

From 2006-present:

- The   20% and 5% files are consistent but are now identified by the CMS contractor.
- The   1% file has `DD` in the 14th and 15th position of `BENE_ID`.
- The 0.1% file has `DDDD` in the 12th-15th position of `BENE_ID`.

Note that since we have "only" a 20% Carrier, the "1%" file is actually a 0.2% for 2006-present.
Similarly, the "0.1%" actually has (0.1*.2)% or 0.002% of all medicare Carrier beneficiaries.

There is a break in the 1% and smaller sample from 2005 to 2006; however,
since these files are mostly used for testing, it should be okay.  I know this is confusing.

The exception is Carrier (Part B) files.  1998-on files are 20% files.
Earlier, 5% was the maximum.  From 1991-2000, the 5% files had
`05`, `20`, `45`, `70`, `95` in positions 8-9 of `EHIC`.  So, the 5%
Carrier files are just symbolic links to those files in the 20pct directory.

!!! note
    The 1985-1990 files had 00-99 in positions 8-9 of `EHIC`; however, `05`, `20`, `45`, `70`, `95` makes up 14-16% each of of the `EHIC`s position 8-9. These appear to be all End Stage Renal Disease (ESRD) beneficiaries.

Also noteworthy about the Carrier files:  In 1998-2000, there are two
versions, H and I. 1998, 1999, and 2000 `a` files are version H.  and
1998-1999 `b`, `c`, and `d` files and 2000 files are version I files.
My guess is that at one time, the 5% Version H files were bought.
At a later time, it became possible to get 20% files, so the 1998-1999
b, c, and d files and the 2000 files were bought.  Both H and I are
needed to make a 20% sample for 1998 and 1999.  It appears based on sample
size that the 2000 files are four-5% draws, and that the 2000 a files
are only useful for historic reasons.

2002-2005 Carrier files are split into four 5% draws f[1-4]
8th and 9th position of `EHIC`.

- f1 ~20% each in (`05`,`20`,`45`,`70`,`95`);
- f2 ~20% each in (`00`,`10`,`15`,`25`,`30`);
- f3 ~20% each in (`35`,`40`,`50`,`55`,`60`);
- f4 ~20% each in (`65`,`75`,`80`,`85`,`90`);

2002-2005 Carrier and DME files are split in to claims `clms` and line items
`lnits` file.  The files can be merged using  `EHIC` and claimindex.

The claims data uses `BENE_ID` as an identifier beginning in 2006. `/disk/agedisk1/medicare/data.NOBACKUP/u/c/100pct/xw`
has a crosswalk between `BENE_ID` and `EHIC` .

```
/disk/aging/medicare/data/`PCT'pct/bsf/[CCYY]/1/unique_in_both_ids[CCYY].[dta|sas7bdat]
```
has annual files of `EHIC` and `BENE_ID` where beneficiaries have unique IDs
in both the `EHIC` and `BENE_ID`.

[jroth@nber.org](jroth@nber.org)  Last updated 2016-06-24
