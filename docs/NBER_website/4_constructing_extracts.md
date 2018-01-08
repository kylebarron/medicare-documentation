# Constructing the Extracts in SAS

## Overview

The goal of the project is to create a series of SAS programs which extract a Medicare cohort which are scalable to the 100 percent Medicare claims files. The initial cohorts are extracted from the files in SAS. Next a series of SAS programs process the original extracts until information has been sufficiently aggregated to the index level, resulting in substantially reduced file sizes. Finally the data is transferred to Stata using Stat/Transfer. Note that SAS is the recommended program for extracting the cohorts and manipulating the data. Using SAS has the benefit of allowing your code to be easily extensible to a larger extract because SAS does not have the same memory constraints as Stata.

The extraction programs use SAS scripts, corresponding to the MedPAR files (based on the Inpatient/SNF claims) and the Carrier, Outpatient, and denominator claims. First the onset of a disease is identified using the programs found in the folder [`1A_flag_candidate_evnt`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/) . Users have the option of using claims from Inpatient, Medpar, Outpatient and/or carrier files to define candidate index events. These disease events are indexed and used to pull claims from the MedPAR, Carrier and Outpatient files after a series of enrollment restrictions are place on the beneficiaries using the denominator file. Next a series of scripts provide information on (1) comorbidities, (2) costs, (3) procedures and (4) cost utilization measures .

In order to preserve the integrity of the SAS data files, the NBER has split the claims data into smaller compressed file parts per year. The SAS programs decompress one part at a time, manipulates it, saves the relevant observations and then deletes the original. While this type of iterative procedure saves on system resources, it can make the code difficult to follow because the program consists of a series of iterative macros defined to process one part at a time and finally combine them in a final step. Note that pre-2006 MedPAR files have not been chunked because of their relative size, where as the rest of the claims have been. Beginning in 2006 the MedPAR files will also be chunked.

In the case of a program crash or a partial run, the program will need to be run again. Rerunning the program in turn will cause SAS to automatically overwrite the log file, which has important information about how the data set was constructed. Care should be taken when debugging the program to make sure log files of interest are not overwritten.

Even if you successfully run the program, and then decide to run a separate extraction program SAS will overwrite the log file in the directory you are working in. For this reason, the programs automatically create a new folder and copies the log and lst file to the folder at the end of each run after tagging them with the date, years run and cohort of interest. Note that if you are running several cohorts the log file is simply copied at the end of the cohort loop and in some cases the full log file information - including total time run - will only be present on the log file of the last cohort.

## Flagging candidate index events

Folder: [`1A_flag_candidate_evnt`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/)

Before running any programs a cohort needs to be defined. This means defining the combination of HCPCS and ICD9-CM codes used to define a specific variable. At the same time the choice of HCPCS or ICD9-CM codes will depend on which claims files are used to pull potential candidate index events from. In many cases individuals choose to uses the primary diagnostic code from an inpatient stay, which can be found either on the Inpatient claims or the MedPAR file.

For example, limiting the sample to AMIs hospitalized will ensure that the AMIs being studied demark a clean start to a new episode of care, since nearly all AMIs are hospitalized soon after onset (unless the victim dies).

