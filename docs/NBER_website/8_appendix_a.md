# Appendix A: Files included with this documentation

**[Download all files!](https://www.nber.org/medicare/public/MedicareNBER.zip)**

Note that all output data sets have the following sub-portions:

```
[DIAGNOSIS][PCT]_[FILE IDENTIFIER]
```

For example: `[ami][05]_[indx]`

## Programs to Create Extracts from Raw Data

### SAS program to define directory macros used to define libraries (directory: `~/`)

| | |
|-|-|
| [`set_up_directory.sas`](https://www.nber.org/medicare/public/unzipped/set_up_directory.sas) | File which defines locations of libraries by saving them in macro variables. Allows you to control all directories from single file. |
| [`set_up_directory.do`](https://www.nber.org/medicare/public/unzipped/set_up_directory.do) | File which defines locations of directories used in Stata. Allows control of all directories from single file. |

### Core SAS extraction scripts (directory: `1cohort_extraction/`)

#### `1A: Flag Candidate Index Events`

| | |
|-|-|
| [`medpar_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/medpar_candidates.sas) | Tag potential index events based on ICD9-CM diagnostic and/or procedure codes |
| [`ip_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/ip_candidates.sas) | Tag potential index events based on ICD9-CM diagnostic and/or procedure codes |
| [`op_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/op_candidates.sas) | Tag potential index events based on HCPCS codes and/or ICD9-CM diagnostic and/or procedure codes |
| [`carrier_candidates.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1A_flag_candidate_evnt/carrier_candidates.sas) | Tag potential index events based on HCPCS codes |

#### `1B: Impose Denominator Restrictions`

| | |
|-|-|
| [`1B_impose_restrictions.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1B_impose_restrictions.sas) | Impose enrollment restrictions from denominator, generating final list of index events. |

#### `1C: Final Claim Extraction`


| | |
|-|-|
| [`medpar_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims/medpar_clm_window.sas) | Extracts the MedPAR claims corresponding to each AMI episode defined in 1B. |
| [`carrier_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims/carrier_clm_window.sas) | Extracts the Carrier claims corresponding to each AMI episode defined in 1B. Data set is at the line items level. |
| [`ip_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims/ip_clm_window.sas) | Extracts the Inpatient claims and revenue centers corresponding to each AMI episode defined in 1B. |
| [`op_clm_window.sas`](https://www.nber.org/medicare/public/unzipped/1cohort_extraction/1C_pull_claims/op_clm_window.sas) | Extracts the Outpatient claims and revenue centers corresponding to each AMI episode defined in 1B. |


#### 0PreProcess Macros - already generated for NBER users (directory: `0PreProcess`)

|                                     |                                                                                                                                                                                                                                                              |
|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`CW_create.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/genxwfiles/CW_create.sas)                       | Script formats and copies the crosswalk to a local directory. Creates indexes which are useful in speeding the merges. Provided for reference only                                                                                                           |
| [`CreatePopDenominatorFile.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/genxwfiles/CreatePopDenominatorFile.sas)        | Script formats the enrollment files into a wide format for the population. In addition creates a bene_id to Dartmouth Atlas HRR crosswalk by year. Provided for reference only                                                                               |
| [`MasterHRRCross.do`](https://www.nber.org/medicare/public/unzipped/0pre_process/genxwfiles/MasterHRRCross.do)                   | Script formats and copies the Dartmouth Atlas crosswalk and converts them into a Stata and SAS data sets. Program should be run on a server running both sas and Stata since it call a sas script to import the data set to sas. Provided for reference only |
| [`importPOS.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/genxwfiles/importPOS.sas)                       | Script imports raw POS files into SAS. Provided for reference only                                                                                                                                                                                           |
| [`FixYearDifferencesBetweenMedpar.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/genxwfiles/FixYearDifferencesBetweenMedpar.sas) | Take the imported SAS scripts and apply a series of edits based on the MedPAR file to ensure that years found in the MedPAR file are also found in the POS file. Also attaches the HRR to the POS info. Provided for reference only.                         |


#### Utility Macros (directory: `SASmacros`)

|                        |                                                                                                                                       |
|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [`UtilityMacros.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/UtilityMacros.sas)      | Script containing various small macros used by the Core SAS scripts                                                                   |
| [`DetermineMax.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/DetermineMax.sas)       | Macro which counts the number of files in a given directory, for use to loop through the different file parts                         |
| [`archiveoldLogfiles.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/archiveoldLogfiles.sas) | Macro which generate folder with same name of program found within and copies lst and log files to folder and tags with date and time |

#### Other macros which 1B_impose_restrictions.sas Calls(directory: `SASmacros`)

|                        |                                                                                                                   |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------|
| [`Labels.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/Labels.sas)             | Script which holds the variable label names                                                                       |
| [`FlagTransfers.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/FlagTransfers.sas)      | Macro used to flag different transfer scenarios which are discussed in Section 2 2.7↑ [REMOVED FROM LONG EXTRACT] |
| [`generateEnrollRest.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/generateEnrollRest.sas) | Used to create flags corresponding to the enrollment decision.                                                    |

#### Decompress Macros (directory: `SASmacros`)

|                      |                                                  |
|:---------------------|:-------------------------------------------------|
| [`decompressDenom.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/decompressDenom.sas)  | SAS program which decompresses denominator files |
| [`decompressEnroll.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/decompressEnroll.sas) | SAS program which decompresses denominator files |
| [`decompressMedPar.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/decompressMedPar.sas) | SAS program which decompresses denominator files |

#### Cross-year Conversion Macros (directory: `SASmacros`)

|                      |                                                                                         |
|:---------------------|:----------------------------------------------------------------------------------------|
| [`CreateXWmacro.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/CreateXWmacro.sas)    | SAS macros which read xw SAS files and generate macro variables with variables          |
| [`ImportVariableXW.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ImportVariableXW.sas) | Import XW text files into a SAS dataset                                                 |
| [`applycrosswalk.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/applycrosswalk.sas)   | Macro which LongExtract.sas uses to correctly merge in the crosswalk with the raw data. |
| [`ConformDenom.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformDenom.sas)     | Contains SAS macro to convert denominator files to common format                        |
| [`ConformMedPAR.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformMedPAR.sas)    | Contains SAS macro to convert MedPAR files to common format                             |
| [`ConformOp.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformOp.sas)        | Extracts the outpatient claims corresponding to each AMI episode                        |
| [`ConformCarrier.sas`](https://www.nber.org/medicare/public/unzipped/SASmacros/ConformCarrier.sas)   | Contains SAS macro to convert Carrier files to common format                            |

#### Data dictionary files (directory: `claim_xw`)

|               |                                                                                            |
|:--------------|:-------------------------------------------------------------------------------------------|
| [`opxw.txt`](https://www.nber.org/medicare/public/unzipped/claim_xw/opxw.txt)      | Crosswalk files with variable name changes called by sas programs to create new variables. |
| [`medparxw.txt`](https://www.nber.org/medicare/public/unzipped/claim_xw/medparxw.txt)  | Crosswalk files with variable name changes called by sas programs to create new variables. |
| [`carrierxw.txt`](https://www.nber.org/medicare/public/unzipped/claim_xw/carrierxw.txt) | Crosswalk files with variable name changes called by sas programs to create new variables. |


### Manipulate Extracts Programs

#### Create Procedure measures (directory: `2create_index_level_measures/xday_flag_procedures`)

|                      |                                                  |
|:---------------------|:-------------------------------------------------|
| [`Step1_tagProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step1_tagProcs.sas)   | Tags procedures in MedPAR, OP and Carrier        |
| [`Step2_matchProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step2_matchProcs.sas) | Matches the carrier with the institutional files |


#### Create comorbidity measure (directory: `2create_index_level_measures /Comorbidity`)

|                          |                                                                |
|:-------------------------|:---------------------------------------------------------------|
| [`ExtComorbidCC.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/last_yr_comorbid/ExtComorbidCC.sas)        | Applies CC to diagnosis in MedPAR.                             |
| [`2010_ICD_9_Crosswalk.txt`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/last_yr_comorbid/2010_ICD_9_Crosswalk.txt) | cross-walk from ICD-9-CM codes to CC codes Create cost measure |

#### Create cost measure (directory: `2create_index_level_measures/xday_costs_raw`)

|                            |                                                              |
|:---------------------------|:-------------------------------------------------------------|
| [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) | Sums costs from the MedPAR, Carrier and OP files. Unadjusted |

#### Create cost utilization measure (directory: `2create_index_level_measures/costutilization`)

|                                        |                                                                                                                                                                     |
|:---------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`2A_CallAllCostUtilizationPrgms.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/2A_CallAllCostUtilizationPrgms.sas)     | Program runs a series of sub-programs (similar to a wrapper program) which generates cost utilization measures (cost measure without policy/geographic adjustments) |
| [`2B_GenerateIndxLevelsCostUtilStats.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/2B_GenerateIndxLevelsCostUtilStats.sas) | Program takes the cost utilization measures and creates X day costs upto the index event level                                                                      |

### Programs no longer used or upkept (maybe useful to someone)

#### Basic Tabulations (directory: `Auxiliary/StataAnalysis`)

|                                  |                                                                                                |
|:---------------------------------|:-----------------------------------------------------------------------------------------------|
| [`SumStatXML.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/StataAnalysis/SumStatXML.do)                    | Generates a whole host of summary measures, exports to excel (XML)                             |
| [`CostCarrier_XML.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/StataAnalysis/CostCarrier_XML.do)               | Generates costs by day and exports to excel (XML) file-carrier                                 |
| [`CostInSNF_XML.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/StataAnalysis/CostInSNF_XML.do)                 | Generates costs by day and exports to excel(XML) file-MedPAR                                   |
| [`CostOp_XML.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/StataAnalysis/CostOp_XML.do)                    | Generates costs by day and exports to excel(XML) file-OP                                       |
| [`CostOp_XML.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/StataAnalysis/CostOp_XML.do)                    | Generates simple tabulations of inpatient/SNF costs and survival rates                         |
| MedicareStateCrosswalk.([dta][MedicareStateCrosswalk_dta]|[csv][MedicareStateCrosswalk_csv]) | Data providing cross-walk from Medicare state codes listed on ResDAC website to Census regions |

[MedicareStateCrosswalk_dta]: https://www.nber.org/medicare/public/unzipped/Auxiliary/MedicareStateCrosswalk.dta
[MedicareStateCrosswalk_csv]: https://www.nber.org/medicare/public/unzipped/Auxiliary/MedicareStateCrosswalk.csv


#### SAS-to-Stata Conversion Scripts- XPORT file only (directory: `Auxiliary/SAS_XPORT`)

|                    |                                                                                        |
|:-------------------|:---------------------------------------------------------------------------------------|
| [`CoreXptToDta.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/SAS_XPORT/CoreXptToDta.do)    | Converts the MedPAR extract, the sample file, and the demographic file, to Stat format |
| [`CarrierXptToDta.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/SAS_XPORT/CarrierXptToDta.do) | Converts the Carrier extract to Stata format                                           |
| [`OpXptToDta.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/attic/SAS_XPORT/OpXptToDta.do)      | Converts the outpatient extract to Stata format                                        |

(For use only if Stat/Transfer is not available, not recommended)

### Using Stat-transfer

There are two possible ways to transfer the data out of SAS. One possibility is
to use a SAS XPORT file. These files are reliable and work as long as you have
access to SAS and Stata, although they require several steps. First each SAS
script writes the extract it generates to a SAS XPT file, which Stata can read
using the fdause command. However this approach can only handle field names of
eight characters or less. To address this problem, the SAS code shortens field
names before writing them to XPT, and the Stata code returns them to their
original form after reading the XPT file. The Stata scripts `MedParXptToDta.do`,
`CarXptToDta.do`, and `OpXptToDta.do` handle the needed renaming for the MedPAR,
Carrier, and outpatient extracts, respectively. The XPT files are not used as a
default because they require extra step and create redundant files.

The other option is to use Stat-Transfer, which of course requires access to
Stat-Transfer but means that the redundant files and extra steps can be avoided.
However, due to the versions of Stat Transfer available on different servers,
when working with files larger then 3G Stat Transfer only works on the AGE1 and
AGE3 machines. In some cases the code in the SAS files which does this have been
commented out, however it is straightforward to implement from the Unix command
prompt. The Stat/Transfer documentation can be found [here](ftp://ftp.stattransfer.com/unixman.pdf).

Stat transfer is currently used as the default, however you should think
about how and where you will be implementing the program before making
your final decision.
