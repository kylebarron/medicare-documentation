## Version Updates

#### 4.0

The major changes made to the code occur in step1, the extraction of the
harmonized data set from the raw data.

1.  The naming convention of the raw data sets has been simplified
    dropping the `dgnPos`, `id=bene_id` and `mn` stubs. These were not adding
    much to the understanding of the data set names. The options still
    exist in the 1A and 1B steps but the final data set names no longer
    use these tags.

2.  Added code to support inpatient extraction

3.  The code is now more flexible allowing individuals to define index
    events from the inpatient, MedPAR, outpatient or carrier claims.
    This meant splitting what used to be a single program
    `1LongitudinalExtract` into 3 different steps.

    1.  The first step (1A) goes through the raw data and flags
        candidate index events in each of the raw files of interest.
        There is a separate program for each claim file of interest.
        Researchers can define the index event however they would like
        by making changes to the ICD-9-CM and HCPCS SAS code found in the
        same folder. These if-then conditions effectively flag candidate
        index event.

    2.  The second step (1B) imposes the enrollment restriction using
        the denominator file. Several other restrictions are place on
        the data to create the final batch of index events, while also
        pulling relevant denominator and geographic information for all
        candidate events.

    3.  The third step (1C) loops through the raw files for each of the
        claims of interest and pulls a window of claims for the final
        batch of index events defined in 1B.

4.  An observation indicator from the raw files was added to the index
    and claims files in order to more easily match up the index file to
    claims, or match the extract back to the raw claims files.

    1.  Inpatient: `iprawindx` - unique with part, fileyear
    2.  MedPAR: `medrawindx` - unique with fileyear
    3.  carrier: `carrawindx` - unique with part, fileyear
    4.  outpatient: `oprawindx` - unique with part, fileyear

5.  Transfer flag code was moved to the `2create_index_level_measures`
    folder, under the transfer sub-folder. The code takes the MedPAR
    claims extracted and goes through and flags the transfer scenarios
    and saves over the original dataset.

6.  Cost utilization measures have been streamlined and simplified.
    Users will need to download the files themselves from the CMS/
    Federal Register websites. Also added a `X` day cost construction of
    the cost utilization measures for each individual.

7.  Updated the definition of the `XX` variable costs in
    [CumulativeCostsPerIndx.sas](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas).
    For example, suppose 30-day costs is the statistic of interest. It
    is possible to have a MedPAR claim with a length of stay of 45 days.
    Assuming the stay occurs at the start of the episode, not all costs
    will necessarily occur within 30 days. In the previous example this
    would mean assigning (30/45) 2/3 of the costs of the say to the 30
    days costs statistic generated.

8.  No longer dropping index events whose length of stay is greater then
    the window of claims extracted. For example, if their was previously
    a case where an individuals index event had a length of stay greater
    then a year. These types of cases were previously dropped due to
    only grabbing a 1 year window of claims. The decision to include or
    exclude such claims should be one made by the researcher and are now
    included.

9.  Added `.emacs` file with lisp files so users can easily start using
    emacs on the servers with my specification.

#### 4.01

1.  Several bug fixes

2.  `op_candidates.sas` is now created at the claim level and allows for
    index events to be generated based on information in the revenue
    centers (HCPCS procedure codes or revenue center codes) and claims
    (ICD-9-CM diagnostic or procedure codes)

3.  Updated cost utilization programs.

4.  updated the bash script `runAllprgms.sh`, which sequences all of the
    programs correctly. If the SAS programs crash, the script now makes
    the program exit and allows for the program to email the user.

#### 4.10

1.  2010 Medicare data

2.  Updated `runAllprgms.sh` bash script to run both Stata and SAS scripts
    in addition to simplifying the program.

3.  Changed the enrollment restrictions found in
    `1B_impose_restrictions.sas` from a symmetric X month restriction to
    X month restriction before the index event date and Y months after
    the index event date. Not a big change, just adds more flexibility
    the program instead of forcing users to use symmetric restrictions.

4.  Added inpatient type indicators in the MedPAR extraction

5.  Fixed several bad links in the website. Some ResDAC documents no
    longer exists. These links are kept for now. Will eventually see if
    they are available through archive.net Way Back Machine.

#### 4.15

1.  2008 PFS conversion factor changed half way through the year - did
    not previously catch. Made changes to the code to use this midyear
    change.

2.  Updated the comorbidity profile software. The CCS to ICD-9-CM
    crosswalk was not entirely complete in the case of ICD-9-CM code with
    trailing zeros. Since some claims report them an other do not, the
    crosswalk was expanded to cover these special cases for all ICD-9-CM
    codes found in the files.