The first step in the AMI example is to generate a sample of candidate index events, after which denominator information can be merged in with to enforce enrollment restriction of interest. Therefore for this example only the the [`medpar_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/medpar_candidates.sas) will be run. Since this program only calls the [`icd9_chrt_definition.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/icd9_chrt_definition.sas) codes, code has been included there which flags a potential AMI admission if it meets two criteria. The restriction to the principal diagnosis (first ICD9-CM code) is done in the [`medpar_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/medpar_candidates.sas) program.

1. **The first ICD-9-CM diagnosis code on the MedPAR record corresponds to an initial episode of care for an AMI.** The first diagnosis code on the record reports the primary reason for hospitalization. Since an AMI will almost always be the primary reason for hospitalization when present, AMI admissions can be readily identified using this field. ICD-9-CM diagnosis codes for the initial episode of AMI care are those with the first three digits 410 and fifth digit (if present) equal to 0 or 1. However it is important to note that the code allows you to define an encounter on principal plus any number of secondary diagnoses for exploratory purposes. If secondary diagnosis codes are used to identify the index event, in addition to the principal diagnosis the parameter `&dgnPos.` in the wrapper macro call simply needs to be changed.
2. **The admission occurred at a hospital, not a skilled nursing facility.** This restriction is imposed because it is unlikely that an AMI would result in an initial admission to a skilled nursing facility, rather than an acute care hospital. These AMIs are flagged and dropped.

Note that the following figure describes the role of the `dgnPos` and `prcPos` parameters in the wrapper programs. Note that carrier candidate file only allows users to define `drgPos` because the HCPCS codes happen at the line items level and there is no meaningful ranking to procedures performed on the same day.

```sas
/* dgnPos=1 — informs the programs to only flag diagnostic
             codes in the first diagnostic position
             (most important). A 2 would have the program look
             into the first 2 procedure diagnostic codes */
/* prcPos=0 — informs the programs that no procedure code are
             being used to define cohort. Turns off the use
             of procedure codes. */
%TagcandidateIndexEvents(
    cohrt1 =ami,
    cohrtN =1,
    dgnPos =1,
    prcPos =0,
    pct    =05,
    yearin =1999,
    yearout=2009,
    dflag  =1,
    clmDTA =0);
```
Figure 4.1 `medpar_candidates.sas` wrapper to only flag the principal diagnosis

Each candidate program generates a data set at the stay, claim or line item depending on which files you are working with.

1. `ami05_d1p0_medparcandidate`: stay level candidates.
2. `ami05_d1p0_opcandidate`: claims level candidates.
3. `ami05_d1_carcandidate`: line item level candidates.
4. `ami05_d1p0_ipcandidate`: claims level candidates.

## Defining the final set of candidate index events

Program: [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas)

The first section describes the basic steps involved in flagging candidate index events for an AMI. However not all candidates are usable especially if our interest is in tracking costs over time. The issue is that since, Medicare Advantage costs are not included in the claims files, patients switching in and out of FFS will have inaccurate costs. For that reason the following step performed by the [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas) programs merges in denominator information and restricts the sample the final set of index events.

Three data files are used to construct this part of the extract:

1. Denominator file: This is an annual file that includes a record for each individual enrolled in Medicare Part A or Medicare Part B during the year. It provides demographic information, including sex, race, date of birth, and date of death (if any) and monthly data on the individual's enrollment status, including whether the individuals' benefits were provided through a private plan.
2. Candidate index event file: This file is generated from the previous step. This step merges the data together and enforces a priority ranking so that index events happening on the same day are assigned to the claims file of interest.

Before any restrictions are place on the data, the program first merges all of the candidate index events, since it is now possible to use several files. The wrapper program for defining this has many parameters. The AMA example is given in the following figure. Note that first off since only the MedPAR file is used the the med= parameter is set to `1` with the rest set to `0`. Also the `med_dgnPos=` and `med_prcPos=` parameters need to match that found in the `medpar_candidates.sas` program.

```sas
%CombinecandidateIndxEvents(
    cohrt      = ami,
    pct        = 05,
    end        = 2009,
    ip         = 0,
    ip_dgnPos  = 0,
    ip_prcPos  = 0,
    med        = 1,
    med_dgnPos = 1,
    med_prcPos = 0,
    car        = 0,
    car_dgnPos = 0,
    op         = 0,
    op_dgnPos  = 0,
    op_prcPos  = 0);
```
Figure 4.2 `medpar_candidates.sas` wrapper to only flag the principal diagnosis

The approach used to defining the sample roughly follows Udvarhelyi et al. (1992), McClellan (1993), McClellan et al. (1994), and McClellan and Newhouse (1997)[^24]. A major restriction is based on enforcing continuous non-HMO enrollment which accounts for a large percent of candidate index events dropping form the sample. The second most important restriction involves allowing the same individual to have more then one index event in the final index set, as long as the candidate events happened at least one year apart. Correspondingly, the procedure includes an AMI in the final sample if the following criteria are met [^25]:

[^24]: The code also includes an approach based upon Skinner, Staiger, and Fisher (2005), which aims to construct a data set of individuals having first AMIs.
[^25]: Two additional data-quality requirements are also imposed: 1) The individual's death date (if listed) must be after the date of the AMI admission; and 2) The individual must have a valid date of birth. These restrictions affect a very small number of individuals.

1. There is no evidence of another AMI admission in the last year. The assumption very important because it defines the amount of time which needs pass between events in order for them to be classified as separate or related. In addition, it also deals with the issue of transfers to some effect. **Control via the `subsquentDgnDayRest` in `X` days.**
2. The individual is continuously enrolled in Parts A and B of traditional Medicare (rather than a Medicare private plan) during the twelve months before AMI and until twelve months after AMI, or until death, whichever comes first. Requiring continuous enrollment before AMI ensures that any AMI occurring during the prior year would indeed appear in the MedPAR file. Requiring continuous enrollment after AMI ensures that the claims files cover all post-AMI service utilization. This continuous enrollment requirement also implies that the earliest AMI included in the data set will be plus 1 year from the first year of the analysis. The last point will correspond to minus 1 year from the last year of data used in the analysis. Finally, note that excluding individuals who were enrolled in a Medicare private plan before or after AMI may not be innocuous. As noted above, the share of Medicare enrollees enrolled in traditional Medicare changes meaningfully over time and selection into private plans is thought to be non-random. While there is probably not a good alternative to excluding these individuals, this feature of the extract should be kept in mind during analysis. **Control via the `contHMOmonth` and `contFFSmonth` parameters. Note that it enforces a `X` month window on each side of the index event.**
3. The individual is at least 66 years of age at the time of the AMI. This restriction excludes individuals who are either: 1) currently eligible for Medicare on the basis of disability; or 2) meet the continuous Medicare enrollment requirement only because they were eligible for Medicare on the basis of disability before turning 65. This ensures that the resulting sample is basically representative of the old-age Medicare population (except for 65 year olds). **Hard coded.**

The following code shows that in addition to defining the cohort with some combination of procedure or diagnostic codes, years of interest and percent of sample, the code also allows for users to tweak the first continuous enrollment restrictions and the days which need to pass before index events before a new index event for a patient can be defined.
```sas
%ImposeSampleRest(cohrt=ami,pct=05,start=1999,end=2009,
2                  subsquentDgnDayRest=365,
3                  contHMOmonthpre=12,contHMOmonthpost=12,
4                  contFFSmonthpre=12,contFFSmonthpost=12);
```
Figure 4.3 `medpar_candidates.sas` wrapper to only flag the principal diagnosis

The only complication in obtaining this demographic and enrollment data is that the names and formats of variables in the denominator file change somewhat over time and differ from those in the enrollment file. The file [`ConformDenom.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformDenom.sas) contains the macro used to convert the denominator files into a common format. The differences between the format of the denominator files are handled directly in [`CreatePopDenominatorFile.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/enroll_denomFiles/CreatePopDenominatorFile.sas). Running this program once for the entire population is recommended for users constructing a Medicare repository.

The exact portion of the code which enforces these restrictions in the code can be found in the following figure. Note that the data set with these flags created but without dropping any variables is available in the data set created by the `1B_ImposeDenominatorRestrictions.sas` program. The data set is stored in the index extract folder and is labeled `&cohrt.&pct._candidateflag` (i.e. `ami05_candidateflag`).

```sas
* Implement criteria for including diags like those in
* McClellan and Newhouse and Udvarhelyi, et al.;
    * 1) Must be no other diag admission in the last year
    * 2) Must have traditional Medicare enrollment for a
         X-month (X+1+X) window around index event;
    * 3) Must be 66 at the time of the diag;
    * 4) Has a date of death on or after the diag date;
    * 5) Has a valid date of birth;
        if  (not diagLastYear and
             contEnrol_post and
          	 contEnrol_pre and
			 ageAtdiag >= 66 and
			 not dobMissing and
			 not badDOD)
		then do;
            output out.&diag.&pct._indx;
		end;
