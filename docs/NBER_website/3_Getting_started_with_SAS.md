# Getting started with the SAS extraction programs

## Overview

The goal of this project is to create a centralized repository of Medicare
extraction programs. Centralizing the code makes it easier for bugs to be found
and fixed. It also has the added impact of flattening the learning curve for new
researchers to the Medicare claim files by leveraging the work done by
researchers who have come before them. Many of the programs are nearly ready to
be run "out of the box". The following section briefly describes an overview of
the SAS code, outlines important restrictions which the program places on the
extracts and details the process of setting up the programs to run in SAS.

The extraction occurs in four general steps, with each of the folders being
labeled in the order in which they should be run. For example the `0PreProcess`
folder programs should be run before the `1PrimaryExtractionPrgms`. Furthermore
programs which are either labeled `1A`, `1B`, or `1C` should be run in the order
designated by the associated letter.

The `/tmp` drives, previously referred to as space drive, referenced in this
section are NBER specific drives which are local to the server processing the
code and helps avoid I/O constraints on the system, in effect speeding up how
fast your code is processed. Note this has recently changed due to system
upgrade and now the network drives are actually faster - depending on system
traffic.

Also for a general overview to thinking about scientific computing, [this
article](http://www.plosbiology.org/article/info:doi/10.1371/journal.pbio.1001745)
provides a nice overview.

The following steps outline how to get started with the programs:

1. Choose a text editor to use on the Linux servers - lots of choices
2. Get comfortable with running code on the Linux servers
3. Download code or use the git clone feature if you're working on the NBER servers
4. Check to make sure that a proper DUA and user name folder has been set up for you on the space, disk and bulk drives. The following step will use these folders to create a directory structure for you.
5. Define directories in the [`set_up_directory.sas`](https://www.nber.org/medicare/public/unzipped/set_up_directory.sas) and [`set_up_directory.do`](https://www.nber.org/medicare/public/unzipped/set_up_directory.do). This file will create the directory structure for you
6. Decide on the group of ICD-9-CM and/or HCPCS codes which will define your cohort and which claims files will be used to flag candidate index events. Put these codes in the [`icd9_chrt_definition.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/icd9_chrt_definition.sas) and/or [`hcpcs_chrt_defintion.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/hcpcs_chrt_defintion.sas). If you are not using the carrier or outpatient files to define your cohort or are not using the HCPCS codes, then you can ignore the `hcpcs_chrt_defintion.sas` files
7. Fill out the parameters in the shell [`programrunAllprgms.sh`](https://www.nber.org/medicare/public/unzipped/runAllprgms.sh) found under the `TODO#` tags. The program has been modified (April 2014) to allow users to simply define variables in this files which are then passed to SAS programs. Saves the hassle of opening and closing SAS files. Note users will still be able to run a single sas program but you will need to update the parameters. As you fill out the different variables it will be important to make sure you understand the different restrictions it passes onto the creation of the extract.

!!! warning
    **Only run programs in `runAllprgms.sh` that your DUA covers. Comment out those files you wish not to run.**

## Getting comfortable with the NBER Unix systems and SAS

### Choosing a text editor

Choosing a text editor is important and is worth taking some time to choose one
that fits your needs the best. Some text editors currently available on the
servers are EMACS, pico, and vi, and there are many others available for use on
your local machine. It is recommended that you use a text editor on the server
or at least a text editor which is able to read files over ssh, in order to
avoid the hassle of having to copy programs from your local machine to the
server. Remember that results are often sensitive and should not be held on your
local machine.

Although Emacs has a steep learning curve, I chose it because it is extensible
and you can trust that the large user community has implemented most any feature
you may want. Beside general coding ease, I have found it quite useful for
writing tex files to display results and for keeping to do lists via the
[org-mode extension](http://orgmode.org/).

Emacs is customized through an initialization file read from the home directory.
The `.emacs` file needs to be created and placed in your home directory. A
sample `.emacs` file is provided at
[`Auxiliary/EMACSDOC`](https://www.nber.org/medicare/public/unzipped/Auxiliary/EMACSDOC/.emacs).
Note that an old copy of ESS is supplied in the same directory. In order for
Emacs to successfully read your initialization file, the location of the actual
lisp programs (`*.el`) needs to be included in the
[`.emacs`](https://www.nber.org/medicare/public/unzipped/Auxiliary/EMACSDOC/.emacs)
file. Yet another useful Emacs module is the M-X-cua-mode which binds the key
short cuts for copy, paste, and undo to those found in the Windows environment.

### Working with the Unix terminal

The terminal is an extremely powerful tool. It is accessible within Stata or
SAS, but you can also place a series of commands into a bash script to automate
parts your program. At a minimum, new users should get comfortable with
_aliases_ and checking the system load with the `top` or `uptime` command. [This
website](http://linuxcommand.org/learning_the_shell.php) provides a nice
overview of learning to use the terminal/shell.

For example, the SAS pack contains a bash script created to run the SAS and
Stata programs in the correct sequence and email the user in the case of a
crash. The program called
[`runAllprgms.sh`](https://www.nber.org/medicare/public/unzipped/runAllprgms.sh)
is a simple but useful example of what you can do with the terminal. To run bash
programs simply type `bash runAllprgms.sh` into the terminal, and assuming you
have assigned the right permissions it should run.

### Learning SAS and how to use SAS macros

The programs developed to pull and harmonize the raw Medicare claims rely
heavily on the SAS macro facility. SAS macros allow users to create code which
takes on a series of parameters which replace keywords (`&macro_parameter.`) in
the code prior to execution. In this way a SAS macro can be though of as a do
file where a series of local variables at the top of the program are used to
change the code in meaningful ways.

Included in the SAS pack are SAS code snippets I have used to test different
feature of SAS code. The programs are available at
[`Auxiliary/codeTest`](https://www.nber.org/medicare/public/unzipped/Auxiliary/codeTest),
and may be useful to someone getting started.

## Setting up SAS programs

Assuming an individual has entered into a DUA with CMS, users need to gain
access to the code, setup the directories correctly and define the type of
episode interested in being studied. Each of these is reviewed in the following
sub-sections.

### Download programs

Download the zipped file and decompress it preserving the directory structure in
a target location of your choosing.

### Define target and input directories

Once the programs have been downloaded, the directory structure the programs use
needs to be configured. All directories which the programs use can be found in
the following two files
[`set_up_directory.sas`](https://www.nber.org/medicare/public/unzipped/set_up_directory.sas)
and
[`set_up_directory.do`](https://www.nber.org/medicare/public/unzipped/set_up_directory.do),
which define the same locations for the SAS and Stata files. The two files need
to be populated with the correct directories prior to running the program - many
of the directories should be the same.

There are generally two types of directories found in these files. Input
directories, which correspond to places where the programs will read data in
from. In these cases, the location of these raw files simply needs to be
defined. The other case, are output directories which the programs will write
to. The `set_up_directory.sas` file will generate the directories for you as
long as you define a base directory correctly.

Once the
[`set_up_directory.sas`](https://www.nber.org/medicare/public/unzipped/set_up_directory.sas)
and
[`set_up_directory.do`](https://www.nber.org/medicare/public/unzipped/set_up_directory.do)
files are populated, run the SAS and/or Stata programs on the 0001% extracts
just to make sure that SAS/Stata has correctly read the directories which you
have defined. At the very beginning of the log file, SAS will check to make sure
that the directories defined exist. Check these notes which SAS outputs to make
sure that you directories are properly defined. The following code snippet
provides an example of the SAS WARNING LOG that occurs with incorrectly defined
directories.

```
libname tempDir "&medtmp.";
WARNING: Apparent symbolic reference MEDTMP not resolved.
NOTE: Library TEMPDIR does not exist.
```

Code: Sample SAS log error code: Incorrectly set up directories

### Define ICD-9-CM/HCPCS cohort of interest

After defining the directory structure, the next order of business involves
correctly specifying your cohort. Studies using administrative claims use
ICD-9-CM or HCPCS codes to define a group of individuals with a similar disease.
ICD-9-CM codes come in both diagnostic and procedure types, whereas the HCPCS
codes are used to define a specific procedure. The code currently has several
examples embedded directly into the code. Note that folder
[`1AFlagcandidateEvents`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt)
holds a series of different programs corresponding to each claim file of
interest. Each program calls in
[`icd9_chrt_definition.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/icd9_chrt_definition.sas)
and/or
[`hcpcs_chrt_defintion.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/hcpcs_chrt_defintion.sas)
depending on what is reported in the claim. The programs use these two files to
look for a cohort definition.

Once a series of ICD-9-CM/HCPCS codes of interest have been selected, a short
bit of code needs to be placed in the relevant file. Note that in addition to
choosing the ICD-9-CM code, a name stub (`ami` in the example below) also needs
to be referenced which all of the following programs will use reference the
cohort. For example, the heart attack example uses `ami`. All programs will use
this stub as a parameter in the macro to correctly identify the index of
interest. Future programs (e.g. `carrier_clm_window.sas`) will also need to use
the same exact stub name to load in the correct data sets.

As the following code snippet demonstrates, the new
[`icd9_chrt_definition.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/icd9_chrt_definition.sas)
SAS code now allows for users to define an index event through the use of a
procedure code. Users for the most part should only need to change the if
condition with the diagnostic code and the `is_snf` condition when changing to
another cohort of interest.

```sas
************************************************************;
***  DEFINES AMI ICD9-CM CODE SEQUENCE;
************************************************************;
%if &cohrt. = ami  %then %do;
***!!!!!! DEAL WITH DIAGNOSTIC CODE- ONLY IF NUMDGN CODES >0;
    %if &numDgnCodes.>0 %then %do;
        do i=1 to &numDgnCodes.;
            **LOOP THROUGH DIAGNOSTIC CODES;
            if substr(dgns_cd_arr(i),1,3) = "410" and
            ((length(dgns_cd_arr(i)) = 5 and
              substr(dgns_cd_arr(i),5,1) ne "2") or
             (length(dgns_cd_arr(i)) < 5) ) then do;
                dgns_cnt_arr(i)=1;
                dgnIndxNum=i;
                dICD9_indx=dgns_cd_arr(i);
        end;
    %end;
    ***!!!INSERT PROCEDURE CODE OG INTEREST IF ANY- ONLY IF PRCDGN CODES >0;
    %if &numProcCodes.>0 %then %do;
        **LOOP THROUGH PROCEDURE CODES;
        do i=1 to &numProcCodes.;
        ** LOOP THROUGH PROCEDURE CODE;
        /* EXAMPLE PROCEDURE CODE ONLY
         if (length(prcdr_cd_arr(i)) =4 ) and
            (
             substr(prcdr_cd_arr(i),1,4) = "3606" or
             substr(prcdr_cd_arr(i),1,4) = "3607" or
		     substr(prcdr_cd_arr(i),1,3) = "360"  or
		 	substr(prcdr_cd_arr(i),1,3) = "361" or
             substr(prcdr_cd_arr(i),1,4) = "3722" or
 			substr(prcdr_cd_arr(i),1,4) = "3723" or
             substr(prcdr_cd_arr(i),1,4) = "8855" or
             substr(prcdr_cd_arr(i),1,4) = "8856" or
             substr(prcdr_cd_arr(i),1,4) = "8857"
            )
            then do;
            	prcdr_cnt_arr(i)=1;
                pICD9_indx=prcdr_cd_arr(i);
	            prcIndxNum=i;
            end;
        */
        end;
    %end;
    **Other options specific to claims file here;
    %if &file. = medpar %then %do;
        **Drop if index event occurs at SNF;
        if is_snf=1 then delete;
    %end;
%end;
```

Code: Sample `icd9_chrt_definition.sas` code: Defining the AMI cohort

### Define SAS parameters in the `runAllprgms.sh` file

The next step is to go through and define all of the parameters which are passed
onto SAS programs found in the `runAllprgms.sh` file. In doing so it is
important to understand the different restrictions used in building the cohort.
Note that an index event is defined as the first episode care for a cohort, it
denotes the beginning of an episode of care. The following list provides and
overview of the steps in building the cohorts and the relevant restrictions.

1. Flag potential (candidate) index event using the procedure/diagnostic codes defined in [`icd9_chrt_definition.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/icd9_chrt_definition.sas) and/or [`hcpcs_chrt_defintion.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/hcpcs_chrt_defintion.sas). The subset of patients are selected by the 1A programs
    1. Parameter `COHRT`: The `cohrt` variable should match the code block found in those files.
    2. Parameters `IP`, `OP`, `MEDPAR`, `CAR`: These binary flags denote which files were used to define the index event. In the example AMI covered in this documentation only the `MEDPAR` parameter would be set to 1 and the others to 0.
    3. Paramters `IP_DXN`, `IP_PROC`, ...: The parameters denote how many diagnostic or procedure codes to look through when defining an index event. For example, in our AMI cohort, as in with many cohorts, the cohort is built only of the principal diagnostic code in the MedPAR file which coincides with the first diagnostic code. In that example only the `MED_DXN` parameter is set to 1 with the rest of the parameters set to 0.
2. Merge in enrollment information and impose enrollment restrictions ([`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas) program)
    1. Parameter `DAYS_BETWEEN_INDEX_EVENT`: Number of days which must pass before an individuals can have another index event assigned. The assumption is very important because in a sense it defines how much time must pass before we want to treat a new candidate episode as a new event. It also takes care of transfers since the first index event will be assigned.
    2. Parameters `FFSmonthpost` and `FFSmonthpre`: The individual is continuously enrolled in Parts A and B of traditional Medicare (rather than a Medicare private plan) during the twelve months before AMI and until twelve months after AMI, or until death. (months can be changed by the variables `FFSmonthpost`/`FFSmonthpre`)
    3. Parameters `HMOmonthpost` and `HMOmonthpre`: The individual is continuously not in HMO during the twelve months before AMI and until twelve months after AMI, or until death. (months can be changed by the variables `HMOmonthpost`/`HMOmonthpre`)
    4. The individual is at least 66 years of age at the time of the AMI

        !!!note
            This is hard coded and would need to be changed in the 1B program.

    5. No bad date of death or birthday

        !!!note
            This is hard coded and would need to be changed in the 1B program.

3. Pull claims around the index event dates, using the index date (first treatment date for disease/procedure of interest) which have been harmonized
4. Run secondary programs to define comorbidities and cost statistics
    1. Raw cost statistics: `DAY1` - `DAY7` variable denote the `X` day cost you want to be calculated. For example setting `DAY1=30`, `DAY2=90` and `DAY3=365` would create 30-day, 90-day, and 365-day costs where the day references the number of days occurring after the index event date.
    2. Parameter `YEARIN`: Since cost statistics combine information across claims, you need to define the earliest year of the claim you are using, it's usually the MedPAR data.

In order to run a specific SAS program, the wrapper macro needs to be invoked
with the correct set of parameters. Most of the time the parameters are very
similar across the programs and is why the `runAllprgm.sh` bash file was created
to feed each SAS program its parameters. Note that the parameters are documented
at the end of each program, with some of the most common parameters defined in
the following table. The programs are generally saved with a sample wrapper
program call at the end. The parameters in many cases will also define the name
of the data set created or loaded up depending on the program. Therefore, it is
important to use the same cohort stub in the different programs, so that the
correct files are loaded.

|           Parameter           |                  Description                   |
|-------------------------------|------------------------------------------------|
| `cohort1`                     | These reference the ICD-9-CM codes in the code |
| `cohort2`                     | You can add as many of these as you would like, however if you start running several (4 plus) the efficiently of the program maybe impacted |
| `cohortN`                     | Define the total number of cohorts you are creating |
| `yearin`                      | Start year for the run |
| `yearout`                     | End year for the run |
| `pct`                         | Define the percent extract you are interested in using |
| `dflag`                       | Set equal to one if you want to delete raw files as you run the program |
| `clmDTA`                      | Set equal to one if you want to convert the all files into a Stata format (DTA), as long as stat transfer is on the server you are running |
| `crashStart`                  | If program crashed, set equal to the year program crashed and it will restart from that year and aggregate the program once finished processing from the yearin to yearout dates. (Carrier and Outpatient extract files only) |
| `win` (year)                  | Define the window around the index event the program is to extract (in years). Note when changing this you may also be interested in changing the window which determines how consecutive index events get dropped. For example currently the program drops AMIs from the index events which occur within the past year. Search variable name `last_dgn_date` in the [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas) program for more info. |
| `subsquentDgnDayRest` (days)  | Defines the minimum amount of time allowed to pass before a beneficiaries with more then one candidate index event can be treated as a index event. The restriction drops all candidate index events which are within `XX` days of each other and it keeps the first one. The restriction is important because it helps ensure that no two index events in the final data set are directly related, through a transfer or something similar. |
| `HMOmonth[pre/post]` (months) | Defines the number of months of continuous HMO enrollment need before and after the index event month, including the month of the index event, used to restrict the sample; |
| `FFSmonth[pre/post]` (months) | Defines the number of months of continuous FFS enrollment need before and after the index event month, including the month of the index event, used to restrict the sample;|

Table: Parameters definitions in wrapper macros

In the case that either the carrier or outpatient extraction programs are run
and they crash, it is easy to restart the programs from the most recent year
which they were running. Refer to the `crashStart` parameters. For example if
you are running a carrier extract between 2000 and 2008 and the program crashes
on 2002. First you would create a copy of your log file and save it some where
else. Next simply run the following wrapper call from within the Carrier
extraction program found at the end of the program.

```sas
%RunCarExtraction(pct=05,
                  cohrt1=ami,
                  cohrtN=1,
                  yearin=2000,yearout=2008,crashStart=2002,
				  win=1,
                  clmDTA=1
				  );
```

Code: Sample Carrier Extraction Wrapper call: Running the program after a crash

### Program sequencing

As noted above, some programs are dependent on the data created by other
programs. In particular, the files in the
[`1cohort_extraction`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction)
folder should be run first. The exact sequencing is given in the following
outline. Any of the programs found in the folder `1A_flag_candidate_evnt`
(bullet point 2a below) should be run before the programs found in
`1C_pull_claims` (bullet point 2b below). `1B_impose_restrictions.sas` should be
run before 2b `op_clm_window.sas` and any of the programs in
`2create_index_level_measures` should be run before any of the programs found in
`3merge_cohort_level_data`.

All programs rely on the `set_up_directory.sas` and `set_up_directory.do` files
to define the directory structure used throughout the project. In addition the
sequencing of programs is important and follows the hierarchy found below.
Conversely, the `runAllprgms.sh` bash script can be used to call all programs in
the correct order after the macros in each program have been correctly been
populated.

1. `0pre_process`
    1. Individuals working on the NBER servers do not need to worry about running these programs. They have been run and the preprocessed datasets are held on the servers.
2. Harmonization of the raw data (three sub steps)(folder:`1cohort_extraction`)
    1. `1A_flag_candidate_evnt`: the programs found here loop through the raw data and pull beneficiaries which match the criteria defined in the `icd9_chrt_definition.sas` and/or `hcpcs_chrt_defintion.sas`.
    2. `1B_impose_restrictions.sas`: The single file is run after all the candidates have been flagged and saved in a separate folder. Beside the initial flagging of beneficiaries, all of the restrictions used to define the final index events are imposed in this file. The program merges all candidates, imposes restriction and defines index events with relevant demographic variables generated.
    3. `1C_pull_claims`: The programs found in this files pull a relevant window around the index claims. This final dataset contains all the harmonized claims for each of the different claims files.
3. Using the harmonized raw files, programs in this folder build index event level measures like 30-day costs or comorbidity profiles. (folder:`2create_index_level_measures`) These programs use output from the previous step to create variables which aggregate measures to the index event level.
4. The final program attempts to build a final analysis file for you which is a the index event level. It merges in datasets onto the index event level. (folder:`3merge_cohort_level_data`). This is a good folder-file to get comfortable with.

### Running the SAS program on the Linux servers

Running the SAS extraction programs on the Linux servers are fairly
straightforward, however there are some additional options which should be used
due to the length of time it take to run the programs.

Many of the extraction programs can run for several days due to the size of the
extracts. Using the `nohup` command on the UNIX servers is important when
running these programs because it will continue running the program even if you
log off or are disconnected from the server. For example, running the following
from the terminal
```
nohup sas carrier_clm_window.sas &
```
would run the `carrier_clm_window.sas` program in the background until it
crashes or finishes running, even if you log off the servers. The ampersand
informs the servers to run the program in the background. The program will only
stop if it finishes or reaches an error which forces it to crash.

In order to avoid running out of space in the work directory, SAS allows you to
set the work directory. Generally the SAS work directory is used when any data
set in the code is referred to without a directory or explicitly with the
directory work.data set. The work directory is written by default to the `/tmp`
directory of the current server. However users can easily overrun the `/tmp`
directory and cause all programs using the `/tmp` to crash on the current server
(not just their program).

This problem is easily avoided by by invoking SAS with the additional options
from the terminal as follows. As a rule of thumb, you only need to worry about
setting the work directory if you are encountering problems with space in the
`/tmp` drives. Note that most users need not do this unless their programs are
crashing due to `/tmp` space.

Note that all the programs have been sequenced for you already and you could
just run the `runAllprgms.sh` script after setting up by typing `bash
runAllprgms.sh` from the terminal.

```
nohup sas -work INSERT/DIRECTORY/HERE carrier_clm_window.sas &
```

Code: Invoke SAS from terminal with separate user defined work directory - **Not Suggested**

### Factors impacting run times

There are two main factors a user has control over that directly impact the run
times. A user can determine which server to run their program on; making sure a
server is not overloaded will increase the speed of your (and everyone else's!)
programs. Being aware of which disks you are writing to can have drastic
improvements to speed. The programs optimize this for NBER users.

It is important to check the system load before starting a SAS program, as
overloading a machine will slow the processing of all the jobs to a crawl.
Therefore it is best to check back later and submit the jobs once the server
load is reduced. Checking the server load can be done from the terminal by using
the `uptime` command, which prints out several pieces of information. The last
three numbers give system load average for the last minute, 5 minutes and 15
minutes. A number over 3 represents a machine that is loaded. For example:
```
> uptime
 16:28:45 up 75 days,  1:51,  2 users,  load average: 0.15, 0.05, 0.14
```

Server load is something which most users will not directly have control over as
it depends what other people are running. By contrast, deciding which disks to
write to is something which a new user will have direct control over and which
also will greatly impact the speed of the program. For example, when
decompressing files it is best to write the decompressed file to a local
directory (i.e. space drive). Note that writing to a local directory can cut
processing times in half.

## Minor data extraction inconsistencies

There is the possibility that some inconsistencies occur in the extracted data
due to the restrictions placed on the code. The percent of claims impacted are
very small, but in the event that an individual attempts to benchmark a specific
measure, like number of unique claims, some inconsistencies may occur. For these
reasons the following section describes when we may expect claims to be
duplicated in the extraction process.

### Possible claim duplication

The possibility for claims to be duplicated in the extracted data exists because
of the way in which claims are pulled. The extraction program goes through and
identifies an index event and then pulls a one-year window of claims around the
index event. Due to the procedure, the possibility for a claim to be duplicated
exists in the event that an individual has more than one potential index event
which occurred more than a year apart but not greater than two years.

Index events within a year of each other for a specific individual are dropped
from the sample, leaving the first index event occurrence in the final data set.
This leaves individuals with an index event occurring more than 1 year apart in
the sample. However since the procedure take a 1-year window, around each index
event, some duplication of claims maybe introduced. The same is true for
individuals pulling claims greater then a 1-year window.

Note that this occurs for an extremely small part of the sample, something on the order of 0.001%.

### EHIC switchers enrollment information

In some cases a `bene_id` associated with more than one EHIC may have two
separate EHIC entries in the denominator files. A subset of these `bene_id`s may
report different enrollment information on the separate EHICs associated with a
single `bene_id`, although they should be the same. The most recent enrollment
observation from the file is kept since it is unclear how to treat these cases.

## Estimating run times

In order to help aid researchers in planning for projects and optimizing their
run times, the following tables provide approximate run times for each program.
Note that the `op_clm_window.sas` and `carrier_clm_window.sas` program can be
run at the same time as long as they are started about 15 minutes or so apart.
The first macro they both call uses the `indx` dataset output from the 1B
program. If you are experiencing much different run times and the servers are
not over loaded, then there is likely an issue with how you have set up the
directories. A first good check is to make sure you are utilizing the local
`agesasscratch#` disks for as much of the writing as possible. This can speed
processing times by a factor of two easily. Note that the times given here cover
all Medicare data years for each file type.

|                                  Program                                   | 5% |  20%  | 100%  |
|----------------------------------------------------------------------------|----|-------|-------|
| Programs found in the `1A_flag_candidate_evnt` folder  (some are optional) |    |       |       |
| `ip_candidates.sas`                                                        | 14 |       |       |
| `medpar_candidates.sas`                                                    | 5  |       | 240   |
| `opcandidatest.sas`                                                        | 38 |       | <1700 |
| `carrier_candidates.sas`                                                   | 78 | 370   |       |
| Program found in `1cohort_extraction`                                      |    |       |       |
| `1B_impose_restrictions.sas`                                               | 30 | 45    | 60    |
| Programs found in the `1C_pull_claims` folder                              |    |       |       |
| `ip_clm_window.sas`                                                        | 1  |       |       |
| `medpar_clm_window.sas`                                                    | 5  | <50   | <190  |
| `op_clm_window.sas`                                                        | 28 | <1000 | <1700 |
| `carrier_clm_window.sas`                                                   | 28 | <350  |       |

Table: Program run times (estimates) in minutes for an AMI cohort running all available years

## Adding new variables to the extract

The current version of the code uses a series of tab delimited text files which
have crosswalks between the final harmonized variable of interest and the raw
variable name in the medicare claims files for each year. In addition, the
crosswalk notes the max length of the variable, whether the variable is defined
as a number or character and whether or not the variable was generated. A series
of SAS macros take the information held within these crosswalks and generate a
harmonized data set.

Looking at the `.lst` file for any extraction program prints out the crosswalk
which has the convenience of providing the exact crosswalk used for the current
program.

Using text file crosswalk has the added convenience that adding a new file to
the extracts is extremely easy as long as the variable is not changing from
numeric to character or vice versa during the time period. Even in this latter
case the process is simple although a bit more involved. Assuming that the
variable stays the same type throughout the time period of interest simply add a
row to the crosswalk file and the program will generate the new file for you.
The cross walks can be found in the `claim_xw` folder.

The latest version no longer uses views and the files are harmonized and saved
on the servers - this save considerable run times.

|    Program     | Crosswalk Files |
|----------------|-----------------|
| `Medpar*.sas`  | [medparxw.txt](https://www.nber.org/medicare/public/unzipped/claim_xw/medparxw.txt) |
| `Ip*.sas`      | [ipxw.txt](https://www.nber.org/medicare/public/unzipped/claim_xw/ipxw.txt) |
| `Op*.sas`      | [opxw.txt](https://www.nber.org/medicare/public/unzipped/claim_xw/opxw.txt) |
| `Carrier*.sas` | [carrierxw.txt](https://www.nber.org/medicare/public/unzipped/claim_xw/carrierxw.txt) |

Table: Crosswalk text files used by the claims files

## Using Git

For NBER users working on the NBER servers who have pulled the code using the
`git clone` command, there are several other useful features which Git affords
you. To begin with Git is a distributed revision control system which is similar
to SVN with the exception that it is distributed. This basically means that each
instance of Git pulls the entire code history which allows users to easily look
at the entire history of change made to a file by typing in `git log -p
direc/filename.here`. The power of Git is in the fact that it allows you to
easily share/compare code with other users and easily created branches to your
code to test certain features and avoid messing with working code. To begin with
you can always type `git log` to see the most recent commit and version of the
code you are using.