3.  Fixed 1B program. Program crashed if you ran code starting on or
    after 2006 - because it was trying to apply the `ehic` to `bene_id`
    crosswalk when it did not need to.

4.  Changes to the raw MedPAR files were incorporated into the
    `decompressMedPAR.sas` script.

#### 4.50

1.  Major revision which separates the the cross-year data harmonization
    from the building of the cohort . The code does this by generating
    harmonized Medicare SAS views using code found under the 0PreProcess
    files. These views have been created and are stored on the NBER
    servers. A sas view can be thought of as compiled SAS code which
    pipes output from view to view. It creates cleaner code and also
    decreases IO requirements. Their are some additional processing and
    time costs to using these views. The programs generally take 30%
    longer to run then in the previous V4.10, however the use of views
    should make it easier for people to understand the code and change
    it to meet their needs.

2.  Cost utilization updates. 2008 PFS split referenced in a previous
    version was never passed. Their was an update to the 2005 PFS also
    found. See AMA website, conversion factor history.

3.  Created code to generate latex reports allowing users to easily
    benchmark results.

4.  A small bug was found in the medpar_candidates.sas file which does
    not impact all of the cohorts. For example it does not impact the 5%
    sample of the AMI, Hip or CHF cohorts generated by this code. It has
    been found to impact other cohorts however.

5.

#### 4.65

1.  Variable names have been [changed to match 2011
    ](https://www.nber.org/medicare/public/unzipped/v465_varname_changes.txt)variables to prepare for
    harmonized update to be done to the raw data.

2.  Some lengths were updated to reflect changed in 2011 and 2010 data.
    Some lengths were not changed because they did not make any sense
    for the variable (upin and npi)

3.  Created new sas views for 1C programs to speed extraction times by
    1/2 or more. New views subset the index events earlier in the
    program. Should not impact users

4.  Changed some SAS memory options to speed up programs, making SAS
    slightly more memory intensive to run.

5.  changed usage of space directory. no longer use agescratch disks.
    the 10g system upgrade made it no longer needed. Raw files are now
    read directly from the dataroot (no need to decompress)

6.  got rid of some sas macros: moved code into main program to make it
    easier to read.

7.  got rid of the erz libraries (for the most part)

8.  Grab zip codes found in the index file directly from raw claims
    files, rather then merge in from denominator file.

9.  Added a [quickstart](https://www.nber.org/medicare/public/unzipped/quickstart.pdf) document to aid
    users in updating programs

10. FEB28-2014: added write up to the documentation about enrollment
    (See section 2.1.1)

11. MAR11-2014: added `elixhauser` to ICD9 diagnostic crosswalk see under
    `0PreProcess` for code.

12. APR09-2014:

    1.  Fixed several improper references to the raw views in the
        `libnames`.

    2.  Created a new `runAllprgm.sh` bash file which allows users to
        change macro parameters directly from the bash script rather
        then having to open each and every SAS program.

    3.  Moved the runcode bash function to a seperate file in the SAS
        macro file - the `runAllprgm.sh` file uses it to run the programs

    4.  To accomidate passing parameters from the bash file to the sas
        programs, each SAS program has macro reference to the variable
        passed to them in the bash file. Note that users can still
        choose to run a single SAS file by filling in the proper macro
        parameters.

#### 5.00 (Feb 2015)

1.  No longer using views for production of cohort

2.  Created and saved harmonized Medicare files for a subset of
    variables on the servers > major speed increase

3.  Harmonized files names and variables match the structure and name of
    the 2012 data

4.  Harmonized files have all the `bene_id`s cross-walked on the raw data

5.  several other smaller bug fixes

6.  Harmonized files directory can be found in the
    `set_up_directory.sas` file > look at the `harmroot` global macro

7.  MARCH 20, 2015: 20% carrier files 1998 and 1999 files were too
    small. Had only extracted the 5% files in error.

#### 6.00 (Dec 2015)

1.  added 2012 and 2013 data

2.  changed the naming of files/folders to make their purpose cleared.
    Note that the number have not changed and can be used to find an
    older file

3.  changed the dirInit.sas/.do files to set_up_directory.sas/do
    files.

4.  moved denominator harmonized files under the same location as the
    raw files

5.  renamed some variables to make it easier to tell if its a patient or
    hospital characteristic and whether it comes from the index event

6.  added 0001% and 01% file extracts

#### 6.01 (Sept)

1.  fixed small bug in the [3] folder which drops index events
    before 2008. It does this after using all years of data.

2.  fixed procedure flag script; although it still only is coded for
    AMIs

#### 6.02 (Sept 6 2016)

1.  was not merging in hrr xw correclty. Updated script and also added
    2014 and 2013 to the repos.
