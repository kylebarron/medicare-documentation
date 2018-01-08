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

|   Index | SAS Name                 | Variable Name                                                                                                                                                              | Limitation   | Code Table   |
|--------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                                                     |              |              |
|       2 | `CLM_ID`                 | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                                                                             | *            |              |
|       3 | `RIC_CD`                 | [NCH Near Line Record Identification Code](https://www.resdac.org/cms-data/variables/NCH-Near-Line-Record-Identification-Code)                                             |              | *            |
|       4 | `CLM_TYPE`               | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                                                                       |              | *            |
|       5 | `FROM_DT`                | [Claim From Date](https://www.resdac.org/cms-data/variables/Claim-Date)                                                                                                    |              |              |
|       6 | `THRU_DT`                | [Claim Through Date](https://www.resdac.org/cms-data/variables/Claim-Through-Date)                                                                                         |              |              |
|       7 | `WKLY_DT`                | [NCH Weekly Claim Processing Date](https://www.resdac.org/cms-data/variables/NCH-Weekly-Claim-Processing-Date)                                                             |              |              |
|       8 | `FI_CLM_PROC_DT`         | [FI Claim Process Date](https://www.resdac.org/cms-data/variables/FI-Claim-Process-Date)                                                                                   |              |              |
|       9 | `QUERY_CD`               | [Claim Query Code](https://www.resdac.org/cms-data/variables/Claim-Query-Code)                                                                                             |              | *            |
|      10 | `PROVIDER`               | [Provider Number](https://www.resdac.org/cms-data/variables/provider-number)                                                                                               |              | *            |
|      11 | `FAC_TYPE`               | [Claim Facility Type Code](https://www.resdac.org/cms-data/variables/Claim-Facility-Type-Code)                                                                             |              | *            |
|      12 | `TYPESRVC`               | [Claim Service Classification Type Code](https://www.resdac.org/cms-data/variables/Claim-Service-classification-Type-Code)                                                 |              | *            |
|      13 | `FREQ_CD`                | [Claim Frequency Code](https://www.resdac.org/cms-data/variables/Claim-Frequency-Code)                                                                                     |              | *            |
|      14 | `FI_NUM`                 | [FI Number](https://www.resdac.org/cms-data/variables/fi-number)                                                                                                           |              | *            |
|      15 | `NOPAY_CD`               | [Claim Medicare Non Payment Reason Code](https://www.resdac.org/cms-data/variables/claim-medicare-non-payment-reason-code)                                                 |              | *            |
|      16 | `PMT_AMT`                | [Claim Payment Amount](https://www.resdac.org/cms-data/variables/Claim-Payment-Amount-0)                                                                                   | *            |              |
|      17 | `PRPAYAMT`               | [NCH Primary Payer Claim Paid Amount*](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Claim-Paid-Amount)                                                      |              |              |
|      18 | `PRPAY_CD`               | [NCH Primary Payer Code](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Code)                                                                                 |              | *            |
|      19 | `ACTIONCD`               | [FI or MAC Claim Action Code](https://www.resdac.org/cms-data/variables/FI-Claim-Action-Code)                                                                              |              | *            |
|      20 | `PRSTATE`                | [NCH Provider State Code](https://www.resdac.org/cms-data/variables/nch-provider-state-code)                                                                               |              | *            |
|      21 | `ORGNPINM`               | [Organization NPI Number](https://www.resdac.org/cms-data/variables/Organization-NPI-Number)                                                                               |              |              |
|      22 | `AT_UPIN`                | [Claim Attending Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-UPIN-Number)                                                   |              |              |
|      23 | `AT_NPI`                 | [Claim Attending Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-NPI-Number)                                                     |              |              |
|      24 | `AT_PHYSN_SPCLTY_CD`     | [Claim Attending Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-attending-physician-specialty-code)                                             |              | *            |
|      25 | `OP_UPIN`                | [Claim Operating Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Operating-Physician-UPIN-Number)                                                   |              |              |
|      26 | `OP_NPI`                 | [Claim Operating Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Operating-Physician-NPI-Number)                                                     |              |              |
|      27 | `OT_NPI`                 | [Claim Other Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Other-Physician-NPI-Number)                                                             |              |              |
|      28 | `OT_UPIN`                | [Claim Other Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Other-Physician-UPIN-Number)                                                           |              |              |
|      29 | `OP_PHYSN_SPCLTY_CD`     | [Claim Operating Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-operating-physician-specialty-code)                                             |              | *            |
|      30 | `OT_PHYSN_SPCLTY_CD`     | [Claim Other Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-other-physician-specialty-code)                                                     |              | *            |
|      31 | `RNDRNG_PHYSN_NPI`       | [Claim Rendering Physician NPI Number](https://www.resdac.org/cms-data/variables/claim-rendering-physician-npi-number)                                                     |              |              |
|      32 | `RNDRNG_PHYSN_SPCLTY_CD` | [Claim Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-rendering-physician-specialty-code)                                             |              | *            |
|      33 | `MCOPDSW`                | [Claim MCO Paid Switch](https://www.resdac.org/cms-data/variables/Claim-MCO-Paid-Switch)                                                                                   | *            | *            |
|      34 | `STUS_CD`                | [Patient Discharge Status Code](https://www.resdac.org/cms-data/variables/patient-discharge-status-code)                                                                   |              | *            |
|      35 | `PPS_IND`                | [Claim PPS Indicator Code](https://www.resdac.org/cms-data/variables/Claim-PPS-Indicator-Code)                                                                             |              | *            |
|      36 | `TOT_CHRG`               | [Claim Total Charge Amount](https://www.resdac.org/cms-data/variables/Claim-Total-Charge-Amount)                                                                           | *            | *            |
|      37 | `ADMSN_DT`               | [Claim Admission Date](https://www.resdac.org/cms-data/variables/Claim-Admission-Date)                                                                                     |              |              |
|      38 | `TYPE_ADM`               | [Claim Inpatient Admission Type Code](https://www.resdac.org/cms-data/variables/Claim-Inpatient-Admission-Type-Code)                                                       |              | *            |
|      39 | `SRC_ADMS`               | [Claim Source Inpatient Admission Code](https://www.resdac.org/cms-data/variables/Claim-Source-Inpatient-Admission-Code)                                                   |              | *            |
|      40 | `PTNTSTUS`               | [NCH Patient Status Indicator Code](https://www.resdac.org/cms-data/variables/NCH-Patient-Status-Indicator-Code)                                                           |              | *            |
|      41 | `DED_AMT`                | [NCH Beneficiary Inpatient Deductible Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Inpatient-Deductible-Amount)                                       |              | *            |
|      42 | `COIN_AMT`               | [NCH Beneficiary Part A Coinsurance Liability Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Part-Coinsurance-Liability-Amount)                         |              | *            |
|      43 | `BLDDEDAM`               | [NCH Beneficiary Blood Deductible Liability Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Blood-Deductible-Liability-Amount)                           |              | *            |
|      44 | `NCCHGAMT`               | [NCH Inpatient Noncovered Charge Amount](https://www.resdac.org/cms-data/variables/NCH-Inpatient-Noncovered-Charge-Amount)                                                 |              | *            |
|      45 | `TDEDAMT`                | [NCH Inpatient Total Deduction Amount](https://www.resdac.org/cms-data/variables/NCH-Inpatient-Total-Deduction-Amount)                                                     |              | *            |
|      46 | `CPTL_FSP`               | [Claim PPS Capital FSP Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-FSP-Amount)                                                                     |              | *            |
|      47 | `CPTLOUTL`               | [Claim PPS Capital Outlier Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Outlier-Amount)                                                             |              | *            |
|      48 | `DISP_SHR`               | [Claim PPS Capital Disproportionate Share Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Disproportionate-Share-Amount)                               |              |              |
|      49 | `IME_AMT`                | [Claim PPS Capital IME Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-IME-Amount)                                                                     |              |              |
|      50 | `CPTL_EXP`               | [Claim PPS Capital Exception Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Exception-Amount)                                                         |              | *            |
|      51 | `HLDHRMLS`               | [Claim PPS Old Capital Hold Harmless Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Old-Capital-Hold-Harmless-Amount)                                         |              |              |
|      52 | `UTIL_DAY`               | [Claim Utilization Day Count](https://www.resdac.org/cms-data/variables/Claim-Utilization-Day-Count)                                                                       |              |              |
|      53 | `COIN_DAY`               | [Beneficiary Total Coinsurance Days Count](https://www.resdac.org/cms-data/variables/Beneficiary-Total-Coinsurance-Days-Count)                                             |              |              |
|      54 | `NUTILDAY`               | [Claim Non Utilization Days Count](https://www.resdac.org/cms-data/variables/Claim-Non-Utilization-Days-Count)                                                             |              |              |
|      55 | `BLDFRNSH`               | [NCH Blood Pints Furnished Quantity](https://www.resdac.org/cms-data/variables/NCH-Blood-Pints-Furnished-Quantity)                                                         |              |              |
|      56 | `QLFYFROM`               | [NCH Qualified Stay From Date](https://www.resdac.org/cms-data/variables/NCH-Qualified-Stay-Date)                                                                          |              |              |
|      57 | `QLFYTHRU`               | [NCH Qualify Stay Through Date](https://www.resdac.org/cms-data/variables/NCH-Qualify-Stay-Through-Date)                                                                   |              |              |
|      58 | `NCOVFROM`               | [NCH Verified Noncovered Stay From Date](https://www.resdac.org/cms-data/variables/NCH-Verified-Noncovered-Stay-Date)                                                      |              |              |
|      59 | `NCOVTHRU`               | [NCH Verified Noncovered Stay Through Date](https://www.resdac.org/cms-data/variables/NCH-Verified-Noncovered-Stay-Through-Date)                                           |              |              |
|      60 | `CARETHRU`               | [NCH Active or Covered Level Care Thru Date](https://www.resdac.org/cms-data/variables/NCH-Active-or-Covered-Level-Care-Thru-Date)                                         |              |              |
|      61 | `EXHST_DT`               | [NCH Beneficiary Medicare Benefits Exhausted Date](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Medicare-Benefits-Exhausted-Date)                             |              |              |
|      62 | `DSCHRGDT`               | [NCH Beneficiary Discharge Date](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Discharge-Date)                                                                 |              |              |
|      63 | `DRG_CD`                 | [Claim Diagnosis Related Group Code](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Related-Group-Code)                                                         |              |              |
|      64 | `ADMTG_DGNS_CD`          | [Claim Admitting Diagnosis Code](https://www.resdac.org/cms-data/variables/Claim-Admitting-Diagnosis-Code)                                                                 |              |              |
|      65 | `PRNCPAL_DGNS_CD`        | [Claim Principal Diagnosis Code](https://www.resdac.org/cms-data/variables/Primary-Claim-Diagnosis-Code)                                                                   |              |              |
|      66 | `ICD_DGNS_CD1`           | [Claim Diagnosis Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-I)                                                                                 |              |              |
|      67 | `ICD_DGNS_CD2`           | [Claim Diagnosis Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-II)                                                                               |              |              |
|      68 | `ICD_DGNS_CD3`           | [Claim Diagnosis Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-III)                                                                             |              |              |
|      69 | `ICD_DGNS_CD4`           | [Claim Diagnosis Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IV)                                                                               |              |              |
|      70 | `ICD_DGNS_CD5`           | [Claim Diagnosis Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-V)                                                                                 |              |              |
|      71 | `ICD_DGNS_CD6`           | [Claim Diagnosis Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VI)                                                                               |              |              |
|      72 | `ICD_DGNS_CD7`           | [Claim Diagnosis Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VII)                                                                             |              |              |
|      73 | `ICD_DGNS_CD8`           | [Claim Diagnosis Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VIII)                                                                           |              |              |
|      74 | `ICD_DGNS_CD9`           | [Claim Diagnosis Code IX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IX)                                                                               |              |              |
|      75 | `ICD_DGNS_CD10`          | [Claim Diagnosis Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-X)                                                                                 |              |              |
|      76 | `ICD_DGNS_CD11`          | [Claim Diagnosis Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XI)                                                                               |              |              |
|      77 | `ICD_DGNS_CD12`          | [Claim Diagnosis Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XII)                                                                             |              |              |
|      78 | `ICD_DGNS_CD13`          | [Claim Diagnosis Code XIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIII)                                                                           |              |              |
|      79 | `ICD_DGNS_CD14`          | [Claim Diagnosis Code XIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIV-0)                                                                           |              |              |
|      80 | `ICD_DGNS_CD15`          | [Claim Diagnosis Code XV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XV)                                                                               |              |              |
|      81 | `ICD_DGNS_CD16`          | [Claim Diagnosis Code XVI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVI)                                                                             |              |              |
|      82 | `ICD_DGNS_CD17`          | [Claim Diagnosis Code XVII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVII)                                                                           |              |              |
|      83 | `ICD_DGNS_CD18`          | [Claim Diagnosis Code XVIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVIII)                                                                         |              |              |
|      84 | `ICD_DGNS_CD19`          | [Claim Diagnosis Code XIX](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xix)                                                                             |              |              |
|      85 | `ICD_DGNS_CD20`          | [Claim Diagnosis Code XX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XX)                                                                               |              |              |
|      86 | `ICD_DGNS_CD21`          | [Claim Diagnosis Code XXI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXI)                                                                             |              |              |
|      87 | `ICD_DGNS_CD22`          | [Claim Diagnosis Code XXII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXII)                                                                           |              |              |
|      88 | `ICD_DGNS_CD23`          | [Claim Diagnosis Code XXIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIII)                                                                         |              |              |
|      89 | `ICD_DGNS_CD24`          | [Claim Diagnosis Code XXIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIV)                                                                           |              |              |
|      90 | `ICD_DGNS_CD25`          | [Claim Diagnosis Code XXV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXV)                                                                             |              |              |
|      91 | `FST_DGNS_E_CD`          | [First Claim Diagnosis E Code](https://www.resdac.org/cms-data/variables/First-Claim-Diagnosis-E-Code)                                                                     |              |              |
|      92 | `ICD_DGNS_E_CD1`         | [Claim Diagnosis E Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-I)                                                                             |              |              |
|      93 | `ICD_DGNS_E_CD2`         | [Claim Diagnosis E Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-II)                                                                           |              |              |
|      94 | `ICD_DGNS_E_CD3`         | [Claim Diagnosis E Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-III)                                                                         |              |              |
|      95 | `ICD_DGNS_E_CD4`         | [Claim Diagnosis E Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-IV)                                                                           |              |              |
|      96 | `ICD_DGNS_E_CD5`         | [Claim Diagnosis E Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-V)                                                                             |              |              |
|      97 | `ICD_DGNS_E_CD6`         | [Claim Diagnosis E Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VI)                                                                           |              |              |
|      98 | `ICD_DGNS_E_CD7`         | [Claim Diagnosis E Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VII)                                                                         |              |              |
|      99 | `ICD_DGNS_E_CD8`         | [Claim Diagnosis E Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VIII)                                                                       |              |              |
|     100 | `ICD_DGNS_E_CD9`         | [Claim Diagnosis E Code IX](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-ix)                                                                           |              |              |
|     101 | `ICD_DGNS_E_CD10`        | [Claim Diagnosis E Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-X)                                                                             |              |              |
|     102 | `ICD_DGNS_E_CD11`        | [Claim Diagnosis E Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XI)                                                                           |              |              |
|     103 | `ICD_DGNS_E_CD12`        | [Claim Diagnosis E Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XII)                                                                         |              |              |
|     104 | `ICD_PRCDR_CD1`          | [Claim Procedure Code I](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-I)                                                                                 |              |              |
|     105 | `PRCDR_DT1`              | [Claim Procedure Code I Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-I-Date)                                                                       |              |              |
|     106 | `ICD_PRCDR_CD2`          | [Claim Procedure Code II](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-II)                                                                               |              |              |
|     107 | `PRCDR_DT2`              | [Claim Procedure Code II Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-II-Date)                                                                     |              |              |
|     108 | `ICD_PRCDR_CD3`          | [Claim Procedure Code III](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-III)                                                                             |              |              |
|     109 | `PRCDR_DT3`              | [Claim Procedure Code III Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-III-Date)                                                                   |              |              |
|     110 | `ICD_PRCDR_CD4`          | [Claim Procedure Code IV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IV)                                                                               |              |              |
|     111 | `PRCDR_DT4`              | [Claim Procedure Code IV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IV-Date)                                                                     |              |              |
|     112 | `ICD_PRCDR_CD5`          | [Claim Procedure Code V](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-V)                                                                                 |              |              |
|     113 | `PRCDR_DT5`              | [Claim Procedure Code V Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-V-Date)                                                                       |              |              |
|     114 | `ICD_PRCDR_CD6`          | [Claim Procedure Code VI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VI)                                                                               |              |              |
|     115 | `PRCDR_DT6`              | [Claim Procedure Code VI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VI-Date)                                                                     |              |              |
|     116 | `ICD_PRCDR_CD7`          | [Claim Procedure Code VII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VII)                                                                             |              |              |
|     117 | `PRCDR_DT7`              | [Claim Procedure Code VII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-CodeVII-Date)                                                                    |              |              |
|     118 | `ICD_PRCDR_CD8`          | [Claim Procedure Code VIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VIII)                                                                           |              |              |
|     119 | `PRCDR_DT8`              | [Claim Procedure Code VIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VIII-Date)                                                                 |              |              |
|     120 | `ICD_PRCDR_CD9`          | [Claim Procedure Code IX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IX)                                                                               |              |              |
|     121 | `PRCDR_DT9`              | [Claim Procedure Code IX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IX-Date)                                                                     |              |              |
|     122 | `ICD_PRCDR_CD10`         | [Claim Procedure Code X](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-X)                                                                                 |              |              |
|     123 | `PRCDR_DT10`             | [Claim Procedure Code X Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-X-Date)                                                                       |              |              |
|     124 | `ICD_PRCDR_CD11`         | [Claim Procedure Code XI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XI)                                                                               |              |              |
|     125 | `PRCDR_DT11`             | [Claim Procedure Code XI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XI-Date)                                                                     |              |              |
|     126 | `ICD_PRCDR_CD12`         | [Claim Procedure Code XII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XII)                                                                             |              |              |
|     127 | `PRCDR_DT12`             | [Claim Procedure Code XII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XII-Date)                                                                   |              |              |
|     128 | `ICD_PRCDR_CD13`         | [Claim Procedure Code XIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIII)                                                                           |              |              |
|     129 | `PRCDR_DT13`             | [Claim Procedure Code XIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIII-Date)                                                                 |              |              |
|     130 | `ICD_PRCDR_CD14`         | [Claim Procedure Code XIV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIV)                                                                             |              |              |
|     131 | `PRCDR_DT14`             | [Claim Procedure Code XIV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIV-Date)                                                                   |              |              |
|     132 | `ICD_PRCDR_CD15`         | [Claim Procedure Code XV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XV)                                                                               |              |              |
|     133 | `PRCDR_DT15`             | [Claim Procedure Code XV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XV-Date)                                                                     |              |              |
|     134 | `ICD_PRCDR_CD16`         | [Claim Procedure Code XVI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVI)                                                                             |              |              |
|     135 | `PRCDR_DT16`             | [Claim Procedure Code XVI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVI-Date)                                                                   |              |              |
|     136 | `ICD_PRCDR_CD17`         | [Claim Procedure Code XVII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVII)                                                                           |              |              |
|     137 | `PRCDR_DT17`             | [Claim Procedure Code XVII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVII-Date)                                                                 |              |              |
|     138 | `ICD_PRCDR_CD18`         | [Claim Procedure Code XVIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVIII)                                                                         |              |              |
|     139 | `PRCDR_DT18`             | [Claim Procedure Code XVIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVIII-Date)                                                               |              |              |
|     140 | `ICD_PRCDR_CD19`         | [Claim Procedure Code XIX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIX)                                                                             |              |              |
|     141 | `PRCDR_DT19`             | [Claim Procedure Code XIX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIX-Date)                                                                   |              |              |
|     142 | `ICD_PRCDR_CD20`         | [Claim Procedure Code XX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XX)                                                                               |              |              |
|     143 | `PRCDR_DT20`             | [Claim Procedure Code XX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XX-Date)                                                                     |              |              |
|     144 | `ICD_PRCDR_CD21`         | [Claim Procedure Code XXI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXI)                                                                             |              |              |
|     145 | `PRCDR_DT21`             | [Claim Procedure Code XXI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXI-Date)                                                                   |              |              |
|     146 | `ICD_PRCDR_CD22`         | [Claim Procedure Code XXII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXII)                                                                           |              |              |
|     147 | `PRCDR_DT22`             | [Claim Procedure Code XXII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXII-Date)                                                                 |              |              |
|     148 | `ICD_PRCDR_CD23`         | [Claim Procedure Code XXIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIII)                                                                         |              |              |
|     149 | `PRCDR_DT23`             | [Claim Procedure Code XXIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIII-Date)                                                               |              |              |
|     150 | `ICD_PRCDR_CD24`         | [Claim Procedure Code XXIV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIV)                                                                           |              |              |
|     151 | `PRCDR_DT24`             | [Claim Procedure Code XXIV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIV-Date)                                                                 |              |              |
|     152 | `ICD_PRCDR_CD25`         | [Claim Procedure Code XXV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXV)                                                                             |              |              |
|     153 | `PRCDR_DT25`             | [Claim Procedure Code XXV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXV-Date)                                                                   |              |              |
|     154 | `DOB_DT`                 | [Date of Birth from Claim (Date)](https://www.resdac.org/cms-data/variables/Date-Birth-Claim-Date)                                                                         |              |              |
|     155 | `GNDR_CD`                | [Gender Code from Claim](https://www.resdac.org/cms-data/variables/Gender-Code-Claim)                                                                                      |              | *            |
|     156 | `RACE_CD`                | [Race Code from Claim](https://www.resdac.org/cms-data/variables/Race-Code-Claim)                                                                                          |              | *            |
|     157 | `CNTY_CD`                | [County Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/County-Code-Claim-SSA)                                                                            |              |              |
|     158 | `STATE_CD`               | [State Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/state-code-claim-ssa)                                                                              |              | *            |
|     159 | `ZIP_CD`                 | [Zip Code of Residence from Claim](https://www.resdac.org/cms-data/variables/Zip-Code-Residence-Claim)                                                                     |              |              |
|     160 | `CLM_MDCL_REC`           | [Claim Medical Record Number](https://www.resdac.org/cms-data/variables/Claim-Medical-Record-Number)                                                                       |              |              |
|     161 | `CLM_TRTMT_AUTHRZTN_NUM` | [Claim Treatment Authorization Number](https://www.resdac.org/cms-data/variables/claim-treatment-authorization-number)                                                     |              | *            |
|     170 | `ACO_ID_NUM`             | [Claim Accountable Care Organization (ACO) Identification Number](https://www.resdac.org/cms-data/variables/claim-accountable-care-organization-aco-identification-number) |              |              |

### Revenue Center File

|   Index | SAS Name                   | Variable Name                                                                                                                                      | Limitation   | Code Table   |
|--------:|:---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                             |              |              |
|       2 | `CLM_ID`                   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                                                     | *            |              |
|       3 | `THRU_DT`                  | [Claim Through Date](https://www.resdac.org/cms-data/variables/Claim-Through-Date)                                                                 |              |              |
|       4 | `CLM_LN`                   | [Claim Line Number](https://www.resdac.org/cms-data/variables/Claim-Line-Number)                                                                   |              |              |
|       5 | `CLM_TYPE`                 | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                                               |              | *            |
|       6 | `REV_CNTR`                 | [Revenue Center Code](https://www.resdac.org/cms-data/variables/revenue-center-code)                                                               |              | *            |
|       7 | `HCPCS_CD`                 | [Revenue Center HCFA Common Procedure Coding System](https://www.resdac.org/cms-data/variables/Revenue-Center-HCFA-Common-Procedure-Coding-System) |              |              |
|       8 | `MDFR_CD1`                 | [HCPCS Initial Modifier Code](https://www.resdac.org/cms-data/variables/hcpcs-initial-modifier-code)                                               |              |              |
|       9 | `MDFR_CD2`                 | [HCPCS Second Modifier Code](https://www.resdac.org/cms-data/variables/hcpcs-second-modifier-code)                                                 |              |              |
|      10 | `MDFR_CD3`                 | [HCPCS Third Modifier Code](https://www.resdac.org/cms-data/variables/hcpcs-third-modifier-code)                                                   |              |              |
|      11 | `REV_UNIT`                 | [Revenue Center Unit Count](https://www.resdac.org/cms-data/variables/Revenue-Center-Unit-Count)                                                   |              |              |
|      12 | `REV_RATE`                 | [Revenue Center Rate Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Rate-Amount)                                                 |              |              |
|      13 | `REV_CHRG`                 | [Revenue Center Total Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Total-Charge-Amount)                                 | *            | *            |
|      14 | `REV_NCVR`                 | [Revenue Center Non-Covered Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Non-Covered-Charge-Amount)                     |              | *            |
|      15 | `REVDEDCD`                 | [Revenue Center Deductible Coinsurance Code](https://www.resdac.org/cms-data/variables/Revenue-Center-Deductible-Coinsurance-Code)                 |              | *            |
|      16 | `REV_CNTR_NDC_QTY`         | [Revenue Center NDC Quantity](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity)                                               |              |              |
|      17 | `REV_CNTR_NDC_QTY_QLFR_CD` | [Revenue Center NDC Quantity Qualifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity-Qualifier-Code)                 |              | *            |
|      18 | `RNDRNG_PHYSN_UPIN`        | [Revenue Center Rendering Physician UPIN](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-UPIN)                       |              |              |
|      19 | `RNDRNG_PHYSN_NPI`         | [Revenue Center Rendering Physician NPI](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-NPI)                         |              |              |
|      20 | `RNDRNG_PHYSN_SPCLTY_CD`   | [Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/rendering-physician-specialty-code)                                 |              | *            |
|      21 | `IDENDC`                   | [Revenue Center IDE, NDC, or UPC Number](https://www.resdac.org/cms-data/variables/revenue-center-ide-ndc-or-upc-number)                           |              |              |
|      22 | `REV_CNTR_PRCNG_IND_CD`    | [Revenue Center Pricing Indicator Code](https://www.resdac.org/cms-data/variables/revenue-center-pricing-indicator-code-0)                         |              | *            |
|      23 | `THRPY_CAP_IND_CD1`        | [Revenue Center Therapy Cap Indicator 1 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-1-code)               |              | *            |
|      24 | `THRPY_CAP_IND_CD2`        | [Revenue Center Therapy Cap Indicator 2 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-2-code)               |              | *            |

### Condition Code File

|   Index | SAS Name   | Variable Name                                                                                                            | Limitation   | Code Table   |
|--------:|:-----------|:-------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                   |              |              |
|       2 | `CLM_ID`   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                           | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                     |              | *            |
|       4 | `RLTCNDSQ` | [Claim Related Condition Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Condition-Code-Sequence) |              |              |
|       5 | `RLT_COND` | [Claim Related Condition Code](https://www.resdac.org/cms-data/variables/claim-related-condition-code)                   |              | *            |

### Occurence Code File

|   Index | SAS Name   | Variable Name                                                                                                              | Limitation   | Code Table   |
|--------:|:-----------|:---------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                     |              |              |
|       2 | `CLM_ID`   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                             | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                       |              | *            |
|       4 | `RLTOCRSQ` | [Claim Related Occurrence Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Occurrence-Code-Sequence) |              |              |
|       5 | `OCRNC_CD` | [Claim Related Occurrence Code](https://www.resdac.org/cms-data/variables/claim-related-occurrence-code)                   |              | *            |
|       6 | `OCRNCDT`  | [Claim Related Occurrence Date](https://www.resdac.org/cms-data/variables/Claim-Related-Occurrence-Date)                   |              |              |

### Span Code File

|   Index | SAS Name   | Variable Name                                                                                                      | Limitation   | Code Table   |
|--------:|:-----------|:-------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)             |              |              |
|       2 | `CLM_ID`   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                     | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                               |              | *            |
|       4 | `RLTSPNSQ` | [Claim Related Span Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Span-Code-Sequence)     |              |              |
|       5 | `SPAN_CD`  | [Claim Occurrence Span Code](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Code)                 |              | *            |
|       6 | `SPANFROM` | [Claim Occurrence Span From Date](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Date)            |              |              |
|       7 | `SPANTHRU` | [Claim Occurrence Span Through Date](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Through-Date) |              |              |

### Value Code File

|   Index | SAS Name   | Variable Name                                                                                                    | Limitation   | Code Table   |
|--------:|:-----------|:-----------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)           |              |              |
|       2 | `CLM_ID`   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                   | *            |              |
|       3 | `CLM_TYPE` | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                             |              | *            |
|       4 | `RLTVALSQ` | [Claim Related Value Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Value-Code-Sequence) |              |              |
|       5 | `VAL_CD`   | [Claim Value Code](https://www.resdac.org/cms-data/variables/claim-value-code)                                   |              | *            |
|       6 | `VAL_AMT`  | [Claim Value Amount](https://www.resdac.org/cms-data/variables/Claim-Value-Amount)                               |              | *            |

### Demonstrations/Innovations Code File

|   Index | SAS Name           | Variable Name                                                                                            | Limitation   | Code Table   |
|--------:|:-------------------|:---------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`          | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)   |              |              |
|       2 | `CLM_ID`           | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                           | *            |              |
|       3 | `CLM_TYPE`         | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                     |              | *            |
|       4 | `DEMO_ID_SQNC_NUM` | [Demonstration sequence number](https://www.resdac.org/cms-data/variables/demonstration-sequence-number) |              |              |
|       5 | `DEMO_ID_NUM`      | [Demonstration number](https://www.resdac.org/cms-data/variables/demonstration-number)                   |              | *            |
|       6 | `DEMO_INFO_TXT`    | [Demo information text](https://www.resdac.org/cms-data/variables/demo-information-text)                 |              |              |