```
Figure 4.4 Sample `LongitudinalExtract` code: Defining the AMI cohort

The [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas) program creates the following files, assuming a 5 percent AMI was run using `bene_id`s and the principal diagnosis only:

1. `ami05_candidateflag`: Data set is unique at the index event level (`diag_id`) and includes relevant information for the stay associated with the defining index event. The file is created by imposing all of the restrictions on the on the data (unlike the `coref` file which simply flags the restrictions).
2. `ami05_indx`:Data set is unique at the index event level (`diag_id`). A file containing all of the potential index event candidates observations in addition to the relevant variables used to further restrict the data set. The data set is useful for better understanding how different restrictions impact the final sample. Note the observations in this data set are the same as if all MedPAR (non SNF) observations with a principal AMI ICD9-CM codes are pulled from the data set.
3. `ami05_demo`: Data set is unique at the individual level (`bene_id`). Contains information on enrollment and demographic information. Note includes information on all individuals in the final index event data set plus all individuals qualifying as an index event (observations in the `coref` data set).
4. `ami05_indxdemo`: Data set is unique at the index event level (`diag_id`). The data set merges relevant demographic information to the index even data set and formats that data further.

The macros have been arranged in a "wrapper" program, called `%RunPrgram`, which provides the correct sequencing and allows the macro to run several different types cohorts within a single run.

After running the `%RunPrgram` macro, a report writing program contained in a separate SAS file, `%CreateReports` can be run which provides several reports, see table below. Just make sure to specify the location where the Excel reports should be written to.

| Filename                 | Description of Report                                                 |
|:-------------------------|:----------------------------------------------------------------------|
| `&cohrt._flagcount..xls` | Tabulates number of encounters by year for each restriction flag defined (i.e. number of individuals under 65) |

Table 4.1 Description of report created by `%CreateReports` macro

## Pulling harmonized claims around the index events 1C_pull_claims

The programs found in the [`1C_pull_claims`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims) folder each use the final set of index events defined previously to pull a window of claims around the index event. The is basically the second pass over the claims, the first being used to define the index events. The length of the window can be set by the researcher.

### Extracting harmonized MedPAR claims

After the AMI index events are defined, the code makes another pass over the MedPAR files in order to obtain records for all hospital and skilled-nursing facility visits in the period around each AMI. In general, the code selects all visits that start at most one year before AMI and have discharge dates at most one year after AMI[^26]. However, note that the user can control this via the parameter found in the wrapper macro.

[^26]: The date of discharge rather than date of admission is used to define the post-AMI period in order to ensure that AMIs that occur in the file year of the data are treated symmetrically to those in earlier years. In particular, suppose that the end of the post-AMI period was instead determined by the date of admission and consider an individual who experiences an AMI in late 2004 who is re-admitted to the hospital in late 2005. If this hospitalization were to last into 2006, it would reported in the 2006 claims file and, thus, fall outside of the set of hospitalizations observed here.

Some SNF claims indicate that the individual was still a patient at the time the claim was finalized and, correspondingly, have missing discharge dates. For these records, the record is included if the admission date and the length of stay field indicate that the services on the claim occurred within one year of AMI[^27].

[^27]:  In addition, for these records, the final extract sets the discharge date field equal to the admission date plus the length of stay (minus 1 day) since it is useful to be able to treat the discharge date as a "claim end" date rather than a true discharge date.

Finally, the extract includes any record with an admission date falling on the date of AMI. As part of this selection process, each claims record is tagged with the `diag_id` for the "AMI episode" of which it is a part.

Note that, as with files containing enrollment information, the MedPAR variable names and formats change significantly from year to year. The file [`ConformMedPAR.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformMedPAR.sas) contains the macro used to convert the MedPAR files to a common format.

