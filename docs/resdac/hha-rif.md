# Home Health Agency RIF

??? note "Source"
    [https://www.resdac.org/cms-data/files/hha-rif](https://www.resdac.org/cms-data/files/hha-rif)

## Overview

The Home Health Agency (HHA) file contains final action, fee-for-service claims submitted by HHA providers. This file includes:

- the number of visits,
- type of visit (skilled-nursing care, home health aides, physical therapy, speech therapy, occupational therapy, and medical social services),
- diagnosis (ICD-9 diagnosis),
- the dates of visits,
- reimbursement amount,
- HHA provider number, and
- beneficiary demographic information.

Availability: CY 1999 - 2015

The 12-month run-off final action claims for 2016 will be available in the beginning of 2018.

## Data Documentation

### Home Health Agency RIF

|   Index | SAS Name                 | Variable Name                                                                                                                                               | Limitation   | Code Table   |
|--------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)                                                                           |              |              |
|       2 | `CLM_ID`                 | [Claim ID](variables/hha-rif.md#claim-id)                                                                                                                   | *            |              |
|       3 | `RIC_CD`                 | [NCH Near Line Record Identification Code](variables/hha-rif.md#nch-near-line-record-identification-code)                                                   |              | *            |
|       4 | `CLM_TYPE`               | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                                                                                             |              | *            |
|       5 | `FROM_DT`                | [Claim From Date](variables/hha-rif.md#claim-from-date)                                                                                                     |              |              |
|       6 | `THRU_DT`                | [Claim Through Date](variables/hha-rif.md#claim-through-date)                                                                                               |              |              |
|       7 | `WKLY_DT`                | [NCH Weekly Claim Processing Date](variables/hha-rif.md#nch-weekly-claim-processing-date)                                                                   |              |              |
|       8 | `FI_CLM_PROC_DT`         | [FI Claim Process Date](variables/hha-rif.md#fi-claim-process-date)                                                                                         |              |              |
|       9 | `PROVIDER`               | [Provider Number](variables/hha-rif.md#provider-number)                                                                                                     |              | *            |
|      10 | `FAC_TYPE`               | [Claim Facility Type Code](variables/hha-rif.md#claim-facility-type-code)                                                                                   |              | *            |
|      11 | `TYPESRVC`               | [Claim Service Classification Type Code](variables/hha-rif.md#claim-service-classification-type-code)                                                       |              | *            |
|      12 | `FREQ_CD`                | [Claim Frequency Code](variables/hha-rif.md#claim-frequency-code)                                                                                           |              | *            |
|      13 | `FI_NUM`                 | [FI Number](variables/hha-rif.md#fi-number)                                                                                                                 |              | *            |
|      14 | `NOPAY_CD`               | [Claim Medicare Non Payment Reason Code](variables/hha-rif.md#claim-medicare-non-payment-reason-code)                                                       |              | *            |
|      15 | `PMT_AMT`                | [Claim Payment Amount](variables/hha-rif.md#claim-payment-amount)                                                                                           | *            |              |
|      16 | `PRPAYAMT`               | [NCH Primary Payer Claim Paid Amount*](variables/hha-rif.md#nch-primary-payer-claim-paid-amount)                                                            |              |              |
|      17 | `PRPAY_CD`               | [NCH Primary Payer Code](variables/hha-rif.md#nch-primary-payer-code)                                                                                       |              | *            |
|      18 | `PRSTATE`                | [NCH Provider State Code](variables/hha-rif.md#nch-provider-state-code)                                                                                     |              | *            |
|      19 | `ORGNPINM`               | [Organization NPI Number](variables/hha-rif.md#organization-npi-number)                                                                                     |              |              |
|      20 | `SRVC_LOC_NPI_NUM`       | [Claim Service Location NPI Number](variables/hha-rif.md#claim-service-location-npi-number)                                                                 |              |              |
|      21 | `AT_UPIN`                | [Claim Attending Physician UPIN Number](variables/hha-rif.md#claim-attending-physician-upin-number)                                                         |              |              |
|      22 | `AT_NPI`                 | [Claim Attending Physician NPI Number](variables/hha-rif.md#claim-attending-physician-npi-number)                                                           |              |              |
|      23 | `AT_PHYSN_SPCLTY_CD`     | [Claim Attending Physician Specialty Code](variables/hha-rif.md#claim-attending-physician-specialty-code)                                                   |              | *            |
|      24 | `OP_NPI`                 | [Claim Operating Physician NPI Number](variables/hha-rif.md#claim-operating-physician-npi-number)                                                           |              |              |
|      25 | `OP_PHYSN_SPCLTY_CD`     | [Claim Operating Physician Specialty Code](variables/hha-rif.md#claim-operating-physician-specialty-code)                                                   |              | *            |
|      26 | `OT_NPI`                 | [Claim Other Physician NPI Number](variables/hha-rif.md#claim-other-physician-npi-number)                                                                   |              |              |
|      27 | `OT_PHYSN_SPCLTY_CD`     | [Claim Other Physician Specialty Code](variables/hha-rif.md#claim-other-physician-specialty-code)                                                           |              | *            |
|      28 | `RNDRNG_PHYSN_NPI`       | [Claim Rendering Physician NPI Number](variables/hha-rif.md#claim-rendering-physician-npi-number)                                                           |              |              |
|      29 | `RNDRNG_PHYSN_SPCLTY_CD` | [Claim Rendering Physician Specialty Code](variables/hha-rif.md#claim-rendering-physician-specialty-code)                                                   |              | *            |
|      30 | `RFR_PHYSN_NPI`          | [Claim Referring Physician NPI Number](variables/hha-rif.md#claim-referring-physician-npi-number)                                                           |              |              |
|      31 | `RFR_PHYSN_SPCLTY_CD`    | [Claim Referring Physician Specialty Code](variables/hha-rif.md#claim-referring-physician-specialty-code)                                                   |              | *            |
|      32 | `STUS_CD`                | [Patient Discharge Status Code](variables/hha-rif.md#patient-discharge-status-code)                                                                         |              | *            |
|      33 | `PPS_IND`                | [Claim PPS Indicator Code](variables/hha-rif.md#claim-pps-indicator-code)                                                                                   |              | *            |
|      34 | `TOT_CHRG`               | [Claim Total Charge Amount](variables/hha-rif.md#claim-total-charge-amount)                                                                                 | *            | *            |
|      35 | `PRNCPAL_DGNS_CD`        | [Claim Principal Diagnosis Code](variables/hha-rif.md#claim-principal-diagnosis-code)                                                                       |              |              |
|      36 | `ICD_DGNS_CD1`           | [Claim Diagnosis Code I](variables/hha-rif.md#claim-diagnosis-code-i)                                                                                       |              |              |
|      37 | `ICD_DGNS_CD2`           | [Claim Diagnosis Code II](variables/hha-rif.md#claim-diagnosis-code-ii)                                                                                     |              |              |
|      38 | `ICD_DGNS_CD3`           | [Claim Diagnosis Code III](variables/hha-rif.md#claim-diagnosis-code-iii)                                                                                   |              |              |
|      39 | `ICD_DGNS_CD4`           | [Claim Diagnosis Code IV](variables/hha-rif.md#claim-diagnosis-code-iv)                                                                                     |              |              |
|      40 | `ICD_DGNS_CD5`           | [Claim Diagnosis Code V](variables/hha-rif.md#claim-diagnosis-code-v)                                                                                       |              |              |
|      41 | `ICD_DGNS_CD6`           | [Claim Diagnosis Code VI](variables/hha-rif.md#claim-diagnosis-code-vi)                                                                                     |              |              |
|      42 | `ICD_DGNS_CD7`           | [Claim Diagnosis Code VII](variables/hha-rif.md#claim-diagnosis-code-vii)                                                                                   |              |              |
|      43 | `ICD_DGNS_CD8`           | [Claim Diagnosis Code VIII](variables/hha-rif.md#claim-diagnosis-code-viii)                                                                                 |              |              |
|      44 | `ICD_DGNS_CD9`           | [Claim Diagnosis Code IX](variables/hha-rif.md#claim-diagnosis-code-ix)                                                                                     |              |              |
|      45 | `ICD_DGNS_CD10`          | [Claim Diagnosis Code X](variables/hha-rif.md#claim-diagnosis-code-x)                                                                                       |              |              |
|      46 | `ICD_DGNS_CD11`          | [Claim Diagnosis Code XI](variables/hha-rif.md#claim-diagnosis-code-xi)                                                                                     |              |              |
|      47 | `ICD_DGNS_CD12`          | [Claim Diagnosis Code XII](variables/hha-rif.md#claim-diagnosis-code-xii)                                                                                   |              |              |
|      48 | `ICD_DGNS_CD13`          | [Claim Diagnosis Code XIII](variables/hha-rif.md#claim-diagnosis-code-xiii)                                                                                 |              |              |
|      49 | `ICD_DGNS_CD14`          | [Claim Diagnosis Code XIV](variables/hha-rif.md#claim-diagnosis-code-xiv)                                                                                   |              |              |
|      50 | `ICD_DGNS_CD15`          | [Claim Diagnosis Code XV](variables/hha-rif.md#claim-diagnosis-code-xv)                                                                                     |              |              |
|      51 | `ICD_DGNS_CD16`          | [Claim Diagnosis Code XVI](variables/hha-rif.md#claim-diagnosis-code-xvi)                                                                                   |              |              |
|      52 | `ICD_DGNS_CD17`          | [Claim Diagnosis Code XVII](variables/hha-rif.md#claim-diagnosis-code-xvii)                                                                                 |              |              |
|      53 | `ICD_DGNS_CD18`          | [Claim Diagnosis Code XVIII](variables/hha-rif.md#claim-diagnosis-code-xviii)                                                                               |              |              |
|      54 | `ICD_DGNS_CD19`          | [Claim Diagnosis Code XIX](variables/hha-rif.md#claim-diagnosis-code-xix)                                                                                   |              |              |
|      55 | `ICD_DGNS_CD20`          | [Claim Diagnosis Code XX](variables/hha-rif.md#claim-diagnosis-code-xx)                                                                                     |              |              |
|      56 | `ICD_DGNS_CD21`          | [Claim Diagnosis Code XXI](variables/hha-rif.md#claim-diagnosis-code-xxi)                                                                                   |              |              |
|      57 | `ICD_DGNS_CD22`          | [Claim Diagnosis Code XXII](variables/hha-rif.md#claim-diagnosis-code-xxii)                                                                                 |              |              |
|      58 | `ICD_DGNS_CD23`          | [Claim Diagnosis Code XXIII](variables/hha-rif.md#claim-diagnosis-code-xxiii)                                                                               |              |              |
|      59 | `ICD_DGNS_CD24`          | [Claim Diagnosis Code XXIV](variables/hha-rif.md#claim-diagnosis-code-xxiv)                                                                                 |              |              |
|      60 | `ICD_DGNS_CD25`          | [Claim Diagnosis Code XXV](variables/hha-rif.md#claim-diagnosis-code-xxv)                                                                                   |              |              |
|      61 | `FST_DGNS_E_CD`          | [First Claim Diagnosis E Code](variables/hha-rif.md#first-claim-diagnosis-e-code)                                                                           |              |              |
|      62 | `ICD_DGNS_E_CD1`         | [Claim Diagnosis E Code I](variables/hha-rif.md#claim-diagnosis-e-code-i)                                                                                   |              |              |
|      63 | `ICD_DGNS_E_CD2`         | [Claim Diagnosis E Code II](variables/hha-rif.md#claim-diagnosis-e-code-ii)                                                                                 |              |              |
|      64 | `ICD_DGNS_E_CD3`         | [Claim Diagnosis E Code III](variables/hha-rif.md#claim-diagnosis-e-code-iii)                                                                               |              |              |
|      65 | `ICD_DGNS_E_CD4`         | [Claim Diagnosis E Code IV](variables/hha-rif.md#claim-diagnosis-e-code-iv)                                                                                 |              |              |
|      66 | `ICD_DGNS_E_CD5`         | [Claim Diagnosis E Code V](variables/hha-rif.md#claim-diagnosis-e-code-v)                                                                                   |              |              |
|      67 | `ICD_DGNS_E_CD6`         | [Claim Diagnosis E Code VI](variables/hha-rif.md#claim-diagnosis-e-code-vi)                                                                                 |              |              |
|      68 | `ICD_DGNS_E_CD7`         | [Claim Diagnosis E Code VII](variables/hha-rif.md#claim-diagnosis-e-code-vii)                                                                               |              |              |
|      69 | `ICD_DGNS_E_CD8`         | [Claim Diagnosis E Code VIII](variables/hha-rif.md#claim-diagnosis-e-code-viii)                                                                             |              |              |
|      70 | `ICD_DGNS_E_CD9`         | [Claim Diagnosis E Code IX](variables/hha-rif.md#claim-diagnosis-e-code-ix)                                                                                 |              |              |
|      71 | `ICD_DGNS_E_CD10`        | [Claim Diagnosis E Code X](variables/hha-rif.md#claim-diagnosis-e-code-x)                                                                                   |              |              |
|      72 | `ICD_DGNS_E_CD11`        | [Claim Diagnosis E Code XI](variables/hha-rif.md#claim-diagnosis-e-code-xi)                                                                                 |              |              |
|      73 | `ICD_DGNS_E_CD12`        | [Claim Diagnosis E Code XII](variables/hha-rif.md#claim-diagnosis-e-code-xii)                                                                               |              |              |
|      74 | `LUPAIND`                | [Claim HHA Low Utilization Payment Adjustment (LUPA) Indicator Code](variables/hha-rif.md#claim-hha-low-utilization-payment-adjustment-lupa-indicator-code) | *            | *            |
|      75 | `HHA_RFRL`               | [Claim HHA Referral Code](variables/hha-rif.md#claim-hha-referral-code)                                                                                     | *            | *            |
|      76 | `VISITCNT`               | [Claim HHA Total Visit Count](variables/hha-rif.md#claim-hha-total-visit-count)                                                                             | *            |              |
|      77 | `HHSTRTDT`               | [Claim HHA Care Start Date](variables/hha-rif.md#claim-hha-care-start-date)                                                                                 |              |              |
|      78 | `DOB_DT`                 | [Date of Birth from Claim (Date)](variables/hha-rif.md#date-of-birth-from-claim-date)                                                                       |              |              |
|      79 | `GNDR_CD`                | [Gender Code from Claim](variables/hha-rif.md#gender-code-from-claim)                                                                                       |              | *            |
|      80 | `RACE_CD`                | [Race Code from Claim](variables/hha-rif.md#race-code-from-claim)                                                                                           |              | *            |
|      81 | `CNTY_CD`                | [County Code from Claim (SSA)](variables/hha-rif.md#county-code-from-claim-ssa)                                                                             |              |              |
|      82 | `STATE_CD`               | [State Code from Claim (SSA)](variables/hha-rif.md#state-code-from-claim-ssa)                                                                               |              | *            |
|      83 | `ZIP_CD`                 | [Zip Code of Residence from Claim](variables/hha-rif.md#zip-code-of-residence-from-claim)                                                                   |              |              |
|      84 | `CLM_MDCL_REC`           | [Claim Medical Record Number](variables/hha-rif.md#claim-medical-record-number)                                                                             |              |              |
|      85 | `QUERY_CD`               | [Claim Query Code](variables/hha-rif.md#claim-query-code)                                                                                                   |              | *            |
|      97 | `ACO_ID_NUM`             | [Claim Accountable Care Organization (ACO) Identification Number](variables/hha-rif.md#claim-accountable-care-organization-aco-identification-number)       |              |              |

### Revenue Center File

|   Index | SAS Name                   | Variable Name                                                                                                                     | Limitation   | Code Table   |
|--------:|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                  | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)                                                 |              |              |
|       2 | `CLM_ID`                   | [Claim ID](variables/hha-rif.md#claim-id)                                                                                         | *            |              |
|       3 | `THRU_DT`                  | [Claim Through Date](variables/hha-rif.md#claim-through-date)                                                                     |              |              |
|       4 | `CLM_LN`                   | [Claim Line Number](variables/hha-rif.md#claim-line-number)                                                                       |              |              |
|       5 | `CLM_TYPE`                 | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                                                                   |              | *            |
|       6 | `REV_CNTR`                 | [Revenue Center Code](variables/hha-rif.md#revenue-center-code)                                                                   |              | *            |
|       7 | `REV_DT`                   | [Revenue Center Date](variables/hha-rif.md#revenue-center-date)                                                                   |              |              |
|       8 | `REVANSI1`                 | [Revenue Center 1st ANSI Code](variables/hha-rif.md#revenue-center-1st-ansi-code)                                                 |              | *            |
|       9 | `APCHIPPS`                 | [Revenue Center APC/HIPPS](variables/hha-rif.md#revenue-center-apchipps)                                                          |              | *            |
|      10 | `HCPCS_CD`                 | [Revenue Center HCFA Common Procedure Coding System](variables/hha-rif.md#revenue-center-hcfa-common-procedure-coding-system)     |              |              |
|      11 | `MDFR_CD1`                 | [Revenue Center HCPCS Initial Modifier Code](variables/hha-rif.md#revenue-center-hcpcs-initial-modifier-code)                     |              |              |
|      12 | `MDFR_CD2`                 | [Revenue Center HCPCS Second Modifier Code](variables/hha-rif.md#revenue-center-hcpcs-second-modifier-code)                       |              |              |
|      13 | `MDFR_CD3`                 | [HCPCS Third Modifier Code](variables/hha-rif.md#hcpcs-third-modifier-code)                                                       |              |              |
|      14 | `PMTMTHD`                  | [Revenue Center Payment Method Indicator Code](variables/hha-rif.md#revenue-center-payment-method-indicator-code)                 |              | *            |
|      15 | `REV_UNIT`                 | [Revenue Center Unit Count](variables/hha-rif.md#revenue-center-unit-count)                                                       |              |              |
|      16 | `REV_RATE`                 | [Revenue Center Rate Amount](variables/hha-rif.md#revenue-center-rate-amount)                                                     |              |              |
|      17 | `REVPMT`                   | [Revenue Center Payment Amount](variables/hha-rif.md#revenue-center-payment-amount)                                               |              |              |
|      18 | `REV_CHRG`                 | [Revenue Center Total Charge Amount](variables/hha-rif.md#revenue-center-total-charge-amount)                                     | *            | *            |
|      19 | `REV_NCVR`                 | [Revenue Center Non-Covered Charge Amount](variables/hha-rif.md#revenue-center-non-covered-charge-amount)                         |              | *            |
|      20 | `REVDEDCD`                 | [Revenue Center Deductible Coinsurance Code](variables/hha-rif.md#revenue-center-deductible-coinsurance-code)                     |              | *            |
|      21 | `REVSTIND`                 | [Revenue Center Status Indicator Code](variables/hha-rif.md#revenue-center-status-indicator-code)                                 |              | *            |
|      22 | `REV_CNTR_NDC_QTY`         | [Revenue Center NDC Quantity](variables/hha-rif.md#revenue-center-ndc-quantity)                                                   |              |              |
|      23 | `REV_CNTR_NDC_QTY_QLFR_CD` | [Revenue Center NDC Quantity Qualifier Code](variables/hha-rif.md#revenue-center-ndc-quantity-qualifier-code)                     |              | *            |
|      24 | `RNDRNG_PHYSN_UPIN`        | [Revenue Center Rendering Physician UPIN](variables/hha-rif.md#revenue-center-rendering-physician-upin)                           |              |              |
|      25 | `RNDRNG_PHYSN_NPI`         | [Revenue Center Rendering Physician NPI](variables/hha-rif.md#revenue-center-rendering-physician-npi)                             |              |              |
|      26 | `RNDRNG_PHYSN_SPCLTY_CD`   | [Rendering Physician Specialty Code](variables/hha-rif.md#rendering-physician-specialty-code)                                     |              | *            |
|      27 | `DSCNTIND`                 | [Revenue Center Discount Indicator Code](variables/hha-rif.md#revenue-center-discount-indicator-code)                             |              | *            |
|      28 | `IDENDC`                   | [Revenue Center IDE, NDC, or UPC Number](variables/hha-rif.md#revenue-center-ide-ndc-or-upc-number)                               |              |              |
|      29 | `RPRVDPMT`                 | [Revenue Center (Medicare) Provider Payment Amount](variables/hha-rif.md#revenue-center-medicare-provider-payment-amount)         |              |              |
|      30 | `PTNTRESP`                 | [Revenue Center Patient Responsibility Payment Amount](variables/hha-rif.md#revenue-center-patient-responsibility-payment-amount) |              | *            |
|      31 | `REV_CNTR_PRCNG_IND_CD`    | [Revenue Center Pricing Indicator Code](variables/hha-rif.md#revenue-center-pricing-indicator-code)                               |              | *            |
|      32 | `THRPY_CAP_IND_CD1`        | [Revenue Center Therapy Cap Indicator 1 Code](variables/hha-rif.md#revenue-center-therapy-cap-indicator-1-code)                   |              | *            |
|      33 | `THRPY_CAP_IND_CD2`        | [Revenue Center Therapy Cap Indicator 2 Code](variables/hha-rif.md#revenue-center-therapy-cap-indicator-2-code)                   |              | *            |

### Condition Code File

|   Index | SAS Name   | Variable Name                                                                                       | Limitation   | Code Table   |
|--------:|:-----------|:----------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)                   |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables/hha-rif.md#claim-id)                                                           | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                                     |              | *            |
|       4 | `RLTCNDSQ` | [Claim Related Condition Code Sequence](variables/hha-rif.md#claim-related-condition-code-sequence) |              |              |
|       5 | `RLT_COND` | [Claim Related Condition Code](variables/hha-rif.md#claim-related-condition-code)                   |              | *            |

### Occurence Code File

|   Index | SAS Name   | Variable Name                                                                                         | Limitation   | Code Table   |
|--------:|:-----------|:------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)                     |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables/hha-rif.md#claim-id)                                                             | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                                       |              | *            |
|       4 | `RLTOCRSQ` | [Claim Related Occurrence Code Sequence](variables/hha-rif.md#claim-related-occurrence-code-sequence) |              |              |
|       5 | `OCRNC_CD` | [Claim Related Occurrence Code](variables/hha-rif.md#claim-related-occurrence-code)                   |              | *            |
|       6 | `OCRNCDT`  | [Claim Related Occurrence Date](variables/hha-rif.md#claim-related-occurrence-date)                   |              |              |

### Span Code File

|   Index | SAS Name   | Variable Name                                                                                 | Limitation   | Code Table   |
|--------:|:-----------|:----------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)             |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables/hha-rif.md#claim-id)                                                     | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                               |              | *            |
|       4 | `RLTSPNSQ` | [Claim Related Span Code Sequence](variables/hha-rif.md#claim-related-span-code-sequence)     |              |              |
|       5 | `SPAN_CD`  | [Claim Occurrence Span Code](variables/hha-rif.md#claim-occurrence-span-code)                 |              | *            |
|       6 | `SPANFROM` | [Claim Occurrence Span From Date](variables/hha-rif.md#claim-occurrence-span-from-date)       |              |              |
|       7 | `SPANTHRU` | [Claim Occurrence Span Through Date](variables/hha-rif.md#claim-occurrence-span-through-date) |              |              |

### Value Code File

|   Index | SAS Name   | Variable Name                                                                               | Limitation   | Code Table   |
|--------:|:-----------|:--------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)           |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables/hha-rif.md#claim-id)                                                   | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                             |              | *            |
|       4 | `RLTVALSQ` | [Claim Related Value Code Sequence](variables/hha-rif.md#claim-related-value-code-sequence) |              |              |
|       5 | `VAL_CD`   | [Claim Value Code](variables/hha-rif.md#claim-value-code)                                   |              | *            |
|       6 | `VAL_AMT`  | [Claim Value Amount](variables/hha-rif.md#claim-value-amount)                               |              | *            |

### Demonstrations/Innovations Code File

|   Index | SAS Name           | Variable Name                                                                       | Limitation   | Code Table   |
|--------:|:-------------------|:------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`          | [Encrypted CCW Beneficiary ID](variables/hha-rif.md#encrypted-ccw-beneficiary-id)   |              |              |
|       2 | `CLM_ID`           | [Claim ID](variables/hha-rif.md#claim-id)                                           | *            |              |
|       3 | `CLM_TYPE`         | [NCH Claim Type Code](variables/hha-rif.md#nch-claim-type-code)                     |              | *            |
|       4 | `DEMO_ID_SQNC_NUM` | [Demonstration sequence number](variables/hha-rif.md#demonstration-sequence-number) |              |              |
|       5 | `DEMO_ID_NUM`      | [Demonstration number](variables/hha-rif.md#demonstration-number)                   |              | *            |
|       6 | `DEMO_INFO_TXT`    | [Demo information text](variables/hha-rif.md#demo-information-text)                 |              |              |
