# Beneficiary Summary File

??? note "Source"
    [https://www.resdac.org/cms-data/files/mbsf](https://www.resdac.org/cms-data/files/mbsf)

## Overview

The Master Beneficiary Summary File includes several segments.

### Base (A/B/C/D) segment
This segment includes beneficiary enrollment information, such as the beneficiary unique identifier, state and county codes, zip code, date of birth, date of death, sex, race, age, monthly entitlement and enrollment information (A/B/C/D) and plan information for Medicare Advantage (Part C) and the Prescription Drug Program (Part D). Part C and Part D enrollment information is available beginning with the 2006 file year.

### Chronic Conditions segment
This segment includes 27 chronic condition data warehouse flags called CCW Flags. This includes 6 new chronic conditions in addition to the 21 chronic conditions previously defined. For more information about the CCW Flags, please see the [CCW User Guide](https://www.ccwdata.org/web/guest/user-documentation).

### Other Chronic or Potentially Disabling Conditions segment
The Other Chronic or Potentially Disabling Conditions segment of the MBSF contains 9 mental health and tobacco use conditions, 15 developmental disorder and disability-related conditions, and 9 other chronic physical and behavioral health conditions which were developed by CMS specifically to enhance research of the Medicare-Medicaid dually enrolled population.

### Cost & Use segment
This segment includes summarized information about the service utilization and Medicare payment amounts by file type.

### National Death Index (NDI) segment
This segment includes the National Death Index cause of death information. This is available for all Medicare beneficiaries from 1999-2008 and for Medicaid recipients from 1999-2007.  There are no plans to update the NDI segment.

## Availability


### Base (A/B/C/D) Segment

Availability:  CY 1999 - 2016

The Part D variables in the Base segment are available for years 2006 and forward only.

### Chronic Conditions Segment

Availability:  CY 1999 - 2016

### Other Chronic or Potentially Disabling Conditions Segment

Availability:  CY 1999 - 2016

### Cost and Use Segment

Availability:  CY 1999 - 2016

The mid-year Cost and Use segment, which is available in the Fall, will not include Part D claims information.

### National Death Index Segment

Availability:  CY 1999 - 2008

This is available for all Medicare beneficiaries from 1999-2008 and for Medicaid recipients from 1999-2007.

## Data Documentation

### Base (A/B/C/D) segment

|   Index | SAS Name                | Variable Name                                                                                                         | Limitation   | Code Table   |
|--------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`               | [Encrypted CCW Beneficiary ID](variables/mbsf.md#encrypted-ccw-beneficiary-id)                                        |              |              |
|       2 | `RFRNC_YR`              | [Reference Year](variables/mbsf.md#reference-year)                                                                    |              |              |
|       3 | `ENRL_SRC`              | [Source of enrollment data](variables/mbsf.md#source-of-enrollment-data)                                              |              | *            |
|       4 | `SAMPLE_GROUP`          | [Medicare Sample Group Indicator](variables/mbsf.md#medicare-sample-group-indicator)                                  |              | *            |
|       5 | `EFIVEPCT`              | [Enhanced Medicare 5% Sample Indicator](variables/mbsf.md#enhanced-medicare-5-sample-indicator)                       |              | *            |
|       6 | `CRNT_BIC`              | [Current Beneficiary Identification Code](variables/mbsf.md#current-beneficiary-identification-code)                  |              | *            |
|       7 | `STATE_CD`              | [State code for beneficiary (SSA code)](variables/mbsf.md#state-code-for-beneficiary-ssa-code)                        |              | *            |
|       8 | `CNTY_CD`               | [County Code for Beneficiary (SSA code)](variables/mbsf.md#county-code-for-beneficiary-ssa-code)                      |              | *            |
|       9 | `ZIP_CD`                | [5-digit ZIP code for beneficiary](variables/mbsf.md#5-digit-zip-code-for-beneficiary)                                |              | *            |
|      10 | `STATE_CNTY_FIPS_CD_01` | [State and county FIPS code - January](variables/mbsf.md#state-and-county-fips-code-january)                          |              | *            |
|      11 | `STATE_CNTY_FIPS_CD_02` | [State and county FIPS code - February](variables/mbsf.md#state-and-county-fips-code-february)                        |              | *            |
|      12 | `STATE_CNTY_FIPS_CD_03` | [State and county FIPS code - March](variables/mbsf.md#state-and-county-fips-code-march)                              |              | *            |
|      13 | `STATE_CNTY_FIPS_CD_04` | [State and county FIPS code - April](variables/mbsf.md#state-and-county-fips-code-april)                              |              | *            |
|      14 | `STATE_CNTY_FIPS_CD_05` | [State and county FIPS code - May](variables/mbsf.md#state-and-county-fips-code-may)                                  |              | *            |
|      15 | `STATE_CNTY_FIPS_CD_06` | [State and county FIPS code - June](variables/mbsf.md#state-and-county-fips-code-june)                                |              | *            |
|      16 | `STATE_CNTY_FIPS_CD_07` | [State and county FIPS code - July](variables/mbsf.md#state-and-county-fips-code-july)                                |              | *            |
|      17 | `STATE_CNTY_FIPS_CD_08` | [State and county FIPS code - August](variables/mbsf.md#state-and-county-fips-code-august)                            |              | *            |
|      18 | `STATE_CNTY_FIPS_CD_09` | [State and county FIPS code - September](variables/mbsf.md#state-and-county-fips-code-september)                      |              | *            |
|      19 | `STATE_CNTY_FIPS_CD_10` | [State and county FIPS code - October](variables/mbsf.md#state-and-county-fips-code-october)                          |              | *            |
|      20 | `STATE_CNTY_FIPS_CD_11` | [State and county FIPS code - November](variables/mbsf.md#state-and-county-fips-code-november)                        |              | *            |
|      21 | `STATE_CNTY_FIPS_CD_12` | [State and county FIPS code - December](variables/mbsf.md#state-and-county-fips-code-december)                        |              | *            |
|      22 | `AGE`                   | [Age of beneficiary at end of year](variables/mbsf.md#age-of-beneficiary-at-end-of-year)                              |              | *            |
|      23 | `BENE_DOB`              | [Beneficiary date of birth](variables/mbsf.md#beneficiary-date-of-birth)                                              |              | *            |
|      24 | `V_DOD_SW`              | [Valid Date of Death Switch](variables/mbsf.md#valid-date-of-death-switch)                                            |              | *            |
|      25 | `DEATH_DT`              | [Date of Death](variables/mbsf.md#date-of-death)                                                                      |              | *            |
|      26 | `SEX`                   | [Sex](variables/mbsf.md#sex)                                                                                          |              | *            |
|      27 | `RACE`                  | [Beneficiary Race Code](variables/mbsf.md#beneficiary-race-code)                                                      |              | *            |
|      28 | `RTI_RACE_CD`           | [Research Triangle Institute (RTI) Race Code](variables/mbsf.md#research-triangle-institute-rti-race-code)            |              | *            |
|      29 | `COVSTART`              | [Medicare Coverage Start Date](variables/mbsf.md#medicare-coverage-start-date)                                        |              | *            |
|      30 | `OREC`                  | [Original Reason for Entitlement Code](variables/mbsf.md#original-reason-for-entitlement-code)                        |              | *            |
|      31 | `CREC`                  | [Current Reason for Entitlement Code](variables/mbsf.md#current-reason-for-entitlement-code)                          |              | *            |
|      32 | `ESRD_IND`              | [End-stage Renal Disease (ESRD) Indicator](variables/mbsf.md#end-stage-renal-disease-esrd-indicator)                  |              | *            |
|      33 | `MDCR_STUS_CD_01`       | [Medicare Status Code - January](variables/mbsf.md#medicare-status-code-january)                                      |              | *            |
|      34 | `MDCR_STUS_CD_02`       | [Medicare Status Code - February](variables/mbsf.md#medicare-status-code-february)                                    |              | *            |
|      35 | `MDCR_STUS_CD_03`       | [Medicare Status Code - March](variables/mbsf.md#medicare-status-code-march)                                          |              | *            |
|      36 | `MDCR_STUS_CD_04`       | [Medicare Status Code - April](variables/mbsf.md#medicare-status-code-april)                                          |              | *            |
|      37 | `MDCR_STUS_CD_05`       | [Medicare Status Code - May](variables/mbsf.md#medicare-status-code-may)                                              |              | *            |
|      38 | `MDCR_STUS_CD_06`       | [Medicare Status Code - June](variables/mbsf.md#medicare-status-code-june)                                            |              | *            |
|      39 | `MDCR_STUS_CD_07`       | [Medicare Status Code - July](variables/mbsf.md#medicare-status-code-july)                                            |              | *            |
|      40 | `MDCR_STUS_CD_08`       | [Medicare Status Code - August](variables/mbsf.md#medicare-status-code-august)                                        |              | *            |
|      41 | `MDCR_STUS_CD_09`       | [Medicare Status Code - September](variables/mbsf.md#medicare-status-code-september)                                  |              | *            |
|      42 | `MDCR_STUS_CD_10`       | [Medicare Status Code - October](variables/mbsf.md#medicare-status-code-october)                                      |              | *            |
|      43 | `MDCR_STUS_CD_11`       | [Medicare Status Code - November](variables/mbsf.md#medicare-status-code-november)                                    |              | *            |
|      44 | `MDCR_STUS_CD_12`       | [Medicare Status Code - December](variables/mbsf.md#medicare-status-code-december)                                    |              | *            |
|      45 | `A_TRM_CD`              | [Part A Termination Code](variables/mbsf.md#part-a-termination-code)                                                  |              | *            |
|      46 | `B_TRM_CD`              | [Part B Termination Code](variables/mbsf.md#part-b-termination-code)                                                  |              | *            |
|      47 | `A_MO_CNT`              | [Part A Months Count](variables/mbsf.md#part-a-months-count)                                                          |              | *            |
|      48 | `B_MO_CNT`              | [Part B Months Count](variables/mbsf.md#part-b-months-count)                                                          |              | *            |
|      49 | `BUYIN_MO`              | [State Buy-In Coverage Count](variables/mbsf.md#state-buy-in-coverage-count)                                          |              | *            |
|      50 | `HMO_MO`                | [HMO Coverage Count](variables/mbsf.md#hmo-coverage-count)                                                            |              | *            |
|      51 | `PTD_MO`                | [Months of Part D Coverage](variables/mbsf.md#months-of-part-d-coverage)                                              |              | *            |
|      52 | `RDS_MO`                | [Months of Retiree Drug Subsidy Coverage](variables/mbsf.md#months-of-retiree-drug-subsidy-coverage)                  |              | *            |
|      53 | `DUAL_MO`               | [Months of Dual Eligibility](variables/mbsf.md#months-of-dual-eligibility)                                            |              | *            |
|      54 | `BUYIN01`               | [Medicare Entitlement/Buy-In Indicator - January](variables/mbsf.md#medicare-entitlementbuy-in-indicator-january)     |              | *            |
|      55 | `BUYIN02`               | [Medicare Entitlement/Buy-In Indicator - February](variables/mbsf.md#medicare-entitlementbuy-in-indicator-february)   |              | *            |
|      56 | `BUYIN03`               | [Medicare Entitlement/Buy-In Indicator - March](variables/mbsf.md#medicare-entitlementbuy-in-indicator-march)         |              | *            |
|      57 | `BUYIN04`               | [Medicare Entitlement/Buy-In Indicator - April](variables/mbsf.md#medicare-entitlementbuy-in-indicator-april)         |              | *            |
|      58 | `BUYIN05`               | [Medicare Entitlement/Buy-In Indicator - May](variables/mbsf.md#medicare-entitlementbuy-in-indicator-may)             |              | *            |
|      59 | `BUYIN06`               | [Medicare Entitlement/Buy-In Indicator - June](variables/mbsf.md#medicare-entitlementbuy-in-indicator-june)           |              | *            |
|      60 | `BUYIN07`               | [Medicare Entitlement/Buy-In Indicator - July](variables/mbsf.md#medicare-entitlementbuy-in-indicator-july)           |              | *            |
|      61 | `BUYIN08`               | [Medicare Entitlement/Buy-In Indicator - August](variables/mbsf.md#medicare-entitlementbuy-in-indicator-august)       |              | *            |
|      62 | `BUYIN09`               | [Medicare Entitlement/Buy-In Indicator - September](variables/mbsf.md#medicare-entitlementbuy-in-indicator-september) |              | *            |
|      63 | `BUYIN10`               | [Medicare Entitlement/Buy-In Indicator - October](variables/mbsf.md#medicare-entitlementbuy-in-indicator-october)     |              | *            |
|      64 | `BUYIN11`               | [Medicare Entitlement/Buy-In Indicator - November](variables/mbsf.md#medicare-entitlementbuy-in-indicator-november)   |              | *            |
|      65 | `BUYIN12`               | [Medicare Entitlement/Buy-In Indicator - December](variables/mbsf.md#medicare-entitlementbuy-in-indicator-december)   |              | *            |
|      66 | `HMOIND01`              | [HMO Indicator - January](variables/mbsf.md#hmo-indicator-january)                                                    |              | *            |
|      67 | `HMOIND02`              | [HMO Indicator - February](variables/mbsf.md#hmo-indicator-february)                                                  |              | *            |
|      68 | `HMOIND03`              | [HMO Indicator - March](variables/mbsf.md#hmo-indicator-march)                                                        |              | *            |
|      69 | `HMOIND04`              | [HMO Indicator - April](variables/mbsf.md#hmo-indicator-april)                                                        |              | *            |
|      70 | `HMOIND05`              | [HMO Indicator - May](variables/mbsf.md#hmo-indicator-may)                                                            |              | *            |
|      71 | `HMOIND06`              | [HMO Indicator - June](variables/mbsf.md#hmo-indicator-june)                                                          |              | *            |
|      72 | `HMOIND07`              | [HMO Indicator - July](variables/mbsf.md#hmo-indicator-july)                                                          |              | *            |
|      73 | `HMOIND08`              | [HMO Indicator - August](variables/mbsf.md#hmo-indicator-august)                                                      |              | *            |
|      74 | `HMOIND09`              | [HMO Indicator - September](variables/mbsf.md#hmo-indicator-september)                                                |              | *            |
|      75 | `HMOIND10`              | [HMO Indicator - October](variables/mbsf.md#hmo-indicator-october)                                                    |              | *            |
|      76 | `HMOIND11`              | [HMO Indicator - November](variables/mbsf.md#hmo-indicator-november)                                                  |              | *            |
|      77 | `HMOIND12`              | [HMO Indicator - December](variables/mbsf.md#hmo-indicator-december)                                                  |              | *            |

### Part C

|   Index | SAS Name              | Variable Name                                                                            | Limitation   | Code Table   |
|--------:|:----------------------|:-----------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `PTC_CNTRCT_ID_01`    | [Part C Contract Number - January](variables/mbsf.md#part-c-contract-number-january)     |              |              |
|       2 | `PTC_CNTRCT_ID_02`    | [Part C Contract Number - February](variables/mbsf.md#part-c-contract-number-february)   |              |              |
|       3 | `PTC_CNTRCT_ID_03`    | [Part C Contract Number - March](variables/mbsf.md#part-c-contract-number-march)         |              |              |
|       4 | `PTC_CNTRCT_ID_04`    | [Part C Contract Number - April](variables/mbsf.md#part-c-contract-number-april)         |              |              |
|       5 | `PTC_CNTRCT_ID_05`    | [Part C Contract Number - May](variables/mbsf.md#part-c-contract-number-may)             |              |              |
|       6 | `PTC_CNTRCT_ID_06`    | [Part C Contract Number - June](variables/mbsf.md#part-c-contract-number-june)           |              |              |
|       7 | `PTC_CNTRCT_ID_07`    | [Part C Contract Number - July](variables/mbsf.md#part-c-contract-number-july)           |              |              |
|       8 | `PTC_CNTRCT_ID_08`    | [Part C Contract Number - August](variables/mbsf.md#part-c-contract-number-august)       |              |              |
|       9 | `PTC_CNTRCT_ID_09`    | [Part C Contract Number - September](variables/mbsf.md#part-c-contract-number-september) |              |              |
|      10 | `PTC_CNTRCT_ID_10`    | [Part C Contract Number - October](variables/mbsf.md#part-c-contract-number-october)     |              |              |
|      11 | `PTC_CNTRCT_ID_11`    | [Part C Contract Number - November](variables/mbsf.md#part-c-contract-number-november)   |              |              |
|      12 | `PTC_CNTRCT_ID_12`    | [Part C Contract Number - December](variables/mbsf.md#part-c-contract-number-december)   |              |              |
|      13 | `PTC_PBP_ID_01`       | [Part C PBP Number - January](variables/mbsf.md#part-c-pbp-number-january)               |              | *            |
|      14 | `PTC_PBP_ID_02`       | [Part C PBP Number - February](variables/mbsf.md#part-c-pbp-number-february)             |              | *            |
|      15 | `PTC_PBP_ID_03`       | [Part C PBP Number - March](variables/mbsf.md#part-c-pbp-number-march)                   |              | *            |
|      16 | `PTC_PBP_ID_04`       | [Part C PBP Number - April](variables/mbsf.md#part-c-pbp-number-april)                   |              | *            |
|      17 | `PTC_PBP_ID_05`       | [Part C PBP Number - May](variables/mbsf.md#part-c-pbp-number-may)                       |              | *            |
|      18 | `PTC_PBP_ID_06`       | [Part C PBP Number - June](variables/mbsf.md#part-c-pbp-number-june)                     |              | *            |
|      19 | `PTC_PBP_ID_07`       | [Part C PBP Number - July](variables/mbsf.md#part-c-pbp-number-july)                     |              | *            |
|      20 | `PTC_PBP_ID_08`       | [Part C PBP Number - August](variables/mbsf.md#part-c-pbp-number-august)                 |              | *            |
|      21 | `PTC_PBP_ID_09`       | [Part C PBP Number - September](variables/mbsf.md#part-c-pbp-number-september)           |              | *            |
|      22 | `PTC_PBP_ID_10`       | [Part C PBP Number - October](variables/mbsf.md#part-c-pbp-number-october)               |              | *            |
|      23 | `PTC_PBP_ID_11`       | [Part C PBP Number - November](variables/mbsf.md#part-c-pbp-number-november)             |              | *            |
|      24 | `PTC_PBP_ID_12`       | [Part C PBP Number - December](variables/mbsf.md#part-c-pbp-number-december)             |              | *            |
|      25 | `PTC_PLAN_TYPE_CD_01` | [Part C Plan Type Code - January](variables/mbsf.md#part-c-plan-type-code-january)       |              | *            |
|      26 | `PTC_PLAN_TYPE_CD_02` | [Part C Plan Type Code - February](variables/mbsf.md#part-c-plan-type-code-february)     |              | *            |
|      27 | `PTC_PLAN_TYPE_CD_03` | [Part C Plan Type Code - March](variables/mbsf.md#part-c-plan-type-code-march)           |              | *            |
|      28 | `PTC_PLAN_TYPE_CD_04` | [Part C Plan Type Code - April](variables/mbsf.md#part-c-plan-type-code-april)           |              | *            |
|      29 | `PTC_PLAN_TYPE_CD_05` | [Part C Plan Type Code - May](variables/mbsf.md#part-c-plan-type-code-may)               |              | *            |
|      30 | `PTC_PLAN_TYPE_CD_06` | [Part C Plan Type Code - June](variables/mbsf.md#part-c-plan-type-code-june)             |              | *            |
|      31 | `PTC_PLAN_TYPE_CD_07` | [Part C Plan Type Code - July](variables/mbsf.md#part-c-plan-type-code-july)             |              | *            |
|      32 | `PTC_PLAN_TYPE_CD_08` | [Part C Plan Type Code - August](variables/mbsf.md#part-c-plan-type-code-august)         |              | *            |
|      33 | `PTC_PLAN_TYPE_CD_09` | [Part C Plan Type Code - September](variables/mbsf.md#part-c-plan-type-code-september)   |              | *            |
|      34 | `PTC_PLAN_TYPE_CD_10` | [Part C Plan Type Code - October](variables/mbsf.md#part-c-plan-type-code-october)       |              | *            |
|      35 | `PTC_PLAN_TYPE_CD_11` | [Part C Plan Type Code - November](variables/mbsf.md#part-c-plan-type-code-november)     |              | *            |
|      36 | `PTC_PLAN_TYPE_CD_12` | [Part C Plan Type Code - December](variables/mbsf.md#part-c-plan-type-code-december)     |              | *            |

### Part D

|   Index | SAS Name      | Variable Name                                                                                                              | Limitation   | Code Table   |
|--------:|:--------------|:---------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `PTDCNTRCT01` | [Part D Contract Number - January](variables/mbsf.md#part-d-contract-number-january)                                       |              | *            |
|       2 | `PTDCNTRCT02` | [Part D Contract Number - February](variables/mbsf.md#part-d-contract-number-february)                                     |              | *            |
|       4 | `PTDCNTRCT04` | [Part D Contract Number - April](variables/mbsf.md#part-d-contract-number-april)                                           |              | *            |
|       5 | `PTDCNTRCT05` | [Part D Contract Number - May](variables/mbsf.md#part-d-contract-number-may)                                               |              | *            |
|       6 | `PTDCNTRCT06` | [Part D Contract Number - June](variables/mbsf.md#part-d-contract-number-june)                                             |              | *            |
|       7 | `PTDCNTRCT07` | [Part D Contract Number - July](variables/mbsf.md#part-d-contract-number-july)                                             |              | *            |
|       8 | `PTDCNTRCT08` | [Part D Contract Number - August](variables/mbsf.md#part-d-contract-number-august)                                         |              | *            |
|       9 | `PTDCNTRCT09` | [Part D Contract Number - September](variables/mbsf.md#part-d-contract-number-september)                                   |              | *            |
|      10 | `PTDCNTRCT10` | [Part D Contract Number - October](variables/mbsf.md#part-d-contract-number-october)                                       |              | *            |
|      11 | `PTDCNTRCT11` | [Part D Contract Number - November](variables/mbsf.md#part-d-contract-number-november)                                     |              | *            |
|      12 | `PTDCNTRCT12` | [Part D Contract Number - December](variables/mbsf.md#part-d-contract-number-december)                                     |              | *            |
|      13 | `PTDPBPID01`  | [Part D PBP Number - January](variables/mbsf.md#part-d-pbp-number-january)                                                 |              | *            |
|      14 | `PTDPBPID02`  | [Part D PBP Number - February](variables/mbsf.md#part-d-pbp-number-february)                                               |              | *            |
|      15 | `PTDPBPID03`  | [Part D PBP Number - March](variables/mbsf.md#part-d-pbp-number-march)                                                     |              | *            |
|      16 | `PTDPBPID04`  | [Part D PBP Number - April](variables/mbsf.md#part-d-pbp-number-april)                                                     |              | *            |
|      17 | `PTDPBPID05`  | [Part D PBP Number - May](variables/mbsf.md#part-d-pbp-number-may)                                                         |              | *            |
|      18 | `PTDPBPID06`  | [Part D PBP Number - June](variables/mbsf.md#part-d-pbp-number-june)                                                       |              | *            |
|      19 | `PTDPBPID07`  | [Part D PBP Number - July](variables/mbsf.md#part-d-pbp-number-july)                                                       |              | *            |
|      20 | `PTDPBPID08`  | [Part D PBP Number - August](variables/mbsf.md#part-d-pbp-number-august)                                                   |              | *            |
|      21 | `PTDPBPID09`  | [Part D PBP Number - September](variables/mbsf.md#part-d-pbp-number-september)                                             |              | *            |
|      22 | `PTDPBPID10`  | [Part D PBP Number - October](variables/mbsf.md#part-d-pbp-number-october)                                                 |              | *            |
|      23 | `PTDPBPID11`  | [Part D PBP Number - November](variables/mbsf.md#part-d-pbp-number-november)                                               |              | *            |
|      24 | `PTDPBPID12`  | [Part D PBP Number - December](variables/mbsf.md#part-d-pbp-number-december)                                               |              | *            |
|      25 | `SGMTID01`    | [Part D Segment Number - January](variables/mbsf.md#part-d-segment-number-january)                                         |              | *            |
|      26 | `SGMTID02`    | [Part D Segment Number - February](variables/mbsf.md#part-d-segment-number-february)                                       |              | *            |
|      27 | `SGMTID03`    | [Part D Segment Number - March](variables/mbsf.md#part-d-segment-number-march)                                             |              | *            |
|      28 | `SGMTID04`    | [Part D Segment Number - April](variables/mbsf.md#part-d-segment-number-april)                                             |              | *            |
|      29 | `SGMTID05`    | [Part D Segment Number - May](variables/mbsf.md#part-d-segment-number-may)                                                 |              | *            |
|      30 | `SGMTID06`    | [Part D Segment Number - June](variables/mbsf.md#part-d-segment-number-june)                                               |              | *            |
|      31 | `SGMTID07`    | [Part D Segment Number - July](variables/mbsf.md#part-d-segment-number-july)                                               |              | *            |
|      32 | `SGMTID08`    | [Part D Segment Number - August](variables/mbsf.md#part-d-segment-number-august)                                           |              | *            |
|      33 | `SGMTID09`    | [Part D Segment Number - September](variables/mbsf.md#part-d-segment-number-september)                                     |              | *            |
|      34 | `SGMTID10`    | [Part D Segment Number - October](variables/mbsf.md#part-d-segment-number-october)                                         |              | *            |
|      35 | `SGMTID11`    | [Part D Segment Number - November](variables/mbsf.md#part-d-segment-number-november)                                       |              | *            |
|      36 | `SGMTID12`    | [Part D Segment Number - December](variables/mbsf.md#part-d-segment-number-december)                                       |              | *            |
|      37 | `RDSIND01`    | [Part D Retiree Drug Subsidy Indicator - January](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-january)         |              | *            |
|      38 | `RDSIND02`    | [Part D Retiree Drug Subsidy Indicator - February](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-february)       |              | *            |
|      39 | `RDSIND03`    | [Part D Retiree Drug Subsidy Indicator - March](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-march)             |              | *            |
|      40 | `RDSIND04`    | [Part D Retiree Drug Subsidy Indicator - April](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-april)             |              | *            |
|      41 | `RDSIND05`    | [Part D Retiree Drug Subsidy Indicator - May](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-may)                 |              | *            |
|      42 | `RDSIND06`    | [Part D Retiree Drug Subsidy Indicator - June](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-june)               |              | *            |
|      43 | `RDSIND07`    | [Part D Retiree Drug Subsidy Indicator - July](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-july)               |              | *            |
|      44 | `RDSIND08`    | [Part D Retiree Drug Subsidy Indicator - August](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-august)           |              | *            |
|      45 | `RDSIND09`    | [Part D Retiree Drug Subsidy Indicator - September](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-september)     |              | *            |
|      46 | `RDSIND10`    | [Part D Retiree Drug Subsidy Indicator - October](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-october)         |              | *            |
|      47 | `RDSIND11`    | [Part D Retiree Drug Subsidy Indicator - November](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-november)       |              | *            |
|      48 | `RDSIND12`    | [Part D Retiree Drug Subsidy Indicator - December](variables/mbsf.md#part-d-retiree-drug-subsidy-indicator-december)       |              | *            |
|      49 | `DUAL_01`     | [Medicare-Medicaid dual eligibility code - January](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-january)     |              | *            |
|      50 | `DUAL_02`     | [Medicare-Medicaid dual eligibility code - February](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-february)   |              | *            |
|      51 | `DUAL_03`     | [Medicare-Medicaid dual eligibility code - March](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-march)         |              | *            |
|      52 | `DUAL_04`     | [Medicare-Medicaid dual eligibility code - April](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-april)         |              | *            |
|      53 | `DUAL_05`     | [Medicare-Medicaid dual eligibility code - May](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-may)             |              | *            |
|      54 | `DUAL_06`     | [Medicare-Medicaid dual eligibility code - June](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-june)           |              | *            |
|      55 | `DUAL_07`     | [Medicare-Medicaid dual eligibility code - July](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-july)           |              | *            |
|      56 | `DUAL_08`     | [Medicare-Medicaid dual eligibility code - August](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-august)       |              | *            |
|      57 | `DUAL_09`     | [Medicare-Medicaid dual eligibility code - September](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-september) |              | *            |
|      58 | `DUAL_10`     | [Medicare-Medicaid dual eligibility code - October](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-october)     |              | *            |
|      59 | `DUAL_11`     | [Medicare-Medicaid dual eligibility code - November](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-november)   |              | *            |
|      60 | `DUAL_12`     | [Medicare-Medicaid dual eligibility code - December](variables/mbsf.md#medicare-medicaid-dual-eligibility-code-december)   |              | *            |
|      61 | `CSTSHR01`    | [Part D low-income cost share group code - January](variables/mbsf.md#part-d-low-income-cost-share-group-code-january)     |              | *            |
|      62 | `CSTSHR02`    | [Part D low-income cost share group code - February](variables/mbsf.md#part-d-low-income-cost-share-group-code-february)   |              | *            |
|      63 | `CSTSHR03`    | [Part D low-income cost share group code - March](variables/mbsf.md#part-d-low-income-cost-share-group-code-march)         |              | *            |
|      64 | `CSTSHR04`    | [Part D low-income cost share group code - April](variables/mbsf.md#part-d-low-income-cost-share-group-code-april)         |              | *            |
|      65 | `CSTSHR05`    | [Part D low-income cost share group code - May](variables/mbsf.md#part-d-low-income-cost-share-group-code-may)             |              | *            |
|      66 | `CSTSHR06`    | [Part D low-income cost share group code - June](variables/mbsf.md#part-d-low-income-cost-share-group-code-june)           |              | *            |
|      67 | `CSTSHR07`    | [Part D low-income cost share group code - July](variables/mbsf.md#part-d-low-income-cost-share-group-code-july)           |              | *            |
|      68 | `CSTSHR08`    | [Part D low-income cost share group code - August](variables/mbsf.md#part-d-low-income-cost-share-group-code-august)       |              | *            |
|      69 | `CSTSHR09`    | [Part D low-income cost share group code - September](variables/mbsf.md#part-d-low-income-cost-share-group-code-september) |              | *            |
|      70 | `CSTSHR10`    | [Part D low-income cost share group code - October](variables/mbsf.md#part-d-low-income-cost-share-group-code-october)     |              | *            |
|      71 | `CSTSHR11`    | [Part D low-income cost share group code - November](variables/mbsf.md#part-d-low-income-cost-share-group-code-november)   |              | *            |
|      72 | `CSTSHR12`    | [Part D low-income cost share group code - December](variables/mbsf.md#part-d-low-income-cost-share-group-code-december)   |              | *            |

### National Death Index segment

|   Index | SAS Name                                | Variable Name                                                                                            | Limitation   | Code Table   |
|--------:|:----------------------------------------|:---------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                               | [Encrypted CCW Beneficiary ID](variables/mbsf.md#encrypted-ccw-beneficiary-id)                           |              |              |
|       2 | `RFRNC_YR`                              | [Reference Year](variables/mbsf.md#reference-year)                                                       |              |              |
|       3 | `DEATH_CERT_NUM`                        | [NDI Death Certificate Number](variables/mbsf.md#ndi-death-certificate-number)                           |              | *            |
|       4 | `NDI_DOD`                               | [NDI Date of Death](variables/mbsf.md#ndi-date-of-death)                                                 |              | *            |
|       5 | `NDI_STATE_DEATH_CD`                    | [NDI State of Death](variables/mbsf.md#ndi-state-of-death)                                               |              | *            |
|       6 | `ICD_CODE`                              | [ICD-10 Code](variables/mbsf.md#icd-10-code)                                                             |              | *            |
|       7 | `ICD_TITLE`                             | [ICD-10 Title](variables/mbsf.md#icd-10-title)                                                           |              | *            |
|       8 | `ICD_CODE_358`                          | [358 ICD-10 Recodes](variables/mbsf.md#358-icd-10-recodes)                                               |              | *            |
|       9 | `ICD_CODE_113`                          | [113 ICD-10 Recodes](variables/mbsf.md#113-icd-10-recodes)                                               |              | *            |
|      10 | `ENTITY_COND_1 (through ENTITY_COND_8)` | [NDI Entity Axis Cause of Death - Condition](variables/mbsf.md#ndi-entity-axis-cause-of-death-condition) |              | *            |
|      11 | `RECORD_COND_1 (through RECORD_COND_8)` | [NDI Record Axis Cause of Death - Condition](variables/mbsf.md#ndi-record-axis-cause-of-death-condition) |              | *            |

### Chronic Conditions segment

|   Index | SAS Name      | Variable Name                                                                                                                                                          | Limitation   | Code Table   |
|--------:|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`     | [Encrypted CCW Beneficiary ID](variables/mbsf.md#encrypted-ccw-beneficiary-id)                                                                                         |              |              |
|       2 | `RFRNC_YR`    | [Reference Year](variables/mbsf.md#reference-year)                                                                                                                     |              |              |
|       3 | `AMI`         | [Acute Myocardial Infarction End-of-Year Flag](variables/mbsf.md#acute-myocardial-infarction-end-of-year-flag)                                                         |              | *            |
|       4 | `AMIM`        | [Acute Myocardial Infarction Mid-Year Flag](variables/mbsf.md#acute-myocardial-infarction-mid-year-flag)                                                               |              | *            |
|       5 | `AMIE`        | [First Occurrence of Acute Myocardial Infarction](variables/mbsf.md#first-occurrence-of-acute-myocardial-infarction)                                                   |              |              |
|       6 | `ALZH`        | [Alzheimer's Disease End-of-Year Flag](variables/mbsf.md#alzheimer's-disease-end-of-year-flag)                                                                         |              | *            |
|       7 | `ALZHM`       | [Alzheimer's Disease Mid-Year Flag](variables/mbsf.md#alzheimer's-disease-mid-year-flag)                                                                               |              | *            |
|       8 | `ALZHE`       | [First Occurrence of Alzheimer's Disease](variables/mbsf.md#first-occurrence-of-alzheimer's-disease)                                                                   |              |              |
|       9 | `ALZHDMTA`    | [Alzheimer's Disease and Rltd Disorders or Senile Dementia EOY Flag](variables/mbsf.md#alzheimer's-disease-and-rltd-disorders-or-senile-dementia-eoy-flag)             |              | *            |
|      10 | `ALZHDMTM`    | [Alzheimer's Disease and Rltd Disorders or Senile Dementia Mid-Year Flag](variables/mbsf.md#alzheimer's-disease-and-rltd-disorders-or-senile-dementia-mid-year-flag)   |              | *            |
|      11 | `ALZHDMTE`    | [1st Occrrnce of Alzheimer's Dsease and Rltd Disorders or Senile Dementia](variables/mbsf.md#1st-occrrnce-of-alzheimer's-dsease-and-rltd-disorders-or-senile-dementia) |              |              |
|      12 | `ATRIALFB`    | [Atrial Fibrillation End-of-Year Flag](variables/mbsf.md#atrial-fibrillation-end-of-year-flag)                                                                         |              | *            |
|      13 | `ATRIALFM`    | [Atrial Fibrillation Mid-Year Flag](variables/mbsf.md#atrial-fibrillation-mid-year-flag)                                                                               |              | *            |
|      14 | `ATRIALFE`    | [First Occurrence of Atrial Fibrillation](variables/mbsf.md#first-occurrence-of-atrial-fibrillation)                                                                   |              |              |
|      15 | `CATARACT`    | [Cataract End-of-Year Flag](variables/mbsf.md#cataract-end-of-year-flag)                                                                                               |              | *            |
|      16 | `CATARCTM`    | [Cataract Mid-Year Flag](variables/mbsf.md#cataract-mid-year-flag)                                                                                                     |              | *            |
|      17 | `CATARCTE`    | [First Occurrence of Cataract](variables/mbsf.md#first-occurrence-of-cataract)                                                                                         |              |              |
|      18 | `CHRNKIDN`    | [Chronic Kidney Disease End-of-Year Flag](variables/mbsf.md#chronic-kidney-disease-end-of-year-flag)                                                                   |              | *            |
|      19 | `CHRNKDNM`    | [Chronic Kidney Disease Mid-Year Flag](variables/mbsf.md#chronic-kidney-disease-mid-year-flag)                                                                         |              | *            |
|      20 | `CHRNKDNE`    | [First Occurrence of Chronic Kidney Disease](variables/mbsf.md#first-occurrence-of-chronic-kidney-disease)                                                             |              |              |
|      21 | `COPD`        | [Chronic Obstructive Pulmonary Disease End-of-Year Flag](variables/mbsf.md#chronic-obstructive-pulmonary-disease-end-of-year-flag)                                     |              | *            |
|      22 | `COPDM`       | [Chronic Obstructive Pulmonary Disease Mid-Year Flag](variables/mbsf.md#chronic-obstructive-pulmonary-disease-mid-year-flag)                                           |              | *            |
|      23 | `COPDE`       | [First Occurrence of Chronic Obstructive Pulmonary Disease](variables/mbsf.md#first-occurrence-of-chronic-obstructive-pulmonary-disease)                               |              |              |
|      24 | `CHF`         | [Heart Failure End-of-Year Flag](variables/mbsf.md#heart-failure-end-of-year-flag)                                                                                     |              | *            |
|      25 | `CHFM`        | [Heart Failure Mid-Year Flag](variables/mbsf.md#heart-failure-mid-year-flag)                                                                                           |              | *            |
|      26 | `CHFE`        | [First Occurrence of Heart Failure](variables/mbsf.md#first-occurrence-of-heart-failure)                                                                               |              |              |
|      27 | `DIABETES`    | [Diabetes End-of-Year Flag](variables/mbsf.md#diabetes-end-of-year-flag)                                                                                               |              | *            |
|      28 | `DIABTESM`    | [Diabetes Mid-Year Flag](variables/mbsf.md#diabetes-mid-year-flag)                                                                                                     |              | *            |
|      29 | `DIABTESE`    | [First Occurrence of Diabetes](variables/mbsf.md#first-occurrence-of-diabetes)                                                                                         |              |              |
|      30 | `GLAUCOMA`    | [Glaucoma End-of-Year Flag](variables/mbsf.md#glaucoma-end-of-year-flag)                                                                                               |              | *            |
|      31 | `GLAUCMAM`    | [Glaucoma Mid-Year Flag](variables/mbsf.md#glaucoma-mid-year-flag)                                                                                                     |              | *            |
|      32 | `GLAUCMAE`    | [First Occurrence of Glaucoma](variables/mbsf.md#first-occurrence-of-glaucoma)                                                                                         |              |              |
|      33 | `HIPFRAC`     | [Hip/Pelvic Fracture End-of-Year Flag](variables/mbsf.md#hippelvic-fracture-end-of-year-flag)                                                                          |              | *            |
|      34 | `HIPFRACM`    | [Hip/Pelvic Fracture Mid-Year Flag](variables/mbsf.md#hippelvic-fracture-mid-year-flag)                                                                                |              | *            |
|      35 | `HIPFRACE`    | [First Occurrence of Hip/Pelvic Fracture](variables/mbsf.md#first-occurrence-of-hippelvic-fracture)                                                                    |              |              |
|      36 | `ISCHMCHT`    | [Ischemic Heart Disease End-of-Year Flag](variables/mbsf.md#ischemic-heart-disease-end-of-year-flag)                                                                   |              | *            |
|      37 | `ISCHMCHM`    | [Ischemic Heart Disease Mid-Year Flag](variables/mbsf.md#ischemic-heart-disease-mid-year-flag)                                                                         |              | *            |
|      38 | `ISCHMCHE`    | [First Occurrence of Ischemic Heart Disease](variables/mbsf.md#first-occurrence-of-ischemic-heart-disease)                                                             |              |              |
|      39 | `DEPRESSN`    | [Depression End-of-Year Flag](variables/mbsf.md#depression-end-of-year-flag)                                                                                           |              | *            |
|      40 | `DEPRSSNM`    | [Depression Mid-Year Flag](variables/mbsf.md#depression-mid-year-flag)                                                                                                 |              | *            |
|      41 | `DEPRSSNE`    | [First Occurrence of Depression](variables/mbsf.md#first-occurrence-of-depression)                                                                                     |              |              |
|      42 | `OSTEOPRS`    | [Osteoporosis End-of-Year Flag](variables/mbsf.md#osteoporosis-end-of-year-flag)                                                                                       |              | *            |
|      43 | `OSTEOPRM`    | [Osteoporosis Mid-Year Flag](variables/mbsf.md#osteoporosis-mid-year-flag)                                                                                             |              | *            |
|      44 | `OSTEOPRE`    | [First Occurrence of Osteoporosis](variables/mbsf.md#first-occurrence-of-osteoporosis)                                                                                 |              |              |
|      45 | `RA_OA`       | [Rheumatoid Arthritis / Osteoarthritis End-of-Year Flag](variables/mbsf.md#rheumatoid-arthritis-osteoarthritis-end-of-year-flag)                                       |              | *            |
|      46 | `RA_OA_M`     | [Rheumatoid Arthritis / Osteoarthritis Mid-Year Flag](variables/mbsf.md#rheumatoid-arthritis-osteoarthritis-mid-year-flag)                                             |              | *            |
|      47 | `RA_OA_E`     | [First Occurrence of Rheumatoid Arthritis / Osteoarthritis](variables/mbsf.md#first-occurrence-of-rheumatoid-arthritis-osteoarthritis)                                 |              | *            |
|      48 | `STRKETIA`    | [Stroke / Transient Ischemic Attack End-of-Year Flag](variables/mbsf.md#stroke-transient-ischemic-attack-end-of-year-flag)                                             |              | *            |
|      49 | `STRKTIAM`    | [Stroke / Transient Ischemic Attack Mid-Year Flag](variables/mbsf.md#stroke-transient-ischemic-attack-mid-year-flag)                                                   |              | *            |
|      50 | `STRKTIAE`    | [First Occurrence of Stroke / Transient Ischemic Attack](variables/mbsf.md#first-occurrence-of-stroke-transient-ischemic-attack)                                       |              | *            |
|      51 | `CNCRBRST`    | [Breast Cancer End-of-Year Flag](variables/mbsf.md#breast-cancer-end-of-year-flag)                                                                                     |              | *            |
|      52 | `CNCRBRSM`    | [Breast Cancer Mid-Year Flag](variables/mbsf.md#breast-cancer-mid-year-flag)                                                                                           |              | *            |
|      53 | `CNCRBRSE`    | [First Occurrence of Breast Cancer](variables/mbsf.md#first-occurrence-of-breast-cancer)                                                                               |              | *            |
|      54 | `CNCRCLRC`    | [Colorectal Cancer End-of-Year Flag](variables/mbsf.md#colorectal-cancer-end-of-year-flag)                                                                             |              | *            |
|      55 | `CNCRCLRM`    | [Colorectal Cancer Mid-Year Flag](variables/mbsf.md#colorectal-cancer-mid-year-flag)                                                                                   |              | *            |
|      56 | `CNCRCLRE`    | [First Occurrence of Colorectal Cancer](variables/mbsf.md#first-occurrence-of-colorectal-cancer)                                                                       |              | *            |
|      57 | `CNCRPRST`    | [Prostate Cancer End-of-Year Flag](variables/mbsf.md#prostate-cancer-end-of-year-flag)                                                                                 |              | *            |
|      58 | `CNCRPRSM`    | [Prostate Cancer Mid-Year Flag](variables/mbsf.md#prostate-cancer-mid-year-flag)                                                                                       |              | *            |
|      59 | `CNCRPRSE`    | [First Occurrence of Prostate Cancer](variables/mbsf.md#first-occurrence-of-prostate-cancer)                                                                           |              |              |
|      60 | `CNCRLUNG`    | [Lung Cancer End-of-Year Flag](variables/mbsf.md#lung-cancer-end-of-year-flag)                                                                                         |              | *            |
|      61 | `CNCRLNGM`    | [Lung Cancer Mid-Year Flag](variables/mbsf.md#lung-cancer-mid-year-flag)                                                                                               |              | *            |
|      62 | `CNCRLNGE`    | [First Occurrence of Lung Cancer](variables/mbsf.md#first-occurrence-of-lung-cancer)                                                                                   |              | *            |
|      63 | `CNCRENDM`    | [Endometrial Cancer End-of-Year Flag](variables/mbsf.md#endometrial-cancer-end-of-year-flag)                                                                           |              | *            |
|      64 | `CNCENDMM`    | [Endometrial Cancer Mid-Year Flag](variables/mbsf.md#endometrial-cancer-mid-year-flag)                                                                                 |              | *            |
|      65 | `CNCENDME`    | [First Occurrence of Endometrial Cancer](variables/mbsf.md#first-occurrence-of-endometrial-cancer)                                                                     |              | *            |
|      66 | `ANEMIA`      | [Anemia End Year Flag](variables/mbsf.md#anemia-end-year-flag)                                                                                                         |              | *            |
|      67 | `ANEMIA_MID`  | [Anemia Mid Year Flag](variables/mbsf.md#anemia-mid-year-flag)                                                                                                         |              | *            |
|      68 | `ANEMIA_EVER` | [Anemia First Ever Occurrence Date](variables/mbsf.md#anemia-first-ever-occurrence-date)                                                                               |              | *            |
|      69 | `ASTHMA`      | [Asthma End Year Flag](variables/mbsf.md#asthma-end-year-flag)                                                                                                         |              | *            |
|      70 | `ASTHMA_MID`  | [Asthma Mid Year Flag](variables/mbsf.md#asthma-mid-year-flag)                                                                                                         |              | *            |
|      71 | `ASTHMA_EVER` | [Asthma First Ever Occurrence Date](variables/mbsf.md#asthma-first-ever-occurrence-date)                                                                               |              | *            |
|      72 | `HYPERL`      | [Hyperlipidemia End Year Flag](variables/mbsf.md#hyperlipidemia-end-year-flag)                                                                                         |              | *            |
|      73 | `HYPERL_MID`  | [Hyperlipidemia Mid Year Flag](variables/mbsf.md#hyperlipidemia-mid-year-flag)                                                                                         |              | *            |
|      74 | `HYPERL_EVER` | [Hyperlipidemia First Ever Occurrence Date](variables/mbsf.md#hyperlipidemia-first-ever-occurrence-date)                                                               |              |              |
|      75 | `HYPERP`      | [Benign Prostatic Hyperplasia End Year Flag](variables/mbsf.md#benign-prostatic-hyperplasia-end-year-flag)                                                             |              | *            |
|      76 | `HYPERP_MID`  | [Benign Prostatic Hyperplasia Mid Year Flag](variables/mbsf.md#benign-prostatic-hyperplasia-mid-year-flag)                                                             |              | *            |
|      77 | `HYPERP_EVER` | [Benign Prostatic Hyperplasia First Ever Occurrence Date](variables/mbsf.md#benign-prostatic-hyperplasia-first-ever-occurrence-date)                                   |              | *            |
|      78 | `HYPERT`      | [Hypertension End Year Flag](variables/mbsf.md#hypertension-end-year-flag)                                                                                             |              | *            |
|      79 | `HYPERT_MID`  | [Hypertension Mid Year Flag](variables/mbsf.md#hypertension-mid-year-flag)                                                                                             |              | *            |
|      80 | `HYPERT_EVER` | [Hypertension First Ever Occurrence Date](variables/mbsf.md#hypertension-first-ever-occurrence-date)                                                                   |              | *            |
|      81 | `HYPOTH`      | [Acquired Hypothyroidism End Year Flag](variables/mbsf.md#acquired-hypothyroidism-end-year-flag)                                                                       |              | *            |
|      82 | `HYPOTH_MID`  | [Acquired Hypothyroidism Mid Year Flag](variables/mbsf.md#acquired-hypothyroidism-mid-year-flag)                                                                       |              | *            |
|      83 | `HYPOTH_EVER` | [Acquired Hypothyroidism First Ever Occurrence Date](variables/mbsf.md#acquired-hypothyroidism-first-ever-occurrence-date)                                             |              | *            |

### Other Chronic or Potentially Disabling Conditions

|   Index | SAS Name                  | Variable Name                                                                                                                                                                                                                                                                          | Limitation   | Code Table   |
|--------:|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                 | [Encrypted CCW Beneficiary ID](variables/mbsf.md#encrypted-ccw-beneficiary-id)                                                                                                                                                                                                         |              |              |
|       2 | `RFRNC_YR`                | [Reference Year](variables/mbsf.md#reference-year)                                                                                                                                                                                                                                     |              |              |
|       3 | `ACP_MEDICARE`            | [ADHD and Other Conduct Disorders - Medicare Only Claims](variables/mbsf.md#adhd-and-other-conduct-disorders-medicare-only-claims)                                                                                                                                                     |              | *            |
|       4 | `ACP_MEDICARE_EVER`       | [ADHD and Other Conduct Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#adhd-and-other-conduct-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                                               |              | *            |
|       5 | `ANXI_MEDICARE`           | [Anxiety Disorders - Medicare Only Claims](variables/mbsf.md#anxiety-disorders-medicare-only-claims)                                                                                                                                                                                   |              | *            |
|       6 | `ANXI_MEDICARE_EVER`      | [Anxiety Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#anxiety-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                                                                             |              | *            |
|       7 | `AUTISM_MEDICARE`         | [Autism Spectrum Disorders - Medicare Only Claims](variables/mbsf.md#autism-spectrum-disorders-medicare-only-claims)                                                                                                                                                                   |              | *            |
|       8 | `AUTISM_MEDICARE_EVER`    | [Autism Spectrum Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#autism-spectrum-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                                                             |              | *            |
|       9 | `BIPL_MEDICARE`           | [Bipolar Disorder - Medicare Only Claims](variables/mbsf.md#bipolar-disorder-medicare-only-claims)                                                                                                                                                                                     |              | *            |
|      10 | `BIPL_MEDICARE_EVER`      | [Bipolar Disorder First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#bipolar-disorder-first-ever-occurrence-date-medicare-only-claims)                                                                                                                               |              | *            |
|      11 | `BRAINJ_MEDICARE`         | [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-to-brain-damage-end-of-year-indicator-medicare-only-claims)                 |              | *            |
|      12 | `BRAINJ_MEDICARE_EVER`    | [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-to-brain-damage-first-ever-occurrence-date-medicare-only-claims)       |              | *            |
|      13 | `CERPAL_MEDICARE`         | [Cerebral Palsy End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#cerebral-palsy-end-of-year-indicator-medicare-only-claims)                                                                                                                                             |              | *            |
|      14 | `CERPAL_MEDICARE_EVER`    | [Cerebral Palsy First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#cerebral-palsy-first-ever-occurrence-date-medicare-only-claims)                                                                                                                                   |              |              |
|      15 | `CYSFIB_MEDICARE`         | [Cystic Fibrosis and Other Metabolic Developmental Disorders End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#cystic-fibrosis-and-other-metabolic-developmental-disorders-end-of-year-indicator-medicare-only-claims)                                                   |              | *            |
|      16 | `CYSFIB_MEDICARE_EVER`    | [Cystic Fibrosis and Other Metabolic Developmental Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#cystic-fibrosis-and-other-metabolic-developmental-disorders-first-ever-occurrence-date-medicare-only-claims)                                         |              |              |
|      17 | `DEPSN_MEDICARE`          | [Major Depressive Affective Disorder End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#major-depressive-affective-disorder-end-of-year-indicator-medicare-only-claims)                                                                                                   |              | *            |
|      18 | `DEPSN_MEDICARE_EVER`     | [Major Depressive Affective Disorder First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#major-depressive-affective-disorder-first-ever-occurrence-date-medicare-only-claims)                                                                                         |              |              |
|      19 | `EPILEP_MEDICARE`         | [Epilepsy End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#epilepsy-end-of-year-indicator-medicare-only-claims)                                                                                                                                                         |              | *            |
|      20 | `EPILEP_MEDICARE_EVER`    | [Epilepsy First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#epilepsy-first-ever-occurrence-date-medicare-only-claims)                                                                                                                                               |              |              |
|      21 | `FIBRO_MEDICARE`          | [Fibromyalgia, Chronic Pain and Fatigue End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#fibromyalgia-chronic-pain-and-fatigue-end-of-year-indicator-medicare-only-claims)                                                                                              |              | *            |
|      22 | `FIBRO_MEDICARE_EVER`     | [Fibromyalgia, Chronic Pain and Fatigue First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#fibromyalgia-chronic-pain-and-fatigue-first-ever-occurrence-date-medicare-only-claims)                                                                                    |              |              |
|      23 | `HEARIM_MEDICARE`         | [Sensory - Deafness and Hearing Impairment End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#sensory-deafness-and-hearing-impairment-end-of-year-indicator-medicare-only-claims)                                                                                         |              | *            |
|      24 | `HEARIM_MEDICARE_EVER`    | [Sensory - Deafness and Hearing Impairment First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#sensory-deafness-and-hearing-impairment-first-ever-occurrence-date-medicare-only-claims)                                                                               |              |              |
|      25 | `HEPVIRAL_MEDICARE`       | [Viral Hepatitis (General) End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#viral-hepatitis-general-end-of-year-indicator-medicare-only-claims)                                                                                                                         |              | *            |
|      26 | `HEPVIRAL_MEDICARE_EVER`  | [Viral Hepatitis (General) First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#viral-hepatitis-general-first-ever-occurrence-date-medicare-only-claims)                                                                                                               |              |              |
|      27 | `HIVAIDS_MEDICARE`        | [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-end-of-year-indicator-medicare-only-claims)           |              | *            |
|      28 | `HIVAIDS_MEDICARE_EVER`   | [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-first-ever-occurrence-date-medicare-only-claims) |              |              |
|      29 | `INTDIS_MEDICARE`         | [Intellectual Disabilities and Related Conditions End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#intellectual-disabilities-and-related-conditions-end-of-year-indicator-medicare-only-claims)                                                                         |              | *            |
|      30 | `INTDIS_MEDICARE_EVER`    | [Intellectual Disabilities and Related Conditions First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#intellectual-disabilities-and-related-conditions-first-ever-occurrence-date-medicare-only-claims)                                                               |              |              |
|      31 | `LEADIS_MEDICARE`         | [Learning Disabilities End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#learning-disabilities-end-of-year-indicator-medicare-only-claims)                                                                                                                               |              | *            |
|      32 | `LEADIS_MEDICARE_EVER`    | [Learning Disabilities First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#learning-disabilities-first-ever-occurrence-date-medicare-only-claims)                                                                                                                     |              |              |
|      33 | `LEUKLYMPH_MEDICARE`      | [Leukemias and Lymphomas End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#leukemias-and-lymphomas-end-of-year-indicator-medicare-only-claims)                                                                                                                           |              | *            |
|      34 | `LEUKLYMPH_MEDICARE_EVER` | [Leukemias and Lymphomas First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#leukemias-and-lymphomas-first-ever-occurrence-date-medicare-only-claims)                                                                                                                 |              |              |
|      35 | `LIVER_MEDICARE`          | [Liver Disease Cirrhosis and Other Liver Conditions (excluding Hepatitis) End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-end-of-year-indicator-medicare-only-claims)                           |              | *            |
|      36 | `LIVER_MEDICARE_EVER`     | [Liver Disease, Cirrhosis and Other Liver Conditions (excluding Hepatitis) First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-first-ever-occurrence-date-medicare-only-claims)                |              |              |
|      37 | `MIGRAINE_MEDICARE`       | [Migraine and other Chronic Headache End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#migraine-and-other-chronic-headache-end-of-year-indicator-medicare-only-claims)                                                                                                   |              | *            |
|      38 | `MIGRAINE_MEDICARE_EVER`  | [Migraine and other Chronic Headache First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#migraine-and-other-chronic-headache-first-ever-occurrence-date-medicare-only-claims)                                                                                         |              |              |
|      39 | `MOBIMP_MEDICARE`         | [Mobility Impairments End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#mobility-impairments-end-of-year-indicator-medicare-only-claims)                                                                                                                                 |              | *            |
|      40 | `MOBIMP_MEDICARE_EVER`    | [Mobility Impairments First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#mobility-impairments-first-ever-occurrence-date-medicare-only-claims)                                                                                                                       |              |              |
|      41 | `MULSCL_MEDICARE`         | [Multiple Sclerosis and Transverse Myelitis End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#multiple-sclerosis-and-transverse-myelitis-end-of-year-indicator-medicare-only-claims)                                                                                     |              | *            |
|      42 | `MULSCL_MEDICARE_EVER`    | [Multiple Sclerosis and Transverse Myelitis First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#multiple-sclerosis-and-transverse-myelitis-first-ever-occurrence-date-medicare-only-claims)                                                                           |              |              |
|      43 | `MUSDYS_MEDICARE`         | [Muscular Dystrophy End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#muscular-dystrophy-end-of-year-indicator-medicare-only-claims)                                                                                                                                     |              | *            |
|      44 | `MUSDYS_MEDICARE_EVER`    | [Muscular Dystrophy First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#muscular-dystrophy-first-ever-occurrence-date-medicare-only-claims)                                                                                                                           |              |              |
|      45 | `OBESITY_MEDICARE`        | [Obesity End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#obesity-end-of-year-indicator-medicare-only-claims)                                                                                                                                                           |              | *            |
|      46 | `OBESITY_MEDICARE_EVER`   | [Obesity First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#obesity-first-ever-occurrence-date-medicare-only-claims)                                                                                                                                                 |              |              |
|      47 | `OTHDEL_MEDICARE`         | [Other Developmental Delays End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#other-developmental-delays-end-of-year-indicator-medicare-only-claims)                                                                                                                     |              | *            |
|      48 | `OTHDEL_MEDICARE_EVER`    | [Other Developmental Delays First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#other-developmental-delays-first-ever-occurrence-date-medicare-only-claims)                                                                                                           |              |              |
|      49 | `PSDS_MEDICARE`           | [Personality Disorders End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#personality-disorders-end-of-year-indicator-medicare-only-claims)                                                                                                                               |              | *            |
|      50 | `PSDS_MEDICARE_EVER`      | [Personality Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#personality-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                                                                     |              |              |
|      51 | `PTRA_MEDICARE`           | [Post-Traumatic Stress Disorder End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#post-traumatic-stress-disorder-end-of-year-indicator-medicare-only-claims)                                                                                                             |              | *            |
|      52 | `PTRA_MEDICARE_EVER`      | [Post-Traumatic Stress Disorder First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#post-traumatic-stress-disorder-first-ever-occurrence-date-medicare-only-claims)                                                                                                   |              |              |
|      53 | `PVD_MEDICARE`            | [Peripheral Vascular Disease End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#peripheral-vascular-disease-end-of-year-indicator-medicare-only-claims)                                                                                                                   |              | *            |
|      54 | `PVD_MEDICARE_EVER`       | [Peripheral Vascular Disease First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#peripheral-vascular-disease-first-ever-occurrence-date-medicare-only-claims)                                                                                                         |              |              |
|      55 | `SCHI_MEDICARE`           | [Schizophrenia End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#schizophrenia-end-of-year-indicator-medicare-only-claims)                                                                                                                                               |              | *            |
|      56 | `SCHI_MEDICARE_EVER`      | [Schizophrenia First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#schizophrenia-first-ever-occurrence-date-medicare-only-claims)                                                                                                                                     |              |              |
|      57 | `SCHIOT_MEDICARE`         | [Schizophrenia and Other Psychotic Disorders End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#schizophrenia-and-other-psychotic-disorders-end-of-year-indicator-medicare-only-claims)                                                                                   |              | *            |
|      58 | `SCHIOT_MEDICARE_EVER`    | [Schizophrenia and Other Psychotic Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#schizophrenia-and-other-psychotic-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                         |              |              |
|      59 | `SPIBIF_MEDICARE`         | [Spina Bifida and Other Congenital Anomalies of the Nervous System End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#spina-bifida-and-other-congenital-anomalies-of-the-nervous-system-end-of-year-indicator-medicare-only-claims)                                       |              | *            |
|      60 | `SPIBIF_MEDICARE_EVER`    | [Spina Bifida and Other Congenital Anomalies of the Nervous System First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#spina-bifida-and-other-congenital-anomalies-of-the-nervous-system-first-ever-occurrence-date-medicare-only-claims)                             |              |              |
|      61 | `SPIINJ_MEDICARE`         | [Spinal Cord Injury End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#spinal-cord-injury-end-of-year-indicator-medicare-only-claims)                                                                                                                                     |              | *            |
|      62 | `SPIINJ_MEDICARE_EVER`    | [Spinal Cord Injury First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#spinal-cord-injury-first-ever-occurrence-date-medicare-only-claims)                                                                                                                           |              |              |
|      63 | `TOBA_MEDICARE`           | [Tobacco Use Disorders End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#tobacco-use-disorders-end-of-year-indicator-medicare-only-claims)                                                                                                                               |              | *            |
|      64 | `TOBA_MEDICARE_EVER`      | [Tobacco Use Disorders First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#tobacco-use-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                                                                     |              |              |
|      65 | `ULCERS_MEDICARE`         | [Pressure Ulcers and Chronic Ulcers End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#pressure-ulcers-and-chronic-ulcers-end-of-year-indicator-medicare-only-claims)                                                                                                     |              | *            |
|      66 | `ULCERS_MEDICARE_EVER`    | [Pressure Ulcers and Chronic Ulcers First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#pressure-ulcers-and-chronic-ulcers-first-ever-occurrence-date-medicare-only-claims)                                                                                           |              |              |
|      67 | `VISUAL_MEDICARE`         | [Sensory - Blindness and Visual Impairment End-of-Year Indicator - Medicare Only Claims](variables/mbsf.md#sensory-blindness-and-visual-impairment-end-of-year-indicator-medicare-only-claims)                                                                                         |              | *            |
|      68 | `VISUAL_MEDICARE_EVER`    | [Sensory - Blindness and Visual Impairment First Ever Occurrence Date - Medicare Only Claims](variables/mbsf.md#sensory-blindness-and-visual-impairment-first-ever-occurrence-date-medicare-only-claims)                                                                               |              |              |

### Cost and Use segment

|   Index | SAS Name            | Variable Name                                                                                                      | Limitation   | Code Table   |
|--------:|:--------------------|:-------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`           | [Encrypted CCW Beneficiary ID](variables/mbsf.md#encrypted-ccw-beneficiary-id)                                     |              |              |
|       2 | `RFRNC_YR`          | [Reference Year](variables/mbsf.md#reference-year)                                                                 |              |              |
|       3 | `HOP_MDCR_PMT`      | [Hospital Outpatient Medicare Payments](variables/mbsf.md#hospital-outpatient-medicare-payments)                   |              | *            |
|       4 | `HOP_BENE_PMT`      | [Hospital Outpatient Beneficiary Payments](variables/mbsf.md#hospital-outpatient-beneficiary-payments)             |              | *            |
|       5 | `HOP_VISITS`        | [Hospital Outpatient Visits](variables/mbsf.md#hospital-outpatient-visits)                                         |              | *            |
|       6 | `HOP_ER_VISITS`     | [Hospital Outpatient Emergency Room Visits](variables/mbsf.md#hospital-outpatient-emergency-room-visits)           |              | *            |
|       7 | `ACUTE_MDCR_PMT`    | [Acute Inpatient Medicare Payments](variables/mbsf.md#acute-inpatient-medicare-payments)                           |              | *            |
|       8 | `ACUTE_BENE_PMT`    | [Acute Inpatient Beneficiary Payments](variables/mbsf.md#acute-inpatient-beneficiary-payments)                     |              | *            |
|       9 | `ACUTE_COV_DAYS`    | [Acute Inpatient Covered Days](variables/mbsf.md#acute-inpatient-covered-days)                                     |              | *            |
|      10 | `ACUTE_STAYS`       | [Acute Inpatient Stays](variables/mbsf.md#acute-inpatient-stays)                                                   |              | *            |
|      11 | `IP_ER_VISITS`      | [Inpatient Emergency Room Visits](variables/mbsf.md#inpatient-emergency-room-visits)                               |              | *            |
|      12 | `READMISSIONS`      | [Hospital Readmissions](variables/mbsf.md#hospital-readmissions)                                                   |              | *            |
|      13 | `OIP_MDCR_PMT`      | [Other Inpatient Medicare Payments](variables/mbsf.md#other-inpatient-medicare-payments)                           |              | *            |
|      14 | `OIP_BENE_PMT`      | [Other Inpatient Beneficiary Payments](variables/mbsf.md#other-inpatient-beneficiary-payments)                     |              | *            |
|      15 | `OIP_COV_DAYS`      | [Other Inpatient Covered Days](variables/mbsf.md#other-inpatient-covered-days)                                     |              | *            |
|      16 | `OIP_STAYS`         | [Other Inpatient Stays](variables/mbsf.md#other-inpatient-stays)                                                   |              | *            |
|      17 | `SNF_MDCR_PMT`      | [Skilled Nursing Facility Medicare Payments](variables/mbsf.md#skilled-nursing-facility-medicare-payments)         |              | *            |
|      18 | `SNF_BENE_PMT`      | [Skilled Nursing Facility Beneficiary Payments](variables/mbsf.md#skilled-nursing-facility-beneficiary-payments)   |              | *            |
|      19 | `SNF_COV_DAYS`      | [Skilled Nursing Facility Covered Days](variables/mbsf.md#skilled-nursing-facility-covered-days)                   |              | *            |
|      20 | `SNF_STAYS`         | [Skilled Nursing Facility Stays](variables/mbsf.md#skilled-nursing-facility-stays)                                 |              | *            |
|      21 | `HOS_MDCR_PMT`      | [Hospice Medicare Payments](variables/mbsf.md#hospice-medicare-payments)                                           |              | *            |
|      22 | `HOS_COV_DAYS`      | [Hospice Covered Days](variables/mbsf.md#hospice-covered-days)                                                     |              | *            |
|      23 | `HOS_STAYS`         | [Hospice Stays](variables/mbsf.md#hospice-stays)                                                                   |              | *            |
|      24 | `HH_MDCR_PMT`       | [Home Health Medicare Payments](variables/mbsf.md#home-health-medicare-payments)                                   |              | *            |
|      25 | `HH_VISITS`         | [Home Health Visits](variables/mbsf.md#home-health-visits)                                                         |              | *            |
|      26 | `ASC_MDCR_PMT`      | [Ambulatory Surgery Center Medicare Payments](variables/mbsf.md#ambulatory-surgery-center-medicare-payments)       |              | *            |
|      27 | `ASC_BENE_PMT`      | [Ambulatory Surgery Center Beneficiary Payments](variables/mbsf.md#ambulatory-surgery-center-beneficiary-payments) |              | *            |
|      28 | `ASC_EVENTS`        | [Ambulatory Surgery Center Events](variables/mbsf.md#ambulatory-surgery-center-events)                             |              | *            |
|      29 | `PTB_DRUG_MDCR_PMT` | [Part B Drug Medicare Payments](variables/mbsf.md#part-b-drug-medicare-payments)                                   |              | *            |
|      30 | `PTB_DRUG_BENE_PMT` | [Part B Drug Beneficiary Payments](variables/mbsf.md#part-b-drug-beneficiary-payments)                             |              | *            |
|      31 | `PTB_DRUG_EVENTS`   | [Part B Drug Events](variables/mbsf.md#part-b-drug-events)                                                         |              | *            |
|      32 | `EM_MDCR_PMT`       | [Evaluation and Management Medicare Payments](variables/mbsf.md#evaluation-and-management-medicare-payments)       |              | *            |
|      33 | `EM_BENE_PMT`       | [Evaluation and Management Beneficiary Payments](variables/mbsf.md#evaluation-and-management-beneficiary-payments) |              | *            |
|      34 | `EM_EVENTS`         | [Evaluation and Management Events](variables/mbsf.md#evaluation-and-management-events)                             |              | *            |
|      35 | `ANES_MDCR_PMT`     | [Anesthesia Medicare Payments](variables/mbsf.md#anesthesia-medicare-payments)                                     |              | *            |
|      36 | `ANES_BENE_PMT`     | [Anesthesia Beneficiary Payments](variables/mbsf.md#anesthesia-beneficiary-payments)                               |              | *            |
|      37 | `ANES_EVENTS`       | [Anesthesia Events](variables/mbsf.md#anesthesia-events)                                                           |              | *            |
|      38 | `DIALYS_MDCR_PMT`   | [Dialysis Medicare Payments](variables/mbsf.md#dialysis-medicare-payments)                                         |              | *            |
|      39 | `DIALYS_BENE_PMT`   | [Dialysis Beneficiary Payments](variables/mbsf.md#dialysis-beneficiary-payments)                                   |              | *            |
|      40 | `DIALYS_EVENTS`     | [Dialysis Events](variables/mbsf.md#dialysis-events)                                                               |              | *            |
|      41 | `OPROC_MDCR_PMT`    | [Other Procedures Medicare Payments](variables/mbsf.md#other-procedures-medicare-payments)                         |              | *            |
|      42 | `OPROC_BENE_PMT`    | [Other Procedures Beneficiary Payments](variables/mbsf.md#other-procedures-beneficiary-payments)                   |              | *            |
|      43 | `OPROC_EVENTS`      | [Other Procedures Events](variables/mbsf.md#other-procedures-events)                                               |              | *            |
|      44 | `IMG_MDCR_PMT`      | [Imaging Medicare Payments](variables/mbsf.md#imaging-medicare-payments)                                           |              | *            |
|      45 | `IMG_BENE_PMT`      | [Imaging Beneficiary Payments](variables/mbsf.md#imaging-beneficiary-payments)                                     |              | *            |
|      46 | `IMG_EVENTS`        | [Imaging Events](variables/mbsf.md#imaging-events)                                                                 |              | *            |
|      47 | `TEST_MDCR_PMT`     | [Tests Medicare Payments](variables/mbsf.md#tests-medicare-payments)                                               |              | *            |
|      48 | `TEST_BENE_PMT`     | [Tests Beneficiary Payments](variables/mbsf.md#tests-beneficiary-payments)                                         |              | *            |
|      49 | `TEST_EVENTS`       | [Tests Events](variables/mbsf.md#tests-events)                                                                     |              | *            |
|      50 | `DME_MDCR_PMT`      | [Durable Medical Equipment Medicare Payments](variables/mbsf.md#durable-medical-equipment-medicare-payments)       |              | *            |
|      51 | `DME_BENE_PMT`      | [Durable Medical Equipment Beneficiary Payments](variables/mbsf.md#durable-medical-equipment-beneficiary-payments) |              | *            |
|      52 | `DME_EVENTS`        | [Durable Medical Equipment Events](variables/mbsf.md#durable-medical-equipment-events)                             |              | *            |
|      53 | `OTHC_MDCR_PMT`     | [Other Part B Carrier Medicare Payments](variables/mbsf.md#other-part-b-carrier-medicare-payments)                 |              | *            |
|      54 | `OTHC_BENE_PMT`     | [Other Part B Carrier Beneficiary Payments](variables/mbsf.md#other-part-b-carrier-beneficiary-payments)           |              | *            |
|      55 | `OTHC_EVENTS`       | [Other Part B Carrier Events](variables/mbsf.md#other-part-b-carrier-events)                                       |              | *            |
|      56 | `PHYS_MDCR_PMT`     | [Part B Physician Medicare Payments](variables/mbsf.md#part-b-physician-medicare-payments)                         |              | *            |
|      57 | `PHYS_BENE_PMT`     | [Part B Physician Beneficiary Payments](variables/mbsf.md#part-b-physician-beneficiary-payments)                   |              | *            |
|      58 | `PHYS_EVENTS`       | [Part B Physician Events](variables/mbsf.md#part-b-physician-events)                                               |              | *            |
|      59 | `PTD_MDCR_PMT`      | [Part D Medicare Payments](variables/mbsf.md#part-d-medicare-payments)                                             |              | *            |
|      60 | `PTD_BENE_PMT`      | [Part D Beneficiary Payments](variables/mbsf.md#part-d-beneficiary-payments)                                       |              | *            |
|      61 | `PTD_EVENTS`        | [Part D Events](variables/mbsf.md#part-d-events)                                                                   |              | *            |
|      62 | `PTD_FILL_CNT`      | [Part D Fill Count](variables/mbsf.md#part-d-fill-count)                                                           |              | *            |
|      63 | `PTD_TOTAL_RX_CST`  | [Part D Total Prescription Costs](variables/mbsf.md#part-d-total-prescription-costs)                               |              | *            |