After all of the raw claims files have been processed, the MedPAR records are put "in order" according to admission and discharge dates. When dates do not permit an unambiguous ordering of the records (e.g. when an individual is admitted to and discharged from multiple hospitals on the same day), the script uses other information on the record, notably admission and discharge status codes, to determine the order in which the various hospital admissions occurred.

The script uses Stat/Transfer to export the files to Stata, however the additional code is included in the Auxiliary folder which uses SAS XPT files. The preferred method is StatTransfer as it makes use of less disk space and avoids an extra Stata import step. See Step 6 in Appendix B.

1. `ami05_medparclms`: Data set us unique at the MedPAR claim/stay level. The data set pulls claims associated with the index events in the file `ami05_1_indx_mn_bene_id`. Claims one year after and one year before the admission date of the index event are found in this file.

### Extracting harmonized Carrier/Physician line items

For many projects, including the current one, it is useful to also obtain claims records for services performed by physicians and other non-institutional providers like ambulance operators and laboratories.

Each year's Carrier file provides detailed information on each service provided, including the type of service (indicated by HCPCS codes), the date of provision, the amount of payment, and the identity of the provider. Different years' Carrier files structure this information in different ways.

For years 1999 and later, however, the Carrier file begins grouping individual services, or "line items," together into "claims." Typically, a claim consists of a group of services provided by the same physician (or other provider) during a single episode of care. How the files present claim and line item information differs by year.

