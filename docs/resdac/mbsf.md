# Beneficiary Summary File

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

| Index | SAS Name                | Variable Name                                                                                                                              | Limitation | Code Table |
|------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `BENE_ID`               | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                     |            |   |
|     2 | `RFRNC_YR`              | [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)                                                                 |            |   |
|     3 | `ENRL_SRC`              | [Source of enrollment data](https://www.resdac.org/cms-data/variables/source-enrollment-data)                                              |            | * |
|     4 | `SAMPLE_GROUP`          | [Medicare Sample Group Indicator](https://www.resdac.org/cms-data/variables/Strict-5-Flag)                                                 |            | * |
|     5 | `EFIVEPCT`              | [Enhanced Medicare 5% Sample Indicator](https://www.resdac.org/cms-data/variables/Enhanced-5-Flag)                                         |            | * |
|     6 | `CRNT_BIC`              | [Current Beneficiary Identification Code](https://www.resdac.org/cms-data/variables/current-beneficiary-identification-code)               |            | * |
|     7 | `STATE_CD`              | [State code for beneficiary (SSA code)](https://www.resdac.org/cms-data/variables/State-Code)                                              |            | * |
|     8 | `CNTY_CD`               | [County Code for Beneficiary (SSA code)](https://www.resdac.org/cms-data/variables/County-Code)                                            |            | * |
|     9 | `ZIP_CD`                | [5-digit ZIP code for beneficiary](https://www.resdac.org/cms-data/variables/Zip-Code-Residence)                                           |            | * |
|    10 | `STATE_CNTY_FIPS_CD_01` | [State and county FIPS code - January](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-january)                       |            | * |
|    11 | `STATE_CNTY_FIPS_CD_02` | [State and county FIPS code - February](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-february)                     |            | * |
|    12 | `STATE_CNTY_FIPS_CD_03` | [State and county FIPS code - March](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-march)                           |            | * |
|    13 | `STATE_CNTY_FIPS_CD_04` | [State and county FIPS code - April](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-april)                           |            | * |
|    14 | `STATE_CNTY_FIPS_CD_05` | [State and county FIPS code - May](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-may)                               |            | * |
|    15 | `STATE_CNTY_FIPS_CD_06` | [State and county FIPS code - June](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-june)                             |            | * |
|    16 | `STATE_CNTY_FIPS_CD_07` | [State and county FIPS code - July](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-july)                             |            | * |
|    17 | `STATE_CNTY_FIPS_CD_08` | [State and county FIPS code - August](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-august)                         |            | * |
|    18 | `STATE_CNTY_FIPS_CD_09` | [State and county FIPS code - September](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-september)                   |            | * |
|    19 | `STATE_CNTY_FIPS_CD_10` | [State and county FIPS code - October](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-october)                       |            | * |
|    20 | `STATE_CNTY_FIPS_CD_11` | [State and county FIPS code - November](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-november)                     |            | * |
|    21 | `STATE_CNTY_FIPS_CD_12` | [State and county FIPS code - December](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-december)                     |            | * |
|    22 | `AGE`                   | [Age of beneficiary at end of year](https://www.resdac.org/cms-data/variables/Age-End-Reference-Year)                                      |            | * |
|    23 | `BENE_DOB`              | [Beneficiary date of birth](https://www.resdac.org/cms-data/variables/Date-Birth)                                                          |            | * |
|    24 | `V_DOD_SW`              | [Valid Date of Death Switch](https://www.resdac.org/cms-data/variables/Valid-Date-Death-Switch)                                            |            | * |
|    25 | `DEATH_DT`              | [Date of Death](https://www.resdac.org/taxonomy/term/219)                                                                                  |            | * |
|    26 | `SEX`                   | [Sex](https://www.resdac.org/cms-data/variables/Sex)                                                                                       |            | * |
|    27 | `RACE`                  | [Beneficiary Race Code](https://www.resdac.org/cms-data/variables/Beneficiary-Race-Code)                                                   |            | * |
|    28 | `RTI_RACE_CD`           | [Research Triangle Institute (RTI) Race Code](https://www.resdac.org/cms-data/variables/Research-Triangle-Institute-RTI-Race-Code)         |            | * |
|    29 | `COVSTART`              | [Medicare Coverage Start Date](https://www.resdac.org/cms-data/variables/Medicare-Coverage-Start-Date)                                     |            | * |
|    30 | `OREC`                  | [Original Reason for Entitlement Code](https://www.resdac.org/cms-data/variables/Original-Reason-Entitlement-Code)                         |            | * |
|    31 | `CREC`                  | [Current Reason for Entitlement Code](https://www.resdac.org/cms-data/variables/Current-Reason-Entitlement-Code)                           |            | * |
|    32 | `ESRD_IND`              | [End-stage Renal Disease (ESRD) Indicator](https://www.resdac.org/cms-data/variables/ESRD-Indicator)                                       |            | * |
|    33 | `MDCR_STUS_CD_01`       | [Medicare Status Code - January](https://www.resdac.org/cms-data/variables/Medicare-Status-Code)                                           |            | * |
|    34 | `MDCR_STUS_CD_02`       | [Medicare Status Code - February](https://www.resdac.org/taxonomy/term/5186)                                                               |            | * |
|    35 | `MDCR_STUS_CD_03`       | [Medicare Status Code - March](https://www.resdac.org/taxonomy/term/5191)                                                                  |            | * |
|    36 | `MDCR_STUS_CD_04`       | [Medicare Status Code - April](https://www.resdac.org/taxonomy/term/5196)                                                                  |            | * |
|    37 | `MDCR_STUS_CD_05`       | [Medicare Status Code - May](https://www.resdac.org/taxonomy/term/5201)                                                                    |            | * |
|    38 | `MDCR_STUS_CD_06`       | [Medicare Status Code - June](https://www.resdac.org/taxonomy/term/5206)                                                                   |            | * |
|    39 | `MDCR_STUS_CD_07`       | [Medicare Status Code - July](https://www.resdac.org/taxonomy/term/5211)                                                                   |            | * |
|    40 | `MDCR_STUS_CD_08`       | [Medicare Status Code - August](https://www.resdac.org/taxonomy/term/5216)                                                                 |            | * |
|    41 | `MDCR_STUS_CD_09`       | [Medicare Status Code - September](https://www.resdac.org/taxonomy/term/5221)                                                              |            | * |
|    42 | `MDCR_STUS_CD_10`       | [Medicare Status Code - October](https://www.resdac.org/taxonomy/term/5226)                                                                |            | * |
|    43 | `MDCR_STUS_CD_11`       | [Medicare Status Code - November](https://www.resdac.org/taxonomy/term/5231)                                                               |            | * |
|    44 | `MDCR_STUS_CD_12`       | [Medicare Status Code - December](https://www.resdac.org/taxonomy/term/5236)                                                               |            | * |
|    45 | `A_TRM_CD`              | [Part A Termination Code](https://www.resdac.org/cms-data/variables/Part-Termination-Code)                                                 |            | * |
|    46 | `B_TRM_CD`              | [Part B Termination Code](https://www.resdac.org/cms-data/variables/Part-B-Termination-Code)                                               |            | * |
|    47 | `A_MO_CNT`              | [Part A Months Count](https://www.resdac.org/cms-data/variables/part-months-count)                                                         |            | * |
|    48 | `B_MO_CNT`              | [Part B Months Count](https://www.resdac.org/cms-data/variables/part-b-months-count)                                                       |            | * |
|    49 | `BUYIN_MO`              | [State Buy-In Coverage Count](https://www.resdac.org/cms-data/variables/State-Buy-Coverage-Count)                                          |            | * |
|    50 | `HMO_MO`                | [HMO Coverage Count](https://www.resdac.org/cms-data/variables/HMO-Coverage-Count)                                                         |            | * |
|    51 | `PTD_MO`                | [Months of Part D Coverage](https://www.resdac.org/cms-data/variables/Plan-Coverage-Months-Number)                                         |            | * |
|    52 | `RDS_MO`                | [Months of Retiree Drug Subsidy Coverage](https://www.resdac.org/cms-data/variables/Retiree-Drug-Subsidy-Coverage-Months-Number)           |            | * |
|    53 | `DUAL_MO`               | [Months of Dual Eligibility](https://www.resdac.org/cms-data/variables/Dual-Eligible-Months-Number)                                        |            | * |
|    54 | `BUYIN01`               | [Medicare Entitlement/Buy-In Indicator - January](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-january)     |            | * |
|    55 | `BUYIN02`               | [Medicare Entitlement/Buy-In Indicator - February](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-february)   |            | * |
|    56 | `BUYIN03`               | [Medicare Entitlement/Buy-In Indicator - March](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-march)         |            | * |
|    57 | `BUYIN04`               | [Medicare Entitlement/Buy-In Indicator - April](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-april)         |            | * |
|    58 | `BUYIN05`               | [Medicare Entitlement/Buy-In Indicator - May](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-may)             |            | * |
|    59 | `BUYIN06`               | [Medicare Entitlement/Buy-In Indicator - June](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-june)           |            | * |
|    60 | `BUYIN07`               | [Medicare Entitlement/Buy-In Indicator - July](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-july)           |            | * |
|    61 | `BUYIN08`               | [Medicare Entitlement/Buy-In Indicator - August](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-august)       |            | * |
|    62 | `BUYIN09`               | [Medicare Entitlement/Buy-In Indicator - September](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-september) |            | * |
|    63 | `BUYIN10`               | [Medicare Entitlement/Buy-In Indicator - October](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-october)     |            | * |
|    64 | `BUYIN11`               | [Medicare Entitlement/Buy-In Indicator - November](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-november)   |            | * |
|    65 | `BUYIN12`               | [Medicare Entitlement/Buy-In Indicator - December](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-december)   |            | * |
|    66 | `HMOIND01`              | [HMO Indicator - January](https://www.resdac.org/cms-data/variables/hmo-indicator-january)                                                 |            | * |
|    67 | `HMOIND02`              | [HMO Indicator - February](https://www.resdac.org/cms-data/variables/hmo-indicator-february)                                               |            | * |
|    68 | `HMOIND03`              | [HMO Indicator - March](https://www.resdac.org/cms-data/variables/hmo-indicator-march)                                                     |            | * |
|    69 | `HMOIND04`              | [HMO Indicator - April](https://www.resdac.org/cms-data/variables/hmo-indicator-april)                                                     |            | * |
|    70 | `HMOIND05`              | [HMO Indicator - May](https://www.resdac.org/cms-data/variables/hmo-indicator-may)                                                         |            | * |
|    71 | `HMOIND06`              | [HMO Indicator - June](https://www.resdac.org/cms-data/variables/hmo-indicator-june)                                                       |            | * |
|    72 | `HMOIND07`              | [HMO Indicator - July](https://www.resdac.org/cms-data/variables/hmo-indicator-july)                                                       |            | * |
|    73 | `HMOIND08`              | [HMO Indicator - August](https://www.resdac.org/cms-data/variables/hmo-indicator-august)                                                   |            | * |
|    74 | `HMOIND09`              | [HMO Indicator - September](https://www.resdac.org/cms-data/variables/hmo-indicator-september)                                             |            | * |
|    75 | `HMOIND10`              | [HMO Indicator - October](https://www.resdac.org/cms-data/variables/hmo-indicator-october)                                                 |            | * |
|    76 | `HMOIND11`              | [HMO Indicator - November](https://www.resdac.org/cms-data/variables/hmo-indicator-november)                                               |            | * |
|    77 | `HMOIND12`              | [HMO Indicator - December](https://www.resdac.org/cms-data/variables/hmo-indicator-december)                                               |            | * |

### Part C

| Index | SAS Name              | Variable Name                                                                                                    | Limitation | Code Table |
|------:|:----------------------|:-----------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `PTC_CNTRCT_ID_01`    | [Part C Contract Number - January](https://www.resdac.org/cms-data/variables/part-c-contract-number-january)     |            |   |
|     2 | `PTC_CNTRCT_ID_02`    | [Part C Contract Number - February](https://www.resdac.org/cms-data/variables/part-c-contract-number-february)   |            |   |
|     3 | `PTC_CNTRCT_ID_03`    | [Part C Contract Number - March](https://www.resdac.org/cms-data/variables/part-c-contract-number-march)         |            |   |
|     4 | `PTC_CNTRCT_ID_04`    | [Part C Contract Number - April](https://www.resdac.org/cms-data/variables/part-c-contract-number-april)         |            |   |
|     5 | `PTC_CNTRCT_ID_05`    | [Part C Contract Number - May](https://www.resdac.org/cms-data/variables/part-c-contract-number-may)             |            |   |
|     6 | `PTC_CNTRCT_ID_06`    | [Part C Contract Number - June](https://www.resdac.org/cms-data/variables/part-c-contract-number-june)           |            |   |
|     7 | `PTC_CNTRCT_ID_07`    | [Part C Contract Number - July](https://www.resdac.org/cms-data/variables/part-c-contract-number-july)           |            |   |
|     8 | `PTC_CNTRCT_ID_08`    | [Part C Contract Number - August](https://www.resdac.org/cms-data/variables/part-c-contract-number-august)       |            |   |
|     9 | `PTC_CNTRCT_ID_09`    | [Part C Contract Number - September](https://www.resdac.org/cms-data/variables/part-c-contract-number-september) |            |   |
|    10 | `PTC_CNTRCT_ID_10`    | [Part C Contract Number - October](https://www.resdac.org/cms-data/variables/part-c-contract-number-october)     |            |   |
|    11 | `PTC_CNTRCT_ID_11`    | [Part C Contract Number - November](https://www.resdac.org/cms-data/variables/part-c-contract-number-november)   |            |   |
|    12 | `PTC_CNTRCT_ID_12`    | [Part C Contract Number - December](https://www.resdac.org/cms-data/variables/part-c-contract-number-december)   |            |   |
|    13 | `PTC_PBP_ID_01`       | [Part C PBP Number - January](https://www.resdac.org/cms-data/variables/part-c-pbp-number-january)               |            | * |
|    14 | `PTC_PBP_ID_02`       | [Part C PBP Number - February](https://www.resdac.org/cms-data/variables/part-c-pbp-number-february)             |            | * |
|    15 | `PTC_PBP_ID_03`       | [Part C PBP Number - March](https://www.resdac.org/cms-data/variables/part-c-pbp-number-march)                   |            | * |
|    16 | `PTC_PBP_ID_04`       | [Part C PBP Number - April](https://www.resdac.org/cms-data/variables/part-c-pbp-number-april)                   |            | * |
|    17 | `PTC_PBP_ID_05`       | [Part C PBP Number - May](https://www.resdac.org/cms-data/variables/part-c-pbp-number-may)                       |            | * |
|    18 | `PTC_PBP_ID_06`       | [Part C PBP Number - June](https://www.resdac.org/cms-data/variables/part-c-pbp-number-june)                     |            | * |
|    19 | `PTC_PBP_ID_07`       | [Part C PBP Number - July](https://www.resdac.org/cms-data/variables/part-c-pbp-number-july)                     |            | * |
|    20 | `PTC_PBP_ID_08`       | [Part C PBP Number - August](https://www.resdac.org/cms-data/variables/part-c-pbp-number-august)                 |            | * |
|    21 | `PTC_PBP_ID_09`       | [Part C PBP Number - September](https://www.resdac.org/cms-data/variables/part-c-pbp-number-september)           |            | * |
|    22 | `PTC_PBP_ID_10`       | [Part C PBP Number - October](https://www.resdac.org/cms-data/variables/part-c-pbp-number-october)               |            | * |
|    23 | `PTC_PBP_ID_11`       | [Part C PBP Number - November](https://www.resdac.org/cms-data/variables/part-c-pbp-number-november)             |            | * |
|    24 | `PTC_PBP_ID_12`       | [Part C PBP Number - December](https://www.resdac.org/cms-data/variables/part-c-pbp-number-december)             |            | * |
|    25 | `PTC_PLAN_TYPE_CD_01` | [Part C Plan Type Code - January](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-january)       |            | * |
|    26 | `PTC_PLAN_TYPE_CD_02` | [Part C Plan Type Code - February](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-february)     |            | * |
|    27 | `PTC_PLAN_TYPE_CD_03` | [Part C Plan Type Code - March](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-march)           |            | * |
|    28 | `PTC_PLAN_TYPE_CD_04` | [Part C Plan Type Code - April](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-april)           |            | * |
|    29 | `PTC_PLAN_TYPE_CD_05` | [Part C Plan Type Code - May](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-may)               |            | * |
|    30 | `PTC_PLAN_TYPE_CD_06` | [Part C Plan Type Code - June](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-june)             |            | * |
|    31 | `PTC_PLAN_TYPE_CD_07` | [Part C Plan Type Code - July](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-july)             |            | * |
|    32 | `PTC_PLAN_TYPE_CD_08` | [Part C Plan Type Code - August](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-august)         |            | * |
|    33 | `PTC_PLAN_TYPE_CD_09` | [Part C Plan Type Code - September](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-september)   |            | * |
|    34 | `PTC_PLAN_TYPE_CD_10` | [Part C Plan Type Code - October](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-october)       |            | * |
|    35 | `PTC_PLAN_TYPE_CD_11` | [Part C Plan Type Code - November](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-november)     |            | * |
|    36 | `PTC_PLAN_TYPE_CD_12` | [Part C Plan Type Code - December](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-december)     |            | * |

### Part D

| Index | SAS Name      | Variable Name                                                                                                                                   | Limitation | Code Table |
|------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `PTDCNTRCT01` | [Part D Contract Number - January](https://www.resdac.org/cms-data/variables/Encrypted-Contract-ID-occurs-12-times)                             |            | * |
|     2 | `PTDCNTRCT02` | [Part D Contract Number - February](https://www.resdac.org/taxonomy/term/5406)                                                                  |            | * |
|     4 | `PTDCNTRCT04` | [Part D Contract Number - April](https://www.resdac.org/taxonomy/term/5416)                                                                     |            | * |
|     5 | `PTDCNTRCT05` | [Part D Contract Number - May](https://www.resdac.org/taxonomy/term/5421)                                                                       |            | * |
|     6 | `PTDCNTRCT06` | [Part D Contract Number - June](https://www.resdac.org/taxonomy/term/5426)                                                                      |            | * |
|     7 | `PTDCNTRCT07` | [Part D Contract Number - July](https://www.resdac.org/taxonomy/term/5431)                                                                      |            | * |
|     8 | `PTDCNTRCT08` | [Part D Contract Number - August](https://www.resdac.org/taxonomy/term/5436)                                                                    |            | * |
|     9 | `PTDCNTRCT09` | [Part D Contract Number - September](https://www.resdac.org/taxonomy/term/5441)                                                                 |            | * |
|    10 | `PTDCNTRCT10` | [Part D Contract Number - October](https://www.resdac.org/taxonomy/term/5446)                                                                   |            | * |
|    11 | `PTDCNTRCT11` | [Part D Contract Number - November](https://www.resdac.org/taxonomy/term/5451)                                                                  |            | * |
|    12 | `PTDCNTRCT12` | [Part D Contract Number - December](https://www.resdac.org/taxonomy/term/5456)                                                                  |            | * |
|    13 | `PTDPBPID01`  | [Part D PBP Number - January](https://www.resdac.org/cms-data/variables/part-d-pbp-number-january)                                              |            | * |
|    14 | `PTDPBPID02`  | [Part D PBP Number - February](https://www.resdac.org/cms-data/variables/part-d-pbp-number-february)                                            |            | * |
|    15 | `PTDPBPID03`  | [Part D PBP Number - March](https://www.resdac.org/cms-data/variables/part-d-pbp-number-march)                                                  |            | * |
|    16 | `PTDPBPID04`  | [Part D PBP Number - April](https://www.resdac.org/cms-data/variables/part-d-pbp-number-april)                                                  |            | * |
|    17 | `PTDPBPID05`  | [Part D PBP Number - May](https://www.resdac.org/cms-data/variables/part-d-pbp-number-may)                                                      |            | * |
|    18 | `PTDPBPID06`  | [Part D PBP Number - June](https://www.resdac.org/cms-data/variables/part-d-pbp-number-june)                                                    |            | * |
|    19 | `PTDPBPID07`  | [Part D PBP Number - July](https://www.resdac.org/cms-data/variables/part-d-pbp-number-july)                                                    |            | * |
|    20 | `PTDPBPID08`  | [Part D PBP Number - August](https://www.resdac.org/cms-data/variables/part-d-pbp-number-august)                                                |            | * |
|    21 | `PTDPBPID09`  | [Part D PBP Number - September](https://www.resdac.org/cms-data/variables/part-d-pbp-number-september)                                          |            | * |
|    22 | `PTDPBPID10`  | [Part D PBP Number - October](https://www.resdac.org/cms-data/variables/part-d-pbp-number-october)                                              |            | * |
|    23 | `PTDPBPID11`  | [Part D PBP Number - November](https://www.resdac.org/cms-data/variables/part-d-pbp-number-november)                                            |            | * |
|    24 | `PTDPBPID12`  | [Part D PBP Number - December](https://www.resdac.org/cms-data/variables/part-d-pbp-number-december)                                            |            | * |
|    25 | `SGMTID01`    | [Part D Segment Number - January](https://www.resdac.org/cms-data/variables/Encrypted-Segment-ID-occurs-12-times)                               |            | * |
|    26 | `SGMTID02`    | [Part D Segment Number - February](https://www.resdac.org/taxonomy/term/5516)                                                                   |            | * |
|    27 | `SGMTID03`    | [Part D Segment Number - March](https://www.resdac.org/taxonomy/term/5521)                                                                      |            | * |
|    28 | `SGMTID04`    | [Part D Segment Number - April](https://www.resdac.org/taxonomy/term/5526)                                                                      |            | * |
|    29 | `SGMTID05`    | [Part D Segment Number - May](https://www.resdac.org/taxonomy/term/5531)                                                                        |            | * |
|    30 | `SGMTID06`    | [Part D Segment Number - June](https://www.resdac.org/taxonomy/term/5536)                                                                       |            | * |
|    31 | `SGMTID07`    | [Part D Segment Number - July](https://www.resdac.org/taxonomy/term/5541)                                                                       |            | * |
|    32 | `SGMTID08`    | [Part D Segment Number - August](https://www.resdac.org/taxonomy/term/5546)                                                                     |            | * |
|    33 | `SGMTID09`    | [Part D Segment Number - September](https://www.resdac.org/taxonomy/term/5551)                                                                  |            | * |
|    34 | `SGMTID10`    | [Part D Segment Number - October](https://www.resdac.org/taxonomy/term/5556)                                                                    |            | * |
|    35 | `SGMTID11`    | [Part D Segment Number - November](https://www.resdac.org/taxonomy/term/5561)                                                                   |            | * |
|    36 | `SGMTID12`    | [Part D Segment Number - December](https://www.resdac.org/taxonomy/term/5566)                                                                   |            | * |
|    37 | `RDSIND01`    | [Part D Retiree Drug Subsidy Indicator - January](https://www.resdac.org/cms-data/variables/RDS-Code-Retiree-Drug-Subsidy-Code-occurs-12-times) |            | * |
|    38 | `RDSIND02`    | [Part D Retiree Drug Subsidy Indicator - February](https://www.resdac.org/taxonomy/term/5571)                                                   |            | * |
|    39 | `RDSIND03`    | [Part D Retiree Drug Subsidy Indicator - March](https://www.resdac.org/taxonomy/term/5576)                                                      |            | * |
|    40 | `RDSIND04`    | [Part D Retiree Drug Subsidy Indicator - April](https://www.resdac.org/taxonomy/term/5581)                                                      |            | * |
|    41 | `RDSIND05`    | [Part D Retiree Drug Subsidy Indicator - May](https://www.resdac.org/taxonomy/term/5586)                                                        |            | * |
|    42 | `RDSIND06`    | [Part D Retiree Drug Subsidy Indicator - June](https://www.resdac.org/taxonomy/term/5591)                                                       |            | * |
|    43 | `RDSIND07`    | [Part D Retiree Drug Subsidy Indicator - July](https://www.resdac.org/taxonomy/term/5596)                                                       |            | * |
|    44 | `RDSIND08`    | [Part D Retiree Drug Subsidy Indicator - August](https://www.resdac.org/taxonomy/term/5601)                                                     |            | * |
|    45 | `RDSIND09`    | [Part D Retiree Drug Subsidy Indicator - September](https://www.resdac.org/taxonomy/term/5606)                                                  |            | * |
|    46 | `RDSIND10`    | [Part D Retiree Drug Subsidy Indicator - October](https://www.resdac.org/taxonomy/term/5611)                                                    |            | * |
|    47 | `RDSIND11`    | [Part D Retiree Drug Subsidy Indicator - November](https://www.resdac.org/taxonomy/term/5616)                                                   |            | * |
|    48 | `RDSIND12`    | [Part D Retiree Drug Subsidy Indicator - December](https://www.resdac.org/taxonomy/term/5621)                                                   |            | * |
|    49 | `DUAL_01`     | [Medicare-Medicaid dual eligibility code - January](https://www.resdac.org/cms-data/variables/Dual-Status-Code-occurs-12-times)                 |            | * |
|    50 | `DUAL_02`     | [Medicare-Medicaid dual eligibility code - February](https://www.resdac.org/taxonomy/term/5626)                                                 |            | * |
|    51 | `DUAL_03`     | [Medicare-Medicaid dual eligibility code - March](https://www.resdac.org/taxonomy/term/5631)                                                    |            | * |
|    52 | `DUAL_04`     | [Medicare-Medicaid dual eligibility code - April](https://www.resdac.org/taxonomy/term/5636)                                                    |            | * |
|    53 | `DUAL_05`     | [Medicare-Medicaid dual eligibility code - May](https://www.resdac.org/taxonomy/term/5641)                                                      |            | * |
|    54 | `DUAL_06`     | [Medicare-Medicaid dual eligibility code - June](https://www.resdac.org/taxonomy/term/5646)                                                     |            | * |
|    55 | `DUAL_07`     | [Medicare-Medicaid dual eligibility code - July](https://www.resdac.org/taxonomy/term/5651)                                                     |            | * |
|    56 | `DUAL_08`     | [Medicare-Medicaid dual eligibility code - August](https://www.resdac.org/taxonomy/term/5656)                                                   |            | * |
|    57 | `DUAL_09`     | [Medicare-Medicaid dual eligibility code - September](https://www.resdac.org/taxonomy/term/5661)                                                |            | * |
|    58 | `DUAL_10`     | [Medicare-Medicaid dual eligibility code - October](https://www.resdac.org/taxonomy/term/5666)                                                  |            | * |
|    59 | `DUAL_11`     | [Medicare-Medicaid dual eligibility code - November](https://www.resdac.org/taxonomy/term/5671)                                                 |            | * |
|    60 | `DUAL_12`     | [Medicare-Medicaid dual eligibility code - December](https://www.resdac.org/taxonomy/term/5676)                                                 |            | * |
|    61 | `CSTSHR01`    | [Part D low-income cost share group code - January](https://www.resdac.org/cms-data/variables/Cost-Share-Group-Code-occurs-12-times)            |            | * |
|    62 | `CSTSHR02`    | [Part D low-income cost share group code - February](https://www.resdac.org/taxonomy/term/5681)                                                 |            | * |
|    63 | `CSTSHR03`    | [Part D low-income cost share group code - March](https://www.resdac.org/taxonomy/term/5686)                                                    |            | * |
|    64 | `CSTSHR04`    | [Part D low-income cost share group code - April](https://www.resdac.org/taxonomy/term/5691)                                                    |            | * |
|    65 | `CSTSHR05`    | [Part D low-income cost share group code - May](https://www.resdac.org/taxonomy/term/5696)                                                      |            | * |
|    66 | `CSTSHR06`    | [Part D low-income cost share group code - June](https://www.resdac.org/taxonomy/term/5701)                                                     |            | * |
|    67 | `CSTSHR07`    | [Part D low-income cost share group code - July](https://www.resdac.org/taxonomy/term/5706)                                                     |            | * |
|    68 | `CSTSHR08`    | [Part D low-income cost share group code - August](https://www.resdac.org/taxonomy/term/5711)                                                   |            | * |
|    69 | `CSTSHR09`    | [Part D low-income cost share group code - September](https://www.resdac.org/taxonomy/term/5716)                                                |            | * |
|    70 | `CSTSHR10`    | [Part D low-income cost share group code - October](https://www.resdac.org/taxonomy/term/5721)                                                  |            | * |
|    71 | `CSTSHR11`    | [Part D low-income cost share group code - November](https://www.resdac.org/taxonomy/term/5726)                                                 |            | * |
|    72 | `CSTSHR12`    | [Part D low-income cost share group code - December](https://www.resdac.org/taxonomy/term/5731)                                                 |            | * |

### National Death Index segment

| Index | SAS Name                                | Variable Name                                                                                                                 | Limitation | Code Table |
|------:|:----------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `BENE_ID`                               | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                        |            |   |
|     2 | `RFRNC_YR`                              | [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)                                                    |            |   |
|     3 | `DEATH_CERT_NUM`                        | [NDI Death Certificate Number](https://www.resdac.org/cms-data/variables/NDI-Death-Certificate-Number)                        |            | * |
|     4 | `NDI_DOD`                               | [NDI Date of Death](https://www.resdac.org/taxonomy/term/586)                                                                 |            | * |
|     5 | `NDI_STATE_DEATH_CD`                    | [NDI State of Death](https://www.resdac.org/cms-data/variables/NDI-State-Death)                                               |            | * |
|     6 | `ICD_CODE`                              | [ICD-10 Code](https://www.resdac.org/cms-data/variables/ICD-10-Code)                                                          |            | * |
|     7 | `ICD_TITLE`                             | [ICD-10 Title](https://www.resdac.org/cms-data/variables/ICD-10-Title)                                                        |            | * |
|     8 | `ICD_CODE_358`                          | [358 ICD-10 Recodes](https://www.resdac.org/cms-data/variables/358-ICD-10-Recodes)                                            |            | * |
|     9 | `ICD_CODE_113`                          | [113 ICD-10 Recodes](https://www.resdac.org/cms-data/variables/113-ICD-10-Recodes)                                            |            | * |
|    10 | `ENTITY_COND_1 (through ENTITY_COND_8)` | [NDI Entity Axis Cause of Death - Condition](https://www.resdac.org/cms-data/variables/NDI-Entity-Axis-Cause-Death-Condition) |            | * |
|    11 | `RECORD_COND_1 (through RECORD_COND_8)` | [NDI Record Axis Cause of Death - Condition](https://www.resdac.org/cms-data/variables/NDI-Record-Axis-Cause-Death-Condition) |            | * |

### Chronic Conditions segment

| Index | SAS Name      | Variable Name                                                                                                                                                                               | Limitation | Code Table |
|------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `BENE_ID`     | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                                                                      |            |   |
|     2 | `RFRNC_YR`    | [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)                                                                                                                  |            |   |
|     3 | `AMI`         | [Acute Myocardial Infarction End-of-Year Flag](https://www.resdac.org/cms-data/variables/Acute-Myocardial-Infarction-End-Year-Flag)                                                         |            | * |
|     4 | `AMIM`        | [Acute Myocardial Infarction Mid-Year Flag](https://www.resdac.org/cms-data/variables/Acute-Myocardial-Infarction-Mid-Year-Flag)                                                            |            | * |
|     5 | `AMIE`        | [First Occurrence of Acute Myocardial Infarction](https://www.resdac.org/cms-data/variables/First-Occurrence-Acute-Myocardial-Infarction)                                                   |            |   |
|     6 | `ALZH`        | [Alzheimer's Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-End-Year-Flag)                                                                          |            | * |
|     7 | `ALZHM`       | [Alzheimer's Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-Mid-Year-Flag)                                                                             |            | * |
|     8 | `ALZHE`       | [First Occurrence of Alzheimer's Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Alzheimers-Disease)                                                                    |            |   |
|     9 | `ALZHDMTA`    | [Alzheimer's Disease and Rltd Disorders or Senile Dementia EOY Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-and-Rltd-Disorders-or-Senile-Dementia-EOY-Flag)           |            | * |
|    10 | `ALZHDMTM`    | [Alzheimer's Disease and Rltd Disorders or Senile Dementia Mid-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-and-Rltd-Disorders-or-Senile-Dementia-Mid-Year-Flag) |            | * |
|    11 | `ALZHDMTE`    | [1st Occrrnce of Alzheimer's Dsease and Rltd Disorders or Senile Dementia](https://www.resdac.org/cms-data/variables/1st-Occrrnce-Alzheimers-Dsease-and-Rltd-Disorders-or-Senile-Dementia)  |            |   |
|    12 | `ATRIALFB`    | [Atrial Fibrillation End-of-Year Flag](https://www.resdac.org/cms-data/variables/Atrial-Fibrillation-End-Year-Flag)                                                                         |            | * |
|    13 | `ATRIALFM`    | [Atrial Fibrillation Mid-Year Flag](https://www.resdac.org/cms-data/variables/Atrial-Fibrillation-Mid-Year-Flag)                                                                            |            | * |
|    14 | `ATRIALFE`    | [First Occurrence of Atrial Fibrillation](https://www.resdac.org/cms-data/variables/First-Occurrence-Atrial-Fibrillation)                                                                   |            |   |
|    15 | `CATARACT`    | [Cataract End-of-Year Flag](https://www.resdac.org/cms-data/variables/Cataract-End-Year-Flag)                                                                                               |            | * |
|    16 | `CATARCTM`    | [Cataract Mid-Year Flag](https://www.resdac.org/cms-data/variables/Cataract-Mid-Year-Flag)                                                                                                  |            | * |
|    17 | `CATARCTE`    | [First Occurrence of Cataract](https://www.resdac.org/cms-data/variables/First-Occurrence-Cataract)                                                                                         |            |   |
|    18 | `CHRNKIDN`    | [Chronic Kidney Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Kidney-Disease-End-Year-Flag)                                                                   |            | * |
|    19 | `CHRNKDNM`    | [Chronic Kidney Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Kidney-Disease-Mid-Year-Flag)                                                                      |            | * |
|    20 | `CHRNKDNE`    | [First Occurrence of Chronic Kidney Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Chronic-Kidney-Disease)                                                             |            |   |
|    21 | `COPD`        | [Chronic Obstructive Pulmonary Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Obstructive-Pulmonary-Disease-End-Year-Flag)                                     |            | * |
|    22 | `COPDM`       | [Chronic Obstructive Pulmonary Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Obstructive-Pulmonary-Disease-Mid-Year-Flag)                                        |            | * |
|    23 | `COPDE`       | [First Occurrence of Chronic Obstructive Pulmonary Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Chronic-Obstructive-Pulmonary-Disease)                               |            |   |
|    24 | `CHF`         | [Heart Failure End-of-Year Flag](https://www.resdac.org/cms-data/variables/Heart-Failure-End-Year-Flag)                                                                                     |            | * |
|    25 | `CHFM`        | [Heart Failure Mid-Year Flag](https://www.resdac.org/cms-data/variables/Heart-Failure-Mid-Year-Flag)                                                                                        |            | * |
|    26 | `CHFE`        | [First Occurrence of Heart Failure](https://www.resdac.org/cms-data/variables/First-Occurrence-Heart-Failure)                                                                               |            |   |
|    27 | `DIABETES`    | [Diabetes End-of-Year Flag](https://www.resdac.org/cms-data/variables/Diabetes-End-Year-Flag)                                                                                               |            | * |
|    28 | `DIABTESM`    | [Diabetes Mid-Year Flag](https://www.resdac.org/cms-data/variables/Diabetes-Mid-Year-Flag)                                                                                                  |            | * |
|    29 | `DIABTESE`    | [First Occurrence of Diabetes](https://www.resdac.org/cms-data/variables/First-Occurrence-Diabetes)                                                                                         |            |   |
|    30 | `GLAUCOMA`    | [Glaucoma End-of-Year Flag](https://www.resdac.org/cms-data/variables/Glaucoma-End-Year-Flag)                                                                                               |            | * |
|    31 | `GLAUCMAM`    | [Glaucoma Mid-Year Flag](https://www.resdac.org/cms-data/variables/Glaucoma-Mid-Year-Flag)                                                                                                  |            | * |
|    32 | `GLAUCMAE`    | [First Occurrence of Glaucoma](https://www.resdac.org/cms-data/variables/First-Occurrence-Glaucoma)                                                                                         |            |   |
|    33 | `HIPFRAC`     | [Hip/Pelvic Fracture End-of-Year Flag](https://www.resdac.org/cms-data/variables/HipPelvic-Fracture-End-Year-Flag)                                                                          |            | * |
|    34 | `HIPFRACM`    | [Hip/Pelvic Fracture Mid-Year Flag](https://www.resdac.org/cms-data/variables/HipPelvic-Fracture-Mid-Year-Flag)                                                                             |            | * |
|    35 | `HIPFRACE`    | [First Occurrence of Hip/Pelvic Fracture](https://www.resdac.org/cms-data/variables/First-Occurrence-HipPelvic-Fracture)                                                                    |            |   |
|    36 | `ISCHMCHT`    | [Ischemic Heart Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Ischemic-Heart-Disease-End-Year-Flag)                                                                   |            | * |
|    37 | `ISCHMCHM`    | [Ischemic Heart Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Ischemic-Heart-Disease-Mid-Year-Flag)                                                                      |            | * |
|    38 | `ISCHMCHE`    | [First Occurrence of Ischemic Heart Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Ischemic-Heart-Disease)                                                             |            |   |
|    39 | `DEPRESSN`    | [Depression End-of-Year Flag](https://www.resdac.org/cms-data/variables/Depression-End-Year-Flag)                                                                                           |            | * |
|    40 | `DEPRSSNM`    | [Depression Mid-Year Flag](https://www.resdac.org/cms-data/variables/Depression-Mid-Year-Flag)                                                                                              |            | * |
|    41 | `DEPRSSNE`    | [First Occurrence of Depression](https://www.resdac.org/cms-data/variables/First-Occurrence-Depression)                                                                                     |            |   |
|    42 | `OSTEOPRS`    | [Osteoporosis End-of-Year Flag](https://www.resdac.org/cms-data/variables/Osteoporosis-End-Year-Flag)                                                                                       |            | * |
|    43 | `OSTEOPRM`    | [Osteoporosis Mid-Year Flag](https://www.resdac.org/cms-data/variables/Osteoporosis-Mid-Year-Flag)                                                                                          |            | * |
|    44 | `OSTEOPRE`    | [First Occurrence of Osteoporosis](https://www.resdac.org/cms-data/variables/First-Occurrence-Osteoporosis)                                                                                 |            |   |
|    45 | `RA_OA`       | [Rheumatoid Arthritis / Osteoarthritis End-of-Year Flag](https://www.resdac.org/cms-data/variables/Rheumatoid-Arthritis-Osteoarthritis-End-Year-Flag)                                       |            | * |
|    46 | `RA_OA_M`     | [Rheumatoid Arthritis / Osteoarthritis Mid-Year Flag](https://www.resdac.org/cms-data/variables/Rheumatoid-Arthritis-Osteoarthritis-Mid-Year-Flag)                                          |            | * |
|    47 | `RA_OA_E`     | [First Occurrence of Rheumatoid Arthritis / Osteoarthritis](https://www.resdac.org/cms-data/variables/First-Occurrence-Rheumatoid-Arthritis-Osteoarthritis)                                 |            | * |
|    48 | `STRKETIA`    | [Stroke / Transient Ischemic Attack End-of-Year Flag](https://www.resdac.org/cms-data/variables/Stroke-Transient-Ischemic-Attack-End-Year-Flag)                                             |            | * |
|    49 | `STRKTIAM`    | [Stroke / Transient Ischemic Attack Mid-Year Flag](https://www.resdac.org/cms-data/variables/Stroke-Transient-Ischemic-Attack-Mid-Year-Flag)                                                |            | * |
|    50 | `STRKTIAE`    | [First Occurrence of Stroke / Transient Ischemic Attack](https://www.resdac.org/cms-data/variables/First-Occurrence-Stroke-Transient-Ischemic-Attack)                                       |            | * |
|    51 | `CNCRBRST`    | [Breast Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Breast-Cancer-End-Year-Flag)                                                                                     |            | * |
|    52 | `CNCRBRSM`    | [Breast Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Breast-Cancer-Mid-Year-Flag)                                                                                        |            | * |
|    53 | `CNCRBRSE`    | [First Occurrence of Breast Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Breast-Cancer)                                                                               |            | * |
|    54 | `CNCRCLRC`    | [Colorectal Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Colorectal-Cancer-End-Year-Flag)                                                                             |            | * |
|    55 | `CNCRCLRM`    | [Colorectal Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Colorectal-Cancer-Mid-Year-Flag)                                                                                |            | * |
|    56 | `CNCRCLRE`    | [First Occurrence of Colorectal Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Colorectal-Cancer)                                                                       |            | * |
|    57 | `CNCRPRST`    | [Prostate Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Prostate-Cancer-End-Year-Flag)                                                                                 |            | * |
|    58 | `CNCRPRSM`    | [Prostate Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Prostate-Cancer-Mid-Year-Flag)                                                                                    |            | * |
|    59 | `CNCRPRSE`    | [First Occurrence of Prostate Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Prostate-Cancer)                                                                           |            |   |
|    60 | `CNCRLUNG`    | [Lung Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Lung-Cancer-End-Year-Flag)                                                                                         |            | * |
|    61 | `CNCRLNGM`    | [Lung Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Lung-Cancer-Mid-Year-Flag)                                                                                            |            | * |
|    62 | `CNCRLNGE`    | [First Occurrence of Lung Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Lung-Cancer)                                                                                   |            | * |
|    63 | `CNCRENDM`    | [Endometrial Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Endometrial-Cancer-End-Year-Flag)                                                                           |            | * |
|    64 | `CNCENDMM`    | [Endometrial Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Endometrial-Cancer-Mid-Year-Flag)                                                                              |            | * |
|    65 | `CNCENDME`    | [First Occurrence of Endometrial Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Endometrial-Cancer)                                                                     |            | * |
|    66 | `ANEMIA`      | [Anemia End Year Flag](https://www.resdac.org/cms-data/variables/Anemia-End-Year-Flag)                                                                                                      |            | * |
|    67 | `ANEMIA_MID`  | [Anemia Mid Year Flag](https://www.resdac.org/cms-data/variables/Anemia-Mid-Year-Flag)                                                                                                      |            | * |
|    68 | `ANEMIA_EVER` | [Anemia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Anemia-First-Ever-Occurrence-Date)                                                                            |            | * |
|    69 | `ASTHMA`      | [Asthma End Year Flag](https://www.resdac.org/cms-data/variables/Asthma-End-Year-Flag)                                                                                                      |            | * |
|    70 | `ASTHMA_MID`  | [Asthma Mid Year Flag](https://www.resdac.org/cms-data/variables/Asthma-Mid-Year-Flag)                                                                                                      |            | * |
|    71 | `ASTHMA_EVER` | [Asthma First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Asthma-First-Ever-Occurrence-Date)                                                                            |            | * |
|    72 | `HYPERL`      | [Hyperlipidemia End Year Flag](https://www.resdac.org/cms-data/variables/Hyperlipidemia-End-Year-Flag)                                                                                      |            | * |
|    73 | `HYPERL_MID`  | [Hyperlipidemia Mid Year Flag](https://www.resdac.org/cms-data/variables/Hyperlipidemia-Mid-Year-Flag)                                                                                      |            | * |
|    74 | `HYPERL_EVER` | [Hyperlipidemia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Hyperlipidemia-First-Ever-Occurrence-Date)                                                            |            |   |
|    75 | `HYPERP`      | [Benign Prostatic Hyperplasia End Year Flag](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-End-Year-Flag)                                                          |            | * |
|    76 | `HYPERP_MID`  | [Benign Prostatic Hyperplasia Mid Year Flag](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-Mid-Year-Flag)                                                          |            | * |
|    77 | `HYPERP_EVER` | [Benign Prostatic Hyperplasia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-First-Ever-Occurrence-Date)                                |            | * |
|    78 | `HYPERT`      | [Hypertension End Year Flag](https://www.resdac.org/cms-data/variables/Hypertension-End-Year-Flag)                                                                                          |            | * |
|    79 | `HYPERT_MID`  | [Hypertension Mid Year Flag](https://www.resdac.org/cms-data/variables/Hypertension-Mid-Year-Flag)                                                                                          |            | * |
|    80 | `HYPERT_EVER` | [Hypertension First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Hypertension-First-Ever-Occurrence-Date)                                                                |            | * |
|    81 | `HYPOTH`      | [Acquired Hypothyroidism End Year Flag](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-End-Year-Flag)                                                                    |            | * |
|    82 | `HYPOTH_MID`  | [Acquired Hypothyroidism Mid Year Flag](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-Mid-Year-Flag)                                                                    |            | * |
|    83 | `HYPOTH_EVER` | [Acquired Hypothyroidism First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-First-Ever-Occurrence-Date)                                          |            | * |

### Other Chronic or Potentially Disabling Conditions

| Index | SAS Name                  | Variable Name                                                                                                                                                                                                                                                    | Limitation | Code Table |
|------:|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `BENE_ID`                 | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                                                                                                                                           |            |   |
|     2 | `RFRNC_YR`                | [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)                                                                                                                                                                                       |            |   |
|     3 | `ACP_MEDICARE`            | [ADHD and Other Conduct Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/adhd-and-other-conduct-disorders-medicare-only-claims)                                                                                                       |            | * |
|     4 | `ACP_MEDICARE_EVER`       | [ADHD and Other Conduct Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/adhd-and-other-conduct-disorders-first-ever-occurrence-date-medicare-only-claim-0)                                                |            | * |
|     5 | `ANXI_MEDICARE`           | [Anxiety Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/anxiety-disorders-medicare-only-claims)                                                                                                                                     |            | * |
|     6 | `ANXI_MEDICARE_EVER`      | [Anxiety Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/anxiety-disorders-first-ever-occurrence-date-medicare-only-claims-0)                                                                             |            | * |
|     7 | `AUTISM_MEDICARE`         | [Autism Spectrum Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/autism-spectrum-disorders-medicare-only-claims)                                                                                                                     |            | * |
|     8 | `AUTISM_MEDICARE_EVER`    | [Autism Spectrum Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/autism-spectrum-disorders-first-ever-occurrence-date-medicare-only-claims-0)                                                             |            | * |
|     9 | `BIPL_MEDICARE`           | [Bipolar Disorder - Medicare Only Claims](https://www.resdac.org/cms-data/variables/bipolar-disorder-medicare-only-claims)                                                                                                                                       |            | * |
|    10 | `BIPL_MEDICARE_EVER`      | [Bipolar Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/bipolar-disorder-first-ever-occurrence-date-medicare-only-claims-0)                                                                               |            | * |
|    11 | `BRAINJ_MEDICARE`         | [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-brain-damage-end-0)           |            | * |
|    12 | `BRAINJ_MEDICARE_EVER`    | [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-brain-damage-first-0)    |            | * |
|    13 | `CERPAL_MEDICARE`         | [Cerebral Palsy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cerebral-palsy-end-year-indicator-medicare-only-claims-0)                                                                                                |            | * |
|    14 | `CERPAL_MEDICARE_EVER`    | [Cerebral Palsy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cerebral-palsy-first-ever-occurrence-date-medicare-only-claims-0)                                                                                   |            |   |
|    15 | `CYSFIB_MEDICARE`         | [Cystic Fibrosis and Other Metabolic Developmental Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cystic-fibrosis-and-other-metabolic-developmental-disorders-end-year-indicator-0)                           |            | * |
|    16 | `CYSFIB_MEDICARE_EVER`    | [Cystic Fibrosis and Other Metabolic Developmental Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cystic-fibrosis-and-other-metabolic-developmental-disorders-first-ever-occurren-0)                     |            |   |
|    17 | `DEPSN_MEDICARE`          | [Major Depressive Affective Disorder End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/major-depressive-affective-disorder-end-year-indicator-medicare-only-claims-0)                                                      |            | * |
|    18 | `DEPSN_MEDICARE_EVER`     | [Major Depressive Affective Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/major-depressive-affective-disorder-first-ever-occurrence-date-medicare-only-0)                                                |            |   |
|    19 | `EPILEP_MEDICARE`         | [Epilepsy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/epilepsy-end-year-indicator-medicare-only-claims-0)                                                                                                            |            | * |
|    20 | `EPILEP_MEDICARE_EVER`    | [Epilepsy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/epilepsy-first-ever-occurrence-date-medicare-only-claims-0)                                                                                               |            |   |
|    21 | `FIBRO_MEDICARE`          | [Fibromyalgia, Chronic Pain and Fatigue End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/fibromyalgia-chronic-pain-and-fatigue-end-year-indicator-medicare-only-claims-0)                                                 |            | * |
|    22 | `FIBRO_MEDICARE_EVER`     | [Fibromyalgia, Chronic Pain and Fatigue First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/fibromyalgia-chronic-pain-and-fatigue-first-ever-occurrence-date-medicare-only-0)                                           |            |   |
|    23 | `HEARIM_MEDICARE`         | [Sensory - Deafness and Hearing Impairment End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-deafness-and-hearing-impairment-end-year-indicator-medicare-only-claims-0)                                            |            | * |
|    24 | `HEARIM_MEDICARE_EVER`    | [Sensory - Deafness and Hearing Impairment First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-deafness-and-hearing-impairment-first-ever-occurrence-date-medicare-onl-0)                                       |            |   |
|    25 | `HEPVIRAL_MEDICARE`       | [Viral Hepatitis (General) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/viral-hepatitis-general-end-year-indicator-medicare-only-claims-0)                                                                            |            | * |
|    26 | `HEPVIRAL_MEDICARE_EVER`  | [Viral Hepatitis (General) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/viral-hepatitis-general-first-ever-occurrence-date-medicare-only-claims-0)                                                               |            |   |
|    27 | `HIVAIDS_MEDICARE`        | [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-e-0)    |            | * |
|    28 | `HIVAIDS_MEDICARE_EVER`   | [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-0) |            |   |
|    29 | `INTDIS_MEDICARE`         | [Intellectual Disabilities and Related Conditions End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/intellectual-disabilities-and-related-conditions-end-year-indicator-medicare-on-0)                                     |            | * |
|    30 | `INTDIS_MEDICARE_EVER`    | [Intellectual Disabilities and Related Conditions First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/intellectual-disabilities-and-related-conditions-first-ever-occurrence-date-0)                                    |            |   |
|    31 | `LEADIS_MEDICARE`         | [Learning Disabilities End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/learning-disabilities-end-year-indicator-medicare-only-claims-0)                                                                                  |            | * |
|    32 | `LEADIS_MEDICARE_EVER`    | [Learning Disabilities First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/learning-disabilities-first-ever-occurrence-date-medicare-only-claims-0)                                                                     |            |   |
|    33 | `LEUKLYMPH_MEDICARE`      | [Leukemias and Lymphomas End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/leukemias-and-lymphomas-end-year-indicator-medicare-only-claims-0)                                                                              |            | * |
|    34 | `LEUKLYMPH_MEDICARE_EVER` | [Leukemias and Lymphomas First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/leukemias-and-lymphomas-first-ever-occurrence-date-medicare-only-claims-0)                                                                 |            |   |
|    35 | `LIVER_MEDICARE`          | [Liver Disease Cirrhosis and Other Liver Conditions (excluding Hepatitis) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-end-year)               |            | * |
|    36 | `LIVER_MEDICARE_EVER`     | [Liver Disease, Cirrhosis and Other Liver Conditions (excluding Hepatitis) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-first-ev-0)       |            |   |
|    37 | `MIGRAINE_MEDICARE`       | [Migraine and other Chronic Headache End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/migraine-and-other-chronic-headache-end-year-indicator-medicare-only-claims-0)                                                      |            | * |
|    38 | `MIGRAINE_MEDICARE_EVER`  | [Migraine and other Chronic Headache First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/migraine-and-other-chronic-headache-first-ever-occurrence-date-medicare-only-0)                                                |            |   |
|    39 | `MOBIMP_MEDICARE`         | [Mobility Impairments End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/mobility-impairments-end-year-indicator-medicare-only-claims-0)                                                                                    |            | * |
|    40 | `MOBIMP_MEDICARE_EVER`    | [Mobility Impairments First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/mobility-impairments-first-ever-occurrence-date-medicare-only-claims-0)                                                                       |            |   |
|    41 | `MULSCL_MEDICARE`         | [Multiple Sclerosis and Transverse Myelitis End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/multiple-sclerosis-and-transverse-myelitis-end-year-indicator-medicare-only-0)                                               |            | * |
|    42 | `MULSCL_MEDICARE_EVER`    | [Multiple Sclerosis and Transverse Myelitis First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/multiple-sclerosis-and-transverse-myelitis-first-ever-occurrence-date-medicare-0)                                       |            |   |
|    43 | `MUSDYS_MEDICARE`         | [Muscular Dystrophy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/muscular-dystrophy-end-year-indicator-medicare-only-claims-0)                                                                                        |            | * |
|    44 | `MUSDYS_MEDICARE_EVER`    | [Muscular Dystrophy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/muscular-dystrophy-first-ever-occurrence-date-medicare-only-claims-0)                                                                           |            |   |
|    45 | `OBESITY_MEDICARE`        | [Obesity End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/obesity-end-year-indicator-medicare-only-claims-0)                                                                                                              |            | * |
|    46 | `OBESITY_MEDICARE_EVER`   | [Obesity First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/obesity-first-ever-occurrence-date-medicare-only-claims-0)                                                                                                 |            |   |
|    47 | `OTHDEL_MEDICARE`         | [Other Developmental Delays End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/other-developmental-delays-end-year-indicator-medicare-only-claims-0)                                                                        |            | * |
|    48 | `OTHDEL_MEDICARE_EVER`    | [Other Developmental Delays First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/other-developmental-delays-first-ever-occurrence-date-medicare-only-claims-0)                                                           |            |   |
|    49 | `PSDS_MEDICARE`           | [Personality Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/personality-disorders-end-year-indicator-medicare-only-claims)                                                                                    |            | * |
|    50 | `PSDS_MEDICARE_EVER`      | [Personality Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/personality-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                       |            |   |
|    51 | `PTRA_MEDICARE`           | [Post-Traumatic Stress Disorder End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/post-traumatic-stress-disorder-end-year-indicator-medicare-only-claims)                                                                  |            | * |
|    52 | `PTRA_MEDICARE_EVER`      | [Post-Traumatic Stress Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/post-traumatic-stress-disorder-first-ever-occurrence-date-medicare-only-claims)                                                     |            |   |
|    53 | `PVD_MEDICARE`            | [Peripheral Vascular Disease End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/peripheral-vascular-disease-end-year-indicator-medicare-only-claims)                                                                        |            | * |
|    54 | `PVD_MEDICARE_EVER`       | [Peripheral Vascular Disease First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/peripheral-vascular-disease-first-ever-occurrence-date-medicare-only-claims)                                                           |            |   |
|    55 | `SCHI_MEDICARE`           | [Schizophrenia End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-end-year-indicator-medicare-only-claims)                                                                                                    |            | * |
|    56 | `SCHI_MEDICARE_EVER`      | [Schizophrenia First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-first-ever-occurrence-date-medicare-only-claims)                                                                                       |            |   |
|    57 | `SCHIOT_MEDICARE`         | [Schizophrenia and Other Psychotic Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-and-other-psychotic-disorders-end-year-indicator-medicare-only)                                               |            | * |
|    58 | `SCHIOT_MEDICARE_EVER`    | [Schizophrenia and Other Psychotic Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-and-other-psychotic-disorders-first-ever-occurrence-date-medicare)                                       |            |   |
|    59 | `SPIBIF_MEDICARE`         | [Spina Bifida and Other Congenital Anomalies of the Nervous System End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spina-bifida-and-other-congenital-anomalies-nervous-system-end-year-indicator)                        |            | * |
|    60 | `SPIBIF_MEDICARE_EVER`    | [Spina Bifida and Other Congenital Anomalies of the Nervous System First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spina-bifida-and-other-congenital-anomalies-nervous-system-first-ever-occurrence)                |            |   |
|    61 | `SPIINJ_MEDICARE`         | [Spinal Cord Injury End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spinal-cord-injury-end-year-indicator-medicare-only-claims)                                                                                          |            | * |
|    62 | `SPIINJ_MEDICARE_EVER`    | [Spinal Cord Injury First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spinal-cord-injury-first-ever-occurrence-date-medicare-only-claims)                                                                             |            |   |
|    63 | `TOBA_MEDICARE`           | [Tobacco Use Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/tobacco-use-disorders-end-year-indicator-medicare-only-claims)                                                                                    |            | * |
|    64 | `TOBA_MEDICARE_EVER`      | [Tobacco Use Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/tobacco-use-disorders-first-ever-occurrence-date-medicare-only-claims)                                                                       |            |   |
|    65 | `ULCERS_MEDICARE`         | [Pressure Ulcers and Chronic Ulcers End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/pressure-ulcers-and-chronic-ulcers-end-year-indicator-medicare-only-claims)                                                          |            | * |
|    66 | `ULCERS_MEDICARE_EVER`    | [Pressure Ulcers and Chronic Ulcers First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/pressure-ulcers-and-chronic-ulcers-first-ever-occurrence-date-medicare-only)                                                    |            |   |
|    67 | `VISUAL_MEDICARE`         | [Sensory - Blindness and Visual Impairment End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-blindness-and-visual-impairment-end-year-indicator-medicare-only-claims)                                              |            | * |
|    68 | `VISUAL_MEDICARE_EVER`    | [Sensory - Blindness and Visual Impairment First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-blindness-and-visual-impairment-first-ever-occurrence-date-medicare-only)                                        |            |   |

### Cost and Use segment

| Index | SAS Name            | Variable Name                                                                                                                              | Limitation | Code Table |
|------:|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:--|
|     1 | `BENE_ID`           | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                     |            |   |
|     2 | `RFRNC_YR`          | [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)                                                                 |            |   |
|     3 | `HOP_MDCR_PMT`      | [Hospital Outpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Medicare-Payments)                   |            | * |
|     4 | `HOP_BENE_PMT`      | [Hospital Outpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Beneficiary-Payments)             |            | * |
|     5 | `HOP_VISITS`        | [Hospital Outpatient Visits](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Visits)                                         |            | * |
|     6 | `HOP_ER_VISITS`     | [Hospital Outpatient Emergency Room Visits](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Emergency-Room-Visits)           |            | * |
|     7 | `ACUTE_MDCR_PMT`    | [Acute Inpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Medicare-Payments)                           |            | * |
|     8 | `ACUTE_BENE_PMT`    | [Acute Inpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Beneficiary-Payments)                     |            | * |
|     9 | `ACUTE_COV_DAYS`    | [Acute Inpatient Covered Days](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Covered-Days)                                     |            | * |
|    10 | `ACUTE_STAYS`       | [Acute Inpatient Stays](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Stays)                                                   |            | * |
|    11 | `IP_ER_VISITS`      | [Inpatient Emergency Room Visits](https://www.resdac.org/cms-data/variables/Inpatient-Emergency-Room-Visits)                               |            | * |
|    12 | `READMISSIONS`      | [Hospital Readmissions](https://www.resdac.org/cms-data/variables/Hospital-Readmissions)                                                   |            | * |
|    13 | `OIP_MDCR_PMT`      | [Other Inpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Inpatient-Medicare-Payments)                           |            | * |
|    14 | `OIP_BENE_PMT`      | [Other Inpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Inpatient-Beneficiary-Payments)                     |            | * |
|    15 | `OIP_COV_DAYS`      | [Other Inpatient Covered Days](https://www.resdac.org/cms-data/variables/Other-Inpatient-Covered-Days)                                     |            | * |
|    16 | `OIP_STAYS`         | [Other Inpatient Stays](https://www.resdac.org/cms-data/variables/Other-Inpatient-Stays)                                                   |            | * |
|    17 | `SNF_MDCR_PMT`      | [Skilled Nursing Facility Medicare Payments](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Medicare-Payments)         |            | * |
|    18 | `SNF_BENE_PMT`      | [Skilled Nursing Facility Beneficiary Payments](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Beneficiary-Payments)   |            | * |
|    19 | `SNF_COV_DAYS`      | [Skilled Nursing Facility Covered Days](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Covered-Days)                   |            | * |
|    20 | `SNF_STAYS`         | [Skilled Nursing Facility Stays](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Stays)                                 |            | * |
|    21 | `HOS_MDCR_PMT`      | [Hospice Medicare Payments](https://www.resdac.org/cms-data/variables/Hospice-Medicare-Payments)                                           |            | * |
|    22 | `HOS_COV_DAYS`      | [Hospice Covered Days](https://www.resdac.org/cms-data/variables/Hospice-Covered-Days)                                                     |            | * |
|    23 | `HOS_STAYS`         | [Hospice Stays](https://www.resdac.org/cms-data/variables/Hospice-Stays)                                                                   |            | * |
|    24 | `HH_MDCR_PMT`       | [Home Health Medicare Payments](https://www.resdac.org/cms-data/variables/Home-Health-Medicare-Payments)                                   |            | * |
|    25 | `HH_VISITS`         | [Home Health Visits](https://www.resdac.org/cms-data/variables/Home-Health-Visits)                                                         |            | * |
|    26 | `ASC_MDCR_PMT`      | [Ambulatory Surgery Center Medicare Payments](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Medicare-Payments)       |            | * |
|    27 | `ASC_BENE_PMT`      | [Ambulatory Surgery Center Beneficiary Payments](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Beneficiary-Payments) |            | * |
|    28 | `ASC_EVENTS`        | [Ambulatory Surgery Center Events](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Events)                             |            | * |
|    29 | `PTB_DRUG_MDCR_PMT` | [Part B Drug Medicare Payments](https://www.resdac.org/cms-data/variables/Part-B-Drug-Medicare-Payments)                                   |            | * |
|    30 | `PTB_DRUG_BENE_PMT` | [Part B Drug Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-B-Drug-Beneficiary-Payments)                             |            | * |
|    31 | `PTB_DRUG_EVENTS`   | [Part B Drug Events](https://www.resdac.org/cms-data/variables/Part-B-Drug-Events)                                                         |            | * |
|    32 | `EM_MDCR_PMT`       | [Evaluation and Management Medicare Payments](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Medicare-Payments)       |            | * |
|    33 | `EM_BENE_PMT`       | [Evaluation and Management Beneficiary Payments](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Beneficiary-Payments) |            | * |
|    34 | `EM_EVENTS`         | [Evaluation and Management Events](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Events)                             |            | * |
|    35 | `ANES_MDCR_PMT`     | [Anesthesia Medicare Payments](https://www.resdac.org/cms-data/variables/Anesthesia-Medicare-Payments)                                     |            | * |
|    36 | `ANES_BENE_PMT`     | [Anesthesia Beneficiary Payments](https://www.resdac.org/cms-data/variables/Anesthesia-Beneficiary-Payments)                               |            | * |
|    37 | `ANES_EVENTS`       | [Anesthesia Events](https://www.resdac.org/cms-data/variables/Anesthesia-Events)                                                           |            | * |
|    38 | `DIALYS_MDCR_PMT`   | [Dialysis Medicare Payments](https://www.resdac.org/cms-data/variables/Dialysis-Medicare-Payments)                                         |            | * |
|    39 | `DIALYS_BENE_PMT`   | [Dialysis Beneficiary Payments](https://www.resdac.org/cms-data/variables/Dialysis-Beneficiary-Payments)                                   |            | * |
|    40 | `DIALYS_EVENTS`     | [Dialysis Events](https://www.resdac.org/cms-data/variables/Dialysis-Events)                                                               |            | * |
|    41 | `OPROC_MDCR_PMT`    | [Other Procedures Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Procedures-Medicare-Payments)                         |            | * |
|    42 | `OPROC_BENE_PMT`    | [Other Procedures Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Procedures-Beneficiary-Payments)                   |            | * |
|    43 | `OPROC_EVENTS`      | [Other Procedures Events](https://www.resdac.org/cms-data/variables/Other-Procedures-Events)                                               |            | * |
|    44 | `IMG_MDCR_PMT`      | [Imaging Medicare Payments](https://www.resdac.org/cms-data/variables/Imaging-Medicare-Payments)                                           |            | * |
|    45 | `IMG_BENE_PMT`      | [Imaging Beneficiary Payments](https://www.resdac.org/cms-data/variables/Imaging-Beneficiary-Payments)                                     |            | * |
|    46 | `IMG_EVENTS`        | [Imaging Events](https://www.resdac.org/cms-data/variables/Imaging-Events)                                                                 |            | * |
|    47 | `TEST_MDCR_PMT`     | [Tests Medicare Payments](https://www.resdac.org/cms-data/variables/Tests-Medicare-Payments)                                               |            | * |
|    48 | `TEST_BENE_PMT`     | [Tests Beneficiary Payments](https://www.resdac.org/cms-data/variables/Tests-Beneficiary-Payments)                                         |            | * |
|    49 | `TEST_EVENTS`       | [Tests Events](https://www.resdac.org/cms-data/variables/Tests-Events)                                                                     |            | * |
|    50 | `DME_MDCR_PMT`      | [Durable Medical Equipment Medicare Payments](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Medicare-Payments)       |            | * |
|    51 | `DME_BENE_PMT`      | [Durable Medical Equipment Beneficiary Payments](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Beneficiary-Payments) |            | * |
|    52 | `DME_EVENTS`        | [Durable Medical Equipment Events](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Events)                             |            | * |
|    53 | `OTHC_MDCR_PMT`     | [Other Part B Carrier Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Medicare-Payments)                 |            | * |
|    54 | `OTHC_BENE_PMT`     | [Other Part B Carrier Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Beneficiary-Payments)           |            | * |
|    55 | `OTHC_EVENTS`       | [Other Part B Carrier Events](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Events)                                       |            | * |
|    56 | `PHYS_MDCR_PMT`     | [Part B Physician Medicare Payments](https://www.resdac.org/cms-data/variables/Part-B-Physician-Medicare-Payments)                         |            | * |
|    57 | `PHYS_BENE_PMT`     | [Part B Physician Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-B-Physician-Beneficiary-Payments)                   |            | * |
|    58 | `PHYS_EVENTS`       | [Part B Physician Events](https://www.resdac.org/cms-data/variables/Part-B-Physician-Events)                                               |            | * |
|    59 | `PTD_MDCR_PMT`      | [Part D Medicare Payments](https://www.resdac.org/cms-data/variables/Part-D-Medicare-Payments)                                             |            | * |
|    60 | `PTD_BENE_PMT`      | [Part D Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-D-Beneficiary-Payments)                                       |            | * |
|    61 | `PTD_EVENTS`        | [Part D Events](https://www.resdac.org/cms-data/variables/Part-D-Events)                                                                   |            | * |
|    62 | `PTD_FILL_CNT`      | [Part D Fill Count](https://www.resdac.org/cms-data/variables/Part-D-Fill-Count)                                                           |            | * |
|    63 | `PTD_TOTAL_RX_CST`  | [Part D Total Prescription Costs](https://www.resdac.org/cms-data/variables/Part-D-Total-Prescription-Costs)                               |            | * |
