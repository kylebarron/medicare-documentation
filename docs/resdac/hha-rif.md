# Home Health Agency RIF

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

|   Index | SAS Name                 | Variable Name                                                                                                                                                                    | Limitation   | Code Table   |
|--------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                                                           |              |              |
|       2 | `CLM_ID`                 | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                                                                                   | *            |              |
|       3 | `RIC_CD`                 | [NCH Near Line Record Identification Code](https://www.resdac.org/cms-data/variables/NCH-Near-Line-Record-Identification-Code)                                                   |              | *            |
|       4 | `CLM_TYPE`               | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                                                                             |              | *            |
|       5 | `FROM_DT`                | [Claim From Date](https://www.resdac.org/cms-data/variables/Claim-Date)                                                                                                          |              |              |
|       6 | `THRU_DT`                | [Claim Through Date](https://www.resdac.org/cms-data/variables/Claim-Through-Date)                                                                                               |              |              |
|       7 | `WKLY_DT`                | [NCH Weekly Claim Processing Date](https://www.resdac.org/cms-data/variables/NCH-Weekly-Claim-Processing-Date)                                                                   |              |              |
|       8 | `FI_CLM_PROC_DT`         | [FI Claim Process Date](https://www.resdac.org/cms-data/variables/FI-Claim-Process-Date)                                                                                         |              |              |
|       9 | `PROVIDER`               | [Provider Number](https://www.resdac.org/cms-data/variables/provider-number)                                                                                                     |              | *            |
|      10 | `FAC_TYPE`               | [Claim Facility Type Code](https://www.resdac.org/cms-data/variables/Claim-Facility-Type-Code)                                                                                   |              | *            |
|      11 | `TYPESRVC`               | [Claim Service Classification Type Code](https://www.resdac.org/cms-data/variables/Claim-Service-classification-Type-Code)                                                       |              | *            |
|      12 | `FREQ_CD`                | [Claim Frequency Code](https://www.resdac.org/cms-data/variables/Claim-Frequency-Code)                                                                                           |              | *            |
|      13 | `FI_NUM`                 | [FI Number](https://www.resdac.org/cms-data/variables/fi-number)                                                                                                                 |              | *            |
|      14 | `NOPAY_CD`               | [Claim Medicare Non Payment Reason Code](https://www.resdac.org/cms-data/variables/claim-medicare-non-payment-reason-code)                                                       |              | *            |
|      15 | `PMT_AMT`                | [Claim Payment Amount](https://www.resdac.org/cms-data/variables/Claim-Payment-Amount-0)                                                                                         | *            |              |
|      16 | `PRPAYAMT`               | [NCH Primary Payer Claim Paid Amount*](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Claim-Paid-Amount)                                                            |              |              |
|      17 | `PRPAY_CD`               | [NCH Primary Payer Code](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Code)                                                                                       |              | *            |
|      18 | `PRSTATE`                | [NCH Provider State Code](https://www.resdac.org/cms-data/variables/nch-provider-state-code)                                                                                     |              | *            |
|      19 | `ORGNPINM`               | [Organization NPI Number](https://www.resdac.org/cms-data/variables/Organization-NPI-Number)                                                                                     |              |              |
|      20 | `SRVC_LOC_NPI_NUM`       | [Claim Service Location NPI Number](https://www.resdac.org/cms-data/variables/claim-service-location-npi-number)                                                                 |              |              |
|      21 | `AT_UPIN`                | [Claim Attending Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-UPIN-Number)                                                         |              |              |
|      22 | `AT_NPI`                 | [Claim Attending Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-NPI-Number)                                                           |              |              |
|      23 | `AT_PHYSN_SPCLTY_CD`     | [Claim Attending Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-attending-physician-specialty-code)                                                   |              | *            |
|      24 | `OP_NPI`                 | [Claim Operating Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Operating-Physician-NPI-Number)                                                           |              |              |
|      25 | `OP_PHYSN_SPCLTY_CD`     | [Claim Operating Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-operating-physician-specialty-code)                                                   |              | *            |
|      26 | `OT_NPI`                 | [Claim Other Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Other-Physician-NPI-Number)                                                                   |              |              |
|      27 | `OT_PHYSN_SPCLTY_CD`     | [Claim Other Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-other-physician-specialty-code)                                                           |              | *            |
|      28 | `RNDRNG_PHYSN_NPI`       | [Claim Rendering Physician NPI Number](https://www.resdac.org/cms-data/variables/claim-rendering-physician-npi-number)                                                           |              |              |
|      29 | `RNDRNG_PHYSN_SPCLTY_CD` | [Claim Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-rendering-physician-specialty-code)                                                   |              | *            |
|      30 | `RFR_PHYSN_NPI`          | [Claim Referring Physician NPI Number](https://www.resdac.org/cms-data/variables/claim-referring-physician-npi-number)                                                           |              |              |
|      31 | `RFR_PHYSN_SPCLTY_CD`    | [Claim Referring Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-referring-physician-specialty-code)                                                   |              | *            |
|      32 | `STUS_CD`                | [Patient Discharge Status Code](https://www.resdac.org/cms-data/variables/patient-discharge-status-code)                                                                         |              | *            |
|      33 | `PPS_IND`                | [Claim PPS Indicator Code](https://www.resdac.org/cms-data/variables/Claim-PPS-Indicator-Code)                                                                                   |              | *            |
|      34 | `TOT_CHRG`               | [Claim Total Charge Amount](https://www.resdac.org/cms-data/variables/Claim-Total-Charge-Amount)                                                                                 | *            | *            |
|      35 | `PRNCPAL_DGNS_CD`        | [Claim Principal Diagnosis Code](https://www.resdac.org/cms-data/variables/Primary-Claim-Diagnosis-Code)                                                                         |              |              |
|      36 | `ICD_DGNS_CD1`           | [Claim Diagnosis Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-I)                                                                                       |              |              |
|      37 | `ICD_DGNS_CD2`           | [Claim Diagnosis Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-II)                                                                                     |              |              |
|      38 | `ICD_DGNS_CD3`           | [Claim Diagnosis Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-III)                                                                                   |              |              |
|      39 | `ICD_DGNS_CD4`           | [Claim Diagnosis Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IV)                                                                                     |              |              |
|      40 | `ICD_DGNS_CD5`           | [Claim Diagnosis Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-V)                                                                                       |              |              |
|      41 | `ICD_DGNS_CD6`           | [Claim Diagnosis Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VI)                                                                                     |              |              |
|      42 | `ICD_DGNS_CD7`           | [Claim Diagnosis Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VII)                                                                                   |              |              |
|      43 | `ICD_DGNS_CD8`           | [Claim Diagnosis Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VIII)                                                                                 |              |              |
|      44 | `ICD_DGNS_CD9`           | [Claim Diagnosis Code IX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IX)                                                                                     |              |              |
|      45 | `ICD_DGNS_CD10`          | [Claim Diagnosis Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-X)                                                                                       |              |              |
|      46 | `ICD_DGNS_CD11`          | [Claim Diagnosis Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XI)                                                                                     |              |              |
|      47 | `ICD_DGNS_CD12`          | [Claim Diagnosis Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XII)                                                                                   |              |              |
|      48 | `ICD_DGNS_CD13`          | [Claim Diagnosis Code XIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIII)                                                                                 |              |              |
|      49 | `ICD_DGNS_CD14`          | [Claim Diagnosis Code XIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIV-0)                                                                                 |              |              |
|      50 | `ICD_DGNS_CD15`          | [Claim Diagnosis Code XV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XV)                                                                                     |              |              |
|      51 | `ICD_DGNS_CD16`          | [Claim Diagnosis Code XVI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVI)                                                                                   |              |              |
|      52 | `ICD_DGNS_CD17`          | [Claim Diagnosis Code XVII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVII)                                                                                 |              |              |
|      53 | `ICD_DGNS_CD18`          | [Claim Diagnosis Code XVIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVIII)                                                                               |              |              |
|      54 | `ICD_DGNS_CD19`          | [Claim Diagnosis Code XIX](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xix)                                                                                   |              |              |
|      55 | `ICD_DGNS_CD20`          | [Claim Diagnosis Code XX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XX)                                                                                     |              |              |
|      56 | `ICD_DGNS_CD21`          | [Claim Diagnosis Code XXI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXI)                                                                                   |              |              |
|      57 | `ICD_DGNS_CD22`          | [Claim Diagnosis Code XXII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXII)                                                                                 |              |              |
|      58 | `ICD_DGNS_CD23`          | [Claim Diagnosis Code XXIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIII)                                                                               |              |              |
|      59 | `ICD_DGNS_CD24`          | [Claim Diagnosis Code XXIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIV)                                                                                 |              |              |
|      60 | `ICD_DGNS_CD25`          | [Claim Diagnosis Code XXV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXV)                                                                                   |              |              |
|      61 | `FST_DGNS_E_CD`          | [First Claim Diagnosis E Code](https://www.resdac.org/cms-data/variables/First-Claim-Diagnosis-E-Code)                                                                           |              |              |
|      62 | `ICD_DGNS_E_CD1`         | [Claim Diagnosis E Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-I)                                                                                   |              |              |
|      63 | `ICD_DGNS_E_CD2`         | [Claim Diagnosis E Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-II)                                                                                 |              |              |
|      64 | `ICD_DGNS_E_CD3`         | [Claim Diagnosis E Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-III)                                                                               |              |              |
|      65 | `ICD_DGNS_E_CD4`         | [Claim Diagnosis E Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-IV)                                                                                 |              |              |
|      66 | `ICD_DGNS_E_CD5`         | [Claim Diagnosis E Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-V)                                                                                   |              |              |
|      67 | `ICD_DGNS_E_CD6`         | [Claim Diagnosis E Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VI)                                                                                 |              |              |
|      68 | `ICD_DGNS_E_CD7`         | [Claim Diagnosis E Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VII)                                                                               |              |              |
|      69 | `ICD_DGNS_E_CD8`         | [Claim Diagnosis E Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VIII)                                                                             |              |              |
|      70 | `ICD_DGNS_E_CD9`         | [Claim Diagnosis E Code IX](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-ix)                                                                                 |              |              |
|      71 | `ICD_DGNS_E_CD10`        | [Claim Diagnosis E Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-X)                                                                                   |              |              |
|      72 | `ICD_DGNS_E_CD11`        | [Claim Diagnosis E Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XI)                                                                                 |              |              |
|      73 | `ICD_DGNS_E_CD12`        | [Claim Diagnosis E Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XII)                                                                               |              |              |
|      74 | `LUPAIND`                | [Claim HHA Low Utilization Payment Adjustment (LUPA) Indicator Code](https://www.resdac.org/cms-data/variables/Claim-HHA-Low-Utilization-Payment-Adjustment-LUPA-Indicator-Code) | *            | *            |
|      75 | `HHA_RFRL`               | [Claim HHA Referral Code](https://www.resdac.org/cms-data/variables/Claim-HHA-Referral-Code)                                                                                     | *            | *            |
|      76 | `VISITCNT`               | [Claim HHA Total Visit Count](https://www.resdac.org/cms-data/variables/Claim-HHA-Total-Visit-Count)                                                                             | *            |              |
|      77 | `HHSTRTDT`               | [Claim HHA Care Start Date](https://www.resdac.org/cms-data/variables/Claim-HHA-Care-Start-Date)                                                                                 |              |              |
|      78 | `DOB_DT`                 | [Date of Birth from Claim (Date)](https://www.resdac.org/cms-data/variables/Date-Birth-Claim-Date)                                                                               |              |              |
|      79 | `GNDR_CD`                | [Gender Code from Claim](https://www.resdac.org/cms-data/variables/Gender-Code-Claim)                                                                                            |              | *            |
|      80 | `RACE_CD`                | [Race Code from Claim](https://www.resdac.org/cms-data/variables/Race-Code-Claim)                                                                                                |              | *            |
|      81 | `CNTY_CD`                | [County Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/County-Code-Claim-SSA)                                                                                  |              |              |
|      82 | `STATE_CD`               | [State Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/state-code-claim-ssa)                                                                                    |              | *            |
|      83 | `ZIP_CD`                 | [Zip Code of Residence from Claim](https://www.resdac.org/cms-data/variables/Zip-Code-Residence-Claim)                                                                           |              |              |
|      84 | `CLM_MDCL_REC`           | [Claim Medical Record Number](https://www.resdac.org/cms-data/variables/Claim-Medical-Record-Number)                                                                             |              |              |
|      85 | `QUERY_CD`               | [Claim Query Code](https://www.resdac.org/cms-data/variables/Claim-Query-Code)                                                                                                   |              | *            |
|      97 | `ACO_ID_NUM`             | [Claim Accountable Care Organization (ACO) Identification Number](https://www.resdac.org/cms-data/variables/claim-accountable-care-organization-aco-identification-number)       |              |              |

### Revenue Center File

|   Index | SAS Name                   | Variable Name                                                                                                                                          | Limitation   | Code Table   |
|--------:|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                  | [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)                                                 |              |              |
|       2 | `CLM_ID`                   | [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)                                                                                         | *            |              |
|       3 | `THRU_DT`                  | [Claim Through Date](https://www.resdac.org/cms-data/variables/Claim-Through-Date)                                                                     |              |              |
|       4 | `CLM_LN`                   | [Claim Line Number](https://www.resdac.org/cms-data/variables/Claim-Line-Number)                                                                       |              |              |
|       5 | `CLM_TYPE`                 | [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)                                                                   |              | *            |
|       6 | `REV_CNTR`                 | [Revenue Center Code](https://www.resdac.org/cms-data/variables/revenue-center-code)                                                                   |              | *            |
|       7 | `REV_DT`                   | [Revenue Center Date](https://www.resdac.org/cms-data/variables/Revenue-Center-Date)                                                                   |              |              |
|       8 | `REVANSI1`                 | [Revenue Center 1st ANSI Code](https://www.resdac.org/cms-data/variables/revenue-center-1st-ansi-code)                                                 |              | *            |
|       9 | `APCHIPPS`                 | [Revenue Center APC/HIPPS](https://www.resdac.org/cms-data/variables/revenue-center-apchipps)                                                          |              | *            |
|      10 | `HCPCS_CD`                 | [Revenue Center HCFA Common Procedure Coding System](https://www.resdac.org/cms-data/variables/Revenue-Center-HCFA-Common-Procedure-Coding-System)     |              |              |
|      11 | `MDFR_CD1`                 | [Revenue Center HCPCS Initial Modifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-HCPCS-Initial-Modifier-Code)                     |              |              |
|      12 | `MDFR_CD2`                 | [Revenue Center HCPCS Second Modifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-HCPCS-Second-Modifier-Code)                       |              |              |
|      13 | `MDFR_CD3`                 | [HCPCS Third Modifier Code](https://www.resdac.org/cms-data/variables/hcpcs-third-modifier-code)                                                       |              |              |
|      14 | `PMTMTHD`                  | [Revenue Center Payment Method Indicator Code](https://www.resdac.org/cms-data/variables/revenue-center-payment-method-indicator-code)                 |              | *            |
|      15 | `REV_UNIT`                 | [Revenue Center Unit Count](https://www.resdac.org/cms-data/variables/Revenue-Center-Unit-Count)                                                       |              |              |
|      16 | `REV_RATE`                 | [Revenue Center Rate Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Rate-Amount)                                                     |              |              |
|      17 | `REVPMT`                   | [Revenue Center Payment Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Payment-Amount)                                               |              |              |
|      18 | `REV_CHRG`                 | [Revenue Center Total Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Total-Charge-Amount)                                     | *            | *            |
|      19 | `REV_NCVR`                 | [Revenue Center Non-Covered Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Non-Covered-Charge-Amount)                         |              | *            |
|      20 | `REVDEDCD`                 | [Revenue Center Deductible Coinsurance Code](https://www.resdac.org/cms-data/variables/Revenue-Center-Deductible-Coinsurance-Code)                     |              | *            |
|      21 | `REVSTIND`                 | [Revenue Center Status Indicator Code](https://www.resdac.org/cms-data/variables/revenue-center-status-indicator-code)                                 |              | *            |
|      22 | `REV_CNTR_NDC_QTY`         | [Revenue Center NDC Quantity](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity)                                                   |              |              |
|      23 | `REV_CNTR_NDC_QTY_QLFR_CD` | [Revenue Center NDC Quantity Qualifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity-Qualifier-Code)                     |              | *            |
|      24 | `RNDRNG_PHYSN_UPIN`        | [Revenue Center Rendering Physician UPIN](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-UPIN)                           |              |              |
|      25 | `RNDRNG_PHYSN_NPI`         | [Revenue Center Rendering Physician NPI](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-NPI)                             |              |              |
|      26 | `RNDRNG_PHYSN_SPCLTY_CD`   | [Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/rendering-physician-specialty-code)                                     |              | *            |
|      27 | `DSCNTIND`                 | [Revenue Center Discount Indicator Code](https://www.resdac.org/cms-data/variables/Revenue-Center-Discount-Indicator-Code)                             |              | *            |
|      28 | `IDENDC`                   | [Revenue Center IDE, NDC, or UPC Number](https://www.resdac.org/cms-data/variables/revenue-center-ide-ndc-or-upc-number)                               |              |              |
|      29 | `RPRVDPMT`                 | [Revenue Center (Medicare) Provider Payment Amount](https://www.resdac.org/cms-data/variables/revenue-center-medicare-provider-payment-amount)         |              |              |
|      30 | `PTNTRESP`                 | [Revenue Center Patient Responsibility Payment Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Patient-Responsibility-Payment-Amount) |              | *            |
|      31 | `REV_CNTR_PRCNG_IND_CD`    | [Revenue Center Pricing Indicator Code](https://www.resdac.org/cms-data/variables/revenue-center-pricing-indicator-code-0)                             |              | *            |
|      32 | `THRPY_CAP_IND_CD1`        | [Revenue Center Therapy Cap Indicator 1 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-1-code)                   |              | *            |
|      33 | `THRPY_CAP_IND_CD2`        | [Revenue Center Therapy Cap Indicator 2 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-2-code)                   |              | *            |

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
