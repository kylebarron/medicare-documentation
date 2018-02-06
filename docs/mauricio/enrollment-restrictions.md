Enrollment Restrictions
=======================

!!! note
    This document was originally written by [Mauricio Cáceres](https://mcaceresb.github.io/).

The denominator file is so named because it can give you, for a given
point in time, the denominator for your query. That is, it can tell you
all the patients that could plausibly be included in your query (at least
that is my understanding of it).

Hence the denominator file is comprehensive and contains records for all
patients eligible for Medicare until the date of their death. Naturally,
not every patient in the denominator file will be enrolled in all parts
of Medicare every month they are present. The denominator file contains
variables that help determine enrollment and continuous enrollment in
Medicare.

File Layout
-----------

The file layout is wide. Each row is a beneficiary and most of the
columns are categorical variables for each month of the denominator
file. They are named

- `hmoind[Year]m[Month]`
- `buyin[Year]m[Month]`

For example, `hmoind2008m8` or `buyin1999m12`. These variables take on
the values:

| HMO Value | Description                                                          |
|:----------|:---------------------------------------------------------------------|
| 0         | Not a member of HMO                                                  |
| 1         | Non lock-in, HCFA to process provider claims                         |
| 2         | Non lock-in, GHO to process in-plan Part A and in-area Part B claims |
| 4         | FFS for disease management demonstration project (2005 forward)      |
| A         | Lock-in, HCFA to process provider claims                             |
| B         | Lock-in, GHO to process in Plan part A and in-area Part B claims     |
| C         | Lock-in, GHO to process all provider claims                          |

| Buy-in Value | Description                     |
|:-------------|:--------------------------------|
| 0            | Not entitled                    |
| 1            | Part A only                     |
| 2            | Part B only                     |
| 3            | Part A and Part B               |
| A            | Part A, state buy-in            |
| B            | Part B, state buy-in            |
| C            | Part A and Part B, state buy-in |

Typically, we are looking for _continuously enrolled_ patients. That is,
patients who were enrolled every month pre/post a particular event for a
certain window of time. We usually say a patient is enrolled if

- HMO is `0` or `4`
- Buy-in is `3` or `C`

The code to run this can be adapted from Maurice's SAS code in
`SASMacros/generateEnrollRest.sas`. The idea is as follows:

- Select the start and end dates for the enrollment restrictions check (e.g. check restrictions from Jan 1999 to Dec 2008).
- Index the first month to 1 and the last month to `[month range]` (e.g. Jan 1999 is 1, Dec 2008 is 120).
- Find the relative month of the index event (e.g. if the event happened January 2004, the month would be 73).
- Determine the date of death of the beneficiary. If missing, we assume the person is alive.
- Determine the number of months pre/post the event to check (e.g. 12).

Now that the program is set up, we aim to generate an HMO indicator
and a buy-in indicator based on the values specified in the table above.

- If the index event occurred before the start date or after the end date, set both HMO and buy-in indicators to `0`.
- If the index event occurred within the window of time to check, then loop from `[relative event month - months before]` through `[relative event month + months after]` and check whether the HMO and buy-in indicators for those months.
- For diseased individuals, stop the search at `min(relative event month + months after, relative death month)`

- Set HMO for that month to `1` if `0` or `4`; `0` otherwise.
- Set buy-in for that month to `1` if `3` or `C`; `0` otherwise.
- Set HMO to `1` if HMO for each month was `1`; `0` otherwise.
- Set buy-in to `1` if buy-in for each month was `1`; `0` otherwise.

Code Example
------------

The CMS Specialists project has a very simple version of this
code available: It takes a date variable, which is assumed
to contain the event dates, and applies the algorithm above:
```sas
/*
 * Example:
 * %generateEnrollRest(admission_date, 1998, 2012, 12, 12, 12, 12);
 */
%macro generateEnrollRest(
        dtvar,        /* Base date for enrollment restriction         */
        end,          /* Stop checking enrollment after &end year     */
        start,        /* Start checking enrollment at &start year     */
        FFSmonthpost, /* Months to check FFS enrollment after &dtvar  */
        HMOmonthpost, /* Months to check HMO enrollment after &dtvar  */
        FFSmonthpre,  /* Months to check FFS enrollment before &dtvar */
        HMOmonthpre   /* Months to check HMO enrollment before &dtvar */
    );

    /*
     * Set up arrays to work with enrollment variables; %genYM() is
     * a untility macro to print the names of the HMO and buy-in
     * variables, since they area formatted in an awkward way
     */
    array affs{%eval(12 * (&end. - &start. + 1))} %genYM(buyin,  &start., &end., month);
    array ahmo{%eval(12 * (&end. - &start. + 1))} %genYM(hmoind, &start., &end., month);

    /*
     * diagmonth is the month number of the indx event. Its the origin
     * around which enrollment will be defined. As defined by the above
     * arrays its a frunction of your start and end date
     */
    diagmonth = (year(&dtvar.) - &start.) * 12 + month(&dtvar.);

    /***************
     *  Pre-Check  *
     ***************/

    * If event before start, all indicators to 0;
    if (year(&dtvar.) < &start.) then do;
        eHMO_pre = 0;
        eFFS_pre = 0;
        end;
    else do;
        * Otherwise start the loop for months pre;
        eHMO_pre = 1;
        eFFS_pre = 1;

        * Check endpoints of window are inside the window being studied;
        if diagmonth - &FFSmonthpre. > 0 then do;
            do m = diagmonth - &FFSmonthpre. to diagmonth;
                eFFS_pre = eFFS_pre and (affs(m) = "3" or affs(m) = "C");
            end;
        end;

        if diagmonth - &HMOmonthpre. > 0 then do;
            do m = diagmonth - &HMOmonthpre. to diagmonth;
                eHMO_pre = eHMO_pre and (ahmo(m) = "0" or ahmo(m) = "4");
            end;
        end;

        * If element cannot be checked in study window, no cont enrollment;
        if diagmonth - &FFSmonthpre. <= 0 then do;
            eFFS_pre = 0 ;
        end;

        * If element cannot be checked in study window, no cont enrollment;
        if diagmonth - &HMOmonthpre. <= 0 then do;
            eHMO_pre = 0;
        end;
    end;

    /*****************
     *  After-Check  *
     *****************/

    * If event after end, set all indicators to 0;
    if (year(&dtvar.) > &end.) or (year(&dtvar.) < &start.)
        then do;
        eHMO_post = 0;
        eFFS_post = 0;
        end;
    else do;
        * Otherwise start the loop for months post;
        eHMO_post = 1;
        eFFS_post = 1;

        * Calculate the number of months over which to Examine enrollment;
        * In particular, do not search after death;
        if (sdod ne .) then deathmonth = (year(sdod) - &start.) * 12 + month(sdod);

        * Special case 1: Individuals who died the year they had indx event;
        * -----------------------------------------------------------------;

        if (sdod ne .) and
            ((deathmonth >= diagmonth) and (deathmonth - diagmonth < &FFSmonthpost.)) then do;
            monthsAheadFFS = deathmonth - diagmonth;
        end;
        else do;
            monthsAheadFFS = &FFSmonthpost.;
        end;

        if (sdod ne .) and
            ((deathmonth >= diagmonth) and (deathmonth - diagmonth < &HMOmonthpost.)) then do;
            monthsAheadHMO = deathmonth - diagmonth;
            end;
        else do;
            monthsAheadHMO = &HMOmonthpost.;
        end;

        * Special case 2: Possible to check enrolment given window and start end year;
        * ---------------------------------------------------------------------------;

        if diagmonth + monthsAheadFFS <= (&end. - &start. + 1) * 12 then do;
            do m = diagmonth to (diagmonth + monthsAheadFFS);
                eFFS_post = eFFS_post and (affs(m) = "3" or affs(m) = "C");
            end;
        end;
        if diagmonth + monthsAheadHMO <= (&end.-&start. + 1) * 12 then do;
            do m = diagmonth to (diagmonth + monthsAheadHMO);
                eHMO_post = eHMO_post and (ahmo(m) = "0" or ahmo(m) = "4");
            end;
        end;

        * Special case 3: Not possible to check window - assume no enrollment;
        * -------------------------------------------------------------------;

        * Includes individuals falling outside study window, for example because;
        * of errant coding. Also ignore individuals who died within X months of;
        * the end point of the study because its impossible for them to have X;
        * months of post enrollment - because the study period ends;
        /*;
        if (diagmonth + monthsAheadFFS > (&end. - &start. + 1) * 12) or
           (diagmonth + &FFSmonthpost. > (&end. - &start. + 1) * 12) then do;
            eFFS_post = 0;
        end;

        if (diagmonth + monthsAheadHMO > (&end. - &start. + 1 ) * 12) or
           (diagmonth + &HMOmonthpost. > (&end. - &start. + 1 ) * 12) then do;
            eHMO_post = 0;
        end;
        */;
    end;
    drop %genYM(buyin,  &start., &end., month) %genYM(hmoind, &start., &end., month);
%mend generateEnrollRest;

%macro genYM(prefix, dstart, dend, by);
    %let s = %sysfunc(intnx(&by, %sysfunc(inputn(01JAN&dstart, date9.)), 0, e));
    %let e = %sysfunc(intnx(&by, %sysfunc(inputn(31DEC&dend,   date9.)), 0, e));
    %do %while (%sysfunc(intck(&by, &s, &e)) gt -1);
        &prefix.%sysfunc(year(&s))m%sysfunc(month(&s))
        %let s = %sysfunc(intnx(&by, &s, 1, e));
    %end;
%mend;
```