For 1999-2001, each Carrier record continues to correspond to a single line item, but each record also contains all claim-level information for the claim of which it is a part. Most fields on the Carrier record appear only at the claim level (e.g. patient's zip code) or only at the line item level (e.g. procedure codes). But some fields appear at both the claim level and the line item level, which can make these years' files treacherous to work with. Most importantly, each record typically includes a field containing the amount paid for the current line item and another field containing the amount paid for all line items in the current claim. Extracting the claim-level payment field rather than the line item-level payment field would lead to dramatic errors.

Starting with the 2002 Carrier file, CMS splits the Carrier file into two sub files: a "claims" file, which contains one record for each claim and contains all claim-level information; and a "line items" file, which contains one record for each line item and contains the line-item level information as well as unique identifiers that facilitate matching to the claims file. While the split means that processing for these years typically requires a merge, it does make it much clearer which fields are claim-level fields and which are line item fields.

The script used to process the Carrier file is called [`carrier_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/carrier_clm_window.sas). It first loads the index events ( individual identifiers and diagnosis dates) created and saved by the [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas). Next, it uses that information to extract all carrier line items (i.e. individual services) with a start date at most one year before the date of AMI and an end date less than one year after AMI[^28]. The code excludes all line items with a missing start or end date, which appears to affect only about one in every million claims. In the process of extracting the line items, it tags each one with the `diag_id` for the "AMI episode" of which it is a part. Finally, the script writes all records to a SAS and Stata file.

[^28]: The start and end dates of carrier line items are often equal or within just a couple of days of each other. Thus, it makes relatively little difference precisely which date is used.

[`carrier_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/carrier_clm_window.sas) must handle significant differences in variable names and formats across Carrier file years. The SAS macro that handles these differences is contained in the file [`ConformCarrier.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformCarrier.sas).

As a final note, keep in mind that, because the Carrier files are extremely large, the code described above can take more than a day to run. There are significant gains to running a program which extracts several diagnosis at once because the file only needs to be unzipped once. The program allows individuals to run several cohorts by adding in different parameters. Furthermore extending the code to other diagnosis cohorts, is straightforward and needs to be coordinated with the [`1cohort_extraction`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction) family of scripts. Note that if you do run a multi-disease cohort run, the Carrier program needs a lot of space dedicated to it. Of course these files are temporary and could be deleted afterwards, however one must be careful before firing of the runs. Additionally, due to amount of time the script takes to run and amount of system resources needed it is possible for the program to crash. Hence the code allows the user to start from any date so that, if the code stops unexpectedly, it need not be re-run from the beginning. See the `crashStart` parameter.

The [`carrier_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/carrier_clm_window.sas) program creates the following files, assuming a 5 percent AMI extract was run using `bene_id`s and the principal diagnosis only

1. `ami05_carlnits`: Data set us unique at the carrier line item level - each index event can have several associated claims, a single claim can have several associated line items. The data set pulls line items associated with the index events in the file `ami05_indx`. Line items one year after and one year before the admission date of the index event are found in this file. Note that collapsing to the claim level requires collapsing by `fileyear` and `clm_id`.

### Extracting harmonized outpatient claims and revenue centers

Outpatient claim records provide summary information, including the beneficiary's EHIC or beneficiary ID (`bene_id`), the total amount of reimbursement, relevant ICD-9-CM diagnosis codes, and the start and end dates of the claim. Each claim also includes a series of "revenue center" records, which provide detailed information on each service provided as part of the claim, including the revenue center (i.e. division) of the institution that provided the service, the amount reimbursed for the service.

For years prior to 2002, revenue center data resided directly on the main claim record. In order that each claim could report dozens of services, each claims record contains dozens of copies of each revenue center field, with the result that some years' files contain upwards of a thousand fields. Since most outpatient claims contain only a handful of individual services, the bulk of these revenue center fields are typically empty. Starting in 2002, CMS began splitting the outpatient file into a "claims" file, which contains the summary information for each claim, and a "revenue center" file, which contains one record for each revenue center. Records in the revenue center file contain a unique identifier that facilitates matching the revenue center record to the corresponding claims record. In many instances a revenue center code of `0000` is output which corresponds to an empty record. As the code currently exists, these are kept for consistency, however at a later time we may simply choose to get rid of these empty, observations.

The script [`op_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims/op_clm_window.sas) processes the outpatient files. The script first loads the list of individual identifiers and AMI dates from the file saved by the 1B sas program. Like the other files, it then selects all claims with start dates at most one year before the AMI date and end dates at most one year after the AMI date. The code drops all claims with a missing start or end date, but this restriction appears to affect virtually no outpatient records. At this point, the script tags all selected claims with the `diag_id` for the "AMI episode" of which the claim is a part.

Next, for those years where the revenue center information resides directly on the claims records (i.e. years before 2002), the code takes the revenue center information off of the claims record and instead saves it in a separate revenue center file where each revenue center has its own record. That is, the code reshapes all years' data so that they match the basic format of the post-2002 files. These two files can be merged using the `fileyear` and `claimindex` fields as a (compound) unique identifier. The amount the provider charged is taken from the revenue centers and saved in the extract created. In cases where a revenue center code for the total charge exists(`0001`), the associated charge is simply added to those found on the claims files. In the case where a `0001` code does not exist, the charge for each revenue center code are summed together. On the other hand, the total amount which Medicare paid for each service is located in a variable which includes the amount reimbursed for all services on a claim (including any revenue center ). These total charge and payment amounts are kept on the extract created.

The extracts do not create costs/reimbursement variables from the revenue center levels despite the fact that this more granular level costs are available. Again, the costs found in the claims files due however account for all costs found in the revenue center level.

There are several year-specific complications that arise in generating these files. First, for 1999-2001, a single claim can stretch across multiple records if the total number of revenue center records in the claim exceeds the number of available revenue center fields in a single record. Thus, throughout, the code makes special provision for handling these records[^32]. Finally, as with the other files, variable names and formats change from year to year. The SAS macro contained in [`ConformOp.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformOp.sas) handles these differences.

[^32]: Keeping together claims that stretch across multiple records requires a unique claim identifier. The ResDAC website suggests that the fields `daily_dt` and `link_num` together form a unique claim identifier in the 1999-2001 outpatient records. Examining the data file suggests, however, that this is not actually the case. In place of these fields, the code uses the “claim control number” as a unique identifier. This field uniquely identifies claims, but also takes on a common value for all segments of the same claim.

As with the Carrier file, processing the outpatient files takes a significant amount of time. For this reason, the outpatient code, like the Carrier code, saves data at various intermediate stages. These intermediate save points often allow the script to be started mid-way through after a crash. The code is able to start at any midyear crash point, by simply adding the year to restart the run to the parameter `crashStart`. That will cause the program to restart the year you indicate in `crashStart` and then merge all of the results together from the original start and end years ( identified by the yearin and yearout parameters).

The op_clm_window.sas program creates the following files, assuming a 5 percent AMI extract was run using `bene_id`s and the principal diagnosis only:

1. `ami05_opclms`: Data set is unique at the outpatient claim level. The data set pulls OP claims associated with the index events in the file `ami05_indx`. Claims one year after and one year before the admission date of the index event are found in this file.
2. `ami05_oprevcntrs`: Data set us unique at revenue center level — each index event can have several claims, a single claim can have several different revenue centers related to it. The data set pulls revenue centers associated outpatient claims from the above data set (`opcmls`).