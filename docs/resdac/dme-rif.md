# Durable Medical Equipment RIF

??? note "Source"
    [https://www.resdac.org/cms-data/files/dme-rif](https://www.resdac.org/cms-data/files/dme-rif)

## Overview

The Durable Medical Equipment (DME) file contains final action, fee-for-service claims submitted by Durable Medical Equipment suppliers. This file includes:

- diagnosis, (ICD-9 diagnosis),
- services provided (CMS Common Procedure Coding System (HCPCS) codes),
- dates of service,
- reimbursement amounts,
- DME provider number, and
- beneficiary demographic information.

Availability: CY 1999 - 2015

The 12-month run-off final action claims for 2016 will be available in the beginning of 2018.

## Data Documentation

### Durable Medical Equipment RIF

|   Index | SAS Name               | Variable Name                                                                                                                                             | Limitation   | Code Table   |
|--------:|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`              | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                                                                                 |              |              |
|       2 | `CLM_ID`               | [Claim ID](variables.md#claim-id)                                                                                                                         | *            |              |
|       3 | `RIC_CD`               | [NCH Near Line Record Identification Code](variables.md#nch-near-line-record-identification-code)                                                         |              | *            |
|       4 | `CLM_TYPE`             | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                                                                                   |              | *            |
|       5 | `FROM_DT`              | [Claim From Date](variables.md#claim-from-date)                                                                                                           |              |              |
|       6 | `THRU_DT`              | [Claim Through Date](variables.md#claim-through-date)                                                                                                     |              |              |
|       7 | `WKLY_DT`              | [NCH Weekly Claim Processing Date](variables.md#nch-weekly-claim-processing-date)                                                                         |              |              |
|       8 | `ENTRY_CD`             | [Carrier Claim Entry Code](variables.md#carrier-claim-entry-code)                                                                                         |              |              |
|       9 | `DISP_CD`              | [Claim Disposition Code](variables.md#claim-disposition-code)                                                                                             |              | *            |
|      10 | `CARR_NUM`             | [Carrier Number](variables.md#carrier-number)                                                                                                             |              | *            |
|      11 | `PMTDNLCD`             | [Carrier Claim Payment Denial Code](variables.md#carrier-claim-payment-denial-code)                                                                       |              | *            |
|      12 | `PMT_AMT`              | [Claim Payment Amount](variables.md#claim-payment-amount)                                                                                                 | *            |              |
|      13 | `PRPAYAMT`             | [Carrier Claim Primary Payer Paid Amount*](variables.md#carrier-claim-primary-payer-paid-amount)                                                          |              |              |
|      14 | `ASGMNTCD`             | [Carrier Claim Provider Assignment Indicator Switch](variables.md#carrier-claim-provider-assignment-indicator-switch)                                     |              | *            |
|      15 | `PROV_PMT`             | [NCH Claim Provider Payment Amount*](variables.md#nch-claim-provider-payment-amount)                                                                      |              |              |
|      16 | `BENE_PMT`             | [NCH Claim Beneficiary Payment Amount*](variables.md#nch-claim-beneficiary-payment-amount)                                                                |              |              |
|      17 | `SBMTCHRG`             | [NCH Carrier Claim Submitted Charge Amount*](variables.md#nch-carrier-claim-submitted-charge-amount)                                                      |              |              |
|      18 | `ALOWCHRG`             | [NCH Carrier Claim Allowed Charge Amount*](variables.md#nch-carrier-claim-allowed-charge-amount)                                                          |              |              |
|      19 | `DEDAPPLY`             | [Carrier Claim Cash Deductible Applied Amount*](variables.md#carrier-claim-cash-deductible-applied-amount)                                                |              |              |
|      20 | `HCPCS_YR`             | [Carrier Claim HCPCS Year Code](variables.md#carrier-claim-hcpcs-year-code)                                                                               |              |              |
|      21 | `PRNCPAL_DGNS_CD`      | [Claim Principal Diagnosis Code](variables.md#claim-principal-diagnosis-code)                                                                             |              |              |
|      22 | `PRNCPAL_DGNS_VRSN_CD` | [Primary Claim Diagnosis Code Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#primary-claim-diagnosis-code-diagnosis-version-code-icd-9-or-icd-10) |              | *            |
|      23 | `ICD_DGNS_CD1`         | [Claim Diagnosis Code I](variables.md#claim-diagnosis-code-i)                                                                                             |              |              |
|      24 | `ICD_DGNS_VRSN_CD1`    | [Claim Diagnosis Code I Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-i-diagnosis-version-code-icd-9-or-icd-10)             |              | *            |
|      25 | `ICD_DGNS_CD2`         | [Claim Diagnosis Code II](variables.md#claim-diagnosis-code-ii)                                                                                           |              |              |
|      26 | `ICD_DGNS_VRSN_CD2`    | [Claim Diagnosis Code II Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-ii-diagnosis-version-code-icd-9-or-icd-10)           |              | *            |
|      27 | `ICD_DGNS_CD3`         | [Claim Diagnosis Code III](variables.md#claim-diagnosis-code-iii)                                                                                         |              |              |
|      28 | `ICD_DGNS_VRSN_CD3`    | [Claim Diagnosis Code III Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-iii-diagnosis-version-code-icd-9-or-icd-10)         |              | *            |
|      29 | `ICD_DGNS_CD4`         | [Claim Diagnosis Code IV](variables.md#claim-diagnosis-code-iv)                                                                                           |              |              |
|      30 | `ICD_DGNS_VRSN_CD4`    | [Claim Diagnosis Code IV Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-iv-diagnosis-version-code-icd-9-or-icd-10)           |              | *            |
|      31 | `ICD_DGNS_CD5`         | [Claim Diagnosis Code V](variables.md#claim-diagnosis-code-v)                                                                                             |              |              |
|      32 | `ICD_DGNS_VRSN_CD5`    | [Claim Diagnosis Code V Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-v-diagnosis-version-code-icd-9-or-icd-10)             |              | *            |
|      33 | `ICD_DGNS_CD6`         | [Claim Diagnosis Code VI](variables.md#claim-diagnosis-code-vi)                                                                                           |              |              |
|      34 | `ICD_DGNS_VRSN_CD6`    | [Claim Diagnosis Code VI Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-vi-diagnosis-version-code-icd-9-or-icd-10)           |              | *            |
|      35 | `ICD_DGNS_CD7`         | [Claim Diagnosis Code VII](variables.md#claim-diagnosis-code-vii)                                                                                         |              |              |
|      36 | `ICD_DGNS_VRSN_CD7`    | [Claim Diagnosis Code VII Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-vii-diagnosis-version-code-icd-9-or-icd-10)         |              | *            |
|      37 | `ICD_DGNS_CD8`         | [Claim Diagnosis Code VIII](variables.md#claim-diagnosis-code-viii)                                                                                       |              |              |
|      38 | `ICD_DGNS_VRSN_CD8`    | [Claim Diagnosis Code VIII Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-viii-diagnosis-version-code-icd-9-or-icd-10)       |              | *            |
|      39 | `ICD_DGNS_CD9`         | [Claim Diagnosis Code IX](variables.md#claim-diagnosis-code-ix)                                                                                           |              |              |
|      40 | `ICD_DGNS_VRSN_CD9`    | [Claim Diagnosis Code IX Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-ix-diagnosis-version-code-icd-9-or-icd-10)           |              | *            |
|      41 | `ICD_DGNS_CD10`        | [Claim Diagnosis Code X](variables.md#claim-diagnosis-code-x)                                                                                             |              |              |
|      42 | `ICD_DGNS_VRSN_CD10`   | [Claim Diagnosis Code X Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-x-diagnosis-version-code-icd-9-or-icd-10)             |              | *            |
|      43 | `ICD_DGNS_CD11`        | [Claim Diagnosis Code XI](variables.md#claim-diagnosis-code-xi)                                                                                           |              |              |
|      44 | `ICD_DGNS_VRSN_CD11`   | [Claim Diagnosis Code XI Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-xi-diagnosis-version-code-icd-9-or-icd-10)           |              | *            |
|      45 | `ICD_DGNS_CD12`        | [Claim Diagnosis Code XII](variables.md#claim-diagnosis-code-xii)                                                                                         |              |              |
|      46 | `ICD_DGNS_VRSN_CD12`   | [Claim Diagnosis Code XII Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#claim-diagnosis-code-xii-diagnosis-version-code-icd-9-or-icd-10)         |              | *            |
|      47 | `RFR_UPIN`             | [DMERC Claim Ordering Physician UPIN Number](variables.md#dmerc-claim-ordering-physician-upin-number)                                                     |              |              |
|      48 | `RFR_NPI`              | [DMERC Claim Ordering Physician NPI Number](variables.md#dmerc-claim-ordering-physician-npi-number)                                                       |              |              |
|      49 | `CCLTRNUM`             | [Clinical Trial Number](variables.md#clinical-trial-number)                                                                                               |              |              |
|      50 | `DOB_DT`               | [Date of Birth from Claim (Date)](variables.md#date-of-birth-from-claim-date)                                                                             |              |              |
|      51 | `GNDR_CD`              | [Gender Code from Claim](variables.md#gender-code-from-claim)                                                                                             |              | *            |
|      52 | `RACE_CD`              | [Race Code from Claim](variables.md#race-code-from-claim)                                                                                                 |              | *            |
|      53 | `CNTY_CD`              | [County Code from Claim (SSA)](variables.md#county-code-from-claim-ssa)                                                                                   |              |              |
|      54 | `STATE_CD`             | [State Code from Claim (SSA)](variables.md#state-code-from-claim-ssa)                                                                                     |              | *            |
|      55 | `ZIP_CD`               | [Zip Code of Residence from Claim](variables.md#zip-code-of-residence-from-claim)                                                                         |              |              |
|      56 | `CLM_BENE_PD_AMT`      | [Carrier Claim Beneficiary Paid Amount](variables.md#carrier-claim-beneficiary-paid-amount)                                                               |              | *            |

### LINE FILE

|   Index | SAS Name                 | Variable Name                                                                                                                           | Limitation   | Code Table   |
|--------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                                                               |              |              |
|       2 | `CLM_ID`                 | [Claim ID](variables.md#claim-id)                                                                                                       | *            |              |
|       3 | `CLM_LN`                 | [Claim Line Number](variables.md#claim-line-number)                                                                                     |              |              |
|       4 | `CLM_TYPE`               | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                                                                 |              | *            |
|       5 | `THRU_DT`                | [Claim Through Date](variables.md#claim-through-date)                                                                                   |              |              |
|       6 | `TAX_NUM`                | [Line Provider Tax Number](variables.md#line-provider-tax-number)                                                                       |              |              |
|       7 | `HCFASPCL`               | [Line HCFA Provider Specialty Code](variables.md#line-hcfa-provider-specialty-code)                                                     |              | *            |
|       8 | `PRTCPTG`                | [Line Provider Participating Indicator Code](variables.md#line-provider-participating-indicator-code)                                   |              | *            |
|       9 | `SRVC_CNT`               | [Line Service Count](variables.md#line-service-count)                                                                                   |              |              |
|      10 | `TYPSRVCB`               | [Line HCFA Type Service Code](variables.md#line-hcfa-type-service-code)                                                                 |              | *            |
|      11 | `PLCSRVC`                | [Line Place Of Service Code](variables.md#line-place-of-service-code)                                                                   |              | *            |
|      12 | `EXPNSDT1`               | [Line First Expense Date](variables.md#line-first-expense-date)                                                                         |              |              |
|      13 | `EXPNSDT2`               | [Line Last Expense Date](variables.md#line-last-expense-date)                                                                           |              |              |
|      14 | `HCPCS_CD`               | [Health Care Common Procedure Coding System](variables.md#health-care-common-procedure-coding-system)                                   |              |              |
|      15 | `MDFR_CD1`               | [Line HCPCS Initial Modifier Code](variables.md#line-hcpcs-initial-modifier-code)                                                       |              |              |
|      16 | `MDFR_CD2`               | [Line HCPCS Second Modifier Code](variables.md#line-hcpcs-second-modifier-code)                                                         |              |              |
|      17 | `BETOS`                  | [Line NCH BETOS Code](variables.md#line-nch-betos-code)                                                                                 |              | *            |
|      18 | `LINEPMT`                | [Line NCH Payment Amount](variables.md#line-nch-payment-amount)                                                                         |              |              |
|      19 | `LBENPMT`                | [Line Beneficiary Payment Amount](variables.md#line-beneficiary-payment-amount)                                                         |              |              |
|      20 | `LPRVPMT`                | [Line Provider Payment Amount](variables.md#line-provider-payment-amount)                                                               |              |              |
|      21 | `LDEDAMT`                | [Line Beneficiary Part B Deductible Amount](variables.md#line-beneficiary-part-b-deductible-amount)                                     |              |              |
|      22 | `LPRPAYCD`               | [Line Beneficiary Primary Payer Code](variables.md#line-beneficiary-primary-payer-code)                                                 |              | *            |
|      23 | `LPRPDAMT`               | [Line Beneficiary Primary Payer Paid Amount](variables.md#line-beneficiary-primary-payer-paid-amount)                                   |              |              |
|      24 | `COINAMT`                | [Line Coinsurance Amount](variables.md#line-coinsurance-amount)                                                                         |              |              |
|      25 | `PRPYALOW`               | [Line Primary Payer Allowed Charge Amount](variables.md#line-primary-payer-allowed-charge-amount)                                       |              |              |
|      26 | `LSBMTCHG`               | [Line Submitted Charge Amount](variables.md#line-submitted-charge-amount)                                                               |              |              |
|      27 | `LALOWCHG`               | [Line Allowed Charge Amount](variables.md#line-allowed-charge-amount)                                                                   |              |              |
|      28 | `PRCNGIND`               | [Line Processing Indicator Code](variables.md#line-processing-indicator-code)                                                           |              | *            |
|      29 | `PMTINDSW`               | [Line Payment 80%/100% Code](variables.md#line-payment-80100-code)                                                                      |              |              |
|      30 | `DED_SW`                 | [Line Service Deductible Indicator Switch](variables.md#line-service-deductible-indicator-switch)                                       |              | *            |
|      31 | `LINE_ICD_DGNS_CD`       | [Line Diagnosis Code](variables.md#line-diagnosis-code)                                                                                 |              |              |
|      32 | `LINE_ICD_DGNS_VRSN_CD`  | [Line Diagnosis Code Diagnosis Version Code (ICD-9 or ICD-10)](variables.md#line-diagnosis-code-diagnosis-version-code-icd-9-or-icd-10) |              | *            |
|      33 | `DME_PURC`               | [Line DME Purchase Price Amount](variables.md#line-dme-purchase-price-amount)                                                           |              | *            |
|      34 | `SUPLRNUM`               | [DMERC Line Supplier Provider Number](variables.md#dmerc-line-supplier-provider-number)                                                 |              |              |
|      35 | `SUP_NPI`                | [DMERC Line Item Supplier NPI Number](variables.md#dmerc-line-item-supplier-npi-number)                                                 |              |              |
|      36 | `PRCNG_ST`               | [DMERC Line Pricing State Code](variables.md#dmerc-line-pricing-state-code)                                                             |              | *            |
|      37 | `PRVSTATE`               | [DMERC Line Provider State Code](variables.md#dmerc-line-provider-state-code)                                                           |              | *            |
|      38 | `SUP_TYPE`               | [DMERC Line Supplier Type Code](variables.md#dmerc-line-supplier-type-code)                                                             |              | *            |
|      39 | `MDFR_CD3`               | [DMERC Line HCPCS Third Modifier Code](variables.md#dmerc-line-hcpcs-third-modifier-code)                                               |              |              |
|      40 | `MDFR_CD4`               | [DMERC Line HCPCS Fourth Modifier Code](variables.md#dmerc-line-hcpcs-fourth-modifier-code)                                             |              |              |
|      41 | `SCRNSVGS`               | [DMERC Line Screen Savings Amount](variables.md#dmerc-line-screen-savings-amount)                                                       |              | *            |
|      42 | `DME_UNIT`               | [DMERC Line Miles/Time/Units/Services Count](variables.md#dmerc-line-milestimeunitsservices-count)                                      |              |              |
|      43 | `UNIT_IND`               | [DMERC Line Miles/Time/Units/Services Indicator Code](variables.md#dmerc-line-milestimeunitsservices-indicator-code)                    |              | *            |
|      44 | `HCTHGBRS`               | [Hematocrit/Hemoglobin Test Results](variables.md#hematocrithemoglobin-test-results)                                                    |              |              |
|      45 | `HCTHGBTP`               | [Hematocrit/Hemoglobin Test Type Code](variables.md#hematocrithemoglobin-test-type-code)                                                |              | *            |
|      46 | `LNNDCCD`                | [Line National Drug Code](variables.md#line-national-drug-code)                                                                         |              |              |
|      47 | `LINE_OTHR_APLD_IND_CD1` | [Line Other Applied Indicator 1st Code](variables.md#line-other-applied-indicator-1st-code)                                             |              | *            |
|      48 | `LINE_OTHR_APLD_IND_CD2` | [Line Other Applied Indicator 2nd Code](variables.md#line-other-applied-indicator-2nd-code)                                             |              | *            |
|      49 | `LINE_OTHR_APLD_IND_CD3` | [Line Other Applied Indicator 3rd Code](variables.md#line-other-applied-indicator-3rd-code)                                             |              | *            |
|      50 | `LINE_OTHR_APLD_IND_CD4` | [Line Other Applied Indicator 4th Code](variables.md#line-other-applied-indicator-4th-code)                                             |              | *            |
|      51 | `LINE_OTHR_APLD_IND_CD5` | [Line Other Applied Indicator 5th Code](variables.md#line-other-applied-indicator-5th-code)                                             |              | *            |
|      52 | `LINE_OTHR_APLD_IND_CD6` | [Line Other Applied Indicator 6th Code](variables.md#line-other-applied-indicator-6th-code)                                             |              | *            |
|      53 | `LINE_OTHR_APLD_IND_CD7` | [Line Other Applied Indicator 7th Code](variables.md#line-other-applied-indicator-7th-code)                                             |              | *            |
|      54 | `LINE_OTHR_APLD_AMT1`    | [Line Other Applied Amount for 1st Code](variables.md#line-other-applied-amount-for-1st-code)                                           |              | *            |
|      55 | `LINE_OTHR_APLD_AMT2`    | [Line Other Applied Amount for 2nd Code](variables.md#line-other-applied-amount-for-2nd-code)                                           |              | *            |
|      56 | `LINE_OTHR_APLD_AMT3`    | [Line Other Applied Amount for 3rd Code](variables.md#line-other-applied-amount-for-3rd-code)                                           |              | *            |
|      57 | `LINE_OTHR_APLD_AMT4`    | [Line Other Applied Amount for 4th Code](variables.md#line-other-applied-amount-for-4th-code)                                           |              | *            |
|      58 | `LINE_OTHR_APLD_AMT5`    | [Line Other Applied Amount for 5th Code](variables.md#line-other-applied-amount-for-5th-code)                                           |              | *            |
|      59 | `LINE_OTHR_APLD_AMT6`    | [Line Other Applied Amount for 6th Code](variables.md#line-other-applied-amount-for-6th-code)                                           |              | *            |
|      60 | `LINE_OTHR_APLD_AMT7`    | [Line Other Applied Amount for 7th Code](variables.md#line-other-applied-amount-for-7th-code)                                           |              | *            |

### Demonstrations/Innovations Code File

|   Index | SAS Name           | Variable Name                                                               | Limitation   | Code Table   |
|--------:|:-------------------|:----------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`          | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)   |              |              |
|       2 | `CLM_ID`           | [Claim ID](variables.md#claim-id)                                           | *            |              |
|       3 | `CLM_TYPE`         | [NCH Claim Type Code](variables.md#nch-claim-type-code)                     |              | *            |
|       4 | `DEMO_ID_SQNC_NUM` | [Demonstration sequence number](variables.md#demonstration-sequence-number) |              |              |
|       5 | `DEMO_ID_NUM`      | [Demonstration number](variables.md#demonstration-number)                   |              | *            |
|       6 | `DEMO_INFO_TXT`    | [Demo information text](variables.md#demo-information-text)                 |              |              |
