# Skilled Nursing Facility RIF

??? note "Source"
    [https://www.resdac.org/cms-data/files/snf-rif](https://www.resdac.org/cms-data/files/snf-rif)

## Overview

The Skilled Nursing Facility (SNF) file contains final action, fee-for-service, claims data submitted by SNF providers.

This file includes:

- diagnosis (ICD-9 diagnosis), and
- procedure (ICD-9 procedure code),
- dates of service,
- reimbursement amount,
- SNF provider number, and
- beneficiary demographic information.

Availability: CY 1999 - 2015

The 12-month run-off final action claims for 2016 will be available in the beginning of 2018.

## Data Documentation

### Skilled Nursing Facility RIF

|   Index | SAS Name                 | Variable Name                                                                                                                                 | Limitation   | Code Table   |
|--------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                                                                     |              |              |
|       2 | `CLM_ID`                 | [Claim ID](variables.md#claim-id)                                                                                                             | *            |              |
|       3 | `RIC_CD`                 | [NCH Near Line Record Identification Code](variables.md#nch-near-line-record-identification-code)                                             |              | *            |
|       4 | `CLM_TYPE`               | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                                                                       |              | *            |
|       5 | `FROM_DT`                | [Claim From Date](variables.md#claim-from-date)                                                                                               |              |              |
|       6 | `THRU_DT`                | [Claim Through Date](variables.md#claim-through-date)                                                                                         |              |              |
|       7 | `WKLY_DT`                | [NCH Weekly Claim Processing Date](variables.md#nch-weekly-claim-processing-date)                                                             |              |              |
|       8 | `FI_CLM_PROC_DT`         | [FI Claim Process Date](variables.md#fi-claim-process-date)                                                                                   |              |              |
|       9 | `QUERY_CD`               | [Claim Query Code](variables.md#claim-query-code)                                                                                             |              | *            |
|      10 | `PROVIDER`               | [Provider Number](variables.md#provider-number)                                                                                               |              | *            |
|      11 | `FAC_TYPE`               | [Claim Facility Type Code](variables.md#claim-facility-type-code)                                                                             |              | *            |
|      12 | `TYPESRVC`               | [Claim Service Classification Type Code](variables.md#claim-service-classification-type-code)                                                 |              | *            |
|      13 | `FREQ_CD`                | [Claim Frequency Code](variables.md#claim-frequency-code)                                                                                     |              | *            |
|      14 | `FI_NUM`                 | [FI Number](variables.md#fi-number)                                                                                                           |              | *            |
|      15 | `NOPAY_CD`               | [Claim Medicare Non Payment Reason Code](variables.md#claim-medicare-non-payment-reason-code)                                                 |              | *            |
|      16 | `PMT_AMT`                | [Claim Payment Amount](variables.md#claim-payment-amount)                                                                                     | *            |              |
|      17 | `PRPAYAMT`               | [NCH Primary Payer Claim Paid Amount*](variables.md#nch-primary-payer-claim-paid-amount)                                                      |              |              |
|      18 | `PRPAY_CD`               | [NCH Primary Payer Code](variables.md#nch-primary-payer-code)                                                                                 |              | *            |
|      19 | `ACTIONCD`               | [FI or MAC Claim Action Code](variables.md#fi-or-mac-claim-action-code)                                                                       |              | *            |
|      20 | `PRSTATE`                | [NCH Provider State Code](variables.md#nch-provider-state-code)                                                                               |              | *            |
|      21 | `ORGNPINM`               | [Organization NPI Number](variables.md#organization-npi-number)                                                                               |              |              |
|      22 | `AT_UPIN`                | [Claim Attending Physician UPIN Number](variables.md#claim-attending-physician-upin-number)                                                   |              |              |
|      23 | `AT_NPI`                 | [Claim Attending Physician NPI Number](variables.md#claim-attending-physician-npi-number)                                                     |              |              |
|      24 | `AT_PHYSN_SPCLTY_CD`     | [Claim Attending Physician Specialty Code](variables.md#claim-attending-physician-specialty-code)                                             |              | *            |
|      25 | `OP_UPIN`                | [Claim Operating Physician UPIN Number](variables.md#claim-operating-physician-upin-number)                                                   |              |              |
|      26 | `OP_NPI`                 | [Claim Operating Physician NPI Number](variables.md#claim-operating-physician-npi-number)                                                     |              |              |
|      27 | `OT_NPI`                 | [Claim Other Physician NPI Number](variables.md#claim-other-physician-npi-number)                                                             |              |              |
|      28 | `OT_UPIN`                | [Claim Other Physician UPIN Number](variables.md#claim-other-physician-upin-number)                                                           |              |              |
|      29 | `OP_PHYSN_SPCLTY_CD`     | [Claim Operating Physician Specialty Code](variables.md#claim-operating-physician-specialty-code)                                             |              | *            |
|      30 | `OT_PHYSN_SPCLTY_CD`     | [Claim Other Physician Specialty Code](variables.md#claim-other-physician-specialty-code)                                                     |              | *            |
|      31 | `RNDRNG_PHYSN_NPI`       | [Claim Rendering Physician NPI Number](variables.md#claim-rendering-physician-npi-number)                                                     |              |              |
|      32 | `RNDRNG_PHYSN_SPCLTY_CD` | [Claim Rendering Physician Specialty Code](variables.md#claim-rendering-physician-specialty-code)                                             |              | *            |
|      33 | `MCOPDSW`                | [Claim MCO Paid Switch](variables.md#claim-mco-paid-switch)                                                                                   | *            | *            |
|      34 | `STUS_CD`                | [Patient Discharge Status Code](variables.md#patient-discharge-status-code)                                                                   |              | *            |
|      35 | `PPS_IND`                | [Claim PPS Indicator Code](variables.md#claim-pps-indicator-code)                                                                             |              | *            |
|      36 | `TOT_CHRG`               | [Claim Total Charge Amount](variables.md#claim-total-charge-amount)                                                                           | *            | *            |
|      37 | `ADMSN_DT`               | [Claim Admission Date](variables.md#claim-admission-date)                                                                                     |              |              |
|      38 | `TYPE_ADM`               | [Claim Inpatient Admission Type Code](variables.md#claim-inpatient-admission-type-code)                                                       |              | *            |
|      39 | `SRC_ADMS`               | [Claim Source Inpatient Admission Code](variables.md#claim-source-inpatient-admission-code)                                                   |              | *            |
|      40 | `PTNTSTUS`               | [NCH Patient Status Indicator Code](variables.md#nch-patient-status-indicator-code)                                                           |              | *            |
|      41 | `DED_AMT`                | [NCH Beneficiary Inpatient Deductible Amount](variables.md#nch-beneficiary-inpatient-deductible-amount)                                       |              | *            |
|      42 | `COIN_AMT`               | [NCH Beneficiary Part A Coinsurance Liability Amount](variables.md#nch-beneficiary-part-a-coinsurance-liability-amount)                       |              | *            |
|      43 | `BLDDEDAM`               | [NCH Beneficiary Blood Deductible Liability Amount](variables.md#nch-beneficiary-blood-deductible-liability-amount)                           |              | *            |
|      44 | `NCCHGAMT`               | [NCH Inpatient Noncovered Charge Amount](variables.md#nch-inpatient-noncovered-charge-amount)                                                 |              | *            |
|      45 | `TDEDAMT`                | [NCH Inpatient Total Deduction Amount](variables.md#nch-inpatient-total-deduction-amount)                                                     |              | *            |
|      46 | `CPTL_FSP`               | [Claim PPS Capital FSP Amount](variables.md#claim-pps-capital-fsp-amount)                                                                     |              | *            |
|      47 | `CPTLOUTL`               | [Claim PPS Capital Outlier Amount](variables.md#claim-pps-capital-outlier-amount)                                                             |              | *            |
|      48 | `DISP_SHR`               | [Claim PPS Capital Disproportionate Share Amount](variables.md#claim-pps-capital-disproportionate-share-amount)                               |              |              |
|      49 | `IME_AMT`                | [Claim PPS Capital IME Amount](variables.md#claim-pps-capital-ime-amount)                                                                     |              |              |
|      50 | `CPTL_EXP`               | [Claim PPS Capital Exception Amount](variables.md#claim-pps-capital-exception-amount)                                                         |              | *            |
|      51 | `HLDHRMLS`               | [Claim PPS Old Capital Hold Harmless Amount](variables.md#claim-pps-old-capital-hold-harmless-amount)                                         |              |              |
|      52 | `UTIL_DAY`               | [Claim Utilization Day Count](variables.md#claim-utilization-day-count)                                                                       |              |              |
|      53 | `COIN_DAY`               | [Beneficiary Total Coinsurance Days Count](variables.md#beneficiary-total-coinsurance-days-count)                                             |              |              |
|      54 | `NUTILDAY`               | [Claim Non Utilization Days Count](variables.md#claim-non-utilization-days-count)                                                             |              |              |
|      55 | `BLDFRNSH`               | [NCH Blood Pints Furnished Quantity](variables.md#nch-blood-pints-furnished-quantity)                                                         |              |              |
|      56 | `QLFYFROM`               | [NCH Qualified Stay From Date](variables.md#nch-qualified-stay-from-date)                                                                     |              |              |
|      57 | `QLFYTHRU`               | [NCH Qualify Stay Through Date](variables.md#nch-qualify-stay-through-date)                                                                   |              |              |
|      58 | `NCOVFROM`               | [NCH Verified Noncovered Stay From Date](variables.md#nch-verified-noncovered-stay-from-date)                                                 |              |              |
|      59 | `NCOVTHRU`               | [NCH Verified Noncovered Stay Through Date](variables.md#nch-verified-noncovered-stay-through-date)                                           |              |              |
|      60 | `CARETHRU`               | [NCH Active or Covered Level Care Thru Date](variables.md#nch-active-or-covered-level-care-thru-date)                                         |              |              |
|      61 | `EXHST_DT`               | [NCH Beneficiary Medicare Benefits Exhausted Date](variables.md#nch-beneficiary-medicare-benefits-exhausted-date)                             |              |              |
|      62 | `DSCHRGDT`               | [NCH Beneficiary Discharge Date](variables.md#nch-beneficiary-discharge-date)                                                                 |              |              |
|      63 | `DRG_CD`                 | [Claim Diagnosis Related Group Code](variables.md#claim-diagnosis-related-group-code)                                                         |              |              |
|      64 | `ADMTG_DGNS_CD`          | [Claim Admitting Diagnosis Code](variables.md#claim-admitting-diagnosis-code)                                                                 |              |              |
|      65 | `PRNCPAL_DGNS_CD`        | [Claim Principal Diagnosis Code](variables.md#claim-principal-diagnosis-code)                                                                 |              |              |
|      66 | `ICD_DGNS_CD1`           | [Claim Diagnosis Code I](variables.md#claim-diagnosis-code-i)                                                                                 |              |              |
|      67 | `ICD_DGNS_CD2`           | [Claim Diagnosis Code II](variables.md#claim-diagnosis-code-ii)                                                                               |              |              |
|      68 | `ICD_DGNS_CD3`           | [Claim Diagnosis Code III](variables.md#claim-diagnosis-code-iii)                                                                             |              |              |
|      69 | `ICD_DGNS_CD4`           | [Claim Diagnosis Code IV](variables.md#claim-diagnosis-code-iv)                                                                               |              |              |
|      70 | `ICD_DGNS_CD5`           | [Claim Diagnosis Code V](variables.md#claim-diagnosis-code-v)                                                                                 |              |              |
|      71 | `ICD_DGNS_CD6`           | [Claim Diagnosis Code VI](variables.md#claim-diagnosis-code-vi)                                                                               |              |              |
|      72 | `ICD_DGNS_CD7`           | [Claim Diagnosis Code VII](variables.md#claim-diagnosis-code-vii)                                                                             |              |              |
|      73 | `ICD_DGNS_CD8`           | [Claim Diagnosis Code VIII](variables.md#claim-diagnosis-code-viii)                                                                           |              |              |
|      74 | `ICD_DGNS_CD9`           | [Claim Diagnosis Code IX](variables.md#claim-diagnosis-code-ix)                                                                               |              |              |
|      75 | `ICD_DGNS_CD10`          | [Claim Diagnosis Code X](variables.md#claim-diagnosis-code-x)                                                                                 |              |              |
|      76 | `ICD_DGNS_CD11`          | [Claim Diagnosis Code XI](variables.md#claim-diagnosis-code-xi)                                                                               |              |              |
|      77 | `ICD_DGNS_CD12`          | [Claim Diagnosis Code XII](variables.md#claim-diagnosis-code-xii)                                                                             |              |              |
|      78 | `ICD_DGNS_CD13`          | [Claim Diagnosis Code XIII](variables.md#claim-diagnosis-code-xiii)                                                                           |              |              |
|      79 | `ICD_DGNS_CD14`          | [Claim Diagnosis Code XIV](variables.md#claim-diagnosis-code-xiv)                                                                             |              |              |
|      80 | `ICD_DGNS_CD15`          | [Claim Diagnosis Code XV](variables.md#claim-diagnosis-code-xv)                                                                               |              |              |
|      81 | `ICD_DGNS_CD16`          | [Claim Diagnosis Code XVI](variables.md#claim-diagnosis-code-xvi)                                                                             |              |              |
|      82 | `ICD_DGNS_CD17`          | [Claim Diagnosis Code XVII](variables.md#claim-diagnosis-code-xvii)                                                                           |              |              |
|      83 | `ICD_DGNS_CD18`          | [Claim Diagnosis Code XVIII](variables.md#claim-diagnosis-code-xviii)                                                                         |              |              |
|      84 | `ICD_DGNS_CD19`          | [Claim Diagnosis Code XIX](variables.md#claim-diagnosis-code-xix)                                                                             |              |              |
|      85 | `ICD_DGNS_CD20`          | [Claim Diagnosis Code XX](variables.md#claim-diagnosis-code-xx)                                                                               |              |              |
|      86 | `ICD_DGNS_CD21`          | [Claim Diagnosis Code XXI](variables.md#claim-diagnosis-code-xxi)                                                                             |              |              |
|      87 | `ICD_DGNS_CD22`          | [Claim Diagnosis Code XXII](variables.md#claim-diagnosis-code-xxii)                                                                           |              |              |
|      88 | `ICD_DGNS_CD23`          | [Claim Diagnosis Code XXIII](variables.md#claim-diagnosis-code-xxiii)                                                                         |              |              |
|      89 | `ICD_DGNS_CD24`          | [Claim Diagnosis Code XXIV](variables.md#claim-diagnosis-code-xxiv)                                                                           |              |              |
|      90 | `ICD_DGNS_CD25`          | [Claim Diagnosis Code XXV](variables.md#claim-diagnosis-code-xxv)                                                                             |              |              |
|      91 | `FST_DGNS_E_CD`          | [First Claim Diagnosis E Code](variables.md#first-claim-diagnosis-e-code)                                                                     |              |              |
|      92 | `ICD_DGNS_E_CD1`         | [Claim Diagnosis E Code I](variables.md#claim-diagnosis-e-code-i)                                                                             |              |              |
|      93 | `ICD_DGNS_E_CD2`         | [Claim Diagnosis E Code II](variables.md#claim-diagnosis-e-code-ii)                                                                           |              |              |
|      94 | `ICD_DGNS_E_CD3`         | [Claim Diagnosis E Code III](variables.md#claim-diagnosis-e-code-iii)                                                                         |              |              |
|      95 | `ICD_DGNS_E_CD4`         | [Claim Diagnosis E Code IV](variables.md#claim-diagnosis-e-code-iv)                                                                           |              |              |
|      96 | `ICD_DGNS_E_CD5`         | [Claim Diagnosis E Code V](variables.md#claim-diagnosis-e-code-v)                                                                             |              |              |
|      97 | `ICD_DGNS_E_CD6`         | [Claim Diagnosis E Code VI](variables.md#claim-diagnosis-e-code-vi)                                                                           |              |              |
|      98 | `ICD_DGNS_E_CD7`         | [Claim Diagnosis E Code VII](variables.md#claim-diagnosis-e-code-vii)                                                                         |              |              |
|      99 | `ICD_DGNS_E_CD8`         | [Claim Diagnosis E Code VIII](variables.md#claim-diagnosis-e-code-viii)                                                                       |              |              |
|     100 | `ICD_DGNS_E_CD9`         | [Claim Diagnosis E Code IX](variables.md#claim-diagnosis-e-code-ix)                                                                           |              |              |
|     101 | `ICD_DGNS_E_CD10`        | [Claim Diagnosis E Code X](variables.md#claim-diagnosis-e-code-x)                                                                             |              |              |
|     102 | `ICD_DGNS_E_CD11`        | [Claim Diagnosis E Code XI](variables.md#claim-diagnosis-e-code-xi)                                                                           |              |              |
|     103 | `ICD_DGNS_E_CD12`        | [Claim Diagnosis E Code XII](variables.md#claim-diagnosis-e-code-xii)                                                                         |              |              |
|     104 | `ICD_PRCDR_CD1`          | [Claim Procedure Code I](variables.md#claim-procedure-code-i)                                                                                 |              |              |
|     105 | `PRCDR_DT1`              | [Claim Procedure Code I Date](variables.md#claim-procedure-code-i-date)                                                                       |              |              |
|     106 | `ICD_PRCDR_CD2`          | [Claim Procedure Code II](variables.md#claim-procedure-code-ii)                                                                               |              |              |
|     107 | `PRCDR_DT2`              | [Claim Procedure Code II Date](variables.md#claim-procedure-code-ii-date)                                                                     |              |              |
|     108 | `ICD_PRCDR_CD3`          | [Claim Procedure Code III](variables.md#claim-procedure-code-iii)                                                                             |              |              |
|     109 | `PRCDR_DT3`              | [Claim Procedure Code III Date](variables.md#claim-procedure-code-iii-date)                                                                   |              |              |
|     110 | `ICD_PRCDR_CD4`          | [Claim Procedure Code IV](variables.md#claim-procedure-code-iv)                                                                               |              |              |
|     111 | `PRCDR_DT4`              | [Claim Procedure Code IV Date](variables.md#claim-procedure-code-iv-date)                                                                     |              |              |
|     112 | `ICD_PRCDR_CD5`          | [Claim Procedure Code V](variables.md#claim-procedure-code-v)                                                                                 |              |              |
|     113 | `PRCDR_DT5`              | [Claim Procedure Code V Date](variables.md#claim-procedure-code-v-date)                                                                       |              |              |
|     114 | `ICD_PRCDR_CD6`          | [Claim Procedure Code VI](variables.md#claim-procedure-code-vi)                                                                               |              |              |
|     115 | `PRCDR_DT6`              | [Claim Procedure Code VI Date](variables.md#claim-procedure-code-vi-date)                                                                     |              |              |
|     116 | `ICD_PRCDR_CD7`          | [Claim Procedure Code VII](variables.md#claim-procedure-code-vii)                                                                             |              |              |
|     117 | `PRCDR_DT7`              | [Claim Procedure Code VII Date](variables.md#claim-procedure-code-vii-date)                                                                   |              |              |
|     118 | `ICD_PRCDR_CD8`          | [Claim Procedure Code VIII](variables.md#claim-procedure-code-viii)                                                                           |              |              |
|     119 | `PRCDR_DT8`              | [Claim Procedure Code VIII Date](variables.md#claim-procedure-code-viii-date)                                                                 |              |              |
|     120 | `ICD_PRCDR_CD9`          | [Claim Procedure Code IX](variables.md#claim-procedure-code-ix)                                                                               |              |              |
|     121 | `PRCDR_DT9`              | [Claim Procedure Code IX Date](variables.md#claim-procedure-code-ix-date)                                                                     |              |              |
|     122 | `ICD_PRCDR_CD10`         | [Claim Procedure Code X](variables.md#claim-procedure-code-x)                                                                                 |              |              |
|     123 | `PRCDR_DT10`             | [Claim Procedure Code X Date](variables.md#claim-procedure-code-x-date)                                                                       |              |              |
|     124 | `ICD_PRCDR_CD11`         | [Claim Procedure Code XI](variables.md#claim-procedure-code-xi)                                                                               |              |              |
|     125 | `PRCDR_DT11`             | [Claim Procedure Code XI Date](variables.md#claim-procedure-code-xi-date)                                                                     |              |              |
|     126 | `ICD_PRCDR_CD12`         | [Claim Procedure Code XII](variables.md#claim-procedure-code-xii)                                                                             |              |              |
|     127 | `PRCDR_DT12`             | [Claim Procedure Code XII Date](variables.md#claim-procedure-code-xii-date)                                                                   |              |              |
|     128 | `ICD_PRCDR_CD13`         | [Claim Procedure Code XIII](variables.md#claim-procedure-code-xiii)                                                                           |              |              |
|     129 | `PRCDR_DT13`             | [Claim Procedure Code XIII Date](variables.md#claim-procedure-code-xiii-date)                                                                 |              |              |
|     130 | `ICD_PRCDR_CD14`         | [Claim Procedure Code XIV](variables.md#claim-procedure-code-xiv)                                                                             |              |              |
|     131 | `PRCDR_DT14`             | [Claim Procedure Code XIV Date](variables.md#claim-procedure-code-xiv-date)                                                                   |              |              |
|     132 | `ICD_PRCDR_CD15`         | [Claim Procedure Code XV](variables.md#claim-procedure-code-xv)                                                                               |              |              |
|     133 | `PRCDR_DT15`             | [Claim Procedure Code XV Date](variables.md#claim-procedure-code-xv-date)                                                                     |              |              |
|     134 | `ICD_PRCDR_CD16`         | [Claim Procedure Code XVI](variables.md#claim-procedure-code-xvi)                                                                             |              |              |
|     135 | `PRCDR_DT16`             | [Claim Procedure Code XVI Date](variables.md#claim-procedure-code-xvi-date)                                                                   |              |              |
|     136 | `ICD_PRCDR_CD17`         | [Claim Procedure Code XVII](variables.md#claim-procedure-code-xvii)                                                                           |              |              |
|     137 | `PRCDR_DT17`             | [Claim Procedure Code XVII Date](variables.md#claim-procedure-code-xvii-date)                                                                 |              |              |
|     138 | `ICD_PRCDR_CD18`         | [Claim Procedure Code XVIII](variables.md#claim-procedure-code-xviii)                                                                         |              |              |
|     139 | `PRCDR_DT18`             | [Claim Procedure Code XVIII Date](variables.md#claim-procedure-code-xviii-date)                                                               |              |              |
|     140 | `ICD_PRCDR_CD19`         | [Claim Procedure Code XIX](variables.md#claim-procedure-code-xix)                                                                             |              |              |
|     141 | `PRCDR_DT19`             | [Claim Procedure Code XIX Date](variables.md#claim-procedure-code-xix-date)                                                                   |              |              |
|     142 | `ICD_PRCDR_CD20`         | [Claim Procedure Code XX](variables.md#claim-procedure-code-xx)                                                                               |              |              |
|     143 | `PRCDR_DT20`             | [Claim Procedure Code XX Date](variables.md#claim-procedure-code-xx-date)                                                                     |              |              |
|     144 | `ICD_PRCDR_CD21`         | [Claim Procedure Code XXI](variables.md#claim-procedure-code-xxi)                                                                             |              |              |
|     145 | `PRCDR_DT21`             | [Claim Procedure Code XXI Date](variables.md#claim-procedure-code-xxi-date)                                                                   |              |              |
|     146 | `ICD_PRCDR_CD22`         | [Claim Procedure Code XXII](variables.md#claim-procedure-code-xxii)                                                                           |              |              |
|     147 | `PRCDR_DT22`             | [Claim Procedure Code XXII Date](variables.md#claim-procedure-code-xxii-date)                                                                 |              |              |
|     148 | `ICD_PRCDR_CD23`         | [Claim Procedure Code XXIII](variables.md#claim-procedure-code-xxiii)                                                                         |              |              |
|     149 | `PRCDR_DT23`             | [Claim Procedure Code XXIII Date](variables.md#claim-procedure-code-xxiii-date)                                                               |              |              |
|     150 | `ICD_PRCDR_CD24`         | [Claim Procedure Code XXIV](variables.md#claim-procedure-code-xxiv)                                                                           |              |              |
|     151 | `PRCDR_DT24`             | [Claim Procedure Code XXIV Date](variables.md#claim-procedure-code-xxiv-date)                                                                 |              |              |
|     152 | `ICD_PRCDR_CD25`         | [Claim Procedure Code XXV](variables.md#claim-procedure-code-xxv)                                                                             |              |              |
|     153 | `PRCDR_DT25`             | [Claim Procedure Code XXV Date](variables.md#claim-procedure-code-xxv-date)                                                                   |              |              |
|     154 | `DOB_DT`                 | [Date of Birth from Claim (Date)](variables.md#date-of-birth-from-claim-date)                                                                 |              |              |
|     155 | `GNDR_CD`                | [Gender Code from Claim](variables.md#gender-code-from-claim)                                                                                 |              | *            |
|     156 | `RACE_CD`                | [Race Code from Claim](variables.md#race-code-from-claim)                                                                                     |              | *            |
|     157 | `CNTY_CD`                | [County Code from Claim (SSA)](variables.md#county-code-from-claim-ssa)                                                                       |              |              |
|     158 | `STATE_CD`               | [State Code from Claim (SSA)](variables.md#state-code-from-claim-ssa)                                                                         |              | *            |
|     159 | `ZIP_CD`                 | [Zip Code of Residence from Claim](variables.md#zip-code-of-residence-from-claim)                                                             |              |              |
|     160 | `CLM_MDCL_REC`           | [Claim Medical Record Number](variables.md#claim-medical-record-number)                                                                       |              |              |
|     161 | `CLM_TRTMT_AUTHRZTN_NUM` | [Claim Treatment Authorization Number](variables.md#claim-treatment-authorization-number)                                                     |              | *            |
|     170 | `ACO_ID_NUM`             | [Claim Accountable Care Organization (ACO) Identification Number](variables.md#claim-accountable-care-organization-aco-identification-number) |              |              |

### Revenue Center File

|   Index | SAS Name                   | Variable Name                                                                                                         | Limitation   | Code Table   |
|--------:|:---------------------------|:----------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                  | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                                             |              |              |
|       2 | `CLM_ID`                   | [Claim ID](variables.md#claim-id)                                                                                     | *            |              |
|       3 | `THRU_DT`                  | [Claim Through Date](variables.md#claim-through-date)                                                                 |              |              |
|       4 | `CLM_LN`                   | [Claim Line Number](variables.md#claim-line-number)                                                                   |              |              |
|       5 | `CLM_TYPE`                 | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                                               |              | *            |
|       6 | `REV_CNTR`                 | [Revenue Center Code](variables.md#revenue-center-code)                                                               |              | *            |
|       7 | `HCPCS_CD`                 | [Revenue Center HCFA Common Procedure Coding System](variables.md#revenue-center-hcfa-common-procedure-coding-system) |              |              |
|       8 | `MDFR_CD1`                 | [HCPCS Initial Modifier Code](variables.md#hcpcs-initial-modifier-code)                                               |              |              |
|       9 | `MDFR_CD2`                 | [HCPCS Second Modifier Code](variables.md#hcpcs-second-modifier-code)                                                 |              |              |
|      10 | `MDFR_CD3`                 | [HCPCS Third Modifier Code](variables.md#hcpcs-third-modifier-code)                                                   |              |              |
|      11 | `REV_UNIT`                 | [Revenue Center Unit Count](variables.md#revenue-center-unit-count)                                                   |              |              |
|      12 | `REV_RATE`                 | [Revenue Center Rate Amount](variables.md#revenue-center-rate-amount)                                                 |              |              |
|      13 | `REV_CHRG`                 | [Revenue Center Total Charge Amount](variables.md#revenue-center-total-charge-amount)                                 | *            | *            |
|      14 | `REV_NCVR`                 | [Revenue Center Non-Covered Charge Amount](variables.md#revenue-center-noncovered-charge-amount)                      |              | *            |
|      15 | `REVDEDCD`                 | [Revenue Center Deductible Coinsurance Code](variables.md#revenue-center-deductible-coinsurance-code)                 |              | *            |
|      16 | `REV_CNTR_NDC_QTY`         | [Revenue Center NDC Quantity](variables.md#revenue-center-ndc-quantity)                                               |              |              |
|      17 | `REV_CNTR_NDC_QTY_QLFR_CD` | [Revenue Center NDC Quantity Qualifier Code](variables.md#revenue-center-ndc-quantity-qualifier-code)                 |              | *            |
|      18 | `RNDRNG_PHYSN_UPIN`        | [Revenue Center Rendering Physician UPIN](variables.md#revenue-center-rendering-physician-upin)                       |              |              |
|      19 | `RNDRNG_PHYSN_NPI`         | [Revenue Center Rendering Physician NPI](variables.md#revenue-center-rendering-physician-npi)                         |              |              |
|      20 | `RNDRNG_PHYSN_SPCLTY_CD`   | [Rendering Physician Specialty Code](variables.md#rendering-physician-specialty-code)                                 |              | *            |
|      21 | `IDENDC`                   | [Revenue Center IDE, NDC, or UPC Number](variables.md#revenue-center-ide-ndc-or-upc-number)                           |              |              |
|      22 | `REV_CNTR_PRCNG_IND_CD`    | [Revenue Center Pricing Indicator Code](variables.md#revenue-center-pricing-indicator-code)                           |              | *            |
|      23 | `THRPY_CAP_IND_CD1`        | [Revenue Center Therapy Cap Indicator 1 Code](variables.md#revenue-center-therapy-cap-indicator-1-code)               |              | *            |
|      24 | `THRPY_CAP_IND_CD2`        | [Revenue Center Therapy Cap Indicator 2 Code](variables.md#revenue-center-therapy-cap-indicator-2-code)               |              | *            |

### Condition Code File

|   Index | SAS Name   | Variable Name                                                                               | Limitation   | Code Table   |
|--------:|:-----------|:--------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                   |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables.md#claim-id)                                                           | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                     |              | *            |
|       4 | `RLTCNDSQ` | [Claim Related Condition Code Sequence](variables.md#claim-related-condition-code-sequence) |              |              |
|       5 | `RLT_COND` | [Claim Related Condition Code](variables.md#claim-related-condition-code)                   |              | *            |

### Occurence Code File

|   Index | SAS Name   | Variable Name                                                                                 | Limitation   | Code Table   |
|--------:|:-----------|:----------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)                     |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables.md#claim-id)                                                             | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables.md#nch-claim-type-code)                                       |              | *            |
|       4 | `RLTOCRSQ` | [Claim Related Occurrence Code Sequence](variables.md#claim-related-occurrence-code-sequence) |              |              |
|       5 | `OCRNC_CD` | [Claim Related Occurrence Code](variables.md#claim-related-occurrence-code)                   |              | *            |
|       6 | `OCRNCDT`  | [Claim Related Occurrence Date](variables.md#claim-related-occurrence-date)                   |              |              |

### Span Code File

|   Index | SAS Name   | Variable Name                                                                         | Limitation   | Code Table   |
|--------:|:-----------|:--------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)             |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables.md#claim-id)                                                     | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables.md#nch-claim-type-code)                               |              | *            |
|       4 | `RLTSPNSQ` | [Claim Related Span Code Sequence](variables.md#claim-related-span-code-sequence)     |              |              |
|       5 | `SPAN_CD`  | [Claim Occurrence Span Code](variables.md#claim-occurrence-span-code)                 |              | *            |
|       6 | `SPANFROM` | [Claim Occurrence Span From Date](variables.md#claim-occurrence-span-from-date)       |              |              |
|       7 | `SPANTHRU` | [Claim Occurrence Span Through Date](variables.md#claim-occurrence-span-through-date) |              |              |

### Value Code File

|   Index | SAS Name   | Variable Name                                                                       | Limitation   | Code Table   |
|--------:|:-----------|:------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)           |              |              |
|       2 | `CLM_ID`   | [Claim ID](variables.md#claim-id)                                                   | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](variables.md#nch-claim-type-code)                             |              | *            |
|       4 | `RLTVALSQ` | [Claim Related Value Code Sequence](variables.md#claim-related-value-code-sequence) |              |              |
|       5 | `VAL_CD`   | [Claim Value Code](variables.md#claim-value-code)                                   |              | *            |
|       6 | `VAL_AMT`  | [Claim Value Amount](variables.md#claim-value-amount)                               |              | *            |

### Demonstrations/Innovations Code File

|   Index | SAS Name           | Variable Name                                                               | Limitation   | Code Table   |
|--------:|:-------------------|:----------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`          | [Encrypted CCW Beneficiary ID](variables.md#encrypted-ccw-beneficiary-id)   |              |              |
|       2 | `CLM_ID`           | [Claim ID](variables.md#claim-id)                                           | *            |              |
|       3 | `CLM_TYPE`         | [NCH Claim Type Code](variables.md#nch-claim-type-code)                     |              | *            |
|       4 | `DEMO_ID_SQNC_NUM` | [Demonstration sequence number](variables.md#demonstration-sequence-number) |              |              |
|       5 | `DEMO_ID_NUM`      | [Demonstration number](variables.md#demonstration-number)                   |              | *            |
|       6 | `DEMO_INFO_TXT`    | [Demo information text](variables.md#demo-information-text)                 |              |              |
