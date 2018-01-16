# MedPAR RIF

## Overview

The MedPAR File contains inpatient hospital and skilled nursing facility (SNF) final action stay records. Each MedPAR record represents a stay in an inpatient hospital or SNF. Each MedPAR record may represent one claim or multiple claims, depending on the length of a beneficiary's stay and the amount of services used throughout the stay.

This file includes:

- diagnosis (ICD-9 diagnosis),
- procedure (ICD-9 procedure code),
- Diagnosis Related Group (DRG),
- dates of service,
- reimbursement amount,
- hospital provider,
- beneficiary demographic information

Availability: CY 1999 - 2016

## Data Documentation

### MedPAR RIF

|   Index | SAS Name                    | Variable Name                                                                                                                               | Limitation   | Code Table   |
|--------:|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-------------|
|       1 | `BENE_ID`                   | [Beneficiary Identification Number](variables.md#beneficiary-identification-number)                                                         |              |              |
|       2 | `MEDPARID`                  | [MedPAR ID Number](variables.md#medpar-id-number)                                                                                           |              |              |
|       3 | `MEDPAR_YR_NUM`             | [MEDPAR Year of Record](variables.md#medpar-year-of-record)                                                                                 |              |              |
|       4 | `CLM_TYPE`                  | [MEDPAR NCH Claim Type Code](variables.md#medpar-nch-claim-type-code)                                                                       |              | *            |
|       5 | `EQ_BIC`                    | [Equated BIC](variables.md#equated-bic)                                                                                                     |              | *            |
|       6 | `AGE_CNT`                   | [MEDPAR Beneficiary Age Count](variables.md#medpar-beneficiary-age-count)                                                                   |              |              |
|       7 | `SEX`                       | [MEDPAR Beneficiary Sex Code](variables.md#medpar-beneficiary-sex-code)                                                                     |              | *            |
|       8 | `RACE`                      | [MEDPAR Beneficiary Race Code](variables.md#medpar-beneficiary-race-code)                                                                   |              | *            |
|       9 | `MS_CD`                     | [MEDPAR Beneficiary Medicare Status Code](variables.md#medpar-beneficiary-medicare-status-code)                                             |              | *            |
|      10 | `STATE_CD`                  | [MEDPAR Beneficiary Residence SSA Standard State Code](variables.md#medpar-beneficiary-residence-ssa-standard-state-code)                   |              | *            |
|      11 | `CNTY_CD`                   | [MEDPAR Beneficiary Residence SSA Standard County Code](variables.md#medpar-beneficiary-residence-ssa-standard-county-code)                 |              |              |
|      12 | `BENE_ZIP`                  | [MEDPAR Beneficiary Mailing Contact Zip Code](variables.md#medpar-beneficiary-mailing-contact-zip-code)                                     |              |              |
|      13 | `ADMSNDAY`                  | [MEDPAR Admission Day Code](variables.md#medpar-admission-day-code)                                                                         |              | *            |
|      14 | `DSCHRGCD`                  | [MEDPAR Beneficiary Discharge Status Code](variables.md#medpar-beneficiary-discharge-status-code)                                           |              | *            |
|      15 | `GHOPDCD`                   | [MEDPAR GHO Paid Code](variables.md#medpar-gho-paid-code)                                                                                   |              | *            |
|      16 | `PPS_IND`                   | [MEDPAR PPS Indicator Code](variables.md#medpar-pps-indicator-code)                                                                         |              | *            |
|      17 | `ORGNPINM`                  | [Organization NPI Number](variables.md#organization-npi-number)                                                                             |              |              |
|      18 | `PRVDRNUM`                  | [MEDPAR Provider Number](variables.md#medpar-provider-number)                                                                               |              | *            |
|      19 | `SPCLUNIT`                  | [MEDPAR Provider Number Special Unit Code](variables.md#medpar-provider-number-special-unit-code)                                           |              | *            |
|      20 | `SSLSSNF`                   | [MEDPAR Short Stay/Long Stay/SNF Indicator Code](variables.md#medpar-short-staylong-staysnf-indicator-code)                                 |              | *            |
|      21 | `ACTV_XREF_IND`             | [MEDPAR Active Cross Reference Indicator](variables.md#medpar-active-cross-reference-indicator)                                             |              | *            |
|      22 | `SLCT_RSN_CD`               | [MEDPAR Case or Control Record](variables.md#medpar-case-or-control-record)                                                                 |              |              |
|      23 | `FACLMCNT`                  | [MEDPAR Stay Final Action Claims Count](variables.md#medpar-stay-final-action-claims-count)                                                 |              |              |
|      24 | `ACRTNDT`                   | [MEDPAR Latest Claim Accretion Date](variables.md#medpar-latest-claim-accretion-date)                                                       |              |              |
|      25 | `EXHST_DT`                  | [MEDPAR Beneficiary Medicare Benefit Exhausted Date](variables.md#medpar-beneficiary-medicare-benefit-exhausted-date)                       |              |              |
|      26 | `QLFYFROM`                  | [MEDPAR SNF Qualification From Date](variables.md#medpar-snf-qualification-from-date)                                                       |              |              |
|      27 | `QLFYTHRU`                  | [MEDPAR SNF Qualification Through Date](variables.md#medpar-snf-qualification-through-date)                                                 |              |              |
|      28 | `ADMSNDT`                   | [MEDPAR Admission Date](variables.md#medpar-admission-date)                                                                                 |              |              |
|      29 | `DSCHRGDT`                  | [MEDPAR Discharge Date](variables.md#medpar-discharge-date)                                                                                 |              |              |
|      30 | `CVRLVLDT`                  | [MEDPAR Covered Level Care Thru Date](variables.md#medpar-covered-level-care-thru-date)                                                     |              |              |
|      31 | `DEATHDT`                   | [MEDPAR Beneficiary Death Date](variables.md#medpar-beneficiary-death-date)                                                                 | *            |              |
|      32 | `DEATHCD`                   | [MEDPAR Beneficiary Death Date Verified Code](variables.md#medpar-beneficiary-death-date-verified-code)                                     |              |              |
|      33 | `SSICD`                     | [MEDPAR Internal Use SSI Indicator Code](variables.md#medpar-internal-use-ssi-indicator-code)                                               |              |              |
|      34 | `SSIDAY`                    | [MEDPAR Internal Use SSI Day Count](variables.md#medpar-internal-use-ssi-day-count)                                                         |              |              |
|      35 | `INTRNL_USE_SSI_DATA`       | [MEDPAR Internal Use SSI Data](variables.md#medpar-internal-use-ssi-data)                                                                   |              |              |
|      36 | `LOSCNT`                    | [MEDPAR Length of Stay Day Count](variables.md#medpar-length-of-stay-day-count)                                                             |              |              |
|      37 | `OUTLRDAY`                  | [MEDPAR Outlier Day Count](variables.md#medpar-outlier-day-count)                                                                           |              |              |
|      38 | `UTIL_DAY`                  | [MEDPAR Utilization Day Count](variables.md#medpar-utilization-day-count)                                                                                                                                             |              |              |
|      39 | `COIN_DAY`                  | [MEDPAR Beneficiary Total Coinsurance Day Count](variables.md#medpar-beneficiary-total-coinsurance-day-count)                               |              |              |
|      40 | `LRD_USE`                   | [MEDPAR Beneficiary LRD Used Count](variables.md#medpar-beneficiary-lrd-used-count)                                                         |              |              |
|      41 | `COIN_AMT`                  | [MEDPAR Beneficiary Part A Coinsurance Liability Amount](variables.md#medpar-beneficiary-part-a-coinsurance-liability-amount)               |              |              |
|      42 | `DED_AMT`                   | [MEDPAR Beneficiary Inpatient Deductible Liability Amount](variables.md#medpar-beneficiary-inpatient-deductible-liability-amount)           |              |              |
|      43 | `BLDDEDAM`                  | [MEDPAR Beneficiary Blood Deductible Liability Amount](variables.md#medpar-beneficiary-blood-deductible-liability-amount)                   | *            |              |
|      44 | `PRPAYAMT`                  | [MEDPAR Beneficiary Primary Payer Amount](variables.md#medpar-beneficiary-primary-payer-amount)                                             |              |              |
|      45 | `OUTLRAMT`                  | [MEDPAR DRG Outlier Approved Payment Amount](variables.md#medpar-drg-outlier-approved-payment-amount)                                       |              |              |
|      46 | `DISP_SHR`                  | [MEDPAR Inpatient Disproportionate Share Amount](variables.md#medpar-inpatient-disproportionate-share-amount)                               |              |              |
|      47 | `IME_AMT`                   | [MEDPAR Indirect Medical Education (IME) Amount](variables.md#medpar-indirect-medical-education-ime-amount)                                 |              |              |
|      48 | `DRGPRICE`                  | [MEDPAR DRG Price Amount](variables.md#medpar-drg-price-amount)                                                                             | *            |              |
|      49 | `PASSTHRU`                  | [MEDPAR Total Pass Through Amount](variables.md#medpar-total-pass-through-amount)                                                           |              |              |
|      50 | `PPS_CPTL`                  | [MEDPAR Total PPS Capital Amount](variables.md#medpar-total-pps-capital-amount)                                                             |              |              |
|      51 | `IP_LOW_VOL_PYMT_AMT`       | [MEDPAR Inpatient Low Volume Payment Amount](variables.md#medpar-inpatient-low-volume-payment-amount)                                       |              |              |
|      52 | `TOTCHRG`                   | [MEDPAR Total Charge Amount](variables.md#medpar-total-charge-amount)                                                                       |              |              |
|      53 | `CVRCHRG`                   | [MEDPAR Total Covered Charge Amount](variables.md#medpar-total-covered-charge-amount)                                                       |              |              |
|      54 | `PMT_AMT`                   | [MEDPAR Medicare Payment Amount](variables.md#medpar-medicare-payment-amount)                                                               |              |              |
|      55 | `ACMDTNS`                   | [MEDPAR All Accommodations Total Charge Amount](variables.md#medpar-all-accommodations-total-charge-amount)                                 |              |              |
|      56 | `DPRTMNTL`                  | [MEDPAR Departmental Total Charge Amount](variables.md#medpar-departmental-total-charge-amount)                                             |              |              |
|      57 | `PRVTDAY`                   | [MEDPAR Private Room Day Count](variables.md#medpar-private-room-day-count)                                                                 |              |              |
|      58 | `SPRVTDAY`                  | [MEDPAR Semiprivate Room Day Count](variables.md#medpar-semiprivate-room-day-count)                                                                                                                                             |              |              |
|      59 | `WARDDAY`                   | [MEDPAR Ward Day Count](variables.md#medpar-ward-day-count)                                                                                 |              |              |
|      60 | `ICARECNT`                  | [MEDPAR Intensive Care Day Count](variables.md#medpar-intensive-care-day-count)                                                             | *            |              |
|      61 | `MCCCNT`                    | [MEDPAR Coronary Care Day Count](variables.md#medpar-coronary-care-day-count)                                                               | *            |              |
|      62 | `PRVTAMT`                   | [MEDPAR Private Room Charge Amount](variables.md#medpar-private-room-charge-amount)                                                                                                                                             |              |              |
|      63 | `SPRVTAMT`                  | [MEDPAR Semi-Private Room Charge Amount](variables.md#medpar-semi-private-room-charge-amount)                                               |              |              |
|      64 | `WARDAMT`                   | [MEDPAR Ward Charge Amount](variables.md#medpar-ward-charge-amount)                                                                         |              |              |
|      65 | `ICAREAMT`                  | [MEDPAR Intensive Care Charge Amount](variables.md#medpar-intensive-care-charge-amount)                                                     |              |              |
|      66 | `CRNRYAMT`                  | [MEDPAR Coronary Care Charge Amount](variables.md#medpar-coronary-care-charge-amount)                                                       |              |              |
|      67 | `OTHRAMT`                   | [MEDPAR Other Service Charge Amount](variables.md#medpar-other-service-charge-amount)                                                       |              |              |
|      68 | `PHRMCAMT`                  | [MEDPAR Pharmacy Charge Amount](variables.md#medpar-pharmacy-charge-amount)                                                                 |              |              |
|      69 | `SUPLYAMT`                  | [MEDPAR Medical/Surgical Supplies Charge Amount](variables.md#medpar-medicalsurgical-supplies-charge-amount)                                |              |              |
|      70 | `DME_AMT`                   | [MEDPAR DME Charge Amount](variables.md#medpar-dme-charge-amount)                                                                           |              |              |
|      71 | `UDME_AMT`                  | [MEDPAR Used DME Charge Amount](variables.md#medpar-used-dme-charge-amount)                                                                 |              |              |
|      72 | `PHYTHAMT`                  | [MEDPAR Physical Therapy Charge Amount](variables.md#medpar-physical-therapy-charge-amount)                                                 |              |              |
|      73 | `OCPTLAMT`                  | [MEDPAR Occupational Therapy Charge Amount](variables.md#medpar-occupational-therapy-charge-amount)                                         |              |              |
|      74 | `SPCH_AMT`                  | [MEDPAR Speech Pathology Charge Amount](variables.md#medpar-speech-pathology-charge-amount)                                                 |              |              |
|      75 | `INHLTAMT`                  | [MEDPAR Inhalation Therapy Charge Amount](variables.md#medpar-inhalation-therapy-charge-amount)                                             |              |              |
|      76 | `BLOODAMT`                  | [MEDPAR Blood Charge Amount](variables.md#medpar-blood-charge-amount)                                                                       |              |              |
|      77 | `BLDADMIN`                  | [MEDPAR Blood Administration Charge Amount](variables.md#medpar-blood-administration-charge-amount)                                         |              |              |
|      78 | `OROOMAMT`                  | [MEDPAR Operating Room Charge Amount](variables.md#medpar-operating-room-charge-amount)                                                     |              |              |
|      79 | `LTHTRPSY`                  | [MEDPAR Lithotripsy Charge Amount](variables.md#medpar-lithotripsy-charge-amount)                                                           |              |              |
|      80 | `CRDLGY`                    | [MEDPAR Cardiology Charge Amount](variables.md#medpar-cardiology-charge-amount)                                                             |              |              |
|      81 | `ANSTHSA`                   | [MEDPAR Anesthesia Charge Amount](variables.md#medpar-anesthesia-charge-amount)                                                             |              |              |
|      82 | `LAB_AMT`                   | [MEDPAR Laboratory Charge Amount](variables.md#medpar-laboratory-charge-amount)                                                             |              |              |
|      83 | `RDLGYAMT`                  | [MEDPAR Radiology Charge Amount](variables.md#medpar-radiology-charge-amount)                                                               |              |              |
|      84 | `MRI_AMT`                   | [MEDPAR MRI Charge Amount](variables.md#medpar-mri-charge-amount)                                                                           |              |              |
|      85 | `OPSRVC`                    | [MEDPAR Outpatient Service Charge Amount](variables.md#medpar-outpatient-service-charge-amount)                                             |              |              |
|      86 | `ER_AMT`                    | [MEDPAR Emergency Room Charge Amount](variables.md#medpar-emergency-room-charge-amount)                                                     |              |              |
|      87 | `AMBLNC`                    | [MEDPAR Ambulance Charge Amount](variables.md#medpar-ambulance-charge-amount)                                                               |              |              |
|      88 | `PROFFEES`                  | [MEDPAR Professional Fees Charge Amount](variables.md#medpar-professional-fees-charge-amount)                                               |              |              |
|      89 | `ORGNAMT`                   | [MEDPAR Organ Acquisition Charge Amount](variables.md#medpar-organ-acquisition-charge-amount)                                               |              |              |
|      90 | `ESRDSETG`                  | [MEDPAR ESRD Revenue Setting Charge Amount](variables.md#medpar-esrd-revenue-setting-charge-amount)                                         |              |              |
|      91 | `CLNC_AMT`                  | [MEDPAR Clinic Visit Charge Amount](variables.md#medpar-clinic-visit-charge-amount)                                                                                                                                             |              |              |
|      92 | `ICUINDCD`                  | [MEDPAR Intensive Care Unit (ICU) Indicator Code](variables.md#medpar-intensive-care-unit-icu-indicator-code)                               | *            | *            |
|      93 | `CRNRY_CD`                  | [MEDPAR Coronary Care Indicator Code](variables.md#medpar-coronary-care-indicator-code)                                                     | *            | *            |
|      94 | `PHRMCYCD`                  | [MEDPAR Pharmacy Indicator Code](variables.md#medpar-pharmacy-indicator-code)                                                               |              | *            |
|      95 | `TRNSPLNT`                  | [MEDPAR Transplant Indicator Code](variables.md#medpar-transplant-indicator-code)                                                           |              | *            |
|      96 | `ONCLGYSW`                  | [MEDPAR Radiology Oncology Indicator Switch](variables.md#medpar-radiology-oncology-indicator-switch)                                       |              | *            |
|      97 | `DGNSTCSW`                  | [MEDPAR Radiology Diagnostic Indicator Switch](variables.md#medpar-radiology-diagnostic-indicator-switch)                                   |              | *            |
|      98 | `THRPTCSW`                  | [MEDPAR Radiology Therapeutic Indicator Switch](variables.md#medpar-radiology-therapeutic-indicator-switch)                                 |              | *            |
|      99 | `NUCLR_SW`                  | [MEDPAR Radiology Nuclear Medicine Indicator Switch](variables.md#medpar-radiology-nuclear-medicine-indicator-switch)                       |              | *            |
|     100 | `CTSCANSW`                  | [MEDPAR Radiology CT Scan Indicator Switch](variables.md#medpar-radiology-ct-scan-indicator-switch)                                         |              | *            |
|     101 | `IMGNG_SW`                  | [MEDPAR Radiology Other Imaging Indicator Switch](variables.md#medpar-radiology-other-imaging-indicator-switch)                             |              | *            |
|     102 | `OPSRVCCD`                  | [MEDPAR Outpatient Services Indicator Code](variables.md#medpar-outpatient-services-indicator-code)                                         |              | *            |
|     103 | `ORGNCD`                    | [MEDPAR Organ Acquisition Indicator Code](variables.md#medpar-organ-acquisition-indicator-code)                                             |              | *            |
|     104 | `ESRDSTG{x}`                | [MEDPAR ESRD Setting Indicator Code](variables.md#medpar-esrd-setting-indicator-code)                                                       |              | *            |
|     105 | `DGNSCNT`                   | [MEDPAR Diagnosis Code Count](variables.md#medpar-diagnosis-code-count)                                                                     |              |              |
|     106 | `DGNS_VRSN_CD_{x}`          | [MEDPAR Diagnosis Version Code](variables.md#medpar-diagnosis-version-code)                                                                 |              |              |
|     107 | `DGNS_E_CD_CNT`             | [MEDPAR Diagnosis E Code Count](variables.md#medpar-diagnosis-e-code-count)                                                                 |              |              |
|     108 | `DGNS_E_VRSN_CD_{x}`        | [MEDPAR Diagnosis E Version Code](variables.md#medpar-diagnosis-e-version-code)                                                             |              |              |
|     109 | `DGNSCD{x}`                 | [MEDPAR Diagnosis Code](variables.md#medpar-diagnosis-code)                                                                                 |              |              |
|     110 | `DGNS_POA`                  | [MEDPAR Diagnosis Code POA Array](variables.md#medpar-diagnosis-code-poa-array)                                                             |              |              |
|     111 | `POA_DGNS_E_CD_CNT`         | [MEDPAR Claim Present on Admission Diagnosis E Code Count](variables.md#medpar-claim-present-on-admission-diagnosis-e-code-count)           |              |              |
|     112 | `POA_DGNS_E_{x}_IND_CD`     | [MEDPAR Diagnosis E Code Present on Admission Indicator](variables.md#medpar-diagnosis-e-code-present-on-admission-indicator)               |              | *            |
|     113 | `POA_DGNS_CD_CNT`           | [MEDPAR Claim Present on Admission Diagnosis Code Count](variables.md#medpar-claim-present-on-admission-diagnosis-code-count)               |              |              |
|     114 | `POA_DGNS_{x}_IND_CD`       | [MEDPAR Diagnosis Present on Admission Indicator Code](variables.md#medpar-diagnosis-present-on-admission-indicator-code)                   |              | *            |
|     115 | `PRCDRSW`                   | [MEDPAR Surgical Procedure Indicator Switch](variables.md#medpar-surgical-procedure-indicator-switch)                                       |              | *            |
|     116 | `PRCDRCNT`                  | [MEDPAR Surgical Procedure Code Count](variables.md#medpar-surgical-procedure-code-count)                                                   |              |              |
|     117 | `PRCDTCNT`                  | [MEDPAR Surgical Procedure Performed Date Count](variables.md#medpar-surgical-procedure-performed-date-count)                               |              |              |
|     118 | `SRGCL_PRCDR_VRSN_CD_{x}`   | [MEDPAR Surgical Procedure Version Code](variables.md#medpar-surgical-procedure-version-code)                                               |              |              |
|     119 | `PRCDRCD{x}`                | [MEDPAR Surgical Procedure Code](variables.md#medpar-surgical-procedure-code)                                                               |              |              |
|     120 | `PRCDRDT{x}`                | [MEDPAR Surgical Procedure Performed Date](variables.md#medpar-surgical-procedure-performed-date)                                           |              |              |
|     121 | `BLDFRNSH`                  | [MEDPAR Blood Pints Furnished Quantity](variables.md#medpar-blood-pints-furnished-quantity)                                                 |              |              |
|     122 | `BIC`                       | [MEDPAR Beneficiary Identification Code](variables.md#medpar-beneficiary-identification-code)                                               |              |              |
|     123 | `DRG_CD`                    | [MEDPAR DRG Code](variables.md#medpar-drg-code)                                                                                             |              |              |
|     124 | `DSTNTNCD`                  | [MEDPAR Discharge Destination Code](variables.md#medpar-discharge-destination-code)                                                                                                                                             |              | *            |
|     125 | `OUTLR_CD`                  | [MEDPAR DRG/Outlier Stay Code](variables.md#medpar-drgoutlier-stay-code)                                                                    |              | *            |
|     126 | `PRPAY_CD`                  | [MEDPAR Beneficiary Primary Payer Code](variables.md#medpar-beneficiary-primary-payer-code)                                                 |              | *            |
|     127 | `ESRD_CD`                   | [MEDPAR ESRD Condition Code](variables.md#medpar-esrd-condition-code)                                                                       |              |              |
|     128 | `SRC_ADMS`                  | [MEDPAR Source Inpatient Admission Code](variables.md#medpar-source-inpatient-admission-code)                                               |              | *            |
|     129 | `TYPE_ADM`                  | [MEDPAR Inpatient Admission Type Code](variables.md#medpar-inpatient-admission-type-code)                                                   |              | *            |
|     130 | `FICARR`                    | [MEDPAR Fiscal Intermediary/Carrier Identification Number](variables.md#medpar-fiscal-intermediarycarrier-identification-number)            |              |              |
|     131 | `AD_DGNS`                   | [MEDPAR Admitting Diagnosis Code](variables.md#medpar-admitting-diagnosis-code)                                                             |              |              |
|     132 | `ADMTG_DGNS_VRSN_CD`        | [MEDPAR Admitting Diagnosis Version Code](variables.md#medpar-admitting-diagnosis-version-code)                                             |              |              |
|     133 | `DEATHDAY`                  | [MEDPAR Admission Death Day Count](variables.md#medpar-admission-death-day-count)                                                           | *            |              |
|     134 | `IPSBCD`                    | [MEDPAR Internal Use (By IPSB) Code](variables.md#medpar-internal-use-by-ipsb-code)                                                         |              |              |
|     135 | `FILDTCD`                   | [MEDPAR Internal Use File Date Code](variables.md#medpar-internal-use-file-date-code)                                                       |              |              |
|     136 | `SMPLSIZE`                  | [MEDPAR Internal Use Sample Size Code](variables.md#medpar-internal-use-sample-size-code)                                                   |              |              |
|     137 | `WRNGCD`                    | [MEDPAR Warning Indicators Code](variables.md#medpar-warning-indicators-code)                                                               |              | *            |
|     138 | `CLM_PTNT_RLTNSHP_CD`       | [MEDPAR Claim Patient Relationship Code](variables.md#medpar-claim-patient-relationship-code)                                               |              |              |
|     139 | `CARE_IMPRVMT_MODEL_{x}_CD` | [MEDPAR Care Improvement Model Code](variables.md#medpar-care-improvement-model-code)                                                       |              |              |
|     140 | `VBP_PRTCPNT_IND_CD`        | [MEDPAR VBP Participant Indicator Code](variables.md#medpar-vbp-participant-indicator-code)                                                 |              |              |
|     141 | `HRR_PRTCPNT_IND_CD`        | [MEDPAR HRR Participant Indicator Code](variables.md#medpar-hrr-participant-indicator-code)                                                 |              |              |
|     142 | `BNDLD_MODEL_DSCNT_PCT`     | [MEDPAR Bundled Model Discount Percent](variables.md#medpar-bundled-model-discount-percent)                                                 |              |              |
|     143 | `VBP_ADJSTMT_PCT`           | [MEDPAR VBP Adjustment Percent](variables.md#medpar-vbp-adjustment-percent)                                                                 |              |              |
|     144 | `HRR_ADJSTMT_PCT`           | [MEDPAR HRR Adjustment Percent](variables.md#medpar-hrr-adjustment-percent)                                                                 |              |              |
|     145 | `INFRMTL_ENCTR_IND_SW`      | [MEDPAR Informational Encounter Indicator Switch](variables.md#medpar-informational-encounter-indicator-switch)                             |              |              |
|     146 | `MA_TCHING_IND_SW`          | [MEDPAR MA Teaching Indicator Switch](variables.md#medpar-ma-teaching-indicator-switch)                                                     |              |              |
|     147 | `PROD_RPLCMT_LIFECYC_SW`    | [MEDPAR Product Replacement within Product Lifecycle Switch](variables.md#medpar-product-replacement-within-product-lifecycle-switch)       |              |              |
|     148 | `PROD_RPLCMT_RCLL_SW`       | [MEDPAR Product Replacement for known Recall of Product Switch](variables.md#medpar-product-replacement-for-known-recall-of-product-switch) |              |              |
|     149 | `CRED_RCVD_RPLCD_DVC_SW`    | [MEDPAR Credit Received Replaced Device Switch](variables.md#medpar-credit-received-replaced-device-switch)                                 |              |              |
|     150 | `OBSRVTN_SW`                | [MEDPAR Observation Switch](variables.md#medpar-observation-switch)                                                                         |              |              |
|     151 | `NEW_TCHNLGY_ADD_ON_AMT`    | [MEDPAR New Technology Add On Amount](variables.md#medpar-new-technology-add-on-amount)                                                     |              |              |
|     152 | `BASE_OPRTG_DRG_AMT`        | [MEDPAR Base Operating DRG Amount](variables.md#medpar-base-operating-drg-amount)                                                           |              |              |
|     153 | `OPRTG_HSP_AMT`             | [MEDPAR Operating Hospital Amount](variables.md#medpar-operating-hospital-amount)                                                           |              |              |
|     154 | `MDCL_SRGCL_GNRL_AMT`       | [MEDPAR Medical Surgical General Amount](variables.md#medpar-medical-surgical-general-amount)                                               |              |              |
|     155 | `MDCL_SRGCL_NSTRL_AMT`      | [MEDPAR Medical Surgical Non-Sterile Supplies Amount](variables.md#medpar-medical-surgical-non-sterile-supplies-amount)                     |              |              |
|     156 | `MDCL_SRGCL_STRL_AMT`       | [MEDPAR Medical Surgical Sterile Supplies Amount](variables.md#medpar-medical-surgical-sterile-supplies-amount)                             |              |              |
|     157 | `TAKE_HOME_AMT`             | [MEDPAR Take Home Amount](variables.md#medpar-take-home-amount)                                                                             |              |              |
|     158 | `PRSTHTC_ORTHTC_AMT`        | [MEDPAR Prosthetic Orthotic Amount](variables.md#medpar-prosthetic-orthotic-amount)                                                         |              |              |
|     159 | `MDCL_SRGCL_PCMKR_AMT`      | [MEDPAR Medical Surgical Pacemaker Amount](variables.md#medpar-medical-surgical-pacemaker-amount)                                           |              |              |
|     160 | `INTRAOCULAR_LENS_AMT`      | [MEDPAR Intraocular Lens Amount](variables.md#medpar-intraocular-lens-amount)                                                               |              |              |
|     161 | `OXYGN_TAKE_HOME_AMT`       | [MEDPAR Oxygen Take Home Amount](variables.md#medpar-oxygen-take-home-amount)                                                               |              |              |
|     162 | `OTHR_IMPLANTS_AMT`         | [MEDPAR Other Implants Amount](variables.md#medpar-other-implants-amount)                                                                   |              |              |
|     163 | `OTHR_SUPLIES_DVC_AMT`      | [MEDPAR Other Supplies Device Amount](variables.md#medpar-other-supplies-device-amount)                                                     |              |              |
|     164 | `INCDNT_RDLGY_AMT`          | [MEDPAR Incident to Radiology Amount](variables.md#medpar-incident-to-radiology-amount)                                                     |              |              |
|     165 | `INCDNT_DGNSTC_SRVCS_AMT`   | [MEDPAR Incident to Other Diagnostic Services Amount](variables.md#medpar-incident-to-other-diagnostic-services-amount)                     |              |              |
|     166 | `MDCL_SRGCL_DRSNG_AMT`      | [MEDPAR Medical Surgical Dressing Amount](variables.md#medpar-medical-surgical-dressing-amount)                                             |              |              |
|     167 | `INVSTGTNL_DVC_AMT`         | [MEDPAR Investigational Device Amount](variables.md#medpar-investigational-device-amount)                                                   |              |              |
|     168 | `MDCL_SRGCL_MISC_AMT`       | [MEDPAR Medical Surgical Miscellaneous Amount](variables.md#medpar-medical-surgical-miscellaneous-amount)                                   |              |              |
|     169 | `RDLGY_ONCOLOGY_AMT`        | [MEDPAR Radiology Oncology Amount](variables.md#medpar-radiology-oncology-amount)                                                           |              |              |
|     170 | `RDLGY_DGNSTC_AMT`          | [MEDPAR Radiology Diagnostic Amount](variables.md#medpar-radiology-diagnostic-amount)                                                       |              |              |
|     171 | `RDLGY_THRPTC_AMT`          | [MEDPAR Radiology Therapeutic Amount](variables.md#medpar-radiology-therapeutic-amount)                                                     |              |              |
|     172 | `RDLGY_NUCLR_MDCN_AMT`      | [MEDPAR Radiology Nuclear Medicine Amount](variables.md#medpar-radiology-nuclear-medicine-amount)                                           |              |              |
|     173 | `RDLGY_CT_SCAN_AMT`         | [MEDPAR Radiology CT Scan Amount](variables.md#medpar-radiology-ct-scan-amount)                                                             |              |              |
|     174 | `RDLGY_OTHR_IMGNG_AMT`      | [MEDPAR Radiology Other Imaging Amount](variables.md#medpar-radiology-other-imaging-amount)                                                 |              |              |
|     175 | `OPRTG_ROOM_AMT`            | [MEDPAR Operating Room Amount](variables.md#medpar-operating-room-amount)                                                                   |              |              |
|     176 | `OR_LABOR_DLVRY_AMT`        | [MEDPAR Operating Room Labor and Delivery Amount](variables.md#medpar-operating-room-labor-and-delivery-amount)                             |              |              |
|     177 | `CRDC_CATHRZTN_AMT`         | [MEDPAR Cardiac Catheterization Amount](variables.md#medpar-cardiac-catheterization-amount)                                                 |              |              |
