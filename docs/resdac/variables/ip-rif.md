# Variable Definitions

!!! note
    These definitions are scraped from ResDAC. Click on the header of a variable description to see the ResDAC page.



## [Beneficiary LRD Used Count](https://www.resdac.org/cms-data/variables/Beneficiary-LRD-Used-Count)

- Short SAS Name: `LRD_USE`
- Long SAS Name: `BENE_LRD_USED_CNT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

The number of lifetime reserve days that the beneficiary has elected to use during the period covered by the institutional claim. Under Medicare, each beneficiary has a one-time reserve of sixty additional days of inpatient hospital coverage that can be used after 90 days of inpatient care have been provided in a single benefit period. This count is used to subtract from the total number of lifetime reserve days that a beneficiary has available.



## [Beneficiary Total Coinsurance Days Count](https://www.resdac.org/cms-data/variables/Beneficiary-Total-Coinsurance-Days-Count)

- Short SAS Name: `COIN_DAY`
- Long SAS Name: `BENE_TOT_COINSRNC_DAYS_CNT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The count of the total number of coinsurance days involved with the beneficiary's stay in a facility.



## [Claim Accountable Care Organization (ACO) Identification Number](https://www.resdac.org/cms-data/variables/claim-accountable-care-organization-aco-identification-number)

- Short SAS Name: `ACO_ID_NUM`
- Long SAS Name: `ACO_ID_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the Accountable Care Organization (ACO) Identification Number.



## [Claim Admission Date](https://www.resdac.org/cms-data/variables/Claim-Admission-Date)

- Short SAS Name: `ADMSN_DT`
- Long SAS Name: `CLM_ADMSN_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date the beneficiary was admitted to the hospital, skilled nursing facility, or christian science sanitorium.



## [Claim Admitting Diagnosis Code](https://www.resdac.org/cms-data/variables/Claim-Admitting-Diagnosis-Code)

- Short SAS Name: `ADMTG_DGNS_CD`
- Long SAS Name: `ADMTG_DGNS_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

A diagnosis code on the institutional claim indicating the beneficiary's initial diagnosis at admission.

NOTE1: Effective 1/1/2004 with the implementa- tion of NCH/NMUD CR#1, the admitting diagnosis (also known as reason for patient visit) was added to the Outpatient claim. This data was stored in positions 572-576 (FILLER) until the implementation of NCH/NMUD CR#2. Prior to 1/1/2004, this field was only present on inpatient claims.

Additional exception: Virgin Island hospitals and hospitals that furnish only inpatient Part B services.



## [Claim Attending Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-NPI-Number)

- Short SAS Name: `AT_NPI`
- Long SAS Name: `AT_PHYSN_NPI`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |
| Outpatient | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |

| Dataset    | 2008     | 2007     | 2006     | 2005     | 2004     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |
| Outpatient | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |

| Dataset    | 2003     | 2002     | 2001     | 2000     | 1999     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |
| Outpatient | `at_npi` | `at_npi` | `at_npi` | `at_npi` | `at_npi` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

On an institutional claim, the national provider identifier (NPI) number assigned to uniquely identify the physician who has overall responsibility for the beneficiary's care and treatment.

NOTE: Effective May 2007, the NPI will be- come the national standard identifier for covered health care providers. NPIs will replace current OSCAR provider number, UPINs, NSC numbers, and local contractor provider identification numbers (PINs) on standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number (UPIN, PIN, OSCAR provider number, etc.)).

NOTE1: CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available in the NCH. After the 5/07 NPI implementation, the standard system main- tainers will add the legacy number to the claim when it is adjudicated. We will continue to receive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no NEW UPINs (legacy number) will be generated for NEW physicians (Part B and Outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.



## [Claim Attending Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-attending-physician-specialty-code)

- Short SAS Name: `AT_PHYSN_SPCLTY_CD`
- Long SAS Name: `AT_PHYSN_SPCLTY_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

This variable is the code used to identify the CMS specialty code corresponding to the attending physician.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00     | Carrier wide                                                                                                                                            |
| 01     | General practice                                                                                                                                        |
| 02     | General Surgery                                                                                                                                         |
| 03     | Allergy/immunology                                                                                                                                      |
| 04     | Otolaryngology                                                                                                                                          |
| 05     | Anesthesiology                                                                                                                                          |
| 06     | Cardiology                                                                                                                                              |
| 07     | Dermatology                                                                                                                                             |
| 08     | Family Practice                                                                                                                                         |
| 09     | Interventional Pain Management (IPM) (eff. 4/1/03)                                                                                                      |
| 10     | Gastroenterology                                                                                                                                        |
| 11     | Internal Medicine                                                                                                                                       |
| 12     | Osteopathic manipulative therapy                                                                                                                        |
| 13     | Neurology                                                                                                                                               |
| 14     | Neurosurgery                                                                                                                                            |
| 15     | Speech/language pathology                                                                                                                               |
| 16     | Obstetrics/gynecology                                                                                                                                   |
| 17     | Hospice and Palliative Care                                                                                                                             |
| 18     | Ophthalmology                                                                                                                                           |
| 19     | Oral surgery (dentists only)                                                                                                                            |
| 20     | Orthopedic surgery                                                                                                                                      |
| 21     | Cardiac Electrophysiology                                                                                                                               |
| 22     | Pathology                                                                                                                                               |
| 24     | Plastic and reconstructive surgery                                                                                                                      |
| 25     | Physical medicine and rehabilitation                                                                                                                    |
| 26     | Psychiatry                                                                                                                                              |
| 27     | General Psychiatry                                                                                                                                      |
| 28     | Colorectal surgery (formerly proctology)                                                                                                                |
| 29     | Pulmonary disease                                                                                                                                       |
| 30     | Diagnostic radiology                                                                                                                                    |
| 31     | Intensive cardiac rehabilitation                                                                                                                        |
| 32     | Anesthesiologist Assistants (eff. 4/1/03 - previously grouped with Certified Registered Nurse Anesthetists (CRNA))                                      |
| 33     | Thoracic surgery                                                                                                                                        |
| 34     | Urology                                                                                                                                                 |
| 35     | Chiropractic                                                                                                                                            |
| 36     | Nuclear medicine                                                                                                                                        |
| 37     | Pediatric medicine                                                                                                                                      |
| 38     | Geriatric medicine                                                                                                                                      |
| 39     | Nephrology                                                                                                                                              |
| 40     | Hand surgery                                                                                                                                            |
| 41     | Optometrist                                                                                                                                             |
| 42     | Certified nurse midwife                                                                                                                                 |
| 43     | Certified Registered Nurse Anesthetist (CRNA) (Anesthesiologist Assistants were removed from this specialty 4/1/03)                                     |
| 44     | Infectious disease                                                                                                                                      |
| 45     | Mammography screening center                                                                                                                            |
| 46     | Endocrinology                                                                                                                                           |
| 47     | Independent Diagnostic Testing Facility (IDTF)                                                                                                          |
| 48     | Podiatry                                                                                                                                                |
| 49     | Ambulatory surgical center (formerly miscellaneous)                                                                                                     |
| 50     | Nurse practitioner                                                                                                                                      |
| 51     | Medical supply company with certified orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                            |
| 52     | Medical supply company with certified prosthetist (certified by American Board for Certification in Prosthetics and Orthotics) e                        |
| 53     | Medical supply company with certified prosthetist-orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                |
| 54     | Medical supply company for DMERC (and not included in 51-53)                                                                                            |
| 55     | Individual certified orthotist                                                                                                                          |
| 56     | Individual certified prosthetist                                                                                                                        |
| 57     | Individual certified prosthetist-orthotist                                                                                                              |
| 58     | Medical supply company with registered pharmacist                                                                                                       |
| 59     | Ambulance service supplier, (e.g., private ambulance companies, funeral homes, etc.)                                                                    |
| 60     | Public health or welfare agencies (federal, state, and local)                                                                                           |
| 61     | Voluntary health or charitable agencies (e.g. National Cancer Society, National Heart Association, Catholic Charities)                                  |
| 62     | Psychologist (billing indepedently)                                                                                                                     |
| 63     | Portable X-ray supplier                                                                                                                                 |
| 64     | Audiologist (billing independently)                                                                                                                     |
| 65     | Physical therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                            |
| 66     | Rheumatology                                                                                                                                            |
| 67     | Occupational therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                        |
| 68     | Clinical psychologist                                                                                                                                   |
| 69     | Clinical laboratory (billing independently)                                                                                                             |
| 70     | Multispecialty clinic or group practice                                                                                                                 |
| 71     | Registered Dietician/Nutrition Professional (eff. 1/1/02)                                                                                               |
| 72     | Pain Management (eff. 1/1/02)                                                                                                                           |
| 73     | Mass Immunization Roster Biller                                                                                                                         |
| 74     | Radiation Therapy Centers (prior to 4/2003 this included independent Diagnostic Testing Facilities (IDTF)                                               |
| 75     | Slide Preparation Facilities (added to differentiate them from Independent Diagnostic Testing Facilities (IDTFs -- eff. 4/1/03)                         |
| 76     | Peripheral vascular disease                                                                                                                             |
| 77     | Vascular surgery                                                                                                                                        |
| 78     | Cardiac surgery                                                                                                                                         |
| 79     | Addiction medicine                                                                                                                                      |
| 80     | Licensed clinical social worker                                                                                                                         |
| 81     | Critical care (intensivists)                                                                                                                            |
| 82     | Hematology                                                                                                                                              |
| 83     | Hematology/oncology                                                                                                                                     |
| 84     | Preventative medicine                                                                                                                                   |
| 85     | Maxillofacial surgery                                                                                                                                   |
| 86     | Neuropsychiatry                                                                                                                                         |
| 87     | All other suppliers (e.g. drug and department stores)                                                                                                   |
| 88     | Unknown supplier/provider specialty                                                                                                                     |
| 89     | Certified clinical nurse specialist                                                                                                                     |
| 90     | Medical oncology                                                                                                                                        |
| 91     | Surgical oncology                                                                                                                                       |
| 92     | Radiation oncology                                                                                                                                      |
| 93     | Emergency medicine                                                                                                                                      |
| 94     | Interventional radiology                                                                                                                                |
| 95     | Competitive Acquisition Program (CAP) Vendor (eff. 07/01/06). Prior to 07/01/06, known as Independent physiological laboratory                          |
| 96     | Optician                                                                                                                                                |
| 97     | Physician assistant                                                                                                                                     |
| 98     | Gynecologist/oncologist                                                                                                                                 |
| 99     | Unknown physician specialty                                                                                                                             |
| A0     | Hospital (DMERCs only)                                                                                                                                  |
| A1     | SNF (DMERCs only)                                                                                                                                       |
| A2     | Intermediate care nursing facility (DMERCs only)                                                                                                        |
| A3     | Nursing facility, other (DMERCs only)                                                                                                                   |
| A4     | Home Health Agency (DMERCs only)                                                                                                                        |
| A5     | Pharmacy (DMERC)                                                                                                                                        |
| A6     | Medical supply company with respiratory therapist (DMERCs only)                                                                                         |
| A7     | Department store (DMERC)                                                                                                                                |
| A8     | Grocery store (DMERC)                                                                                                                                   |
| A9     | Indian Health Service (IHS), tribe and tribal organizations (non-hospital or non-hospital based facilities, eff. 1/2005)                                |
| B1     | Supplier of oxygen and/or oxygen related equipment (eff. 10/2/07)                                                                                       |
| B2     | Pedorthic Personnel (eff. 10/2/07)                                                                                                                      |
| B3     | Medical Supply Company with pedorthic personnel (eff. 10/2/07)                                                                                          |
| B4     | Does not meet definition of health care provider (e.g., Rehabilitation agency, organ procurement organizations, histocompatibility labs) (eff. 10/2/07) |
| B5     | Ocularist                                                                                                                                               |
| C0     | Sleep medicine                                                                                                                                          |
| C1     | Centralized flu                                                                                                                                         |
| C2     | Indirect payment procedure                                                                                                                              |
| C3     | Interventional cardiology                                                                                                                               |
| C5     | Dentist (off. 7/2016)                                                                                                                                   |

## [Claim Attending Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Attending-Physician-UPIN-Number)

- Short SAS Name: `AT_UPIN`
- Long SAS Name: `AT_PHYSN_UPIN`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |
| Outpatient | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |
| Outpatient | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |
| Outpatient | `at_upin` | `at_upin` | `at_upin` | `at_upin` | `at_upin` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

On an institutional claim, the unique physician identification number (UPIN) of the physician who would normally be expected to certify and recertify the medical necessity of the services rendered and/or who has primary responsibility for the beneficiary's medical care and treatment (attending physician).

NPIs replaced UPINs as the standard provider identifiers beginning in 2007. The UPIN is almost never populated after 2009.



## [Claim Base Operating DRG Amount](https://www.resdac.org/cms-data/variables/claim-base-operating-drg-amount)

- Short SAS Name: `CLM_BASE_OPRTG_DRG_AMT`
- Long SAS Name: `CLM_BASE_OPRTG_DRG_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

The amount of the wage-adjusted DRG operating payment plus the technology add-on payment.

This variable was new in 2011.   It is populated only for Inpatient claims.



## [Claim Bundled Adjustment Payment Amount](https://www.resdac.org/cms-data/variables/claim-bundled-adjustment-payment-amount)

- Short SAS Name: `CLM_BNDLD_ADJSTMT_PMT_AMT`
- Long SAS Name: `CLM_BNDLD_ADJSTMT_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field represents the amount the claim was reduced for those hospitals participating in Model 1 of the Bundled Payments for Care Improvement initiative (BPCI, Model 1).

The hospital must be participating in the Model 1 of the Bundled Payments for Care Improvement initiative (refer to CLM_CARE_IMPRVMT_MODEL_CD1). The percentage of the discount that this amount represents is in the field called CLM_BNDLD_MODEL_1_DSCNT_PCT.   This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Bundled Model 1 Discount Percent](https://www.resdac.org/cms-data/variables/claim-bundled-model-1-discount-percent)

- Short SAS Name: `CLM_BNDLD_MODEL_1_DSCNT_PCT`
- Long SAS Name: `CLM_BNDLD_MODEL_1_DSCNT_PCT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field identifies the discount percentage which will be applied to payment for all participating hospitals' DRG over the lifetime of the Bundled Payments for Care Improvement initiative (BPCI, Model 1).

The hospital must be participating in the Model 1 of the BPCI (refer to CLM_CARE_IMPRVMT_MODEL_CD1).
The dollar amount of the payment reduction for the service is in the field called CLM_BNDLD_ADJSTMT_PMT_AMT.
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code   |
|:-------|
| X.XX   |

## [Claim Care Improvement Model 1 Code (bundled payment)](https://www.resdac.org/cms-data/variables/claim-care-improvement-model-1-code-bundled-payment)

- Short SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD1`
- Long SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD1`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This code is used to identify that the care improvement model 1 is being used for bundling payments. The initiative if referred to as the Bundled Payments for Care Improvement initiative (BPCI, Model 1).

There are 4 of these Care Improvement Model fields (CLM_CARE_IMPRVMT_MODEL_CD1-CLM_CARE_IMPRVMT_MODEL_CD4).
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                       |
|:-------------|:---------------------------------|
| 61           | Care Improvement Model 1 is used |
| Null/missing | nan                              |

## [Claim Care Improvement Model 2 Code](https://www.resdac.org/cms-data/variables/claim-care-improvement-model-2-code)

- Short SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD2`
- Long SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD2`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This code is used to identify that the care improvement model 2 is being used for payments.

There are 4 of these Care Improvement Model fields (CLM_CARE_IMPRVMT_MODEL_CD1-CLM_CARE_IMPRVMT_MODEL_CD4).
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                       |
|:-------------|:---------------------------------|
| 62           | Care Improvement Model 2 is used |
| Null/missing | nan                              |

## [Claim Care Improvement Model 3 Code](https://www.resdac.org/cms-data/variables/claim-care-improvement-model-3-code)

- Short SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD3`
- Long SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD3`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This code is used to identify that the care improvement model 3 is being used for payments. 

There are 4 of these Care Improvement Model fields (CLM_CARE_IMPRVMT_MODEL_CD1-CLM_CARE_IMPRVMT_MODEL_CD4).
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                       |
|:-------------|:---------------------------------|
| 63           | Care Improvement Model 3 is used |
| Null/missing | nan                              |

## [Claim Care Improvement Model 4 Code](https://www.resdac.org/cms-data/variables/claim-care-improvement-model-4-code)

- Short SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD4`
- Long SAS Name: `CLM_CARE_IMPRVMT_MODEL_CD4`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This code is used to identify that the care improvement model 4 is being used for payments.

There are 4 of these Care Improvement Model fields (CLM_CARE_IMPRVMT_MODEL_CD1-CLM_CARE_IMPRVMT_MODEL_CD4).
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                       |
|:-------------|:---------------------------------|
| 64           | Care Improvement Model 4 is used |
| Null/missing | nan                              |

## [Claim Diagnosis Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-I)

- Short SAS Name: `ICD_DGNS_CD1`
- Long SAS Name: `ICD_DGNS_CD1`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd1` | `icd_dgns_cd1` | `icd_dgns_cd1` | `dgns_cd1` |
| Inpatient  | `icd_dgns_cd1` | `icd_dgns_cd1` | `icd_dgns_cd1` | `icd_dgns_cd1` | `dgnscd1`  |
| Outpatient | `icd_dgns_cd1` | `icd_dgns_cd1` | `icd_dgns_cd1` | `icd_dgns_cd1` | `dgnscd1`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` |
| Inpatient  | `dgnscd1`  | `dgnscd1`  | `dgnscd1`  | `dgns_cd1` | `dgns_cd1` |
| Outpatient | `dgnscd1`  | `dgnscd1`  | `dgnscd1`  | `dgns_cd1` | `dgns_cd1` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` | `bdx1`    |
| Inpatient  | `dgns_cd1` | `dgns_cd1` | `dgnscd1`  | `dgnscd1`  | `dgnscd1` |
| Outpatient | `dgns_cd1` | `dgns_cd1` | `dgns_cd1` | `dgnscd1`  | `dgnscd1` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code). NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code I Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-i-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW1`
- Long SAS Name: `CLM_POA_IND_SW1`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.

??? limitation
	DESCRIPTION :
	DESCRIPTION:
	Missing present on admission (POA) indicators on the NCH claims.
	BACKGROUND :
	A problem has been discovered with the Inpatient claims received
	from CWF from July 6, 2009 through October 4, 2009. The
	claims received during this timeperiod have no POA indicators.
	The problem was a result of a defect in the conversion code
	used by CWF to convert the new 5010 record format back to the
	4010 format for the NCH. The reason CWF was converting the
	claims to the 4010 format was because they implemented the 5010
	format beginning in July 2009 but the NCH is still using
	the 4010 until 1/3/2011.
	CORRECTIVE ACTION:
	CWF will be sending in adjustment claims to correct the
	problem. The claims will come into the NCH the week of
	December 19, 2009. There were approximately 3 million
	claims missing the POA indicator.CLM_POA_IND_CD_LIM

<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |
| Blank  | Identifies diagnosis codes that are exempt from the POA reporting requirements (replaces the '1'). NOTE: NCH/NMUD will carry a '0' in place of a blank.                                                                                                                                                                                                                             |

## [Claim Diagnosis Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-II)

- Short SAS Name: `ICD_DGNS_CD2`
- Long SAS Name: `ICD_DGNS_CD2`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd2` | `icd_dgns_cd2` | `icd_dgns_cd2` | `dgns_cd2` |
| Inpatient  | `icd_dgns_cd2` | `icd_dgns_cd2` | `icd_dgns_cd2` | `icd_dgns_cd2` | `dgnscd2`  |
| Outpatient | `icd_dgns_cd2` | `icd_dgns_cd2` | `icd_dgns_cd2` | `icd_dgns_cd2` | `dgnscd2`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` |
| Inpatient  | `dgnscd2`  | `dgnscd2`  | `dgnscd2`  | `dgns_cd2` | `dgns_cd2` |
| Outpatient | `dgnscd2`  | `dgnscd2`  | `dgnscd2`  | `dgns_cd2` | `dgns_cd2` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` | `bdx2`    |
| Inpatient  | `dgns_cd2` | `dgns_cd2` | `dgnscd2`  | `dgnscd2`  | `dgnscd2` |
| Outpatient | `dgns_cd2` | `dgns_cd2` | `dgns_cd2` | `dgnscd2`  | `dgnscd2` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code). NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code II Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-ii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW2`
- Long SAS Name: `CLM_POA_IND_SW2`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-III)

- Short SAS Name: `ICD_DGNS_CD3`
- Long SAS Name: `ICD_DGNS_CD3`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd3` | `icd_dgns_cd3` | `icd_dgns_cd3` | `dgns_cd3` |
| Inpatient  | `icd_dgns_cd3` | `icd_dgns_cd3` | `icd_dgns_cd3` | `icd_dgns_cd3` | `dgnscd3`  |
| Outpatient | `icd_dgns_cd3` | `icd_dgns_cd3` | `icd_dgns_cd3` | `icd_dgns_cd3` | `dgnscd3`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` |
| Inpatient  | `dgnscd3`  | `dgnscd3`  | `dgnscd3`  | `dgns_cd3` | `dgns_cd3` |
| Outpatient | `dgnscd3`  | `dgnscd3`  | `dgnscd3`  | `dgns_cd3` | `dgns_cd3` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` | `bdx3`    |
| Inpatient  | `dgns_cd3` | `dgns_cd3` | `dgnscd3`  | `dgnscd3`  | `dgnscd3` |
| Outpatient | `dgns_cd3` | `dgns_cd3` | `dgns_cd3` | `dgnscd3`  | `dgnscd3` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code). NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code III Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-iii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW3`
- Long SAS Name: `CLM_POA_IND_SW3`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IV)

- Short SAS Name: `ICD_DGNS_CD4`
- Long SAS Name: `ICD_DGNS_CD4`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd4` | `icd_dgns_cd4` | `icd_dgns_cd4` | `dgns_cd4` |
| Inpatient  | `icd_dgns_cd4` | `icd_dgns_cd4` | `icd_dgns_cd4` | `icd_dgns_cd4` | `dgnscd4`  |
| Outpatient | `icd_dgns_cd4` | `icd_dgns_cd4` | `icd_dgns_cd4` | `icd_dgns_cd4` | `dgnscd4`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` |
| Inpatient  | `dgnscd4`  | `dgnscd4`  | `dgnscd4`  | `dgns_cd4` | `dgns_cd4` |
| Outpatient | `dgnscd4`  | `dgnscd4`  | `dgnscd4`  | `dgns_cd4` | `dgns_cd4` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` | `bdx4`    |
| Inpatient  | `dgns_cd4` | `dgns_cd4` | `dgnscd4`  | `dgnscd4`  | `dgnscd4` |
| Outpatient | `dgns_cd4` | `dgns_cd4` | `dgns_cd4` | `dgnscd4`  | `dgnscd4` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code). NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code IV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-iv-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW4`
- Long SAS Name: `CLM_POA_IND_SW4`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code IX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IX)

- Short SAS Name: `ICD_DGNS_CD9`
- Long SAS Name: `ICD_DGNS_CD9`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009      |
|:-----------|:---------------|:---------------|:---------------|:---------------|:----------|
| Carrier    |                | `icd_dgns_cd9` | `icd_dgns_cd9` | `icd_dgns_cd9` |           |
| Inpatient  | `icd_dgns_cd9` | `icd_dgns_cd9` | `icd_dgns_cd9` | `icd_dgns_cd9` | `dgnscd9` |
| Outpatient | `icd_dgns_cd9` | `icd_dgns_cd9` | `icd_dgns_cd9` | `icd_dgns_cd9` | `dgnscd9` |

| Dataset    | 2008      | 2007      | 2006      | 2005       | 2004       |
|:-----------|:----------|:----------|:----------|:-----------|:-----------|
| Carrier    |           |           |           |            |            |
| Inpatient  | `dgnscd9` | `dgnscd9` | `dgnscd9` | `dgns_cd9` | `dgns_cd9` |
| Outpatient | `dgnscd9` | `dgnscd9` | `dgnscd9` | `dgns_cd9` | `dgns_cd9` |

| Dataset    | 2003       | 2002       | 2001       | 2000      | 1999      |
|:-----------|:-----------|:-----------|:-----------|:----------|:----------|
| Carrier    |            |            |            |           |           |
| Inpatient  | `dgns_cd9` | `dgns_cd9` | `dgnscd9`  | `dgnscd9` | `dgnscd9` |
| Outpatient | `dgns_cd9` | `dgns_cd9` | `dgns_cd9` | `dgnscd9` | `dgnscd9` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code IX Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-ix-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW9`
- Long SAS Name: `CLM_POA_IND_SW9`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-V)

- Short SAS Name: `ICD_DGNS_CD5`
- Long SAS Name: `ICD_DGNS_CD5`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd5` | `icd_dgns_cd5` | `icd_dgns_cd5` | `dgns_cd5` |
| Inpatient  | `icd_dgns_cd5` | `icd_dgns_cd5` | `icd_dgns_cd5` | `icd_dgns_cd5` | `dgnscd5`  |
| Outpatient | `icd_dgns_cd5` | `icd_dgns_cd5` | `icd_dgns_cd5` | `icd_dgns_cd5` | `dgnscd5`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd5` | `dgns_cd5` | `dgns_cd5` |            |            |
| Inpatient  | `dgnscd5`  | `dgnscd5`  | `dgnscd5`  | `dgns_cd5` | `dgns_cd5` |
| Outpatient | `dgnscd5`  | `dgnscd5`  | `dgnscd5`  | `dgns_cd5` | `dgns_cd5` |

| Dataset    | 2003       | 2002       | 2001       | 2000      | 1999      |
|:-----------|:-----------|:-----------|:-----------|:----------|:----------|
| Carrier    |            |            |            |           |           |
| Inpatient  | `dgns_cd5` | `dgns_cd5` | `dgnscd5`  | `dgnscd5` | `dgnscd5` |
| Outpatient | `dgns_cd5` | `dgns_cd5` | `dgns_cd5` | `dgnscd5` | `dgnscd5` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code V Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-v-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW5`
- Long SAS Name: `CLM_POA_IND_SW5`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VI)

- Short SAS Name: `ICD_DGNS_CD6`
- Long SAS Name: `ICD_DGNS_CD6`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd6` | `icd_dgns_cd6` | `icd_dgns_cd6` | `dgns_cd6` |
| Inpatient  | `icd_dgns_cd6` | `icd_dgns_cd6` | `icd_dgns_cd6` | `icd_dgns_cd6` | `dgnscd6`  |
| Outpatient | `icd_dgns_cd6` | `icd_dgns_cd6` | `icd_dgns_cd6` | `icd_dgns_cd6` | `dgnscd6`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd6` | `dgns_cd6` | `dgns_cd6` |            |            |
| Inpatient  | `dgnscd6`  | `dgnscd6`  | `dgnscd6`  | `dgns_cd6` | `dgns_cd6` |
| Outpatient | `dgnscd6`  | `dgnscd6`  | `dgnscd6`  | `dgns_cd6` | `dgns_cd6` |

| Dataset    | 2003       | 2002       | 2001       | 2000      | 1999      |
|:-----------|:-----------|:-----------|:-----------|:----------|:----------|
| Carrier    |            |            |            |           |           |
| Inpatient  | `dgns_cd6` | `dgns_cd6` | `dgnscd6`  | `dgnscd6` | `dgnscd6` |
| Outpatient | `dgns_cd6` | `dgns_cd6` | `dgns_cd6` | `dgnscd6` | `dgnscd6` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code VI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-vi-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW6`
- Long SAS Name: `CLM_POA_IND_SW6`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VII)

- Short SAS Name: `ICD_DGNS_CD7`
- Long SAS Name: `ICD_DGNS_CD7`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd7` | `icd_dgns_cd7` | `icd_dgns_cd7` | `dgns_cd7` |
| Inpatient  | `icd_dgns_cd7` | `icd_dgns_cd7` | `icd_dgns_cd7` | `icd_dgns_cd7` | `dgnscd7`  |
| Outpatient | `icd_dgns_cd7` | `icd_dgns_cd7` | `icd_dgns_cd7` | `icd_dgns_cd7` | `dgnscd7`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd7` | `dgns_cd7` | `dgns_cd7` |            |            |
| Inpatient  | `dgnscd7`  | `dgnscd7`  | `dgnscd7`  | `dgns_cd7` | `dgns_cd7` |
| Outpatient | `dgnscd7`  | `dgnscd7`  | `dgnscd7`  | `dgns_cd7` | `dgns_cd7` |

| Dataset    | 2003       | 2002       | 2001       | 2000      | 1999      |
|:-----------|:-----------|:-----------|:-----------|:----------|:----------|
| Carrier    |            |            |            |           |           |
| Inpatient  | `dgns_cd7` | `dgns_cd7` | `dgnscd7`  | `dgnscd7` | `dgnscd7` |
| Outpatient | `dgns_cd7` | `dgns_cd7` | `dgns_cd7` | `dgnscd7` | `dgnscd7` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code VII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-vii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW7`
- Long SAS Name: `CLM_POA_IND_SW7`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                               |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                               |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                       |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                         |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                   |
| 1      | Unreported/not used -exempt from POA reporting. This code is equivalent to a blank on the UB-04, however, blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1'. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                               |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                             |

## [Claim Diagnosis Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VIII)

- Short SAS Name: `ICD_DGNS_CD8`
- Long SAS Name: `ICD_DGNS_CD8`

<h3>Variable Names</h3>

| Dataset    | 2013           | 2012           | 2011           | 2010           | 2009       |
|:-----------|:---------------|:---------------|:---------------|:---------------|:-----------|
| Carrier    |                | `icd_dgns_cd8` | `icd_dgns_cd8` | `icd_dgns_cd8` | `dgns_cd8` |
| Inpatient  | `icd_dgns_cd8` | `icd_dgns_cd8` | `icd_dgns_cd8` | `icd_dgns_cd8` | `dgnscd8`  |
| Outpatient | `icd_dgns_cd8` | `icd_dgns_cd8` | `icd_dgns_cd8` | `icd_dgns_cd8` | `dgnscd8`  |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `dgns_cd8` | `dgns_cd8` | `dgns_cd8` |            |            |
| Inpatient  | `dgnscd8`  | `dgnscd8`  | `dgnscd8`  | `dgns_cd8` | `dgns_cd8` |
| Outpatient | `dgnscd8`  | `dgnscd8`  | `dgnscd8`  | `dgns_cd8` | `dgns_cd8` |

| Dataset    | 2003       | 2002       | 2001       | 2000      | 1999      |
|:-----------|:-----------|:-----------|:-----------|:----------|:----------|
| Carrier    |            |            |            |           |           |
| Inpatient  | `dgns_cd8` | `dgns_cd8` | `dgnscd8`  | `dgnscd8` | `dgnscd8` |
| Outpatient | `dgns_cd8` | `dgns_cd8` | `dgns_cd8` | `dgnscd8` | `dgnscd8` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code VIII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-viii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW8`
- Long SAS Name: `CLM_POA_IND_SW8`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-X)

- Short SAS Name: `ICD_DGNS_CD10`
- Long SAS Name: `ICD_DGNS_CD10`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Carrier    |                 | `icd_dgns_cd10` | `icd_dgns_cd10` | `icd_dgns_cd10` |            |
| Inpatient  | `icd_dgns_cd10` | `icd_dgns_cd10` | `icd_dgns_cd10` | `icd_dgns_cd10` | `dgnscd10` |
| Outpatient | `icd_dgns_cd10` | `icd_dgns_cd10` | `icd_dgns_cd10` | `icd_dgns_cd10` | `dgnscd10` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Carrier    |            |            |            |             |             |
| Inpatient  | `dgnscd10` | `dgnscd10` | `dgnscd10` | `dgns_cd10` | `dgns_cd10` |
| Outpatient | `dgnscd10` | `dgnscd10` | `dgnscd10` | `dgns_cd10` | `dgns_cd10` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Carrier    |             |             |             |            |            |
| Inpatient  | `dgns_cd10` | `dgns_cd10` | `dgnscd10`  | `dgnscd10` | `dgnscd10` |
| Outpatient | `dgns_cd10` | `dgns_cd10` | `dgns_cd10` | `dgnscd10` | `dgnscd10` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code X Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-x-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW10`
- Long SAS Name: `CLM_POA_IND_SW10`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XI)

- Short SAS Name: `ICD_DGNS_CD11`
- Long SAS Name: `ICD_DGNS_CD11`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Carrier    |                 | `icd_dgns_cd11` | `icd_dgns_cd11` | `icd_dgns_cd11` |
| Inpatient  | `icd_dgns_cd11` | `icd_dgns_cd11` | `icd_dgns_cd11` | `icd_dgns_cd11` |
| Outpatient | `icd_dgns_cd11` | `icd_dgns_cd11` | `icd_dgns_cd11` | `icd_dgns_cd11` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xi-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW11`
- Long SAS Name: `CLM_POA_IND_SW11`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XII)

- Short SAS Name: `ICD_DGNS_CD12`
- Long SAS Name: `ICD_DGNS_CD12`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Carrier    |                 | `icd_dgns_cd12` | `icd_dgns_cd12` | `icd_dgns_cd12` |
| Inpatient  | `icd_dgns_cd12` | `icd_dgns_cd12` | `icd_dgns_cd12` | `icd_dgns_cd12` |
| Outpatient | `icd_dgns_cd12` | `icd_dgns_cd12` | `icd_dgns_cd12` | `icd_dgns_cd12` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10. NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW12`
- Long SAS Name: `CLM_POA_IND_SW12`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIII)

- Short SAS Name: `ICD_DGNS_CD13`
- Long SAS Name: `ICD_DGNS_CD13`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd13` | `icd_dgns_cd13` | `icd_dgns_cd13` | `icd_dgns_cd13` |
| Outpatient | `icd_dgns_cd13` | `icd_dgns_cd13` | `icd_dgns_cd13` | `icd_dgns_cd13` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XIII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xiii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW13`
- Long SAS Name: `CLM_POA_IND_SW13`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XIV-0)

- Short SAS Name: `ICD_DGNS_CD14`
- Long SAS Name: `ICD_DGNS_CD14`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd14` | `icd_dgns_cd14` | `icd_dgns_cd14` | `icd_dgns_cd14` |
| Outpatient | `icd_dgns_cd14` | `icd_dgns_cd14` | `icd_dgns_cd14` | `icd_dgns_cd14` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XIV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xiv-diagnosis-present-admission-indicator-code-0)

- Short SAS Name: `CLM POA IND SW14`
- Long SAS Name: `CLM_POA_IND_SW14`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XIX](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xix)

- Short SAS Name: `ICD_DGNS_CD19`
- Long SAS Name: `ICD_DGNS_CD19`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd19` | `icd_dgns_cd19` | `icd_dgns_cd19` | `icd_dgns_cd19` |
| Outpatient | `icd_dgns_cd19` | `icd_dgns_cd19` | `icd_dgns_cd19` | `icd_dgns_cd19` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XIX Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xix-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW19`
- Long SAS Name: `CLM_POA_IND_SW19`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XV)

- Short SAS Name: `ICD_DGNS_CD15`
- Long SAS Name: `ICD_DGNS_CD15`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd15` | `icd_dgns_cd15` | `icd_dgns_cd15` | `icd_dgns_cd15` |
| Outpatient | `icd_dgns_cd15` | `icd_dgns_cd15` | `icd_dgns_cd15` | `icd_dgns_cd15` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xv-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW15`
- Long SAS Name: `CLM_POA_IND_SW15`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XVI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVI)

- Short SAS Name: `ICD_DGNS_CD16`
- Long SAS Name: `ICD_DGNS_CD16`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd16` | `icd_dgns_cd16` | `icd_dgns_cd16` | `icd_dgns_cd16` |
| Outpatient | `icd_dgns_cd16` | `icd_dgns_cd16` | `icd_dgns_cd16` | `icd_dgns_cd16` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XVI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xvi-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW16`
- Long SAS Name: `CLM_POA_IND_SW16`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XVII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVII)

- Short SAS Name: `ICD_DGNS_CD17`
- Long SAS Name: `ICD_DGNS_CD17`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd17` | `icd_dgns_cd17` | `icd_dgns_cd17` | `icd_dgns_cd17` |
| Outpatient | `icd_dgns_cd17` | `icd_dgns_cd17` | `icd_dgns_cd17` | `icd_dgns_cd17` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XVII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xvii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW17`
- Long SAS Name: `CLM_POA_IND_SW17`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XVIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XVIII)

- Short SAS Name: `ICD_DGNS_CD18`
- Long SAS Name: `ICD_DGNS_CD18`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd18` | `icd_dgns_cd18` | `icd_dgns_cd18` | `icd_dgns_cd18` |
| Outpatient | `icd_dgns_cd18` | `icd_dgns_cd18` | `icd_dgns_cd18` | `icd_dgns_cd18` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XVIII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xviii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW18`
- Long SAS Name: `CLM_POA_IND_SW18`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XX](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XX)

- Short SAS Name: `ICD_DGNS_CD20`
- Long SAS Name: `ICD_DGNS_CD20`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd20` | `icd_dgns_cd20` | `icd_dgns_cd20` | `icd_dgns_cd20` |
| Outpatient | `icd_dgns_cd20` | `icd_dgns_cd20` | `icd_dgns_cd20` | `icd_dgns_cd20` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XX Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xx-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW20`
- Long SAS Name: `CLM_POA_IND_SW20`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XXI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXI)

- Short SAS Name: `ICD_DGNS_CD21`
- Long SAS Name: `ICD_DGNS_CD21`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd21` | `icd_dgns_cd21` | `icd_dgns_cd21` | `icd_dgns_cd21` |
| Outpatient | `icd_dgns_cd21` | `icd_dgns_cd21` | `icd_dgns_cd21` | `icd_dgns_cd21` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XXI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xxi-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW21`
- Long SAS Name: `CLM_POA_IND_SW21`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XXII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXII)

- Short SAS Name: `ICD_DGNS_CD22`
- Long SAS Name: `ICD_DGNS_CD22`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd22` | `icd_dgns_cd22` | `icd_dgns_cd22` | `icd_dgns_cd22` |
| Outpatient | `icd_dgns_cd22` | `icd_dgns_cd22` | `icd_dgns_cd22` | `icd_dgns_cd22` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XXII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xxii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW22`
- Long SAS Name: `CLM_POA_IND_SW22`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XXIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIII)

- Short SAS Name: `ICD_DGNS_CD23`
- Long SAS Name: `ICD_DGNS_CD23`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd23` | `icd_dgns_cd23` | `icd_dgns_cd23` | `icd_dgns_cd23` |
| Outpatient | `icd_dgns_cd23` | `icd_dgns_cd23` | `icd_dgns_cd23` | `icd_dgns_cd23` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XXIII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xxiii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW23`
- Long SAS Name: `CLM_POA_IND_SW23`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XXIV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXIV)

- Short SAS Name: `ICD_DGNS_CD24`
- Long SAS Name: `ICD_DGNS_CD24`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd24` | `icd_dgns_cd24` | `icd_dgns_cd24` | `icd_dgns_cd24` |
| Outpatient | `icd_dgns_cd24` | `icd_dgns_cd24` | `icd_dgns_cd24` | `icd_dgns_cd24` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XXIV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xxiv-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW24`
- Long SAS Name: `CLM_POA_IND_SW24`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Code XXV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XXV)

- Short SAS Name: `ICD_DGNS_CD25`
- Long SAS Name: `ICD_DGNS_CD25`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_dgns_cd25` | `icd_dgns_cd25` | `icd_dgns_cd25` | `icd_dgns_cd25` |
| Outpatient | `icd_dgns_cd25` | `icd_dgns_cd25` | `icd_dgns_cd25` | `icd_dgns_cd25` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).



## [Claim Diagnosis Code XXV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-code-xxv-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM POA IND SW25`
- Long SAS Name: `CLM_POA_IND_SW25`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code I](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-I)

- Short SAS Name: `ICD_DGNS_E_CD1`
- Long SAS Name: `ICD_DGNS_E_CD1`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse effect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code I Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-i-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW1`
- Long SAS Name: `CLM_E_POA_IND_SW1`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code II](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-II)

- Short SAS Name: `ICD_DGNS_E_CD2`
- Long SAS Name: `ICD_DGNS_E_CD2`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code II Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-ii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW2`
- Long SAS Name: `CLM_E_POA_IND_SW2`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code III](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-III)

- Short SAS Name: `ICD_DGNS_E_CD3`
- Long SAS Name: `ICD_DGNS_E_CD3`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code III Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-iii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW3`
- Long SAS Name: `CLM_E_POA_IND_SW3`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code IV](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-IV)

- Short SAS Name: `ICD_DGNS_E_CD4`
- Long SAS Name: `ICD_DGNS_E_CD4`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code IV Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-iv-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW4`
- Long SAS Name: `CLM_E_POA_IND_SW4`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code IX](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-ix)

- Short SAS Name: `ICD_DGNS_E_CD9`
- Long SAS Name: `ICD_DGNS_E_CD9`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code IX Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-ix-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW9`
- Long SAS Name: `CLM_E_POA_IND_SW9`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code V](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-V)

- Short SAS Name: `ICD_DGNS_E_CD5`
- Long SAS Name: `ICD_DGNS_E_CD5`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code V Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-v-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW5`
- Long SAS Name: `CLM_E_POA_IND_SW5`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code VI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VI)

- Short SAS Name: `ICD_DGNS_E_CD6`
- Long SAS Name: `ICD_DGNS_E_CD6`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code VI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-vi-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW6`
- Long SAS Name: `CLM_E_POA_IND_SW6`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code VII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VII)

- Short SAS Name: `ICD_DGNS_E_CD7`
- Long SAS Name: `ICD_DGNS_E_CD7`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code VII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-vii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW7`
- Long SAS Name: `CLM_E_POA_IND_SW7`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code VIII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-VIII)

- Short SAS Name: `ICD_DGNS_E_CD8`
- Long SAS Name: `ICD_DGNS_E_CD8`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code VIII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-viii-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW8`
- Long SAS Name: `CLM_E_POA_IND_SW8`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code X](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-X)

- Short SAS Name: `ICD_DGNS_E_CD10`
- Long SAS Name: `ICD_DGNS_E_CD10`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code X Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/claim-diagnosis-e-code-x-diagnosis-present-admission-indicator-code)

- Short SAS Name: `CLM E POA IND SW10`
- Long SAS Name: `CLM_E_POA_IND_SW10`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code XI](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XI)

- Short SAS Name: `ICD_DGNS_E_CD11`
- Long SAS Name: `ICD_DGNS_E_CD11`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code XI Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XI-Diagnosis-Present-Admission-Indicator-Code)

- Short SAS Name: `CLM E POA IND SW11`
- Long SAS Name: `CLM_E_POA_IND_SW11`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis E Code XII](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XII)

- Short SAS Name: `ICD_DGNS_E_CD12`
- Long SAS Name: `ICD_DGNS_E_CD12`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version J, the code used to identify the external cause of injury, poisoning, or other adverse affect.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accomodate the future implementation of ICD-10. During the Version 'J' conversion this field was populated throughout history.



## [Claim Diagnosis E Code XII Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-E-Code-XII-Diagnosis-Present-Admission-Indicator-Code)

- Short SAS Name: `CLM E POA IND SW12`
- Long SAS Name: `CLM_E_POA_IND_SW12`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the present on admission(POA) indicator code associated with the diagnosis codes.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.                                                                                                                                                                                                                          |
| N      | Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.                                                                                                                                                                                                                  |
| U      | Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.                                                                                                                                                                    |
| W      | Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.                                                                                                                                              |
| 1      | Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list. |
| Z      | Denotes the end of the POA indicators (terminated 1/2011).                                                                                                                                                                                                                                                                                                                          |
| X      | Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).                                                                                                                                                                                                                                        |

## [Claim Diagnosis Related Group Code](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Related-Group-Code)

- Short SAS Name: `DRG_CD`
- Long SAS Name: `CLM_DRG_CD`

<h3>Variable Names</h3>

| Dataset   | 2013     | 2012     | 2011     | 2010     | 2009     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` |
| MedPAR    | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` |

| Dataset   | 2008     | 2007     | 2006     | 2005     | 2004     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` |
| MedPAR    | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` |

| Dataset   | 2003     | 2002     | 2001     | 2000     | 1999     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` | `drg_cd` |
| MedPAR    | `drg_cd` | `drg_cd` | `mdrg`   | `mdrg`   | `mdrg`   |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The diagnostic related group to which a hospital claim belongs for prospective payment purposes.



## [Claim Diagnosis Related Group Outlier Stay Code](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Related-Group-Outlier-Stay-Code)

- Short SAS Name: `OUTLR_CD`
- Long SAS Name: `CLM_DRG_OUTLIER_STAY_CD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlr_cd` | `outlr_cd` | `outlr_cd` | `outlr_cd` | `outlr_cd` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlr_cd` | `outlr_cd` | `outlr_cd` | `outlr_cd` | `outlr_cd` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlr_cd` | `outlr_cd` | `moutlier` | `moutlier` | `moutlier` |

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the code that indicates the beneficiary stay under the prospective payment system which, although classified into a specific diagnosis related group, has an unusually long length (day outlier) or exceptionally high cost (cost outlier).



<h3>Values</h3>

Non-PPS Only

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | No outlier                        |
| 1      | Day outlier (condition code 60)   |
| 2      | Cost outlier, (condition code 61) |

| Code   | Code Value                                                          |
|:-------|:--------------------------------------------------------------------|
| 6      | Valid diagnosis related groups (DRG) received from the intermediary |
| 7      | CMS developed DRG                                                   |
| 8      | CMS developed DRG using patient status code                         |
| 9      | Not groupable                                                       |

## [Claim Electronic Health Record (EHR) Payment Adjustment Amount](https://www.resdac.org/cms-data/variables/claim-electronic-health-record-ehr-payment-adjustment-amount)

- Short SAS Name: `EHR_PYMT_ADJSTMT_AMT`
- Long SAS Name: `EHR_PYMT_ADJSTMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

The claims adjustment payment amount for Hospitals that are not meaningful users of certified Electronic Health Record (EHR) technology.

This field was new in 2012, and is null/missing for all previous years.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Electronic Health Records (EHR) Program Reduction Indicator Switch](https://www.resdac.org/cms-data/variables/claim-electronic-health-records-ehr-program-reduction-indicator-switch)

- Short SAS Name: `EHR_PGM_RDCTN_IND_SW `
- Long SAS Name: `EHR_PGM_RDCTN_IND_SW`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field is a switch that identifies which hospitals are Electronic Health Records(EHR) meaningful users, and distinguishes hospitals that will have a payment penalty for not being meaningful users.

This field is new in October 2014. This field only applies to Inpatient claims.



<h3>Values</h3>

| Code   | Code Value                                               |
|:-------|:---------------------------------------------------------|
| Y      | hospital is subject to a reduction under the EHR program |
| Blank  | not applicable                                           |

## [Claim Facility Type Code](https://www.resdac.org/cms-data/variables/Claim-Facility-Type-Code)

- Short SAS Name: `FAC_TYPE`
- Long SAS Name: `CLM_FAC_TYPE_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The first digit of the type of bill (TOB1) submitted on an institutional claim used to identify the type of facility that provided care to the beneficiary.



<h3>Values</h3>

| Code   | Code Value                                                                                                       |
|:-------|:-----------------------------------------------------------------------------------------------------------------|
| 1      | Hospital                                                                                                         |
| 2      | Skilled nursing facility (SNF)                                                                                   |
| 3      | Home health agency (HHA)                                                                                         |
| 4      | Religious Nonmedical (Hospital) (eff. 8/1/00); prior to 8/00 referenced Christian Science (CS)                   |
| 5      | Religious Nonmedical (Extended Care) (eff. 8/1/00); prior to 8/00 referenced CS (discontinued effective 10/1/05) |
| 6      | Intermediate care                                                                                                |
| 7      | Clinic or hospital-based renal dialysis facility                                                                 |
| 8      | Special facility or ASC surgery                                                                                  |
| 9      | Reserved                                                                                                         |

## [Claim Final Standard Payment Amount](https://www.resdac.org/cms-data/variables/claim-final-standard-payment-amount)

- Short SAS Name: `FINL_STD_AMT `
- Long SAS Name: `FINL_STD_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This amount further adjusts the standard Medicare Payment amount (field called PPS_STD_VAL_PYMT_AMT) by applying additional standardization requirements (e.g. sequestration).

This amount is never used for payments. It is used for comparisons across different regions of the country for the value-based purchasing initiatives and for research.  It is a standard Medicare payment amount, without the geographical payment adjustments and some of the other add-on payments that actually go to the hospitals.    

This field is new in October 2014. This field only applies to Inpatient claims.



<h3>Values</h3>

| Code   |
|:-------|
| XX.XX  |

## [Claim Frequency Code](https://www.resdac.org/cms-data/variables/Claim-Frequency-Code)

- Short SAS Name: `FREQ_CD`
- Long SAS Name: `CLM_FREQ_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The third digit of the type of bill (TOB3) submitted on an institutional claim record to indicate the sequence of a claim in the beneficiary's current episode of care.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                               |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Non-payment/zero claims                                                                                                                                                                                                                                  |
| 1      | Admit thru discharge claim                                                                                                                                                                                                                               |
| 2      | Interim - first claim                                                                                                                                                                                                                                    |
| 3      | Interim - continuing claim (not valid for PPS claims)                                                                                                                                                                                                    |
| 4      | Interim - last claim (not valid for PPS claims)                                                                                                                                                                                                          |
| 5      | Late charge(s) only claim                                                                                                                                                                                                                                |
| 6      | Adjustment of prior claim                                                                                                                                                                                                                                |
| 7      | Replacement of prior claim (eff 10/93) provider debit                                                                                                                                                                                                    |
| 8      | Void/cancel prior claim (eff 10/93) provider cancel                                                                                                                                                                                                      |
| 9      | Final claim -- used in an HH PPS episode to indicate the claim should be processed like debit/credit adjustment to RAP (initial claim) (eff. 10/00)                                                                                                      |
| A      | Admission election notice - used when hospice or Religious Nonmedical Health Care Institution is submitting the HCFA-1450 as an admission notice - hospice NOE only                                                                                      |
| B      | Hospice/Medicare Coordinated Care Demonstration/RNCHI - Termination/Revocation Notice - hospice NOE only (eff 9/93)                                                                                                                                      |
| C      | Hospice change of provider notice - hospice NOE only (eff 9/93)                                                                                                                                                                                          |
| D      | Hospice/Medicare Coordinated Care Demonstration/RNHCI - void/cancel - hospice NOE only (eff 9/93)                                                                                                                                                        |
| E      | Hospice change of ownership - hospice NOE only (eff 1/97)                                                                                                                                                                                                |
| F      | Beneficiary initiated adjustment claim (eff 10/93)                                                                                                                                                                                                       |
| G      | CWF generated adjustment claim (eff 10/93)                                                                                                                                                                                                               |
| H      | CMS generated adjustment claim (eff 10/93)                                                                                                                                                                                                               |
| I      | Misc adjustment claim (other than PRO or provider) - used to identify a debit adjustment initiated by CMS or an intermediary (other than QIO or Provider) - eff 10/93, used to identify intermediary initiated adjustment only                           |
| J      | Other adjustment request (eff 10/93)                                                                                                                                                                                                                     |
| K      | OIG initiated adjustment (eff 10/93)                                                                                                                                                                                                                     |
| M      | MSP adjustment (eff 10/93)                                                                                                                                                                                                                               |
| P      | Adjustment required by Quality Improvement Organization (QIO) -- formerly Peer Review Organization (PRO)                                                                                                                                                 |
| X      | Special adjustment processing - used for QA editing (eff 8/92)                                                                                                                                                                                           |
| Z      | Hospital Encounter Data alternate submission (TOB '11Z') used for MCO enrollee hospital discharges 7/1/97-12/31/98; not stored in NCH. Exception: Problem in startup months may have resulted in this abbreviated UB-92 being erroneously stored in NCH. |

## [Claim From Date](https://www.resdac.org/cms-data/variables/Claim-Date)

- Short SAS Name: `FROM_DT`
- Long SAS Name: `CLM_FROM_DT`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    |           | `from_dt` | `from_dt` | `from_dt` | `from_dt` |
| Inpatient  | `from_dt` | `from_dt` | `from_dt` | `from_dt` | `from_dt` |
| Outpatient | `from_dt` | `from_dt` | `from_dt` | `from_dt` | `from_dt` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    | `from_dt` | `from_dt` | `from_dt` | `sfromdt` | `sfromdt` |
| Inpatient  | `from_dt` | `from_dt` | `from_dt` | `sfromdt` | `sfromdt` |
| Outpatient | `from_dt` | `from_dt` | `from_dt` | `sfromdt` | `sfromdt` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    | `sfromdt` | `sfromdt` | `from_dt` | `from_dt` | `bfromdt` |
| Inpatient  | `sfromdt` | `sfromdt` | `from_dt` | `from_dt` | `from_dt` |
| Outpatient | `sfromdt` | `sfromdt` | `sfromdt` | `from_dt` | `from_dt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The first day on the billing statement covering services rendered to the bene- ficiary (a.k.a. 'Statement Covers From Date').

NOTE: For Home Health PPS claims, the 'from' date and the 'thru' date on the RAP (initial claim) must always match.



## [Claim Full Standard Payment Amount](https://www.resdac.org/cms-data/variables/claim-full-standard-payment-amount)

- Short SAS Name: `CLM_FULL_STD_PYMT_AMT`
- Long SAS Name: `CLM_FULL_STD_PYMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This variable is the standard payment amount for long-term care hospitals (LTCH) under the Medicare prospective payment system (PPS), which is based on the MS-LTC-DRG.    

This amount does not include any applicable outlier payment amount.

Applies only to Inpatient (LTCH) claims.  This field is new in October 2015. For a LTCH PPS claim, only one of four fields will be populated (CLM_SITE_NTRL_PYMT_CST_AMT, CLM_SITE_NTRL_PYMT_IPPS_AMT, CLM_FULL_STD_PYMT_AMT, or CLM_SS_OUTLIER_STD_PYMT_AMT) as they are mutually exclusive (i.e., only one of the 4 fields will have a non-zero value). The field with the non-zero value is included in the Claim Payment Amount field.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim HRR Adjustment Percent](https://www.resdac.org/cms-data/variables/claim-hrr-adjustment-percent)

- Short SAS Name: `CLM_HRR_ADJSTMT_PCT `
- Long SAS Name: `CLM_HRR_ADJSTMT_PCT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

 Under the Hospital Readmissions Reduction (HRR) Program, the amount used to identify the readmission adjustment factor that will be applied.

The ACA (Section 3025) requires CMS to reduce payments to subsection (d) Inpatient Prospective Payment System (IPPS) hospitals with excess readmissions. There is a variable that indicates whether the hospital was excluded from the HRR program (see CLM_HRR_PRTCPNT_IND_CD). This percentage reduction is applied to the base operating DRG amount(defined as the wage-adjusted DRG payment plus new technology add-on payments). 

Additional information is available on the CMS "Hospital Value-Based Purchasing" website. 

The actual dollar amount of the adjustment that applied to the claim is found in the variable called CLM_HRR_ADJSTMT_PMT_AMT.    

This initiative began in 4th Quarter of 2012 (i.e., beginning of Federal fiscal year 13).   

This field was new in 2012, and is null/missing for all previous years.



<h3>Values</h3>

| Code   |
|:-------|
| X.XXXX |

## [Claim Hospital Acquired Condition (HAC) Program Reduction Indicator Switch](https://www.resdac.org/cms-data/variables/claim-hospital-acquired-condition-hac-program-reduction-indicator-switch)

- Short SAS Name: `HAC_PGM_RDCTN_IND_SW`
- Long SAS Name: `HAC_PGM_RDCTN_IND_SW`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field is a switch that identifies hospitals subject to a Hospital Acquired Conditions (HAC) reduction of what they would otherwise be paid under the inpatient prospective payment system (IPPS).

This field is new in October 2014. This field only applies to Inpatient claims.  

For details on the CMS hospital readmission reduction program see the CMS website: http://www.cms.gov/Medicare/Medicare-Fee-For-ServicePayment/AcuteInpatie...



<h3>Values</h3>

| Code   | Code Value                                                             |
|:-------|:-----------------------------------------------------------------------|
| Y      | hospital subject to a reduction under the HAC Reduction Program        |
| N      | hospital is not subject to a reduction under the HAC Reduction Program |

## [Claim Hospital Readmission Reduction (HRR) Adjustment Payment Amount](https://www.resdac.org/cms-data/variables/claim-hospital-readmission-reduction-hrr-adjustment-payment-amount)

- Short SAS Name: `CLM_HRR_ADJSTMT_PMT_AMT`
- Long SAS Name: `CLM_HRR_ADJSTMT_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field represents the Hospital Readmission Reduction (HRR) Program Payment Amount. The amount is the reduction to the claim for a readmission. SHORT

The ACA (Section 3025) requires CMS to reduce payments to subsection (d) Inpatient Prospective Payment System (IPPS) hospitals with excess readmissions. 

There is a variable that indicates whether the hospital was excluded from the HRR program (see CLM_HRR_PRTCPNT_IND_CD). This percentage reduction is applied to the base operating DRG amount(defined as the wage-adjusted DRG payment plus new technology add-on payments). Additional information is available on the CMS "Hospital Value-Based Purchasing" website.   This amount is based on a percent (CLM_HRR_ADJSTMT_PCT).    

This initiative began in 4th Quarter of 2012 (i.e., beginning of Federal fiscal year 13).   

This field was new in 2012, and is null/missing for all previous years.



<h3>Values</h3>

| Code                             |
|:---------------------------------|
| XXX.XX (may be a negative value) |

## [Claim Hospital Readmission Reduction (HRR) Participant Indicator Code](https://www.resdac.org/cms-data/variables/claim-hospital-readmission-reduction-hrr-participant-indicator-code)

- Short SAS Name: `CLM_HRR_PRTCPNT_IND_CD`
- Long SAS Name: `CLM_HRR_PRTCPNT_IND_CD`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field is the code used to identify whether the hospital is participating in the Hospital Readmissions Reduction (HRR) program.

The ACA (Section 3025) requires CMS to reduce payments to Inpatient Prospective Payment System (IPPS) hospitals with excess readmissions.  

Additional information is available on the CMS "Hospital Value-Based Purchasing" website.   

This initiative began in 4th Quarter of 2012 (i.e., beginning of Federal fiscal year 13).   

This field was new in 2012, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                            |
|:-------------|:--------------------------------------|
| 0            | Not participating                     |
| 1            | Participating and not equal to 1.0000 |
| 2            | Participating and equal to 1.0000     |
| Null/missing | Not participating                     |

## [Claim ID](https://www.resdac.org/cms-data/variables/Claim-ID)

- Short SAS Name: `CLM_ID`
- Long SAS Name: `CLM_ID`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Carrier    |          | `clm_id` | `clm_id` | `clm_id` | `clm_id` |
| Inpatient  | `clm_id` | `clm_id` | `clm_id` | `clm_id` | `clm_id` |
| Outpatient | `clm_id` | `clm_id` | `clm_id` | `clm_id` | `clm_id` |

| Dataset    | 2008     | 2007     | 2006     | 2005         | 2004         |
|:-----------|:---------|:---------|:---------|:-------------|:-------------|
| Carrier    | `clm_id` | `clm_id` | `clm_id` | `claimindex` | `claimindex` |
| Inpatient  | `clm_id` | `clm_id` | `clm_id` | `claimindex` | `claimindex` |
| Outpatient | `clm_id` | `clm_id` | `clm_id` | `claimindex` | `claimindex` |

| Dataset    | 2003         | 2002         | 2001         | 2000       | 1999       |
|:-----------|:-------------|:-------------|:-------------|:-----------|:-----------|
| Carrier    | `claimindex` | `claimindex` | `carrcntl`   | `carrcntl` | `bccn`     |
| Inpatient  | `claimindex` | `claimindex` | `link_num`   | `link_num` | `clm_cntl` |
| Outpatient | `claimindex` | `claimindex` | `claimindex` | `link_num` | `link_num` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The Unique CCW indentifier for a base claim. Simple encryption applied for extracts. Non-encrypted if pulled directly from CCW Oracle.

??? limitation
	When pulled directly from CCW, this is a numeric column.

## [Claim Inpatient Admission Type Code](https://www.resdac.org/cms-data/variables/Claim-Inpatient-Admission-Type-Code)

- Short SAS Name: `TYPE_ADM`
- Long SAS Name: `CLM_IP_ADMSN_TYPE_CD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `type_adm` | `type_adm` | `type_adm` | `type_adm` | `type_adm` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `type_adm` | `type_adm` | `type_adm` | `type_adm` | `type_adm` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `type_adm` | `type_adm` | `madmtype` | `madmtype` | `madmtype` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code indicating the type and priority of an inpatient admission associated with the service on an intermediary submitted claim.



<h3>Values</h3>

| Code     | Code Value                                                                                                                                                                                                                         |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0        | Blank                                                                                                                                                                                                                              |
| 1        | Emergency - The patient required immediate medical intervention as a result of severe, life threatening, or potentially disabling conditions. Generally, the patient was admitted through the emergency room.                      |
| 2        | Urgent - The patient required immediate attention for the care and treatment of a physical or mental disorder. Generally, the patient was admitted to the first available and suitable accommodation.                              |
| 3        | Elective - The patient's condition permitted adequate time to schedule the availability of suitable accommodations.                                                                                                                |
| 4        | Newborn - Necessitates the use of special source of admission codes.                                                                                                                                                               |
| 5        | Trauma Center - visits to a trauma center/hospital as licensed or designated by the State or local government authority authorized to do so, or as verified by the American College of Surgeons and involving a trauma activation. |
| 6 THRU 8 | Reserved                                                                                                                                                                                                                           |
| 9        | Unknown - Information not available.                                                                                                                                                                                               |

## [Claim Inpatient Low Volume Payment Amount](https://www.resdac.org/cms-data/variables/claim-inpatient-low-volume-payment-amount)

- Short SAS Name: `CLM_IP_LOW_VOL_PMT_AMT `
- Long SAS Name: `CLM_IP_LOW_VOL_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

 This is the amount field used to identify a payment adjustment given to hospitals to account for the higher costs per discharge for low income hospitals under the Inpatient Prospective Payment System (IPPS).

Payment adjustment for low income IPPS hospitals.   This field was new in 2011.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Line Number](https://www.resdac.org/cms-data/variables/Claim-Line-Number)

- Short SAS Name: `CLM_LN`
- Long SAS Name: `CLM_LINE_NUM`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Outpatient | `clm_ln` | `clm_ln` | `clm_ln` | `clm_ln` | `clm_ln` |

| Dataset    | 2008     | 2007     | 2006     | 2005        | 2004        |
|:-----------|:---------|:---------|:---------|:------------|:------------|
| Outpatient | `clm_ln` | `clm_ln` | `clm_ln` | `cntrindex` | `cntrindex` |

| Dataset    | 2003        | 2002        | 2001        |
|:-----------|:------------|:------------|:------------|
| Outpatient | `cntrindex` | `cntrindex` | `cntrindex` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The claim line number for detail revenue or part B line.



## [Claim MCO Paid Switch](https://www.resdac.org/cms-data/variables/Claim-MCO-Paid-Switch)

- Short SAS Name: `MCOPDSW`
- Long SAS Name: `CLM_MCO_PD_SW`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

A switch indicating whether or not a Managed Care Organization (MCO) has paid the provider for an institutional claim.

??? limitation
	DESCRIPTION :
	The MCO paid switch made consistent with criteria used to identify an inpatient encounter claim.
	
	BACKGROUND :
	During the NCH Version 'I' conversion, history was populated with an NCH Claim Type Code that will identify the record as an inpatient encounter claim.
	When applying the CWF logic to identify an inpatient encounter claim, it was discovered that when all the criteria was met the MCO paid switch was sometimes a blank or '0' (reflecting that the MCO did not pay the provider).
	
	CORRECTIVE ACTION :
	With the inception of the Version 'I' processing (7/00), if all the criteria for identifying an inpatient encounter claim is met but the MCO paid switch is a blank or '0' it is changed to a '1'. A patch code = '13' was applied to all claims back to 7/1/97 service year thru date.
	

<h3>Values</h3>

| Code       | Code Value                                |
|:-----------|:------------------------------------------|
| 1          | MCO has paid the provider for a claim     |
| BLANK or 0 | MCO has not paid the provider for a claim |

## [Claim Medical Record Number](https://www.resdac.org/cms-data/variables/Claim-Medical-Record-Number)

- Short SAS Name: `CLM_MDCL_REC`
- Long SAS Name: `CLM_MDCL_REC`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The number assigned by the provider to the beneficiary's medical record to assist in record retrieval.



## [Claim Medicare Non Payment Reason Code](https://www.resdac.org/cms-data/variables/claim-medicare-non-payment-reason-code)

- Short SAS Name: `NOPAY_CD`
- Long SAS Name: `CLM_MDCR_NON_PMT_RSN_CD`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `nopay_cd` | `nopay_cd` | `nopay_cd` | `nopay_cd` | `nopay_cd` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `nopay_cd` | `nopay_cd` | `nopay_cd` | `nopay_cd` | `nopay_cd` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `nopay_cd` | `nopay_cd` | `nopay_cd` | `nopay_cd` | `cancelcd` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The reason that no Medicare payment is made for services on an institutional claim.

NOTE1: This field was put on all institutional claim types but data did not start coming in on OP/HHA/Hospice until 4/1/02. Prior to 4/1/02, data only came in Inpatient/SNF claims.

NOTE2: Effective 4/1/02, this field was also expanded to two bytes to accommodate new values. The NCH Nearline file did not expand the current 1-byte field but instituted a crosswalk of the 2-byte field to the 1-byte character value. See table of code for the crosswalk.

NOTE3: Effective with Version 'J', the field has been expanded on the NCH claim to 2 bytes. With this expansion the NCH will no longer use the character values to represent the official two byte values being sent in by CWF since 4/2002.

During the Version 'J' conversion, all character values were converted to the two byte values.

NOTE4: These code values were not identified as part of the original CMS data documentation.  ResDAC has identified the values and has provided them for convenience.



<h3>Values</h3>

Valid Values effective 1/2011 (2-byte values are replacing the character values)

| Code   | Code Value                                                                                                                                                                        |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A      | Covered worker's compensation (Obsolete)                                                                                                                                          |
| B      | Benefit exhausted                                                                                                                                                                 |
| C      | Custodial care - noncovered care (includes all 'beneficiary at fault'waiver cases) (Obsolete)                                                                                     |
| E      | HMO out-of-plan services not emergency or urgently needed (Obsolete)                                                                                                              |
| E      | MSP cost avoided - IRS/SSA/HCFA Data Match (eff. 7/00)                                                                                                                            |
| F      | MSP cost avoid HMO Rate Cell (eff. 7/00)                                                                                                                                          |
| G      | MSP cost avoided Litigation Settlement (eff. 7/00)                                                                                                                                |
| H      | MSP cost avoided Employer Voluntary Reporting (eff. 7/00)                                                                                                                         |
| J      | MSP cost avoid Insurer Voluntary Reporting (eff. 7/00)                                                                                                                            |
| K      | MSP cost avoid Initial Enrollment Questionnaire (eff. 7/00)                                                                                                                       |
| N      | All other reasons for nonpayment                                                                                                                                                  |
| P      | Payment requested                                                                                                                                                                 |
| Q      | MSP cost avoided Voluntary Agreement (eff. 7/00)                                                                                                                                  |
| R      | Benefits refused, or evidence not submitted                                                                                                                                       |
| T      | MSP cost avoided - IEQ contractor (eff. 9/76) (obsolete 6/30/00)                                                                                                                  |
| U      | MSP cost avoided - HMO rate cell adjustment (eff. 9/76) (Obsolete 6/30/00)                                                                                                        |
| V      | MSP cost avoided - litigation settlement (eff. 9/76) (Obsolete 6/30/00)                                                                                                           |
| W      | Worker's compensation (Obsolete)                                                                                                                                                  |
| X      | MSP cost avoided - generic                                                                                                                                                        |
| Y      | MSP cost avoided - IRS/SSA data match project (obsolete 6/30/00)                                                                                                                  |
| Z      | Zero reimbursement RAPs -- zero reimbursement made due to medical review intervention or where provider specific zero payment has been determined. (effective with HHPPS - 10/00) |
| 00     | MSP cost avoided - COB Contractor                                                                                                                                                 |
| 12     | MSP cost avoided - BCBS Voluntary Agreements                                                                                                                                      |
| 13     | MSP cost avoided - Office of Personnel Management                                                                                                                                 |
| 14     | MSP cost avoided - Workman's Compensation (WC) Datamatch                                                                                                                          |
| 15     | MSP cost avoided - Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA) (eff. 4/2006)                                                                       |
| 16     | MSP cost avoided - Liability Insurer VDSA (eff. 4/2006)                                                                                                                           |
| 17     | MSP cost avoided - No-Fault Insurer VDSA (eff. 4/2006)                                                                                                                            |
| 18     | MSP cost avoided - Pharmacy Benefit Manager Data Sharing Agreement (eff. 4/2006)                                                                                                  |
| 19     | SEE NOTE4: Coordination of Benefits Contractor 11119 (see CMS Change Request 7906 for identification of the contractor.)                                                          |
| 21     | MSP cost avoided - MIR Group Heqalth Plan (eff. 1/2009)                                                                                                                           |
| 22     | MSP cost avoided - MIR non-Group Health Plan (eff. 1/2009)                                                                                                                        |
| 25     | MSP cost avoided - Recovery Audit Contractor - California (eff. 10/2005)                                                                                                          |
| 26     | MSP cost avoided - Recovery Audit Contractor - Florida (eff. 10/2005)                                                                                                             |
| 42     | SEE NOTE4: Coordination of Benefits Contractor 11142 (see CMS Change Request 7906 for identification of the contractor.)                                                          |
| 43     | SEE NOTE4: Coordination of Benefits Contractor 11143 (see CMS Change Request 7906 for identification of the contractor.)                                                          |

Effective 4/1/02, the Medicare nonpayment reason code was expanded to a 2-byte field.  The NCH instituted a crosswalk from the 2-byte code to a 1-byte character code. Below are the character codes (found in NCH & NMUD). At some point, NMUD will carry the 2-byte code but NCH will continue to have the 1-byte character code.

| Code   | Code Value                                                                                                                     |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------|
| !      | MSP cost avoided - COB Contractor ('00' 2-byte code)                                                                           |
| @      | MSP cost avoided - BC/BS Voluntary Agreements ('12' 2-byte code)                                                               |
| #      | MSP cost avoided - Office of Personnel Management ('13' 2-byte code)                                                           |
| $      | MSP cost avoided - Workman's Compensation (WC) Datamatch ('14' 2-byte code)                                                    |
| *      | MSP cost avoided - Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA) ('15' 2-byte code) (eff. 4/2006) |
| (      | MSP cost avoided - Liability Insurer VDSA ('16' 2-byte code) (eff. 4/2006)                                                     |
| )      | MSP cost avoided - No-Fault Insurer VDSA ('17' 2-byte code) (eff. 4/2006)                                                      |
| +      | MSP cost avoided - Pharmacy Benefit Manager Data Sharing Agreement ('18' 2-byte code) (eff. 4/2006)                            |
| <      | MSP cost avoided - MIR Group Health Plan ('21' 2-byte code) (eff. 1/2009)                                                      |
| >      | MSP cost avoided - MIR non-Group Health Plan ('22' 2-byte code) (eff. 1/2009)                                                  |
| %      | MSP cost avoided - Recovery Audit Contractor - California ('25' 2-byte code) (eff. 10/2005)                                    |
| &      | MSP cost avoided - Recovery Audit Contractor - Florida ('26' 2-byte code) (eff. 10/2005)                                       |

## [Claim Model 4 Readmission Indicator Code](https://www.resdac.org/cms-data/variables/claim-model-4-readmission-indicator-code)

- Short SAS Name: `CLM_MODEL_4_READMSN_IND_CD `
- Long SAS Name: `CLM_MODEL_4_READMSN_IND_CD`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field identifies the method of payment of a claim billed within 30 days of a Model 4 Bundled Payments for Care Improvement (BPCI) admission.

Bundling payment for services that patients receive across a single episode of care, such as heart bypass surgery or a hip replacement, is one way to encourage doctors, hospitals and other health care providers to work together to better coordinate care for patients. Under the Model 4 BPCI pilot, CMS will reimburse qualified acute care hospitals a blended payment for hospital inpatient care and physician services connected with a single episode of care. This will occur in association with inpatient hospital claims that the BPCI participating hospital will bill to their jurisdictional A/B MAC as type of bill 11X claims.



<h3>Values</h3>

| Code         | Code Value                                                                                                                             |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| 1            | claim is related readmission to a Model 4 BPCI claim and shall pay IME, DSH, and Capital Only.                                         |
| 2            | two Model 4 BPCI claims within 30 days of each other, first claim in episode shall process as it would in the absence of Model 4 BPCI. |
| 3            | two Model 4 BPCI claims within 30 days of each other, this is the second claim in the episode and paid as Model 4.                     |
| Null/missing | not a BPCI claim                                                                                                                       |

## [Claim Next Generation (NG) Accountable Care Organization (ACO) Indicator Code - 3 day SNF waiver](https://www.resdac.org/cms-data/variables/claim-next-generation-ng-accountable-care-organization-aco-indicator-code-3-day)

- Short SAS Name: `CLM_NEXT_GNRTN_ACO_IND_4_CD`
- Long SAS Name: `CLM_NEXT_GNRTN_ACO_IND_CD4`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the claims that qualify for specific claims processing edits related to benefit enhancement through the Next Generation (NG) Accountable Care Organization (ACO).

There are 5 of these ACO fields (CLM_NEXT_GNRTN_ACO_IND_CD1 -CLM_NEXT_GNRTN_ACO_IND_CD5).



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | Base record (no enhancements)     |
| 1      | Population Based Payments (PBP)   |
| 2      | Telehealth                        |
| 3      | Post Discharge Home Health Visits |
| 4      | 3-Day SNF Waiver                  |
| 5      | Capitation                        |

## [Claim Next Generation (NG) Accountable Care Organization (ACO) Indicator Code - Capitation](https://www.resdac.org/cms-data/variables/claim-next-generation-ng-accountable-care-organization-aco-indicator-code-1)

- Short SAS Name: `CLM_NEXT_GNRTN_ACO_IND_5_CD`
- Long SAS Name: `CLM_NEXT_GNRTN_ACO_IND_CD5`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the claims that qualify for specific claims processing edits related to benefit enhancement through the Next Generation (NG) Accountable Care Organization (ACO).

There are 5 of these ACO fields (CLM_NEXT_GNRTN_ACO_IND_CD1 -CLM_NEXT_GNRTN_ACO_IND_CD5).



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | Base record (no enhancements)     |
| 1      | Population Based Payments (PBP)   |
| 2      | Telehealth                        |
| 3      | Post Discharge Home Health Visits |
| 4      | 3-Day SNF Waiver                  |
| 5      | Capitation                        |

## [Claim Next Generation (NG) Accountable Care Organization (ACO) Indicator Code - Population based payments (PBP)](https://www.resdac.org/cms-data/variables/claim-next-generation-ng-accountable-care-organization-aco-indicator-code)

- Short SAS Name: `CLM_NEXT_GNRTN_ACO_IND_1_CD`
- Long SAS Name: `CLM_NEXT_GNRTN_ACO_IND_CD1`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the claims that qualify for specific claims processing edits related to benefit enhancement through the Next Generation (NG) Accountable Care Organization (ACO).

There are 5 of these ACO fields (CLM_NEXT_GNRTN_ACO_IND_CD1 -CLM_NEXT_GNRTN_ACO_IND_CD5).



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | Base record (no enhancements)     |
| 1      | Population Based Payments (PBP)   |
| 2      | Telehealth                        |
| 3      | Post Discharge Home Health Visits |
| 4      | 3-Day SNF Waiver                  |
| 5      | Capitation                        |

## [Claim Next Generation (NG) Accountable Care Organization (ACO) Indicator Code - Post Discharge HH visits](https://www.resdac.org/cms-data/variables/claim-next-generation-ng-accountable-care-organization-aco-indicator-code-post)

- Short SAS Name: `CLM_NEXT_GNRTN_ACO_IND_3_CD`
- Long SAS Name: `CLM_NEXT_GNRTN_ACO_IND_CD3`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the claims that qualify for specific claims processing edits related to benefit enhancement through the Next Generation (NG) Accountable Care Organization (ACO).

There are 5 of these ACO fields (CLM_NEXT_GNRTN_ACO_IND_CD1 -CLM_NEXT_GNRTN_ACO_IND_CD5).



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | Base record (no enhancements)     |
| 1      | Population Based Payments (PBP)   |
| 2      | Telehealth                        |
| 3      | Post Discharge Home Health Visits |
| 4      | 3-Day SNF Waiver                  |
| 5      | Capitation                        |

## [Claim Next Generation (NG) Accountable Care Organization (ACO) Indicator Code - Telehealth](https://www.resdac.org/cms-data/variables/claim-next-generation-ng-accountable-care-organization-aco-indicator-code-0)

- Short SAS Name: `CLM_NEXT_GNRTN_ACO_IND_2_CD`
- Long SAS Name: `CLM_NEXT_GNRTN_ACO_IND_CD2`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field identifies the claims that qualify for specific claims processing edits related to benefit enhancement through the Next Generation (NG) Accountable Care Organization (ACO).

There are 5 of these ACO fields (CLM_NEXT_GNRTN_ACO_IND_CD1 -CLM_NEXT_GNRTN_ACO_IND_CD5).



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | Base record (no enhancements)     |
| 1      | Population Based Payments (PBP)   |
| 2      | Telehealth                        |
| 3      | Post Discharge Home Health Visits |
| 4      | 3-Day SNF Waiver                  |
| 5      | Capitation                        |

## [Claim Non Utilization Days Count](https://www.resdac.org/cms-data/variables/Claim-Non-Utilization-Days-Count)

- Short SAS Name: `NUTILDAY`
- Long SAS Name: `CLM_NON_UTLZTN_DAYS_CNT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the number of days of care that are not chargeable to Medicare facility utilization.



## [Claim Occurrence Span Code](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Code)

- Short SAS Name: `SPAN_CD`
- Long SAS Name: `CLM_SPAN_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code that identifies a significant event relating to an institutional claim that may affect payer processing. These codes are claim-related occurrences that are related to a time period (span of dates).



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                        |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 70     | Eff 10/93, payer use only, the nonutilization from/thru dates for PPS-inlier stay where bene had exhausted all full/coinsurance days, but covered on cost report. SNF qualifying hospital stay from/thru dates                                                                    |
| 71     | Hospital prior stay dates - the from/thru dates of any hospital stay that ended within 60 days of this hospital or SNF admission.                                                                                                                                                 |
| 72     | First/last visit - the dates of the first and last visits occurring in this billing period if the dates are different from those in the statement covers period.                                                                                                                  |
| 73     | Benefit eligibility period - the inclusive dates during which CHAMPUS medical benefits are available to a sponsor's bene as shown on the bene's ID card.                                                                                                                          |
| 74     | Non-covered level of care - the from/thru dates of a period at a noncovered level of care in an otherwise covered stay, excluding any period reported with occurrence span code 76, 77, or 79.                                                                                    |
| 75     | The from/thru dates of SNF level of care during IP hospital stay. Shows PRO approval of patient remaining in hospital because SNF bed not available. Not applicable to swing bed cases. PPS hospitals use in day outlier cases only.                                              |
| 76     | Patient liability - From/thru dates of period of noncovered care for which hospital may charge bene. The FI or PRO must have approved such charges in advance. Patient must be notified in writing 3 days prior to noncovered period                                              |
| 77     | Provider liability (utilization charged) - The from/thru dates of period of noncovered care for which the provider is liable. Eff 3/92, applies to provider liability where bene is charged with utilization and is liable for deductible/coinsurance                             |
| 78     | SNF prior stay dates - The from/thru dates of any SNF stay that ended within 60 days of this hospital or SNF admission.                                                                                                                                                           |
| 79     | Provider Liability (non-utilization) (Payer code) - Eff 3/92, from/thru dates of period of non-covered care where bene is not charged with utilization, deductible, or coinsurance and provider is liable. Eff 9/93, non-covered period of care due to lack of medical necessity. |
| 80     | Prior Same-SNF Stay Dates for Payment Ban Purposes - the from/thru dates of a prior same-SNF stay indicating a patient resided in the SNF prior to, and if applicable, during a payment ban period up until their discharge to a hospital.                                        |
| 81-99  | Reserved for state assignment                                                                                                                                                                                                                                                     |
| M0     | QIO/UR approved stay dates - Eff 10/93, the first and last days that were approved where not all of the stay was approved.                                                                                                                                                        |
| M1     | Provider Liability-No Utilization - from/thru dates of a period of non-covered care that is denied due to lack of medical necessity or custodial care for which the provider is liable. (eff. 10/01)                                                                              |
| M2     | Dates of Inpatient Respite Care - from/thru dates of a period of inpatient respite care for hospice patients. (eff. 10/00)                                                                                                                                                        |
| M3     | ICF Level of Care - the from/thru dates of a period of intermediate level of care during an inpatient hospital stay.                                                                                                                                                              |
| M4     | Residential Level of Care - the from/thru dates of a period of residential level of care during an inpatient hospital stay.                                                                                                                                                       |

## [Claim Occurrence Span From Date](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Date)

- Short SAS Name: `SPANFROM`
- Long SAS Name: `CLM_SPAN_FROM_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The from date of a period associated with an occurrence of a specific event relating to an institutional claim that may affect payer processing.



## [Claim Occurrence Span Through Date](https://www.resdac.org/cms-data/variables/Claim-Occurrence-Span-Through-Date)

- Short SAS Name: `SPANTHRU`
- Long SAS Name: `CLM_SPAN_THRU_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The thru date of a period associated with an occurrence of a specific event relating to an institutional claim that may affect payer processing.



## [Claim Operating Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Operating-Physician-NPI-Number)

- Short SAS Name: `OP_NPI`
- Long SAS Name: `OP_PHYSN_NPI`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |
| Outpatient | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |

| Dataset    | 2008     | 2007     | 2006     | 2005     | 2004     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |
| Outpatient | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |

| Dataset    | 2003     | 2002     | 2001     | 2000     | 1999     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |
| Outpatient | `op_npi` | `op_npi` | `op_npi` | `op_npi` | `op_npi` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

On an institutional claim, the National Provider Identifier (NPI) number assigned to uniquely identify the physician with the primary responsibility for performing the surgical procedure(s).

NOTE: Effective May 2007, the NPI will become the national standard identifier for covered health care providers. NPIs will replace the current OSCAR provider number, UPINs, NSC numbers, and local contractor provider identi- fication numbers (PINs) on standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number (UPIN, PIN, OSCAR provider number, etc.)).

NOTE1: CMS has determined that dual provider identifiers (old legacy number and new NPI) must be available in the NCH. After the 5/07 NPI implementation, the standard system maint- tainers will add the legacy number to the claim when its adjudicated. We will continue to re- ceive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no NEW UPINs (legacy numbers) will be generated for NEW physicians (Part B and outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.



## [Claim Operating Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-operating-physician-specialty-code)

- Short SAS Name: `OP_PHYSN_SPCLTY_CD`
- Long SAS Name: `OP_PHYSN_SPCLTY_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the CMS specialty code corresponding to the operating physician. The Affordable Care Act (ACA) provides for incentive payments for physicians and non-physician practitioners with specific primary specialty designations. In order to determine if the physician or non-physicians is eligible for the incentive payment, the specialty code, NPI and name must be carried on the claims. 



<h3>Values</h3>

| Code   | Code Value                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00     | Carrier wide                                                                                                                                            |
| 01     | General practice                                                                                                                                        |
| 02     | General surgery                                                                                                                                         |
| 03     | Allergy/immunology                                                                                                                                      |
| 04     | Otolaryngology                                                                                                                                          |
| 05     | Anesthesiology                                                                                                                                          |
| 06     | Cardiology                                                                                                                                              |
| 07     | Dermatology                                                                                                                                             |
| 08     | Family practice                                                                                                                                         |
| 09     | Interventional Pain Management (IPM) (eff. 4/1/03)                                                                                                      |
| 10     | Gastroenterology                                                                                                                                        |
| 11     | Internal medicine                                                                                                                                       |
| 12     | Osteopathic manipulative therapy                                                                                                                        |
| 13     | Neurology                                                                                                                                               |
| 14     | Neurosurgery                                                                                                                                            |
| 15     | Speech/language pathology                                                                                                                               |
| 16     | Obstetrics/gynecology                                                                                                                                   |
| 17     | Hospice and Palliative Care                                                                                                                             |
| 18     | Ophthalmology                                                                                                                                           |
| 19     | Oral surgery (dentists only)                                                                                                                            |
| 20     | Orthopedic surgery                                                                                                                                      |
| 21     | Cardiac Electrophysiology                                                                                                                               |
| 22     | Pathology                                                                                                                                               |
| 24     | Plastic and reconstructive surgery                                                                                                                      |
| 25     | Physical medicine and rehabilitation                                                                                                                    |
| 26     | Psychiatry                                                                                                                                              |
| 27     | General Psychiatry                                                                                                                                      |
| 28     | Colorectal surgery (formerly proctology)                                                                                                                |
| 29     | Pulmonary disease                                                                                                                                       |
| 30     | Diagnostic radiology                                                                                                                                    |
| 31     | Intensive cardiac rehabilitation                                                                                                                        |
| 32     | Anesthesiologist Assistants (eff. 4/1/03--previously grouped with Certified Registered Nurse Anesthetists (CRNA))                                       |
| 33     | Thoracic surgery                                                                                                                                        |
| 34     | Urology                                                                                                                                                 |
| 35     | Chiropractic                                                                                                                                            |
| 36     | Nuclear medicine                                                                                                                                        |
| 37     | Pediatric medicine                                                                                                                                      |
| 38     | Geriatric medicine                                                                                                                                      |
| 39     | Nephrology                                                                                                                                              |
| 40     | Hand surgery                                                                                                                                            |
| 41     | Optometrist                                                                                                                                             |
| 42     | Certified nurse midwife                                                                                                                                 |
| 43     | Certified Registered Nurse Anesthetist (CRNA) (Anesthesiologist Assistants were removed from this specialty 4/1/03)                                     |
| 44     | Infectious disease                                                                                                                                      |
| 45     | Mammography screening center                                                                                                                            |
| 46     | Endocrinology                                                                                                                                           |
| 47     | Independent Diagnostic Testing Facility (IDTF)                                                                                                          |
| 48     | Podiatry                                                                                                                                                |
| 49     | Ambulatory surgical center (formerly miscellaneous)                                                                                                     |
| 50     | Nurse practitioner                                                                                                                                      |
| 51     | Medical supply company with certified orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                            |
| 52     | Medical supply company with certified prosthetist (certified by American Board for Certification in Prosthetics and Orthotics)                          |
| 53     | Medical supply company with certified prosthetics-orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                |
| 54     | Medical supply company for DMERC (and not included in 51-53)                                                                                            |
| 55     | Individual certified orthoptist                                                                                                                         |
| 56     | Individual certified prosthetist                                                                                                                        |
| 57     | Individual certified prosthetist-orthotist                                                                                                              |
| 58     | Medical supply company with registered pharmacist                                                                                                       |
| 59     | Ambulance service supplier, (e.g., private ambulance companies, funeral homes, etc.)                                                                    |
| 60     | Public health or welfare agencies (federal, state, and local)                                                                                           |
| 61     | Voluntary health or charitable agencies (e.g. National Cancer Society, National Heart Association, Catholic Charities)                                  |
| 62     | Psychologist (billing independently)                                                                                                                    |
| 63     | Portable X-ray supplier                                                                                                                                 |
| 64     | Audiologist (billing independently)                                                                                                                     |
| 65     | Physical therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                            |
| 66     | Rheumatology                                                                                                                                            |
| 67     | Occupational therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                        |
| 68     | Clinical laboratory (billing independently)                                                                                                             |
| 69     | Clinical laboratory (billing independently)                                                                                                             |
| 70     | Multispecialty clinic or group practice                                                                                                                 |
| 71     | Registered Dietician/Nutrition Professional (eff. 1/1/02)                                                                                               |
| 72     | Pain Management (eff. 1/1/02)                                                                                                                           |
| 73     | Mass Immunization Roster Biller                                                                                                                         |
| 74     | Radiation Therapy Centers (prior to 4/2003 this included independent Diagnostic Testing Facilities (IDTF))                                              |
| 75     | Slide Preparation Facilities (added to differentiate them from Independent Diagnostic Testing Facilities (IDTFs--eff. 4/1/03))                          |
| 76     | Peripheral vascular disease                                                                                                                             |
| 77     | Vascular surgery                                                                                                                                        |
| 78     | Cardiac surgery                                                                                                                                         |
| 79     | Addiction medicine                                                                                                                                      |
| 80     | Licensed clinical social worker                                                                                                                         |
| 81     | Critical care (intensivists)                                                                                                                            |
| 82     | Hematology                                                                                                                                              |
| 83     | Hematology/oncology                                                                                                                                     |
| 84     | Preventive medicine                                                                                                                                     |
| 85     | Maxillofacial surgery                                                                                                                                   |
| 86     | Neuropsychiatry                                                                                                                                         |
| 87     | All other suppliers (e.g. drug and department stores)                                                                                                   |
| 88     | Unknown supplier/provider specialty                                                                                                                     |
| 89     | Certified clinical nurse specialist                                                                                                                     |
| 90     | Medical oncology                                                                                                                                        |
| 91     | Surgical oncology                                                                                                                                       |
| 92     | Radiation oncology                                                                                                                                      |
| 93     | Emergency medicine                                                                                                                                      |
| 94     | Interventional radiology                                                                                                                                |
| 95     | Competitive Acquisition Program (CAP) Vendor (eff. 07/01/06). Prior to 07/10/06, known as Independent physiological laboratory                          |
| 96     | Optician                                                                                                                                                |
| 97     | Physician assistant                                                                                                                                     |
| 98     | Gynecologist/oncologist                                                                                                                                 |
| 99     | Unknown physician specialty                                                                                                                             |
| A0     | Hospital (DMERCs only)                                                                                                                                  |
| A1     | SNF (DMERCs only)                                                                                                                                       |
| A2     | Intermediate care nursing facility (DMERCs only)                                                                                                        |
| A3     | Nursing facility, other (DMERCs only)                                                                                                                   |
| A4     | Home Health Agency (DMERCs only)                                                                                                                        |
| A5     | Pharmacy (DMERC)                                                                                                                                        |
| A6     | Medical supply company with respiratory therapist (DMERCs only)                                                                                         |
| A7     | Department store (DMERC)                                                                                                                                |
| A8     | Grocery store (DMERC)                                                                                                                                   |
| A9     | Indian Health Service (IHS), tribe and tribal organizations (non-hospital or non-hospital based facilities, eff. 1/2005)                                |
| B1     | Supplier of oxygen and/or oxygen related equipment (eff. 10/2/07)                                                                                       |
| B2     | Pedorthic Personnel (eff. 10/2/07)                                                                                                                      |
| B3     | Medical Supply Company with pedorthic personnel (eff. 10/2/07)                                                                                          |
| B4     | Does not meet definition of health care provider (e.g., Rehabilitation agency, organ procurement organizations, histocompatibility labs) (eff. 10/2/07) |
| B5     | Ocularist                                                                                                                                               |
| C0     | Sleep medicine                                                                                                                                          |
| C1     | Centralized flu                                                                                                                                         |
| C2     | Indirect payment procedure                                                                                                                              |
| C3     | Interventional cardiology                                                                                                                               |
| C5     | Dentist (eff. 7/2016)                                                                                                                                   |

## [Claim Operating Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Operating-Physician-UPIN-Number)

- Short SAS Name: `OP_UPIN`
- Long SAS Name: `OP_PHYSN_UPIN`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |
| Outpatient | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |
| Outpatient | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |
| Outpatient | `op_upin` | `op_upin` | `op_upin` | `op_upin` | `op_upin` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the unique physician identification number (UPIN) of the physician who performed the principal procedure. This element is used by the provider to identify the operating physician who performed the surgi- cal procedure.



## [Claim Other Physician NPI Number](https://www.resdac.org/cms-data/variables/Claim-Other-Physician-NPI-Number)

- Short SAS Name: `OT_NPI`
- Long SAS Name: `OT_PHYSN_NPI`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |
| Outpatient | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |

| Dataset    | 2008     | 2007     | 2006     | 2005     | 2004     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |
| Outpatient | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |

| Dataset    | 2003     | 2002     | 2001     | 2000     | 1999     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Inpatient  | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |
| Outpatient | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` | `ot_npi` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

On an institutional claim, the National Provider Identifier (NPI) number assigned to uniquely identify the other physician associated with the institutiohal claim.

NOTE: Effective May 2007, the NPI will be- come the national standard identifier for covered health care providers. NPIs will replace current OSCAR provider number, UPINs, NSC numbers, and local contractor provider identification numbers (PINs) on standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number (UPIN, PIN, OSCAR provider number, etc.)).

NOTE1: CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available in the NCH. After the 5/07 NPI implementation, the standard system main- tainers will add the legacy number to the claim when it is adjudicated. We will continue to receive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no NEW UPINs (legacy number) will be generated for NEW physicians (Part B AND outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.



## [Claim Other Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-other-physician-specialty-code)

- Short SAS Name: `OT_PHYSN_SPCLTY_CD`
- Long SAS Name: `OT_PHYSN_SPCLTY_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the CMS specialty code corresponding to the other physician. 

The Affordable Care Act (ACA) provides for incentive payments for physicians and non-physician practitioners with specific primary specialty designations. In order to determine if the physician or non-physician is eligible for the incentive payment, the specialty code, NPI and name must be carried on the claims.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00     | Carrier wide                                                                                                                                            |
| 01     | General practice                                                                                                                                        |
| 02     | General surgery                                                                                                                                         |
| 03     | Allergy/immunology                                                                                                                                      |
| 04     | Otolaryngology                                                                                                                                          |
| 05     | Anesthesiology                                                                                                                                          |
| 06     | Cardiology                                                                                                                                              |
| 07     | Dermatology                                                                                                                                             |
| 08     | Family Practice                                                                                                                                         |
| 09     | Interventional Pain Management (IPM) (eff. 4/1/03)                                                                                                      |
| 10     | Gastroenterology                                                                                                                                        |
| 11     | Internal medicine                                                                                                                                       |
| 12     | Osteopathic manipulative therapy                                                                                                                        |
| 13     | Neurology                                                                                                                                               |
| 14     | Neurosurgery                                                                                                                                            |
| 15     | Speech/language pathology                                                                                                                               |
| 16     | Obstetrics/gynecology                                                                                                                                   |
| 17     | Hospice and Palliative Care                                                                                                                             |
| 18     | Ophthalmology                                                                                                                                           |
| 19     | Oral surgery (dentists only)                                                                                                                            |
| 20     | Orthopedic surgery                                                                                                                                      |
| 21     | Cardiac Electrophysiology                                                                                                                               |
| 22     | Pathology                                                                                                                                               |
| 24     | Plastic and reconstructive surgery                                                                                                                      |
| 25     | Physical medicine and rehabilitation                                                                                                                    |
| 26     | Psychiatry                                                                                                                                              |
| 27     | General Psychiatry                                                                                                                                      |
| 28     | Colorectal surgery (formerly proctology)                                                                                                                |
| 29     | Pulmonary disease                                                                                                                                       |
| 30     | Diagnostic radiology                                                                                                                                    |
| 31     | Intensive cardiac rehabilitation                                                                                                                        |
| 32     | Anesthesiologist Assistants (eff. 4/1/03--previously grouped with Certified Registered Nurse Anesthetists (CRNA))                                       |
| 33     | Thoracic surgery                                                                                                                                        |
| 34     | Urology                                                                                                                                                 |
| 35     | Chiropractic                                                                                                                                            |
| 36     | Nuclear medicine                                                                                                                                        |
| 37     | Pediatric medicine                                                                                                                                      |
| 38     | Geriatric medicine                                                                                                                                      |
| 39     | Nephrology                                                                                                                                              |
| 40     | Hand surgery                                                                                                                                            |
| 41     | Optometrist                                                                                                                                             |
| 42     | Certified nurse midwife                                                                                                                                 |
| 43     | Certified Registered Nurse Anesthetist (CRNA) (Anesthesiologist Assistants were removed from this specialty 4/1/03)                                     |
| 44     | Infectious disease                                                                                                                                      |
| 45     | Mammography screening center                                                                                                                            |
| 46     | Endocrinology                                                                                                                                           |
| 47     | Independent Diagnostic Testing Facility (IDTF)                                                                                                          |
| 48     | Podiatry                                                                                                                                                |
| 49     | Ambulatory surgical center (formerly miscellaneous)                                                                                                     |
| 50     | Nurse practitioner                                                                                                                                      |
| 51     | Medical supply company with certified orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                            |
| 52     | Medical supply company with certified prosthetist (certified by American Board for Certification in Prosthetics and Orthotics)                          |
| 53     | Medical supply company with certified prosthetist-orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                |
| 54     | Medical supply company for DMERC (and not included in 51-53)                                                                                            |
| 55     | Individual certified orthotist                                                                                                                          |
| 56     | Individual certified prosthetist                                                                                                                        |
| 57     | Individual certified prosthetist-orthotist                                                                                                              |
| 58     | Medical supply company with registered pharmacist                                                                                                       |
| 59     | Ambulance service supplier, (e.g., private ambulance companies, funeral homes, etc.)                                                                    |
| 60     | Public health or welfare agencies (federal, state, and local)                                                                                           |
| 61     | Voluntary health or charitable agencies (e.g. National Cancer Society, National Heart Association, Catholic Charities)                                  |
| 62     | Psychologist (billing independently)                                                                                                                    |
| 63     | Portable X-ray supplier                                                                                                                                 |
| 64     | Audiologist (billing independently)                                                                                                                     |
| 65     | Physical therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                            |
| 66     | Rheumatology                                                                                                                                            |
| 67     | Occupational therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                        |
| 68     | Clinical psychologist                                                                                                                                   |
| 69     | Clinical laboratory (billing independently)                                                                                                             |
| 70     | Multispecialty clinic or group practice                                                                                                                 |
| 71     | Registered Dietician/Nutrition Professional (eff. 1/1/02)                                                                                               |
| 72     | Pain Management (eff. 1/1/02)                                                                                                                           |
| 73     | Mass Immunization Roster Biller                                                                                                                         |
| 74     | Radiation Therapy Centers (prior to 4/2003 this included Independent Diagnostic Testing Facilities (IDTF))                                              |
| 75     | Slide Preparation Facilities (added to differentiate them from Independent Diagnostic Testing Facilities (IDTFs -- eff. 4/1/03))                        |
| 76     | Peripheral vascular disease                                                                                                                             |
| 77     | Vascular surgery                                                                                                                                        |
| 78     | Cardiac surgery                                                                                                                                         |
| 79     | Addiction medicine                                                                                                                                      |
| 80     | Licensed clinical social worker                                                                                                                         |
| 81     | Critical care (intensivists)                                                                                                                            |
| 82     | Hematology                                                                                                                                              |
| 83     | Hematology/oncology                                                                                                                                     |
| 84     | Preventive medicine                                                                                                                                     |
| 85     | Maxillofacial surgery                                                                                                                                   |
| 86     | Neuropsychiatry                                                                                                                                         |
| 87     | All other suppliers (e.g. drug and department stores)                                                                                                   |
| 88     | Unknown supplier/provider specialty                                                                                                                     |
| 89     | Certified clinical nurse specialist                                                                                                                     |
| 90     | Medical oncology                                                                                                                                        |
| 91     | Surgical oncology                                                                                                                                       |
| 92     | Radiation oncology                                                                                                                                      |
| 93     | Emergency medicine                                                                                                                                      |
| 94     | Interventional radiology                                                                                                                                |
| 95     | Competitive Acquisition Program (CAP) Vendor (eff. 07/01/06). Prior to 07/01/06, known as Independent physiological laboratory                          |
| 96     | Optician                                                                                                                                                |
| 97     | Physician assistnat                                                                                                                                     |
| 98     | Gynecologist/oncologist                                                                                                                                 |
| 99     | Unknown physician specialty                                                                                                                             |
| A0     | Hospital (DMERCs only)                                                                                                                                  |
| A1     | SNF (DMERCs only)                                                                                                                                       |
| A2     | Intermediate care nursing facility (DMERCs only)                                                                                                        |
| A3     | Nursing facility, other (DMERCs only)                                                                                                                   |
| A5     | Pharmacy (DMERC)                                                                                                                                        |
| A6     | Medical supply company with respiratory therapist (DMERCs only)                                                                                         |
| A7     | Department store (DMERC)                                                                                                                                |
| A8     | Grocery store (DMERC)                                                                                                                                   |
| A9     | Indian Health Service (IHS), tribe and tribal organizations (non-hospital or non-hospital based facilities, eff. 1/2005)                                |
| B1     | Supplier of oxygen and/or oxygen related equipment (eff. 10/2/07)                                                                                       |
| B2     | Pedorthic Personnel (eff. 10/2/07)                                                                                                                      |
| B3     | Medical Supply Company with pedorthic personnel (eff. 10/2/07)                                                                                          |
| B4     | Does not meet definition of health care provider (e.g., Rehabilitation agency, organ procurement organizations, histocompatibility labs) (eff. 10/2/07) |
| B5     | Ocularist                                                                                                                                               |
| C0     | Sleep medicine                                                                                                                                          |
| C1     | Centralized flu                                                                                                                                         |
| C2     | Indirect payment procedure                                                                                                                              |
| C3     | Interventional cardiology                                                                                                                               |
| C5     | Dentist (eff. 7/2016)                                                                                                                                   |

## [Claim Other Physician UPIN Number](https://www.resdac.org/cms-data/variables/Claim-Other-Physician-UPIN-Number)

- Short SAS Name: `OT_UPIN`
- Long SAS Name: `OT_PHYSN_UPIN`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |
| Outpatient | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |
| Outpatient | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |
| Outpatient | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` | `ot_upin` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the unique physician identification number (UPIN) of the other physician associated with the institutional claim.



## [Claim PPS Capital DRG Weight Number](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-DRG-Weight-Number)

- Short SAS Name: `DRGWTAMT`
- Long SAS Name: `CLM_PPS_CPTL_DRG_WT_NUM`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the number used to determine a transfer adjusted case mix index for capital PPS. The number is determined by multiplying the DRG weight times the discharge fraction.

??? limitation
	DESCRIPTION :
	Field erroneously blanked out on segments 2-10.
	BACKGROUND :
	During the Version 'I' conversion of all service years
	(1991-6/30/00) the following field was erroneously
	blanked out on segments 2-10.During the Version 'I' planning process, it was decided
	that all codes, dates, numbers, names and percent fields
	would be populated on all segments of a claim; but
	amount, counts, and quantities would be zeroed out on
	segments 2-10 to eliminate the risk of overstating values.
	CORRECTIVE ACTION :
	This data can not be recovered.
	

## [Claim PPS Capital Disproportionate Share Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Disproportionate-Share-Amount)

- Short SAS Name: `DISP_SHR`
- Long SAS Name: `CLM_PPS_CPTL_DSPRPRTNT_SHR_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `disp_shr` | `disp_shr` | `disp_shr` | `disp_shr` | `disp_shr` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `disp_shr` | `disp_shr` | `disp_shr` | `disp_shr` | `disp_shr` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `disp_shr` | `disp_shr` | `mdprpamt` | `mdprpamt` | `mdprpamt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the amount of disproportionate share (rate reflecting indigent population served) portion of the PPS payment for capital.



## [Claim PPS Capital Exception Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Exception-Amount)

- Short SAS Name: `CPTL_EXP`
- Long SAS Name: `CLM_PPS_CPTL_EXCPTN_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the capital PPS amount of exception payments provided for hospitals with inordinately high levels of capital obligations. Exception payments expire at the end of the 10-year transition period.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim PPS Capital FSP Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-FSP-Amount)

- Short SAS Name: `CPTL_FSP`
- Long SAS Name: `CLM_PPS_CPTL_FSP_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the amount of the federal specific portion of the PPS payment for capital.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim PPS Capital IME Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-IME-Amount)

- Short SAS Name: `IME_AMT`
- Long SAS Name: `CLM_PPS_CPTL_IME_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `ime_amt` | `ime_amt` | `ime_amt` | `ime_amt` | `ime_amt` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `ime_amt` | `ime_amt` | `ime_amt` | `ime_amt` | `ime_amt` |

| Dataset   | 2003      | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `ime_amt` | `ime_amt` | `mtotime` | `mtotime` | `mtotime` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the amount of the indirect medical education (IME) (reimbursable amount for teaching hospitals only; an added amount passed by Congress to augment normal PPS payments for teaching hospitals to compensate them for higher patient costs resulting from medical education programs for interns and residents) portion of the PPS payment for capital.



## [Claim PPS Capital Outlier Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Capital-Outlier-Amount)

- Short SAS Name: `CPTLOUTL`
- Long SAS Name: `CLM_PPS_CPTL_OUTLIER_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, the amount of the outlier portion of the PPS payment for capital.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim PPS Indicator Code](https://www.resdac.org/cms-data/variables/Claim-PPS-Indicator-Code)

- Short SAS Name: `PPS_IND`
- Long SAS Name: `CLM_PPS_IND_CD`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `pps_ind` | `pps_ind` | `pps_ind` | `pps_ind` | `pps_ind` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `pps_ind` | `pps_ind` | `pps_ind` | `pps_ind` | `pps_ind` |

| Dataset   | 2003      | 2002      | 2001   | 2000   | 1999   |
|:----------|:----------|:----------|:-------|:-------|:-------|
| MedPAR    | `pps_ind` | `pps_ind` | `mpps` | `mpps` | `mpps` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version H, the code indicating whether or not the (1) claim is PPS and/or (2) the beneficiary is a deemed insured Medicare Qualified Government Employee (MQGE).

NOTE: Beginning with NCH weekly process date 10/3/97 through 5/29/98, this field was pop- ulated with only the PPS indicator. Beginning with NCH weekly process date 6/5/98, this field was additionally populated with the deemed MQGE indicator. Claims processed prior to 10/3/97 will contain spaces.



<h3>Values</h3>

Effective NCH weekly process date 10/3/97 - 5/29/98

| Code   | Code Value                                     |
|:-------|:-----------------------------------------------|
| 0      | not PPS bill (claim contains no PPS indicator) |
| 2      | PPS bill ( claim contains PPS indicator)       |

Effective NCH weekly process date 6/5/98

| Code   | Code Value                                                                               |
|:-------|:-----------------------------------------------------------------------------------------|
| 0      | not applicable (claim contains neither PPS nor deemed insured MQGE status indicators)    |
| 1      | Deemed insured MQGE (claim contains deemed insured MQGE indicator but not PPS indicator) |
| 2      | PPS bill ( claim contains PPS indicator but no deemed insured MQGE status indicator)     |
| 3      | Both PPS and deemed insured MQGE (contains both PPS and deemed insured MQGE indicators)  |

## [Claim PPS Old Capital Hold Harmless Amount](https://www.resdac.org/cms-data/variables/Claim-PPS-Old-Capital-Hold-Harmless-Amount)

- Short SAS Name: `HLDHRMLS`
- Long SAS Name: `CLM_PPS_OLD_CPTL_HLD_HRMLS_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective 3/2/92, this amount is the hold harmless amount payable for old capital as computed by PRICER for providers with a payment code equal to 'A'. The hold harmless amount-old capital is 100 percent of the reasonable costs of old capital for sole community sole community hospitals, or 85 percent of the reasonable costs associated with old capital for all other hospitals, plus a payment for new capital.



## [Claim Pass Thru Per Diem Amount](https://www.resdac.org/cms-data/variables/Claim-Pass-Thru-Diem-Amount)

- Short SAS Name: `PER_DIEM`
- Long SAS Name: `CLM_PASS_THRU_PER_DIEM_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `per_diem` | `per_diem` | `per_diem` | `per_diem` | `per_diem` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `per_diem` | `per_diem` | `per_diem` | `per_diem` | `per_diem` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `per_diem` | `per_diem` | `per_diem` | `per_diem` | `per_diem` |

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

The amount of the established reimbursable costs for the current year divided by the estimated Medicare days for the current year (all PPS claims), as calculated by the FI and reim- bursement staff. Items reimbursed as a pass through include capital-related costs; direct medical education costs; kidney acquisition costs for hospitals approved as RTCs; and bad debts (per Provider Reimbursement Manual, Part 1, Section 2405.2). **Note: Pass throughs are not included in the Claim Payment Amount.



## [Claim Pricer Return Code](https://www.resdac.org/cms-data/variables/claim-pricer-return-code)

- Short SAS Name: `CLM_PRCR_RTRN_CD`
- Long SAS Name: `CLM_PRCR_RTRN_CD`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

The code used to identify various prospective payment system (PPS) payment adjustment types. This code identifies the payment return code or the error return code for every claim type calculated by the PRICER tool.

The payment return code identifies the type of payment calculated by the PRICER software.



<h3>Values</h3>

The meaning of the values varies by type of bill (TOB)   
****Inpatient Hospital Pricer Return Codes******   
******************TOB 11X***********************   
Inpatient Hospital Payment return codes: 

| Code   | Code Value                                                                                                                                                                                       |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Paid normal DRG payment                                                                                                                                                                          |
| 1      | Paid as a day outlier (Note: day outlier no longer being paid as of 10/1/97)                                                                                                                     |
| 2      | Paid as a cost outlier                                                                                                                                                                           |
| 3      | Transfer paid on a per diem basis up to and including the full DRG                                                                                                                               |
| 5      | Transfer paid on a per diem basis up to and including the full DRG which also qualified for a cost outlier payment                                                                               |
| 6      | Provider refused cost outlier                                                                                                                                                                    |
| 10     | DRG is 209, 210, or 211 and post-acute transfer                                                                                                                                                  |
| 12     | Post-acute transfer with specific DRGs. The following DRG's: 14, 113, 236, 263, 264, 429, 483                                                                                                    |
| 14     | Paid normal DRG payment with per diem days = or > GM ALOS                                                                                                                                        |
| 16     | Paid as a cost outlier with per diem days = or > GM ALOS                                                                                                                                         |
| nan    | Inpatient Hospital Error return codes:                                                                                                                                                           |
| 51     | No provider specific information found                                                                                                                                                           |
| 52     | Invalid MSA# in provider file                                                                                                                                                                    |
| 53     | Waiver state - not calculated by PPS                                                                                                                                                             |
| 54     | DRG < 001 or > 511, or = 214, 215, 221, 222, 438, 456, 457, 458                                                                                                                                  |
| 55     | Discharge date < provider effective start date or discharge date < MSA effective start date for PPS                                                                                              |
| 56     | Invalid length of stay                                                                                                                                                                           |
| 57     | Review code invalid (Not 00, 03, 06, 07, 09)                                                                                                                                                     |
| 58     | Total charges not numeric                                                                                                                                                                        |
| 61     | Lifetime reserve days not numeric or BILL-LTR-DAYS > 60                                                                                                                                          |
| 62     | Invalid number of covered days                                                                                                                                                                   |
| 65     | PAY-CODE not = A, B or C on provider specific file for capital                                                                                                                                   |
| 67     | Cost outlier with LOS > covered days                                                                                                                                                             |
| nan    | ***Inpatient Rehab Facility (IRF) Pricer Return Codes***                                                                                                                                         |
| nan    | IRF Payment return codes:                                                                                                                                                                        |
| 0      | Paid normal CMG payment without outlier                                                                                                                                                          |
| 1      | Paid normal CMG payment with outlier                                                                                                                                                             |
| 2      | Transfer paid on a per diem basis without outlier                                                                                                                                                |
| 3      | Transfer paid on a per diem basis with outlier                                                                                                                                                   |
| 4      | Blended CMG payment -- 2/3 Federal PPS rate + 1/3 provider specific rate -- without outlier                                                                                                      |
| 5      | Blended CMG payment -- 2/3 Federal PPS rate + 1/3 provider specific rate -- with outlier                                                                                                         |
| 6      | Blended transfer payment -- 2/3 Federal PPS transfer rate + 1/3 provider specific rate -- without outlier                                                                                        |
| 7      | Blended transfer payment -- 2/3 Federal PPS transfer rate + 1/3 provider specific rate -- with outlier                                                                                           |
| 10     | Paid normal CMG payment with penalty without outlier                                                                                                                                             |
| 11     | Paid normal CMG payment with penalty with outlier                                                                                                                                                |
| 12     | Transfer paid on a per diem basis with penalty without outlier                                                                                                                                   |
| 13     | Transfer paid on a per diem basis with penalty with outlier                                                                                                                                      |
| 14     | Blended CMG payment -- 2/3 Federal PPS rate + 1/3 provider specific rate -- with penalty without outlier                                                                                         |
| 15     | Blended CMG payment -- 2/3 Federal PPS rate + 1/3 provider specific rate -- with penalty with outlier                                                                                            |
| 16     | Blended transfer payment -- 2/3 Federal PPS transfer rate + 1/3 provider specific rate -- with penalty without outlier                                                                           |
| 17     | Blended transfer payment -- 2/3 Federal PPS transfer rate + 1/3 provider specific rate -- with penalty with outlier                                                                              |
| nan    | IRF Error return codes:                                                                                                                                                                          |
| 50     | Provider specific rate not numeric                                                                                                                                                               |
| 51     | Provider record terminated                                                                                                                                                                       |
| 52     | Invalid wage index                                                                                                                                                                               |
| 53     | Waiver state - not calculated by PPS                                                                                                                                                             |
| 54     | CMG on claim not found in table                                                                                                                                                                  |
| 55     | Discharge date < provider effective start date or discharge date < MSA effective start date for PPS                                                                                              |
| 56     | Invalid length of stay                                                                                                                                                                           |
| 57     | Provider specific rate zero when blended payment requested                                                                                                                                       |
| 58     | Total covered charges not numeric                                                                                                                                                                |
| 59     | Provider specific record not found                                                                                                                                                               |
| 60     | MSA wage index record not found                                                                                                                                                                  |
| 61     | Lifetime reserve days not numeric or BILL-LTR-DAYS > 60                                                                                                                                          |
| 62     | Invalid number of covered days                                                                                                                                                                   |
| 65     | Operating cost-to-charge ratio not numeric                                                                                                                                                       |
| 67     | Cost outlier with LOS > covered days or cost outlier threshold calculation                                                                                                                       |
| 72     | Invalid blend indicator (not 3 or 4)                                                                                                                                                             |
| 73     | Discharged before provider FY begin date                                                                                                                                                         |
| 74     | Provider FY begin date not in 2002                                                                                                                                                               |
| nan    | ***Long Term Care Hospital (LTCH) Pricer Return Codes***                                                                                                                                         |
| nan    | LTCH Payment return codes:                                                                                                                                                                       |
| 0      | Normal DRG payment without outlier                                                                                                                                                               |
| 1      | Normal DRG payment with outlier                                                                                                                                                                  |
| 2      | Short stay payment without outlier                                                                                                                                                               |
| 3      | Short stay payment with outlier                                                                                                                                                                  |
| 4      | Blend year 1 - 80% facility rate plus 20% normal DRG payment without outlier                                                                                                                     |
| 5      | Blend year 1 - 80% facility rate plus 20% normal DRG payment with outlier                                                                                                                        |
| 6      | Blend year 1 - 80% facility rate plus 20% short stay payment without outlier                                                                                                                     |
| 7      | Blend year 1 - 80% facility rate plus 20% short stay payment with outlier                                                                                                                        |
| 8      | Blend year 2 - 60% facility rate plus 40% normal DRG payment without outlier                                                                                                                     |
| 9      | Blend year 2 - 60% facility rate plus 40% normal DRG payment with outlier                                                                                                                        |
| 10     | Blend year 2 - 60% facility rate plus 40% short stay payment without outlier                                                                                                                     |
| 11     | 60% facility rate plus 40% short stay payment with outlier                                                                                                                                       |
| 12     | Blend year 3 - 40% facility rate plus 60% normal DRG payment without outlier                                                                                                                     |
| 13     | Blend year 3 - 40% facility rate plus 60% normal DRG payment with outlier                                                                                                                        |
| 14     | Blend year 3 - 40% facility rate plus 60% short stay payment without outlier                                                                                                                     |
| 15     | Blend year 3 - 40% facility rate plus 60% short stay payment with outlier                                                                                                                        |
| 16     | Blend year 4 - 20% facility rate plus 80% normal DRG payment without outlier                                                                                                                     |
| 17     | Blend year 4 - 20% facility rate plus 80% normal DRG payment with outlier                                                                                                                        |
| 18     | Blend year 4 - 20% facility rate plus 80% short stay payment without outlier                                                                                                                     |
| 19     | Blend year 4 - 20% facility rate plus 80% short stay payment with outlier                                                                                                                        |
| nan    | LTCH Error return codes:                                                                                                                                                                         |
| 50     | Provider specific rate not numeric                                                                                                                                                               |
| 51     | Provider record terminated                                                                                                                                                                       |
| 52     | Invalid wage index                                                                                                                                                                               |
| 53     | Waiver state - not calculated by PPS                                                                                                                                                             |
| 54     | DRG on claim not found in table                                                                                                                                                                  |
| 55     | Discharge date < provider effective start date or discharge date < MSA effective start date for PPS                                                                                              |
| 56     | Invalid length of stay                                                                                                                                                                           |
| 57     | Provider specific rate zero when blended payment requested                                                                                                                                       |
| 58     | Total covered charges not numeric                                                                                                                                                                |
| 59     | Provider specific record not found                                                                                                                                                               |
| 60     | MSA wage index record not found                                                                                                                                                                  |
| 61     | Lifetime reserve days not numeric or BILL-LTR-DAYS > 60                                                                                                                                          |
| 62     | Invalid number of covered days                                                                                                                                                                   |
| 65     | Operating cost-to-charge ratio not numeric                                                                                                                                                       |
| 67     | Cost outlier with LOS > covered days or cost outlier threshold calculation                                                                                                                       |
| 72     | Invalid blend indicator (not 1 thru 5)                                                                                                                                                           |
| 73     | Discharged before provider FY begin date                                                                                                                                                         |
| 74     | Provider FY begin date not in 2002                                                                                                                                                               |
| nan    | *************SNF Pricer Return Codes*********                                                                                                                                                    |
| nan    | *******************TOB 21X*******************                                                                                                                                                    |
| nan    | SNF Payment return codes:                                                                                                                                                                        |
| 0      | RUG III group rate returned SNF Error return codes:                                                                                                                                              |
| 20     | Bad RUG code                                                                                                                                                                                     |
| 30     | Bad MSA code                                                                                                                                                                                     |
| 40     | Thru date < July 1, 1998 or invalid                                                                                                                                                              |
| 50     | Invalid Federal blend for that year                                                                                                                                                              |
| 60     | Invalid Federal blend                                                                                                                                                                            |
| 61     | Federal blend = 0 and SNF thru date < January 1, 2000                                                                                                                                            |
| nan    | *********Hospice Pricer Return Codes************                                                                                                                                                 |
| nan    | **************TOB 81X or 82X********************                                                                                                                                                 |
| nan    | Hospice Payment Return Codes:                                                                                                                                                                    |
| 0      | Home rate returned Hospice Error Return Codes:                                                                                                                                                   |
| 10     | Bad units                                                                                                                                                                                        |
| 20     | Bad units2 < 8                                                                                                                                                                                   |
| 30     | Bad MSA code                                                                                                                                                                                     |
| 40     | Bad hospice wage index from MSA file                                                                                                                                                             |
| 50     | Bad bene wage index from MSA file                                                                                                                                                                |
| 51     | Bad provider number                                                                                                                                                                              |
| nan    | *******Home Health Pricer Return Codes************                                                                                                                                               |
| nan    | *****TOB 32X or 33X, DOS 10/1/2000 and after******                                                                                                                                               |
| nan    | Home Health Payment Return Codes:                                                                                                                                                                |
| 0      | Final payment where no outlier applies                                                                                                                                                           |
| 1      | Final payment where outlier applies                                                                                                                                                              |
| 3      | Initial percentage payment, 0%                                                                                                                                                                   |
| 4      | Initial percentage payment, 50%                                                                                                                                                                  |
| 5      | Initial percentage payment, 60%                                                                                                                                                                  |
| 6      | LUPA payment only                                                                                                                                                                                |
| 7      | Final payment, SCIC                                                                                                                                                                              |
| 8      | Final payment, SCIC with outlier                                                                                                                                                                 |
| 9      | Final payment, PEP                                                                                                                                                                               |
| 11     | Final payment, PEP with outlier                                                                                                                                                                  |
| 12     | Final payment, SCIC within PEP                                                                                                                                                                   |
| 13     | Final payment, SCIS within PEP with outlier                                                                                                                                                      |
| nan    | Home Health Error Return Codes:                                                                                                                                                                  |
| 10     | Invalid TOB                                                                                                                                                                                      |
| 15     | Invalid PEP Days                                                                                                                                                                                 |
| 16     | Invalid HRG Days, >60                                                                                                                                                                            |
| 20     | PEP indicator invalid                                                                                                                                                                            |
| 25     | Med review indicator invalid                                                                                                                                                                     |
| 30     | Invalid MSA code                                                                                                                                                                                 |
| 35     | Invalid Initial Payment Indicator                                                                                                                                                                |
| 40     | Dates < October 1, 2000 or invalid                                                                                                                                                               |
| 70     | Invalid HRG Code                                                                                                                                                                                 |
| 75     | No HRG present in 1st occurrence                                                                                                                                                                 |
| 80     | Invalid Revenue code                                                                                                                                                                             |
| 85     | No revenue code present on HH final claim/adjustment                                                                                                                                             |
| nan    | ************Outpatient PPS Pricer Return Codes******                                                                                                                                             |
| nan    | Outpatient PPS Payment return codes:                                                                                                                                                             |
| 1      | Line processed to payment                                                                                                                                                                        |
| 20     | Line processed but payment = 0 bene deductible = > adjusted payment                                                                                                                              |
| nan    | Outpatient PPS Error return codes:                                                                                                                                                               |
| 30     | Missing, deleted or invalid APC                                                                                                                                                                  |
| 38     | Missing or invalid discount factor                                                                                                                                                               |
| 40     | Invalid service indicator passed by the OCE                                                                                                                                                      |
| 41     | Service indicator invalid for OPPS PRICER                                                                                                                                                        |
| 42     | APC = '00000' or (packaging flag = 1 or 2)                                                                                                                                                       |
| 43     | Payment indicator not = to 1 or 5 thru 9                                                                                                                                                         |
| 44     | Service indicator = 'H' but payment indicator not = to 6                                                                                                                                         |
| 45     | Packaging flag not = to 0                                                                                                                                                                        |
| 46     | Line item denial/reject flag not = to 0 or line item denial/reject flag = to 1 and (APC not = 0033 or 0034 or 0322 or 0323 or 0324 or 0325 or 0373 or 0374)) or line item action flag not = to 1 |
| 47     | Line item action flag = 2 or 3                                                                                                                                                                   |
| 48     | Payment adjustment flag not valid                                                                                                                                                                |
| 49     | Site of service flag not = to 0 or (APC 0033 is not on the claim and service indicator = 'P' or APC = 0322, 0325, 0373, 0374)                                                                    |
| 50     | Wage index not located                                                                                                                                                                           |
| 51     | Wage index equals zero                                                                                                                                                                           |
| 52     | Provider specific file wage index reclassification code invalid or missing                                                                                                                       |
| 53     | Service from date not numeric or < 20000801                                                                                                                                                      |
| 54     | Service from date < provider effective date or service from date > provider termination date                                                                                                     |
| nan    | ***End Stage Renal Disease (ESRD) Pricer Return Codes***                                                                                                                                         |
| nan    | ESRD Payment return codes:                                                                                                                                                                       |
| 0      | ESRD PPS payment calculated                                                                                                                                                                      |
| 1      | ESRD facility rate > zero                                                                                                                                                                        |
| nan    | ESRD Error return codes:                                                                                                                                                                         |
| 50     | ESRD facility rate not numeric                                                                                                                                                                   |
| 52     | Provider type not = '40' or '41'                                                                                                                                                                 |
| 53     | Special payment indicator not = '1' or blank                                                                                                                                                     |
| 54     | Date of birth not numeric or = zero                                                                                                                                                              |
| 55     | Patient weight not numeric or = zero                                                                                                                                                             |
| 56     | Patient height not numeric or = zero                                                                                                                                                             |
| 57     | Revenue center code not in range                                                                                                                                                                 |
| 58     | Condition code not = '73' or '74' or blank                                                                                                                                                       |
| 60     | MSA wage adjusted rate record not found                                                                                                                                                          |
| 98     | Claim through date before 4/1/2005 or not numeric                                                                                                                                                |

## [Claim Principal Diagnosis Code](https://www.resdac.org/cms-data/variables/Primary-Claim-Diagnosis-Code)

- Short SAS Name: `PRNCPAL_DGNS_CD`
- Long SAS Name: `PRNCPAL_DGNS_CD`

<h3>Variable Names</h3>

| Dataset   | 2012              | 2011              | 2010              | 2009       | 2008       |
|:----------|:------------------|:------------------|:------------------|:-----------|:-----------|
| Carrier   | `prncpal_dgns_cd` | `prncpal_dgns_cd` | `prncpal_dgns_cd` | `dgns_cd1` | `dgns_cd1` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `dgns_cd1` | `dgns_cd1` | `pdgns_cd` | `pdgns_cd` | `pdgns_cd` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `pdgns_cd` | `pdgns_cd` | `pdgns_cd` | `pdgns_cd` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The diagnosis code identifying the diagnosis, condition, problem or other reason for the admission/encounter/visit shown in the medical record to be chiefly responsible for the services provided.

NOTE: Effective with Version H, this data is also redundantly stored as the first occurrence of the diagnosis trailer.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.



## [Claim Procedure Code I](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-I)

- Short SAS Name: `ICD_PRCDR_CD1`
- Long SAS Name: `ICD_PRCDR_CD1`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `prcdrcd1` |
| Outpatient | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `icd_prcdr_cd1` | `prcdrcd1` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd1` | `prcdrcd1` | `prcdrcd1` | `prcdr_cd1` | `prcdr_cd1` |
| Outpatient | `prcdrcd1` | `prcdrcd1` | `prcdrcd1` | `prcdr_cd1` | `prcdr_cd1` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd1` | `prcdr_cd1` | `prcdrcd1`  | `prcdrcd1` | `prcdrcd1` |
| Outpatient | `prcdr_cd1` | `prcdr_cd1` | `prcdr_cd1` | `prcdrcd1` | `prcdrcd1` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code I Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-I-Date)

- Short SAS Name: `PRCDR_DT1`
- Long SAS Name: `PRCDR_DT1`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt1` | `prcdr_dt1` | `prcdr_dt1` | `prcdr_dt1` | `prcdrdt1` |
| Outpatient | `prcdr_dt1` | `prcdr_dt1` | `prcdr_dt1` | `prcdr_dt1` | `prcdrdt1` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt1` | `prcdrdt1` | `prcdrdt1` | `prcdr_dt1` | `prcdr_dt1` |
| Outpatient | `prcdrdt1` | `prcdrdt1` | `prcdrdt1` | `prcdr_dt1` | `prcdr_dt1` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt1` | `prcdr_dt1` | `prcdrdt1`  | `prcdr_dt1` | `prcdrdt1` |
| Outpatient | `prcdr_dt1` | `prcdr_dt1` | `prcdr_dt1` | `prcdrdt1`  | `prcdrdt1` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code II](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-II)

- Short SAS Name: `ICD_PRCDR_CD2`
- Long SAS Name: `ICD_PRCDR_CD2`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `prcdrcd2` |
| Outpatient | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `icd_prcdr_cd2` | `prcdrcd2` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd2` | `prcdrcd2` | `prcdrcd2` | `prcdr_cd2` | `prcdr_cd2` |
| Outpatient | `prcdrcd2` | `prcdrcd2` | `prcdrcd2` | `prcdr_cd2` | `prcdr_cd2` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd2` | `prcdr_cd2` | `prcdrcd2`  | `prcdrcd2` | `prcdrcd2` |
| Outpatient | `prcdr_cd2` | `prcdr_cd2` | `prcdr_cd2` | `prcdrcd2` | `prcdrcd2` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code II Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-II-Date)

- Short SAS Name: `PRCDR_DT2`
- Long SAS Name: `PRCDR_DT2`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt2` | `prcdr_dt2` | `prcdr_dt2` | `prcdr_dt2` | `prcdrdt2` |
| Outpatient | `prcdr_dt2` | `prcdr_dt2` | `prcdr_dt2` | `prcdr_dt2` | `prcdrdt2` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt2` | `prcdrdt2` | `prcdrdt2` | `prcdr_dt2` | `prcdr_dt2` |
| Outpatient | `prcdrdt2` | `prcdrdt2` | `prcdrdt2` | `prcdr_dt2` | `prcdr_dt2` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt2` | `prcdr_dt2` | `prcdrdt2`  | `prcdr_dt2` | `prcdrdt2` |
| Outpatient | `prcdr_dt2` | `prcdr_dt2` | `prcdr_dt2` | `prcdrdt2`  | `prcdrdt2` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code III](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-III)

- Short SAS Name: `ICD_PRCDR_CD3`
- Long SAS Name: `ICD_PRCDR_CD3`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `prcdrcd3` |
| Outpatient | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `icd_prcdr_cd3` | `prcdrcd3` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd3` | `prcdrcd3` | `prcdrcd3` | `prcdr_cd3` | `prcdr_cd3` |
| Outpatient | `prcdrcd3` | `prcdrcd3` | `prcdrcd3` | `prcdr_cd3` | `prcdr_cd3` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd3` | `prcdr_cd3` | `prcdrcd3`  | `prcdrcd3` | `prcdrcd3` |
| Outpatient | `prcdr_cd3` | `prcdr_cd3` | `prcdr_cd3` | `prcdrcd3` | `prcdrcd3` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code III Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-III-Date)

- Short SAS Name: `PRCDR_DT3`
- Long SAS Name: `PRCDR_DT3`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt3` | `prcdr_dt3` | `prcdr_dt3` | `prcdr_dt3` | `prcdrdt3` |
| Outpatient | `prcdr_dt3` | `prcdr_dt3` | `prcdr_dt3` | `prcdr_dt3` | `prcdrdt3` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt3` | `prcdrdt3` | `prcdrdt3` | `prcdr_dt3` | `prcdr_dt3` |
| Outpatient | `prcdrdt3` | `prcdrdt3` | `prcdrdt3` | `prcdr_dt3` | `prcdr_dt3` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt3` | `prcdr_dt3` | `prcdrdt3`  | `prcdr_dt3` | `prcdrdt3` |
| Outpatient | `prcdr_dt3` | `prcdr_dt3` | `prcdr_dt3` | `prcdrdt3`  | `prcdrdt3` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code IV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IV)

- Short SAS Name: `ICD_PRCDR_CD4`
- Long SAS Name: `ICD_PRCDR_CD4`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `prcdrcd4` |
| Outpatient | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `icd_prcdr_cd4` | `prcdrcd4` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd4` | `prcdrcd4` | `prcdrcd4` | `prcdr_cd4` | `prcdr_cd4` |
| Outpatient | `prcdrcd4` | `prcdrcd4` | `prcdrcd4` | `prcdr_cd4` | `prcdr_cd4` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd4` | `prcdr_cd4` | `prcdrcd4`  | `prcdrcd4` | `prcdrcd4` |
| Outpatient | `prcdr_cd4` | `prcdr_cd4` | `prcdr_cd4` | `prcdrcd4` | `prcdrcd4` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code IV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IV-Date)

- Short SAS Name: `PRCDR_DT4`
- Long SAS Name: `PRCDR_DT4`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt4` | `prcdr_dt4` | `prcdr_dt4` | `prcdr_dt4` | `prcdrdt4` |
| Outpatient | `prcdr_dt4` | `prcdr_dt4` | `prcdr_dt4` | `prcdr_dt4` | `prcdrdt4` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt4` | `prcdrdt4` | `prcdrdt4` | `prcdr_dt4` | `prcdr_dt4` |
| Outpatient | `prcdrdt4` | `prcdrdt4` | `prcdrdt4` | `prcdr_dt4` | `prcdr_dt4` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt4` | `prcdr_dt4` | `prcdrdt4`  | `prcdr_dt4` | `prcdrdt4` |
| Outpatient | `prcdr_dt4` | `prcdr_dt4` | `prcdr_dt4` | `prcdrdt4`  | `prcdrdt4` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code IX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IX)

- Short SAS Name: `ICD_PRCDR_CD9`
- Long SAS Name: `ICD_PRCDR_CD9`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_prcdr_cd9` | `icd_prcdr_cd9` | `icd_prcdr_cd9` | `icd_prcdr_cd9` |
| Outpatient | `icd_prcdr_cd9` | `icd_prcdr_cd9` | `icd_prcdr_cd9` | `icd_prcdr_cd9` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code IX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-IX-Date)

- Short SAS Name: `PRCDR_DT9`
- Long SAS Name: `PRCDR_DT9`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        |
|:-----------|:------------|:------------|:------------|:------------|
| Inpatient  | `prcdr_dt9` | `prcdr_dt9` | `prcdr_dt9` | `prcdr_dt9` |
| Outpatient | `prcdr_dt9` | `prcdr_dt9` | `prcdr_dt9` | `prcdr_dt9` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code V](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-V)

- Short SAS Name: `ICD_PRCDR_CD5`
- Long SAS Name: `ICD_PRCDR_CD5`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `prcdrcd5` |
| Outpatient | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `icd_prcdr_cd5` | `prcdrcd5` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd5` | `prcdrcd5` | `prcdrcd5` | `prcdr_cd5` | `prcdr_cd5` |
| Outpatient | `prcdrcd5` | `prcdrcd5` | `prcdrcd5` | `prcdr_cd5` | `prcdr_cd5` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd5` | `prcdr_cd5` | `prcdrcd5`  | `prcdrcd5` | `prcdrcd5` |
| Outpatient | `prcdr_cd5` | `prcdr_cd5` | `prcdr_cd5` | `prcdrcd5` | `prcdrcd5` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code V Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-V-Date)

- Short SAS Name: `PRCDR_DT5`
- Long SAS Name: `PRCDR_DT5`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt5` | `prcdr_dt5` | `prcdr_dt5` | `prcdr_dt5` | `prcdrdt5` |
| Outpatient | `prcdr_dt5` | `prcdr_dt5` | `prcdr_dt5` | `prcdr_dt5` | `prcdrdt5` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt5` | `prcdrdt5` | `prcdrdt5` | `prcdr_dt5` | `prcdr_dt5` |
| Outpatient | `prcdrdt5` | `prcdrdt5` | `prcdrdt5` | `prcdr_dt5` | `prcdr_dt5` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt5` | `prcdr_dt5` | `prcdrdt5`  | `prcdr_dt5` | `prcdrdt5` |
| Outpatient | `prcdr_dt5` | `prcdr_dt5` | `prcdr_dt5` | `prcdrdt5`  | `prcdrdt5` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code VI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VI)

- Short SAS Name: `ICD_PRCDR_CD6`
- Long SAS Name: `ICD_PRCDR_CD6`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            | 2009       |
|:-----------|:----------------|:----------------|:----------------|:----------------|:-----------|
| Inpatient  | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `prcdrcd6` |
| Outpatient | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `icd_prcdr_cd6` | `prcdrcd6` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrcd6` | `prcdrcd6` | `prcdrcd6` | `prcdr_cd6` | `prcdr_cd6` |
| Outpatient | `prcdrcd6` | `prcdrcd6` | `prcdrcd6` | `prcdr_cd6` | `prcdr_cd6` |

| Dataset    | 2003        | 2002        | 2001        | 2000       | 1999       |
|:-----------|:------------|:------------|:------------|:-----------|:-----------|
| Inpatient  | `prcdr_cd6` | `prcdr_cd6` | `prcdrcd6`  | `prcdrcd6` | `prcdrcd6` |
| Outpatient | `prcdr_cd6` | `prcdr_cd6` | `prcdr_cd6` | `prcdrcd6` | `prcdrcd6` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code VI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VI-Date)

- Short SAS Name: `PRCDR_DT6`
- Long SAS Name: `PRCDR_DT6`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        | 2009       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt6` | `prcdr_dt6` | `prcdr_dt6` | `prcdr_dt6` | `prcdrdt6` |
| Outpatient | `prcdr_dt6` | `prcdr_dt6` | `prcdr_dt6` | `prcdr_dt6` | `prcdrdt6` |

| Dataset    | 2008       | 2007       | 2006       | 2005        | 2004        |
|:-----------|:-----------|:-----------|:-----------|:------------|:------------|
| Inpatient  | `prcdrdt6` | `prcdrdt6` | `prcdrdt6` | `prcdr_dt6` | `prcdr_dt6` |
| Outpatient | `prcdrdt6` | `prcdrdt6` | `prcdrdt6` | `prcdr_dt6` | `prcdr_dt6` |

| Dataset    | 2003        | 2002        | 2001        | 2000        | 1999       |
|:-----------|:------------|:------------|:------------|:------------|:-----------|
| Inpatient  | `prcdr_dt6` | `prcdr_dt6` | `prcdrdt6`  | `prcdr_dt6` | `prcdrdt6` |
| Outpatient | `prcdr_dt6` | `prcdr_dt6` | `prcdr_dt6` | `prcdrdt6`  | `prcdrdt6` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code VII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VII)

- Short SAS Name: `ICD_PRCDR_CD7`
- Long SAS Name: `ICD_PRCDR_CD7`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_prcdr_cd7` | `icd_prcdr_cd7` | `icd_prcdr_cd7` | `icd_prcdr_cd7` |
| Outpatient | `icd_prcdr_cd7` | `icd_prcdr_cd7` | `icd_prcdr_cd7` | `icd_prcdr_cd7` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code VII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-CodeVII-Date)

- Short SAS Name: `PRCDR_DT7`
- Long SAS Name: `PRCDR_DT7`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        |
|:-----------|:------------|:------------|:------------|:------------|
| Inpatient  | `prcdr_dt7` | `prcdr_dt7` | `prcdr_dt7` | `prcdr_dt7` |
| Outpatient | `prcdr_dt7` | `prcdr_dt7` | `prcdr_dt7` | `prcdr_dt7` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code VIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VIII)

- Short SAS Name: `ICD_PRCDR_CD8`
- Long SAS Name: `ICD_PRCDR_CD8`

<h3>Variable Names</h3>

| Dataset    | 2013            | 2012            | 2011            | 2010            |
|:-----------|:----------------|:----------------|:----------------|:----------------|
| Inpatient  | `icd_prcdr_cd8` | `icd_prcdr_cd8` | `icd_prcdr_cd8` | `icd_prcdr_cd8` |
| Outpatient | `icd_prcdr_cd8` | `icd_prcdr_cd8` | `icd_prcdr_cd8` | `icd_prcdr_cd8` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code VIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-VIII-Date)

- Short SAS Name: `PRCDR_DT8`
- Long SAS Name: `PRCDR_DT8`

<h3>Variable Names</h3>

| Dataset    | 2013        | 2012        | 2011        | 2010        |
|:-----------|:------------|:------------|:------------|:------------|
| Inpatient  | `prcdr_dt8` | `prcdr_dt8` | `prcdr_dt8` | `prcdr_dt8` |
| Outpatient | `prcdr_dt8` | `prcdr_dt8` | `prcdr_dt8` | `prcdr_dt8` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code X](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-X)

- Short SAS Name: `ICD_PRCDR_CD10`
- Long SAS Name: `ICD_PRCDR_CD10`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd10` | `icd_prcdr_cd10` | `icd_prcdr_cd10` | `icd_prcdr_cd10` |
| Outpatient | `icd_prcdr_cd10` | `icd_prcdr_cd10` | `icd_prcdr_cd10` | `icd_prcdr_cd10` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code X Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-X-Date)

- Short SAS Name: `PRCDR_DT10`
- Long SAS Name: `PRCDR_DT10`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt10` | `prcdr_dt10` | `prcdr_dt10` | `prcdr_dt10` |
| Outpatient | `prcdr_dt10` | `prcdr_dt10` | `prcdr_dt10` | `prcdr_dt10` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XI)

- Short SAS Name: `ICD_PRCDR_CD11`
- Long SAS Name: `ICD_PRCDR_CD11`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd11` | `icd_prcdr_cd11` | `icd_prcdr_cd11` | `icd_prcdr_cd11` |
| Outpatient | `icd_prcdr_cd11` | `icd_prcdr_cd11` | `icd_prcdr_cd11` | `icd_prcdr_cd11` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XI-Date)

- Short SAS Name: `PRCDR_DT11`
- Long SAS Name: `PRCDR_DT11`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt11` | `prcdr_dt11` | `prcdr_dt11` | `prcdr_dt11` |
| Outpatient | `prcdr_dt11` | `prcdr_dt11` | `prcdr_dt11` | `prcdr_dt11` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XII)

- Short SAS Name: `ICD_PRCDR_CD12`
- Long SAS Name: `ICD_PRCDR_CD12`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd12` | `icd_prcdr_cd12` | `icd_prcdr_cd12` | `icd_prcdr_cd12` |
| Outpatient | `icd_prcdr_cd12` | `icd_prcdr_cd12` | `icd_prcdr_cd12` | `icd_prcdr_cd12` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XII-Date)

- Short SAS Name: `PRCDR_DT12`
- Long SAS Name: `PRCDR_DT12`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt12` | `prcdr_dt12` | `prcdr_dt12` | `prcdr_dt12` |
| Outpatient | `prcdr_dt12` | `prcdr_dt12` | `prcdr_dt12` | `prcdr_dt12` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIII)

- Short SAS Name: `ICD_PRCDR_CD13`
- Long SAS Name: `ICD_PRCDR_CD13`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd13` | `icd_prcdr_cd13` | `icd_prcdr_cd13` | `icd_prcdr_cd13` |
| Outpatient | `icd_prcdr_cd13` | `icd_prcdr_cd13` | `icd_prcdr_cd13` | `icd_prcdr_cd13` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIII-Date)

- Short SAS Name: `PRCDR_DT13`
- Long SAS Name: `PRCDR_DT13`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt13` | `prcdr_dt13` | `prcdr_dt13` | `prcdr_dt13` |
| Outpatient | `prcdr_dt13` | `prcdr_dt13` | `prcdr_dt13` | `prcdr_dt13` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XIV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIV)

- Short SAS Name: `ICD_PRCDR_CD14`
- Long SAS Name: `ICD_PRCDR_CD14`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd14` | `icd_prcdr_cd14` | `icd_prcdr_cd14` | `icd_prcdr_cd14` |
| Outpatient | `icd_prcdr_cd14` | `icd_prcdr_cd14` | `icd_prcdr_cd14` | `icd_prcdr_cd14` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XIV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIV-Date)

- Short SAS Name: `PRCDR_DT14`
- Long SAS Name: `PRCDR_DT14`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt14` | `prcdr_dt14` | `prcdr_dt14` | `prcdr_dt14` |
| Outpatient | `prcdr_dt14` | `prcdr_dt14` | `prcdr_dt14` | `prcdr_dt14` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XIX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIX)

- Short SAS Name: `ICD_PRCDR_CD19`
- Long SAS Name: `ICD_PRCDR_CD19`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd19` | `icd_prcdr_cd19` | `icd_prcdr_cd19` | `icd_prcdr_cd19` |
| Outpatient | `icd_prcdr_cd19` | `icd_prcdr_cd19` | `icd_prcdr_cd19` | `icd_prcdr_cd19` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XIX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XIX-Date)

- Short SAS Name: `PRCDR_DT19`
- Long SAS Name: `PRCDR_DT19`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt19` | `prcdr_dt19` | `prcdr_dt19` | `prcdr_dt19` |
| Outpatient | `prcdr_dt19` | `prcdr_dt19` | `prcdr_dt19` | `prcdr_dt19` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XV)

- Short SAS Name: `ICD_PRCDR_CD15`
- Long SAS Name: `ICD_PRCDR_CD15`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd15` | `icd_prcdr_cd15` | `icd_prcdr_cd15` | `icd_prcdr_cd15` |
| Outpatient | `icd_prcdr_cd15` | `icd_prcdr_cd15` | `icd_prcdr_cd15` | `icd_prcdr_cd15` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XV-Date)

- Short SAS Name: `PRCDR_DT15`
- Long SAS Name: `PRCDR_DT15`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt15` | `prcdr_dt15` | `prcdr_dt15` | `prcdr_dt15` |
| Outpatient | `prcdr_dt15` | `prcdr_dt15` | `prcdr_dt15` | `prcdr_dt15` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XVI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVI)

- Short SAS Name: `ICD_PRCDR_CD16`
- Long SAS Name: `ICD_PRCDR_CD16`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd16` | `icd_prcdr_cd16` | `icd_prcdr_cd16` | `icd_prcdr_cd16` |
| Outpatient | `icd_prcdr_cd16` | `icd_prcdr_cd16` | `icd_prcdr_cd16` | `icd_prcdr_cd16` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XVI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVI-Date)

- Short SAS Name: `PRCDR_DT16`
- Long SAS Name: `PRCDR_DT16`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt16` | `prcdr_dt16` | `prcdr_dt16` | `prcdr_dt16` |
| Outpatient | `prcdr_dt16` | `prcdr_dt16` | `prcdr_dt16` | `prcdr_dt16` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XVII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVII)

- Short SAS Name: `ICD_PRCDR_CD17`
- Long SAS Name: `ICD_PRCDR_CD17`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd17` | `icd_prcdr_cd17` | `icd_prcdr_cd17` | `icd_prcdr_cd17` |
| Outpatient | `icd_prcdr_cd17` | `icd_prcdr_cd17` | `icd_prcdr_cd17` | `icd_prcdr_cd17` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XVII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVII-Date)

- Short SAS Name: `PRCDR_DT17`
- Long SAS Name: `PRCDR_DT17`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt17` | `prcdr_dt17` | `prcdr_dt17` | `prcdr_dt17` |
| Outpatient | `prcdr_dt17` | `prcdr_dt17` | `prcdr_dt17` | `prcdr_dt17` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XVIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVIII)

- Short SAS Name: `ICD_PRCDR_CD18`
- Long SAS Name: `ICD_PRCDR_CD18`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd18` | `icd_prcdr_cd18` | `icd_prcdr_cd18` | `icd_prcdr_cd18` |
| Outpatient | `icd_prcdr_cd18` | `icd_prcdr_cd18` | `icd_prcdr_cd18` | `icd_prcdr_cd18` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XVIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XVIII-Date)

- Short SAS Name: `PRCDR_DT18`
- Long SAS Name: `PRCDR_DT18`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt18` | `prcdr_dt18` | `prcdr_dt18` | `prcdr_dt18` |
| Outpatient | `prcdr_dt18` | `prcdr_dt18` | `prcdr_dt18` | `prcdr_dt18` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XX](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XX)

- Short SAS Name: `ICD_PRCDR_CD20`
- Long SAS Name: `ICD_PRCDR_CD20`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd20` | `icd_prcdr_cd20` | `icd_prcdr_cd20` | `icd_prcdr_cd20` |
| Outpatient | `icd_prcdr_cd20` | `icd_prcdr_cd20` | `icd_prcdr_cd20` | `icd_prcdr_cd20` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XX Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XX-Date)

- Short SAS Name: `PRCDR_DT20`
- Long SAS Name: `PRCDR_DT20`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt20` | `prcdr_dt20` | `prcdr_dt20` | `prcdr_dt20` |
| Outpatient | `prcdr_dt20` | `prcdr_dt20` | `prcdr_dt20` | `prcdr_dt20` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XXI](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXI)

- Short SAS Name: `ICD_PRCDR_CD21`
- Long SAS Name: `ICD_PRCDR_CD21`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd21` | `icd_prcdr_cd21` | `icd_prcdr_cd21` | `icd_prcdr_cd21` |
| Outpatient | `icd_prcdr_cd21` | `icd_prcdr_cd21` | `icd_prcdr_cd21` | `icd_prcdr_cd21` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XXI Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXI-Date)

- Short SAS Name: `PRCDR_DT21`
- Long SAS Name: `PRCDR_DT21`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt21` | `prcdr_dt21` | `prcdr_dt21` | `prcdr_dt21` |
| Outpatient | `prcdr_dt21` | `prcdr_dt21` | `prcdr_dt21` | `prcdr_dt21` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XXII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXII)

- Short SAS Name: `ICD_PRCDR_CD22`
- Long SAS Name: `ICD_PRCDR_CD22`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd22` | `icd_prcdr_cd22` | `icd_prcdr_cd22` | `icd_prcdr_cd22` |
| Outpatient | `icd_prcdr_cd22` | `icd_prcdr_cd22` | `icd_prcdr_cd22` | `icd_prcdr_cd22` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XXII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXII-Date)

- Short SAS Name: `PRCDR_DT22`
- Long SAS Name: `PRCDR_DT22`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt22` | `prcdr_dt22` | `prcdr_dt22` | `prcdr_dt22` |
| Outpatient | `prcdr_dt22` | `prcdr_dt22` | `prcdr_dt22` | `prcdr_dt22` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XXIII](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIII)

- Short SAS Name: `ICD_PRCDR_CD23`
- Long SAS Name: `ICD_PRCDR_CD23`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd23` | `icd_prcdr_cd23` | `icd_prcdr_cd23` | `icd_prcdr_cd23` |
| Outpatient | `icd_prcdr_cd23` | `icd_prcdr_cd23` | `icd_prcdr_cd23` | `icd_prcdr_cd23` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XXIII Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIII-Date)

- Short SAS Name: `PRCDR_DT23`
- Long SAS Name: `PRCDR_DT23`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt23` | `prcdr_dt23` | `prcdr_dt23` | `prcdr_dt23` |
| Outpatient | `prcdr_dt23` | `prcdr_dt23` | `prcdr_dt23` | `prcdr_dt23` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XXIV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIV)

- Short SAS Name: `ICD_PRCDR_CD24`
- Long SAS Name: `ICD_PRCDR_CD24`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd24` | `icd_prcdr_cd24` | `icd_prcdr_cd24` | `icd_prcdr_cd24` |
| Outpatient | `icd_prcdr_cd24` | `icd_prcdr_cd24` | `icd_prcdr_cd24` | `icd_prcdr_cd24` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XXIV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXIV-Date)

- Short SAS Name: `PRCDR_DT24`
- Long SAS Name: `PRCDR_DT24`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt24` | `prcdr_dt24` | `prcdr_dt24` | `prcdr_dt24` |
| Outpatient | `prcdr_dt24` | `prcdr_dt24` | `prcdr_dt24` | `prcdr_dt24` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Procedure Code XXV](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXV)

- Short SAS Name: `ICD_PRCDR_CD25`
- Long SAS Name: `ICD_PRCDR_CD25`

<h3>Variable Names</h3>

| Dataset    | 2013             | 2012             | 2011             | 2010             |
|:-----------|:-----------------|:-----------------|:-----------------|:-----------------|
| Inpatient  | `icd_prcdr_cd25` | `icd_prcdr_cd25` | `icd_prcdr_cd25` | `icd_prcdr_cd25` |
| Outpatient | `icd_prcdr_cd25` | `icd_prcdr_cd25` | `icd_prcdr_cd25` | `icd_prcdr_cd25` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code that indicates the principal or other procedure performed during the period covered by the institutional claim.

NOTE: Effective July 2004, ICD-9-CM procedure codes are no longer being accepted on Outpatient claims. The ICD-9-CM codes were named as the HIPPA standard code set for inpatient hospital procedures. HCPCS/CPT codes were named as the standard code set for physician services and other health care services.



## [Claim Procedure Code XXV Date](https://www.resdac.org/cms-data/variables/Claim-Procedure-Code-XXV-Date)

- Short SAS Name: `PRCDR_DT25`
- Long SAS Name: `PRCDR_DT25`

<h3>Variable Names</h3>

| Dataset    | 2013         | 2012         | 2011         | 2010         |
|:-----------|:-------------|:-------------|:-------------|:-------------|
| Inpatient  | `prcdr_dt25` | `prcdr_dt25` | `prcdr_dt25` | `prcdr_dt25` |
| Outpatient | `prcdr_dt25` | `prcdr_dt25` | `prcdr_dt25` | `prcdr_dt25` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the date on which the principal or other procedure was performed.



## [Claim Query Code](https://www.resdac.org/cms-data/variables/Claim-Query-Code)

- Short SAS Name: `QUERY_CD`
- Long SAS Name: `CLAIM_QUERY_CODE`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Code indicating the type of claim record being processed with respect to payment (debit/credit indicator; interim/final indicator).



<h3>Values</h3>

| Code   | Code Value       |
|:-------|:-----------------|
| 1      | Interim bill     |
| 3      | Final bill       |
| 5      | Debit adjustment |

## [Claim Related Condition Code](https://www.resdac.org/cms-data/variables/claim-related-condition-code)

- Short SAS Name: `RLT_COND`
- Long SAS Name: `CLM_RLT_COND_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code that indicates a condition relating to an institutional claim that may affect payer processing.



<h3>Values</h3>

For codes C1 THRU C7, NOTE: Beginning July 2005, this code is relevant to types of bill other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).

| Code       | Code Value                                                                                    |
|:-----------|:----------------------------------------------------------------------------------------------|
| 01 THRU 16 | Insurance related                                                                             |
| 17 THRU 30 | Special condition                                                                             |
| 31 THRU 35 | Student status codes which are required when a patient is a dependent child over 18 years old |
| 36 THRU 45 | Accommodation                                                                                 |
| 46 THRU 54 | CHAMPUS information                                                                           |
| 55 THRU 59 | Skilled nursing facility                                                                      |
| 60 THRU 70 | Prospective payment                                                                           |
| 71 THRU 99 | Renal dialysis setting                                                                        |
| A0 THRU B9 | Special program codes                                                                         |
| C0 THRU C9 | QIO approval services                                                                         |
| D0 THRU W0 | Change conditions                                                                             |

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01     | Military service related - Medical condition incurred during military service.                                                                                                                                                                                                                                                                                                                                                      |
| 02     | Employment related - Patient alleged that the medical condition causing this episode of care was due to environment/events resulting from employment.                                                                                                                                                                                                                                                                               |
| 03     | Patient covered by insurance not reflected here - Indicates that patient or patient representative has stated that coverage may exist beyond that reflected on this bill.                                                                                                                                                                                                                                                           |
| 04     | Health Maintenance Organization (HMO) enrollee - Medicare beneficiary is enrolled in an HMO. Eff 9/93, hospital must also expect to receive payment from HMO.                                                                                                                                                                                                                                                                       |
| 05     | Lien has been filed - Provider has filed legal claim for recovery of funds potentially due a patient as a result of legal action initiated by or on behalf of the patient.                                                                                                                                                                                                                                                          |
| 06     | ESRD patient in 1st 18 months of entitlement covered by employer group health insurance - indicates Medicare may be secondary insurer. Eff 3/1/96, ESRD patient in 1st 30 months of entitlement covered by employer group health insurance.                                                                                                                                                                                         |
| 07     | Treatment of nonterminal condition for hospice patient - The patient is a hospice enrollee, but the provider is not treating a terminal condition and is requesting Medicare reimbursement.                                                                                                                                                                                                                                         |
| 08     | Beneficiary would not provide information concerning other insurance coverage.                                                                                                                                                                                                                                                                                                                                                      |
| 09     | Neither patient nor spouse is employed - Code indicates that in response to development questions, the patient and spouse have denied employment.                                                                                                                                                                                                                                                                                   |
| 10     | Patient and/or spouse is employed but no EGHP coverage exists or (eff 9/93) other employer sponsored/provided health insurance covering patient.                                                                                                                                                                                                                                                                                    |
| 11     | The disabled beneficiary and/or family member has no group coverage from a LGHP or (eff 9/93) other employer sponsored/provided health insurance covering patient.                                                                                                                                                                                                                                                                  |
| 12     | Payer code - Reserved for internal use only by third party payers. HCFA will assign as needed. Providers will not report them.                                                                                                                                                                                                                                                                                                      |
| 13     | Payer code - Reserved for internal use only by third party payers. HCFA will assign as needed. Providers will not report them.                                                                                                                                                                                                                                                                                                      |
| 14     | Payer code - Reserved for internal use only by third party payers. HCFA will assign as needed. Providers will not report them.                                                                                                                                                                                                                                                                                                      |
| 15     | Clean claim (eff 10/92)                                                                                                                                                                                                                                                                                                                                                                                                             |
| 16     | SNF transition exemption - An exemption from the post-hospital requirement applies for this SNF stay or the qualifying stay dates are more than 30 days prior to the admission date                                                                                                                                                                                                                                                 |
| 17     | Patient is over 100 years old - Code indicates that the patient was over 100 years old at the date of admission.                                                                                                                                                                                                                                                                                                                    |
| 18     | Maiden name retained - A dependent spouse entitled to benefits who does not use her husband's last name.                                                                                                                                                                                                                                                                                                                            |
| 19     | Child retains mother's name - A patient who is a dependent child entitled to CHAMPVA benefits that does not have father's last name.                                                                                                                                                                                                                                                                                                |
| 20     | Bene requested billing - Provider realizes the services on this bill are at a noncovered level of care or otherwise excluded from coverage, but the bene has requested formal determination                                                                                                                                                                                                                                         |
| 21     | Billing for denial notice - The SNF or HHA realizes services are at a noncovered level of care or excluded, but requests a Medicare denial in order to bill medicaid or other insurer                                                                                                                                                                                                                                               |
| 22     | Patient on multiple drug regimen - A patient who is receiving multiple intravenous drugs while on home IV therapy                                                                                                                                                                                                                                                                                                                   |
| 23     | Homecaregiver available - The patient has a caregiver available to assist him or her during self-administration of an intravenous drug                                                                                                                                                                                                                                                                                              |
| 24     | Home IV patient also receiving HHA services - the patient is under care of HHA while receiving home IV drug therapy services                                                                                                                                                                                                                                                                                                        |
| 25     | Reserved for national assignment                                                                                                                                                                                                                                                                                                                                                                                                    |
| 26     | VA eligible patient chooses to receive services in Medicare certified facility rather than a VA facility (eff 3/92)                                                                                                                                                                                                                                                                                                                 |
| 27     | Patient referred to a sole community hospital for a diagnostic laborator test - (sole community hospital only) (eff 9/93)                                                                                                                                                                                                                                                                                                           |
| 28     | Patient and/or spouse's EGHP is secondary to Medicare - Qualifying EGHP for employers who have fewer than 20 employees (eff 9/93)                                                                                                                                                                                                                                                                                                   |
| 29     | Disabled beneficiary and/or family member's LGHP is secondary to Medicare - Qualifying LGHP for employer having fewer than 100 full and part-time employees                                                                                                                                                                                                                                                                         |
| 30     | Qualifying Clinical Trials - Non-research services provided to all patients, including managed care enrollees, enrolled in a Qualified Clinical Trial.                                                                                                                                                                                                                                                                              |
| 31     | Patient is student (full time - day) - Patient declares that he or she is enrolled as a full time day student.                                                                                                                                                                                                                                                                                                                      |
| 32     | Patient is student (cooperative/work study program)                                                                                                                                                                                                                                                                                                                                                                                 |
| 33     | Patient is student (full time - night) - Patient declares that he or she is enrolled as a full time night student.                                                                                                                                                                                                                                                                                                                  |
| 34     | Patient is student (part time) - Patient declares that he or she is enrolled as a part time student.                                                                                                                                                                                                                                                                                                                                |
| 36     | General care patient in a special unit - Patient is temporarily placed in special care unit bed because no general care beds were available.                                                                                                                                                                                                                                                                                        |
| 37     | Ward accommodation is patient's request - Patient is assigned to ward accommodations at patient's request.                                                                                                                                                                                                                                                                                                                          |
| 38     | Semi-private room not available - Indicates that either private or ward accommodations were assigned because semi-private accomodations were not available.                                                                                                                                                                                                                                                                         |
| 39     | Private room medically necessary - Patient needed a private room for medical reasons.                                                                                                                                                                                                                                                                                                                                               |
| 40     | Same day transfer - Patient transferred to another facility before midnight of the day of admission.                                                                                                                                                                                                                                                                                                                                |
| 41     | Partial hospitalization - Eff 3/92, indicates claim is for partial hospitalization services. For OP services, this includes a variety of psych programs.                                                                                                                                                                                                                                                                            |
| 42     | Continuing Care Not Related to Inpatient Admission - continuing care not related to the condition or diagnosis for which the beneficiary received inpatient hospital services (eff. 10/01)                                                                                                                                                                                                                                          |
| 43     | Continuing Care Not Provided Within Prescribed Postdischarge Window - continuing care was related to the inpatient admission but the prescribed care was not provided within the post-discharge window (eff. 10/01)                                                                                                                                                                                                                 |
| 44     | Inpatient Admission Changed to Outpatient - For use on outpatient claims only, when the physician ordered inpatient services, but upon internal review performed before the claim was initially submitted, the hospital determined the services did not meet its inpatient criteria (eff. 4/1/04)                                                                                                                                   |
| 45     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 46     | Nonavailability statement on file for CHAMPUS claim for nonemergency IP care for CHAMPUS bene residing within the catchment area (usually a 40 mile radius) of a uniform services hospital.                                                                                                                                                                                                                                         |
| 47     | Reserved for CHAMPUS.                                                                                                                                                                                                                                                                                                                                                                                                               |
| 48     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 49     | Product Replacement within Product Lifecycle-replacement of a product earlier than the anticipated lifecycle due to an indication that the product is not functioning properly (eff. 4/2006)                                                                                                                                                                                                                                        |
| 50     | Product Replacement for Known Recall of a Product - Manufacturer or FDA has identified the product for recall and therefore replacement (eff. 4/2006)                                                                                                                                                                                                                                                                               |
| 51     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 52     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 53     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 54     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 55     | SNF bed not available - The patient's SNF admission was delayed more than 30 days after hospital discharge because a SNF bed was not available.                                                                                                                                                                                                                                                                                     |
| 56     | Medical appropriateness - Patient's SNF admission was delayed more than 30 days after hospital discharge because physical condition made it inappropriate to begin active care within that period                                                                                                                                                                                                                                   |
| 57     | SNF readmission - Patient previously received Medicare covered SNF care within 30 days of the current SNF admission.                                                                                                                                                                                                                                                                                                                |
| 58     | Payment of SNF claims for beneficiaries disenrolling from terminating M+C plans plans who have not met the 3-day hospital stay requirement (eff. 10/1/00)                                                                                                                                                                                                                                                                           |
| 59     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 60     | Operating cost day outlier - PRICER indicates this bill is length of stay outlier (PPS)                                                                                                                                                                                                                                                                                                                                             |
| 61     | Operating cost cost outlier - PRICER indicates this bill is a cost outlier (PPS)                                                                                                                                                                                                                                                                                                                                                    |
| 62     | PIP bill - This bill is a periodic interim payment bill.                                                                                                                                                                                                                                                                                                                                                                            |
| 63     | PRO denial received before batch clearance report - The HCSSACL receipt date is used on PRO adjustment if the PRO's notification is before orig bill's acceptance report (Payer only code eff 9/93)                                                                                                                                                                                                                                 |
| 64     | Other than clean claim - The claim is not a 'clean claim'                                                                                                                                                                                                                                                                                                                                                                           |
| 65     | Non-PPS code - The bill is not a prospective payment system bill.                                                                                                                                                                                                                                                                                                                                                                   |
| 66     | Outlier not claimed - Bill may meet the criteria for cost outlier, but the hospital did not claim the cost outlier (PPS)                                                                                                                                                                                                                                                                                                            |
| 67     | Beneficiary elects not to use LTR days                                                                                                                                                                                                                                                                                                                                                                                              |
| 68     | Beneficiary elects to use LTR days                                                                                                                                                                                                                                                                                                                                                                                                  |
| 69     | Operating IME Payment Only - providers request for IME payment for each discharge of MCO enrollee, beginning 1/1/98, from teaching hospitals (facilities with approved medical residency training program); not stored in NCH. Exception: problem in startup year may have resulted in this special IME payment request being erroneously stored in NCH. If present, disregard claim as condition code '69' is not valid NCH claim. |
| 70     | Self-administered EPO - Billing is for a home dialysis patient who self administers EPO.                                                                                                                                                                                                                                                                                                                                            |
| 71     | Full care in unit - Billing is for a patient who received staff assisted dialysis services in a hospital or renal dialysis facility.                                                                                                                                                                                                                                                                                                |
| 72     | Self care in unit - Billing is for a patient who managed his own dialysis services without staff assistance in a hospital or renal dialysis facility.                                                                                                                                                                                                                                                                               |
| 73     | Self care training - Billing is for special dialysis services where the patient and helper (if necessary) were learning to perform dialysis.                                                                                                                                                                                                                                                                                        |
| 74     | Home - Billing is for a patient who received dialysis services at home.                                                                                                                                                                                                                                                                                                                                                             |
| 75     | Home 100% reimbursement - (not to be used for services after 4/15/90) The billing is for home dialsis patient using a dialysis machine that was purchased under the 100% program.                                                                                                                                                                                                                                                   |
| 76     | Back-up facility - Billing is for a patient who received dialysis services in a back-up facility.                                                                                                                                                                                                                                                                                                                                   |
| 77     | Provider accepts or is obligated/required due to contractual agreement or law to accept payment by a primary payer as payment in full - Medicare pays nothing.                                                                                                                                                                                                                                                                      |
| 78     | New coverage not implemented by HMO - eff 3/92, indicates newly covered service under Medicare for which HMO does not pay.                                                                                                                                                                                                                                                                                                          |
| 79     | CORF services provided off site - Code indicates that physical therapy, occupational therapy, or speech pathology services were provided off site.                                                                                                                                                                                                                                                                                  |
| 80     | Home Dialysis - Nursing Facility - Home dialysis furnished in a SNF or nursing facility. (eff. 4/4/05)                                                                                                                                                                                                                                                                                                                              |
| 81-99  | Reserved for state assignment.                                                                                                                                                                                                                                                                                                                                                                                                      |
| A0     | Special Zip Code Reporting - five digit zip code of the location from which the beneficiary is initially placed on board the ambulance (eff. 9/01)                                                                                                                                                                                                                                                                                  |
| A0     | CHAMPUS external partnership program special program indicator code (eff 10/93) (obsolete)                                                                                                                                                                                                                                                                                                                                          |
| A1     | EPSDT/CHAP - Early and periodic screening diagnosis and treatment special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                                        |
| A2     | Physically handicapped children's program - Services provided receive special funding through Title 8 of the Social Security Act or the CHAMPUS program for the handicapped. (eff 10/93)                                                                                                                                                                                                                                            |
| A3     | Special federal funding - Designed for uniform use by state uniform billing committees. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                  |
| A4     | Family planning - Designed for uniform use by state uniform billing committees. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                          |
| A5     | Disability - Designed for uniform use by state uniform billing committees. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                               |
| A6     | PPV/Medicare - Identifies that pneumococcal pneumonia 100% payment vaccine (PPV) services should be reimbursed under a special Medicare program provision. Special program indicator code (eff 10/93)                                                                                                                                                                                                                               |
| A7     | Induced abortion to avoid danger to woman's life. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                                                        |
| A8     | Induced abortion - Victim of rape/incest. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                                                                                                                |
| A9     | Second opinion surgery - Service requested to support second opinion on surgery. Part B deductible and coinsurance do not apply. Special program indicator code (eff 10/93)                                                                                                                                                                                                                                                         |
| AA     | Abortion Performed due to Rape (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                                                       |
| AB     | Abortion Performed due to Incest (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                                                     |
| AC     | Abortion Performed due to Serious Fetal Genetic Defect, Deformity or Abnormality (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                     |
| AD     | Abortion Performed due to a Life Endangering Physical Condition Caused by, arising from or exacerbated by the Pregnancy itself (eff. 10/1/02)                                                                                                                                                                                                                                                                                       |
| AE     | Abortion Performed due to physical health of mother that is not life endangering (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                     |
| AF     | Abortion Performed due to emotional/psychological health of mother (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                   |
| AG     | Abortion performed due to social economic reasons (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                                    |
| AH     | Elective Abortion (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                                                                    |
| AI     | Sterilization (eff. 10/1/02)                                                                                                                                                                                                                                                                                                                                                                                                        |
| AJ     | Payer Responsible for copayment (4/1/03)                                                                                                                                                                                                                                                                                                                                                                                            |
| AK     | Air Ambulance Required - For ambulance claims. Time needed to transport poses a threat. (eff. 10/16/03)                                                                                                                                                                                                                                                                                                                             |
| AL     | Specialized Treatment/bed Unavailable - For ambulance claims. Specialized treatment bed unavailable. Transported to alternate facility. (eff. 10/16/03)                                                                                                                                                                                                                                                                             |
| AM     | Non-emergency Medically Necessary Stretcher Transport Required - For ambulance claims. Non-emergency medically necessary stretcher transport required. (eff. 10/16/03)                                                                                                                                                                                                                                                              |
| AN     | Preadmission Screening Not Required - person meets the criteria for an exemption from preadmission screening. (eff. 1/1/04)                                                                                                                                                                                                                                                                                                         |
| B0     | Medicare Coordinated Care Demonstration Program - patient is a participant in a Medicare Coordinated Care Demonstration (eff. 10/01)                                                                                                                                                                                                                                                                                                |
| B1     | Beneficiary ineligible for demonstration program (eff. 1/02).                                                                                                                                                                                                                                                                                                                                                                       |
| B2     | Critical Access Hospital Ambulance Attestation - Attestation by CAH that it meets the criteria for exemption from the Ambulance Fee Schedule                                                                                                                                                                                                                                                                                        |
| B3     | Pregnancy Indicator - Indicates the patient is pregnant. Required when mandated by law. (eff. 10/16/03)                                                                                                                                                                                                                                                                                                                             |
| B4     | Admission Unrelated to Discharge - Admission unrelated to discharge on same day. This code is for discharges starting on January 1, 2004.                                                                                                                                                                                                                                                                                           |
| B5     | Special program indicator Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                         |
| B6     | Special program indicator Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                         |
| B7     | Special program indicator Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                         |
| B8     | Special program indicator Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                         |
| B9     | Special program indicator Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                         |
| C0     | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                                                                                                   |
| C1     | Approved as billed - The services provided for this billing period have been reviewed by the QIO/UR or intermediary and are fully approved including any day or cost outlier. (eff 10/93) NOTE: Beginning July 2005, this code is relevant to type of bills other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                     |
| C2     | Automatic approval as billed based on focused review. (No longer used for Medicare) QIO approval indicator services (eff 10/93) NOTE: Beginning July 2005, this code is relevant to type of bills other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                                                                               |
| C3     | Partial approval - The services provided for this billing period have been reviewed by the QIO/UR or intermediary and some portion has been denied (days or services). (eff 10/93) NOTE: Beginning July 2005, this code is relevant to type of bills other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                            |
| C4     | Admission/services denied - Indicates that all of the services were denied by the QIO/UR. QIO approval indicator services (eff 10/93) NOTE: Beginning July 2005, this code is relevant to types of bill other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                                                                         |
| C5     | Postpayment review applicable - QIO/UR review to take place after payment. QIO approval indicator services (eff 10/93) NOTE: Beginning July 2005, this code is relevant to types of bill other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                                                                                        |
| C6     | Admission preauthorization - The QIO/UR authorized this admission/service but has not reviewed the services provided. QIO approval indicator services (eff 10/93) NOTE: Beginning July 2005, this code is relevant to types of bill other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                                             |
| C7     | Extended authorization - the QIO has authorized these services for an extended length of time but has not reviewed the services provided. QIO approval indicator services (eff 10/93) NOTE: Beginning July 2005, this code is relevant to types of bill other than inpatient (18X, 21X, 22X, 32X, 33X, 34X, 75X, 81X, 82X).                                                                                                         |
| C8     | Reserved for national assignment. QIO approval indicator services (eff 10/93)                                                                                                                                                                                                                                                                                                                                                       |
| C9     | Reserved for national assignment. QIO approval indicator services (eff 10/93)                                                                                                                                                                                                                                                                                                                                                       |
| D0     | Changes to service dates. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                                              |
| D1     | Changes in charges. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                                                    |
| D2     | Changes in revenue codes/HCPCS/HIPPS Rate Code Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                         |
| D3     | Second or subsequent interim PPS bill. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                                 |
| D4     | Change in ICD-9-CM diagnosis and/or procedure code Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                     |
| D5     | Cancel only to correct a beneficiary claim account number or provider identification number. change condition (eff 10/93)                                                                                                                                                                                                                                                                                                           |
| D6     | Cancel only to repay a duplicate payment or OIG overpayment (includes cancellation of an OP bill containing services required to be included on the IP bill). Change condition eff 10/93.                                                                                                                                                                                                                                           |
| D7     | Change to make Medicare the secondary payer. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                           |
| D8     | Change to make Medicare the primary payer. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                             |
| D9     | Any other change. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                                                      |
| DR     | Disaster Relief (eff. 10/2005) - Code used to facilitate claims processing and track services and items provided to victims of Hurricane Katrina and any future disasters.                                                                                                                                                                                                                                                          |
| E0     | Change in patient status. Change condition (eff 10/93)                                                                                                                                                                                                                                                                                                                                                                              |
| EY     | National Emphysema Treatment Trial (NETT) or Lung Volume Reduction Surgery (LVRS) clinical study (eff. 11/97)                                                                                                                                                                                                                                                                                                                       |
| G0     | Multiple medical visits occur on the same day in the same revenue center but visits are distinct and constitute independent visits (allows for payment under outpatient PPS -- eff. 7/3/00).                                                                                                                                                                                                                                        |
| H0     | Delayed Filing, Statement of Intent Submitted -- statement of intent was submitted within the qualifying period to specifically identify the existence of another third party liability situation. (eff. 9/01)                                                                                                                                                                                                                      |
| M0     | All inclusive rate for outpatient services. (payer only code)                                                                                                                                                                                                                                                                                                                                                                       |
| M1     | Roster billed influenza virus vaccine. (payer only code) Eff 10/96, also includes pneumoccocal pneumonia vaccine (PPV)                                                                                                                                                                                                                                                                                                              |
| M2     | HH override code - home health total reimbursement exceeds the $150,000 cap or the number of total visits exceeds the 150 limitation. (eff 4/3/95) (payer only code)                                                                                                                                                                                                                                                                |
| W0     | United Mine Workers of America (UMWA) SNF demonstration indicator (eff 1/97); but no claims transmitted until 2/98)                                                                                                                                                                                                                                                                                                                 |
| XX     | Transgender/Hermaphrodite Beneficiaries (eff. 1/2/07)                                                                                                                                                                                                                                                                                                                                                                               |

## [Claim Related Condition Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Condition-Code-Sequence)

- Short SAS Name: `RLTCNDSQ`
- Long SAS Name: `RLT_COND_CD_SEQ`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The sequence number of the related institutional condition code for normal forms layout used in CCW.



## [Claim Related Occurrence Code](https://www.resdac.org/cms-data/variables/claim-related-occurrence-code)

- Short SAS Name: `OCRNC_CD`
- Long SAS Name: `CLM_RLT_OCRNC_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code that identifies a significant event relating to an institutional claim that may affect payer processing. These codes are claim-related occurrences that are related to a specific date.



<h3>Values</h3>

| Code       | Code Value        |
|:-----------|:------------------|
| 01 THRU 09 | Accident          |
| 10 THRU 19 | Medical condition |
| 20 THRU 39 | Insurance related |
| 40 THRU 69 | Service related   |
| A1-A3      | Miscellaneous     |

| Code    | Code Value                                                                                                                                                                                                                                                                                                                                              |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01      | Auto accident - The date of an auto accident.                                                                                                                                                                                                                                                                                                           |
| 02      | No-fault insurance involved, including auto accident/other - The date of an accident where the state has applicable no-fault liability laws, (i.e., legal basis for settlement without admission or proof of guilt).                                                                                                                                    |
| 03      | Accident/tort liability - The date of an accident resulting from a third party's action that may involve a civil court process in an attempt to require payment by the third party, other than no-fault liability.                                                                                                                                      |
| 04      | Accident/employment related - The date of an accident relating to the patient's employment.                                                                                                                                                                                                                                                             |
| 05      | Other accident - The date of an accident not described by the codes 01 thru 04.                                                                                                                                                                                                                                                                         |
| 06      | Crime victim - Code indicating the date on which a medical condition resulted from alleged criminal action committed by one or more parties.                                                                                                                                                                                                            |
| 07      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 08      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 11      | Onset of symptoms/illness - The date the patient first became aware of symptoms/illness.                                                                                                                                                                                                                                                                |
| 12      | Date of onset for a chronically dependent individual - Code indicates the date the patient/bene became a chronically dependent individual.                                                                                                                                                                                                              |
| 13      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 14      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 15      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 16      | Reserved for national assignment.                                                                                                                                                                                                                                                                                                                       |
| 17      | Date outpatient occupational therapy plan established or last reviewed - Code indicating the date an occupational therapy plan was established or last reviewed (eff 3/93)                                                                                                                                                                              |
| 18      | Date of retirement (patient/bene) - Code indicates the date of retirement for the patient/bene.                                                                                                                                                                                                                                                         |
| 19      | Date of retirement spouse - Code indicates the date of retirement for the patient's spouse.                                                                                                                                                                                                                                                             |
| 20      | Guarantee of payment began - The date on which the provider began claiming Medicare payment under the guarantee of payment provision.                                                                                                                                                                                                                   |
| 21      | UR notice received - Code indicating the date of receipt by the hospital & SNF of the UR committee's finding that the admission or future stay was not medically necessary.                                                                                                                                                                             |
| 22      | Active care ended - The date on which a covered level of care ended in a SNF or general hospital, or date active care ended in a psychiatric or tuberculosis hospital or date on which patient was released on a trial basis from a residential facility. Code is not required if code "21" is used.                                                    |
| 23      | Cancellation of Hospice benefits - The date the RHHI cancelled the hospice benefit. (eff. 10/00). NOTE: this will be different than the revocation of the hospice benefit by beneficiaries. Benefits exhausted - The last date for which benefits can be paid. (term 9/30/93; replaced by code A3)                                                      |
| 24      | Date insurance denied - The date the insurer's denial of coverage was received by a higher priority payer.                                                                                                                                                                                                                                              |
| 25      | Date benefits terminated by primary payer - The date on which coverage (including worker's compensation benefits or no-fault coverage) is no longer available to the patient.                                                                                                                                                                           |
| 26      | Date skilled nursing facility (SNF) bed available - The date on which a SNF bed became available to a hospital inpatient who required only SNF level of care.                                                                                                                                                                                           |
| 27      | Date of Hospice Certification or Re-Certification -- code indicates the date of certification or recertification of the hospice benefit period, beginning with the first two initial benefit periods of 90 days each and the subsequent 60-day benefit periods. (eff. 9/01)                                                                             |
| 27      | Date home health plan established or last reviewed - Code indicating the date a home health plan of treatment was established or last reviewed. (Obsolete) not used by hospital unless owner of facility                                                                                                                                                |
| 28      | Date comprehensive outpatient rehabilitation plan established or last reviewed - Code indicating the date a comprehensive outpatient rehabilitation plan was established or last reviewed. not used by hospital unless owner of facility                                                                                                                |
| 29      | Date OPT plan established or last reviewed - the date a plan of treatment was established for outpatient physical therapy. Not used by hospital unless owner of facility                                                                                                                                                                                |
| 30      | Date speech pathology plan treatment established or last reviewed - The date a speech pathology plan of treatment was established or last reviewed. Not used by hospital unless owner of facility                                                                                                                                                       |
| 31      | Date bene notified of intent to bill (accommodations) - The date of the notice provided to the patient by the hospital stating that he no longer required a covered level of IP care.                                                                                                                                                                   |
| 32      | Date bene notified of intent to bill (procedures or treatment) - The date of the notice provided to the patient by the hospital stating requested care (diagnostic procedures or treatments) is not considered reasonable or necessary.                                                                                                                 |
| 33      | First day of the Medicare coordination period for ESRD bene - During which Medicare benefits are secondary to benefits payable under an EGHP. Required only for ESRD beneficiaries.                                                                                                                                                                     |
| 34      | Date of election of extended care facilities - The date the guest elected to receive extended care services (used by Religious Nonmedical Health Care Institutions only).                                                                                                                                                                               |
| 35      | Date treatment started for physical therapy - Code indicates the date services were initiated by the billing provider for physical therapy.                                                                                                                                                                                                             |
| 36      | Date of discharge for the IP hospital stay when patient received a transplant procedure - Hospital is billing for immunosuppressive drugs.                                                                                                                                                                                                              |
| 37      | The date of discharge for the IP hospital stay when patient received a noncovered transplant procedure - Hospital is billing for immunosuppresive drugs.                                                                                                                                                                                                |
| 38      | Date treatment started for home IV therapy - Date the patient was first treated in his home for IV therapy.                                                                                                                                                                                                                                             |
| 39      | Date discharged on a continuous course of IV therapy - Date the patient was discharged from the hospital on a continuous course of IV therapy.                                                                                                                                                                                                          |
| 40      | Scheduled date of admission - The date on which a patient will be admitted as an inpatient to the hospital. (This code may only be used on an outpatient claim.)                                                                                                                                                                                        |
| 41      | Date of First Test for Pre-admission Testing - The date on which the first outpatient diagnostic test was performed as part of a pre-admission testing (PAT) program. This code may only be used if a date of admission was scheduled prior to the administration of the test(s). (eff. 10/01)                                                          |
| 42      | Date of discharge/termination of hospice care - for the final bill for hospice care. Eff 5/93, definition revised to apply only to date patient revoked hospice election.                                                                                                                                                                               |
| 43      | Scheduled Date of Canceled Surgery - date which ambulatory surgery was scheduled. (eff. 9/01)                                                                                                                                                                                                                                                           |
| 44      | Date treatment started for occupational therapy - Code indicates the date services were initiated by the billing provider for occupational therapy.                                                                                                                                                                                                     |
| 45      | Date treatment started for speech therapy - Code indicates the date services were initiated by the billing provider for speech therapy.                                                                                                                                                                                                                 |
| 46      | Date treatment started for cardiac rehabilitation - Code indicates the date services were initiated by the billing provider for cardiac rehabilitation.                                                                                                                                                                                                 |
| 47      | Date Cost Outlier Status Begins - code indicates that this is the first day the cost outlier threshold is reached. For Medicare purposes, a bene must have regular coinsurance and/or lifetime reserve days available beginning on this date to allow coverage of additional daily charges for the purpose of making cost outlier payments. (eff. 9/01) |
| 48      | Payer code - Code reserved for internal use only by third party payers. HCFA assigns as needed for your use. Providers will not report it.                                                                                                                                                                                                              |
| 49      | Payer code - Code reserved for internal use only by third party payers. HCFA assigns as needed for your use. Providers will not report it.                                                                                                                                                                                                              |
| 50 - 69 | Reserved for state assignment                                                                                                                                                                                                                                                                                                                           |
| A1      | Birthdate, Insured A - The birthdate of the individual in whose name the insurance is carried. (Eff 10/93)                                                                                                                                                                                                                                              |
| A2      | Effective date, Insured A policy - A code indicating the first date insurance is in force. (eff 10/93)                                                                                                                                                                                                                                                  |
| A3      | Benefits exhausted - Code indicating the last date for which benefits are available and after which no payment can be made to payer A. (eff 10/93)                                                                                                                                                                                                      |
| B1      | Birthdate, Insured B - The birthdate of the individual in whose name the insurance is carried. (eff 10/93)                                                                                                                                                                                                                                              |
| B2      | Effective date, Insured B policy - A code indicating the first date insurance is in force. (eff 10/93)                                                                                                                                                                                                                                                  |
| B3      | Benefits exhausted - code indicating the last date for which benefits are available and after which no payment can be made to payer B. (eff 10/93)                                                                                                                                                                                                      |
| C1      | Birthdate, Insured C - The birthdate of the individual in whose name the insurance is carried. (eff 10/93)                                                                                                                                                                                                                                              |
| C2      | Effective date, Insured C policy - A code indicating the first date insurance is in force. (eff 10/93)                                                                                                                                                                                                                                                  |
| C3      | Benefits exhausted - Code indicating the last date for which benefits are available and after which no payment can be made to payer C. (eff 10/93)                                                                                                                                                                                                      |

## [Claim Related Occurrence Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Occurrence-Code-Sequence)

- Short SAS Name: `RLTOCRSQ`
- Long SAS Name: `RLT_OCRNC_CD_SEQ`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The sequence number of the related institutional occurrence code for normal forms layout used in CCW.



## [Claim Related Occurrence Date](https://www.resdac.org/cms-data/variables/Claim-Related-Occurrence-Date)

- Short SAS Name: `OCRNCDT`
- Long SAS Name: `CLM_RLT_OCRNC_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The date associated with a significant event related to an institutional claim that may affect payer processing.



## [Claim Related Span Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Span-Code-Sequence)

- Short SAS Name: `RLTSPNSQ`
- Long SAS Name: `RLT_SPAN_CD_SEQ`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The sequence number of the related institutional span code for normal forms layout used in CCW.



## [Claim Related Value Code Sequence](https://www.resdac.org/cms-data/variables/Claim-Related-Value-Code-Sequence)

- Short SAS Name: `RLTVALSQ`
- Long SAS Name: `RLT_VAL_CD_SEQ`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The sequence number of the related institutional value code for normal forms layout used in CCW.



## [Claim Rendering Physician NPI Number](https://www.resdac.org/cms-data/variables/claim-rendering-physician-npi-number)

- Short SAS Name: `RNDRNG_PHYSN_NPI`
- Long SAS Name: `CLM_RNDRNG_PHYSN_NPI_NUM`

<h3>Variable Names</h3>

| Dataset    | 2013               | 2012               | 2011               | 2010               |
|:-----------|:-------------------|:-------------------|:-------------------|:-------------------|
| Outpatient | `rndrng_physn_npi` | `rndrng_physn_npi` | `rndrng_physn_npi` | `rndrng_physn_npi` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

This variable is the National Provider Identifier (NPI) for the physician who rendered the services. NPIs replaced UPINs as the standard provider identifiers beginning in 2007. The UPIN is almost never populated after 2009. 

CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available in the NCH. After the 5/07 NPI implementation, the standard system maintainers will add the legacy number to the claim when it is adjudicated. We will continue to receive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no new UPINs (legacy numbers) will be generated for new physicians (Part B and outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.



## [Claim Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/claim-rendering-physician-specialty-code)

- Short SAS Name: `RNDRNG_PHYSN_SPCLTY_CD`
- Long SAS Name: `CLM_RNDRNG_PHYSN_SPCLTY_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the CMS specilty code of the rendering physician/practitioner. 



<h3>Values</h3>

| Code   | Code Value                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00     | Carrier wide                                                                                                                                            |
| 01     | General practice                                                                                                                                        |
| 02     | General surgery                                                                                                                                         |
| 03     | Allergy/immunology                                                                                                                                      |
| 04     | Otolaryngology                                                                                                                                          |
| 05     | Anesthesiology                                                                                                                                          |
| 06     | Cardiology                                                                                                                                              |
| 07     | Dermatology                                                                                                                                             |
| 08     | Family practice                                                                                                                                         |
| 09     | Interventional Pain Management (IPM) (eff. 4/1/03)                                                                                                      |
| 10     | Gastroenterology                                                                                                                                        |
| 11     | Internal medicine                                                                                                                                       |
| 12     | Osteopathic manipulative therapy                                                                                                                        |
| 13     | Neurology                                                                                                                                               |
| 14     | Neurosurgery                                                                                                                                            |
| 15     | Speech/language pathology                                                                                                                               |
| 16     | Obstetrics/gynecology                                                                                                                                   |
| 17     | Hospice and Palliative Care                                                                                                                             |
| 18     | Ophthalmology                                                                                                                                           |
| 19     | Oral surgery (dentists only)                                                                                                                            |
| 20     | Orthopedic surgery                                                                                                                                      |
| 21     | Cardiac Electrophysiology                                                                                                                               |
| 22     | Pathology                                                                                                                                               |
| 24     | Plastic and reconstructive surgery                                                                                                                      |
| 25     | Physical medicine and rehabilitation                                                                                                                    |
| 26     | Physchiatry                                                                                                                                             |
| 27     | General Psychiatry                                                                                                                                      |
| 28     | Colorectal surgery (formerly proctology)                                                                                                                |
| 29     | Pulmonary disease                                                                                                                                       |
| 30     | Diagnostic radiology                                                                                                                                    |
| 31     | Intensive cardiac rehabilitation                                                                                                                        |
| 32     | Anesthesiologist Assistants (eff. 4/1/03--previously grouped with Certified Registered Nurse Anesthetists (CRNA))                                       |
| 33     | Thoracic surgery                                                                                                                                        |
| 34     | Urology                                                                                                                                                 |
| 35     | Chiropractic                                                                                                                                            |
| 36     | Nuclear medicine                                                                                                                                        |
| 37     | Pediatric medicine                                                                                                                                      |
| 38     | Geriatric medicine                                                                                                                                      |
| 39     | Nephrology                                                                                                                                              |
| 40     | Hand surgery                                                                                                                                            |
| 41     | Optometrist                                                                                                                                             |
| 42     | Certified nurse midwife                                                                                                                                 |
| 43     | Certified Registered Nurse Anesthetist (CRNA) (Anesthesiologist Assistants were removed from this specialty 4/1/03)                                     |
| 44     | Infectious disease                                                                                                                                      |
| 45     | Mammography screening center                                                                                                                            |
| 46     | Endocrinology                                                                                                                                           |
| 47     | Independent Diagnostic Testing Facility (IDTF)                                                                                                          |
| 48     | Podiatry                                                                                                                                                |
| 49     | Ambulatory surgical center (formerly miscellaneous)                                                                                                     |
| 50     | Nurse practitioner                                                                                                                                      |
| 51     | Medical supply company with certified orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                            |
| 52     | Medical supply company with certified prosthetist (certified by American Board for Certification in Prosthetics and Orthotics)                          |
| 53     | Medical supply company with certified prosthetist-orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                |
| 54     | Medical supply company for DMERC (and not included in 51-53)                                                                                            |
| 55     | Individual certified orthotist                                                                                                                          |
| 56     | Individual certified prosthetist                                                                                                                        |
| 57     | Individual certified prosthetist-orthotist                                                                                                              |
| 58     | Medical supply company with registered pharmacist                                                                                                       |
| 59     | Ambulance service supplier, (e.g., private ambulance companies, funeral homes, etc.)                                                                    |
| 60     | Public Health or welfare agencies (federal, state, and local)                                                                                           |
| 61     | Voluntary health or charitable agencies (e.g. National Cancer Society, National Heart Association, Catholic Charities)                                  |
| 62     | Psychologist (billing independently)                                                                                                                    |
| 63     | Portable X-ray supplier                                                                                                                                 |
| 64     | Audiologist (billing independently)                                                                                                                     |
| 65     | Physical therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                            |
| 66     | Rheumatology                                                                                                                                            |
| 67     | Occupational therapist (private practice added 4/103) (independently practicing removed 4/1/03)                                                         |
| 68     | Clinical psychologist                                                                                                                                   |
| 69     | Clinical laboratory (billing independently)                                                                                                             |
| 70     | Multispecialty clinic or group practice                                                                                                                 |
| 71     | Registered Dietician/Nutrition Professional (eff.1/1/02)                                                                                                |
| 72     | Pain Management (eff. 1/1/02)                                                                                                                           |
| 73     | Mass Immunization Roster Biller                                                                                                                         |
| 74     | Radiation Therapy Centers (prior to 4/2003 this included Independent Diagnostic Testing Facilities (IDFT))                                              |
| 75     | Slide Preparation Facilities (added to differentiate them from Independent Diagnostic Testing Facilities (IDTFs--eff. 4//1/03))                         |
| 76     | Peripheral vascular disease                                                                                                                             |
| 77     | Vascular surgery                                                                                                                                        |
| 78     | Cardiac surgery                                                                                                                                         |
| 79     | Addiction medicine                                                                                                                                      |
| 80     | Licensed clinical social worker                                                                                                                         |
| 81     | Critical care (intensivists)                                                                                                                            |
| 82     | Hematology                                                                                                                                              |
| 83     | Hematology/oncology                                                                                                                                     |
| 84     | Preventive medicine                                                                                                                                     |
| 85     | Maxillofacial surgery                                                                                                                                   |
| 86     | Neuropsychiatry                                                                                                                                         |
| 87     | All other suppliers (e.g. drug and department stores)                                                                                                   |
| 88     | Unknown supplier/provider specialty                                                                                                                     |
| 89     | Certified clinical nurse specialist                                                                                                                     |
| 90     | Medical oncology                                                                                                                                        |
| 91     | Surgical oncology                                                                                                                                       |
| 92     | Radiation oncology                                                                                                                                      |
| 93     | Emergency medicine                                                                                                                                      |
| 94     | Interventional radiology                                                                                                                                |
| 95     | Competitive Acquisition Program (CAP) Vendor (eff. 07/01/06). Prior to 07/01/06, known as Independent physiological laboratory                          |
| 96     | Optician                                                                                                                                                |
| 97     | Physician assistant                                                                                                                                     |
| 98     | Gynecologist/oncologist                                                                                                                                 |
| 99     | Unknown physician specialty                                                                                                                             |
| A0     | Hospital (DMERCs only)                                                                                                                                  |
| A1     | SNF (DMERCs only)                                                                                                                                       |
| A2     | Intermediate care nursing facility (DMERCs only)                                                                                                        |
| A3     | Nursing facility, other (DMERCs only)                                                                                                                   |
| A4     | Home Health Agency (DMERCs only)                                                                                                                        |
| A5     | Pharmacy (DMERC)                                                                                                                                        |
| A6     | Medical supply company with respiratory therapist (DMERCs only)                                                                                         |
| A7     | Department store (DMERC)                                                                                                                                |
| A8     | Grocery store (DMERC)                                                                                                                                   |
| A9     | Indian Health Service (IHS), tribe and tribal organizations (non-hospital or non-hospital based facilities, eff. 1/2005)                                |
| B1     | Supplier of oxygen and/or oxygen related equipment (eff. 10/2/07)                                                                                       |
| B2     | Pedorthic Personnel (eff. 10/2/07)                                                                                                                      |
| B3     | Medical Supply Company with pedorthic personnel (eff. 10/2/07)                                                                                          |
| B4     | Does not meet definition of health care provider (e.g., Rehabilitation agency, organ procurement organizations, histocompatibility labs) (eff. 10/2/07) |
| B5     | Ocularist                                                                                                                                               |
| C0     | Sleep medicine                                                                                                                                          |
| C1     | Centralized flu                                                                                                                                         |
| C2     | Indirect payment procedure                                                                                                                              |
| C3     | Interventional cardiology                                                                                                                               |
| C5     | Dentist (eff. 7/2016)                                                                                                                                   |

## [Claim Service Classification Type Code](https://www.resdac.org/cms-data/variables/Claim-Service-classification-Type-Code)

- Short SAS Name: `TYPESRVC`
- Long SAS Name: `CLM_SRVC_CLSFCTN_TYPE_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The second digit of the type of bill (TOB2) submitted on an institutional claim record to indicate the classification of the type of service provided to the beneficiary.



<h3>Values</h3>

For facility type code 1 thru 6, and 9

| Code   | Code Value                                                                                                                                                                                                                                                     |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Inpatient (including Part A)                                                                                                                                                                                                                                   |
| 2      | Hospital based or Inpatient (Part B only) or home health visits under Part B                                                                                                                                                                                   |
| 3      | Outpatient (HHA-A also)                                                                                                                                                                                                                                        |
| 4      | Other (Part B) -- (Includes HHA medical and other health services not under a plan of treatment, hospital or SNF for diagnostic clinical laboratory services for "nonpatients," and referenced diagnostic services. For HHAs under PPS, indicates an osteoporo |
| 5      | Intermediate care - level I                                                                                                                                                                                                                                    |
| 6      | Intermediate care - level II                                                                                                                                                                                                                                   |
| 7      | Subacute Inpatient (revenue code 019X required) (formerly Intermediate care - level III) NOTE: 17X & 27X are discontinued effective 10/1/05.                                                                                                                   |
| 8      | Swing beds (used to indicate billing for SNF level of care in a hospital with an approved swing bed agreement)                                                                                                                                                 |
| 9      | Reserved for national assignment                                                                                                                                                                                                                               |

For facility type code 7

| Code   | Code Value                                                                                                             |
|:-------|:-----------------------------------------------------------------------------------------------------------------------|
| 1      | Rural Health Clinic (RHC)                                                                                              |
| 2      | Hospital based or independent renal dialysis facility                                                                  |
| 3      | Free-standing provider based federally qualified health center (FQHC) (eff 10/91)                                      |
| 4      | Other Rehabilitation Facility (ORF) and Community Mental Health Center (CMHC) (eff 10/91 - 3/97); ORF only (eff. 4/97) |
| 5      | Comprehensive Rehabilitation Center (CORF)                                                                             |
| 6      | Community Mental Health Center (CMHC) (eff 4/97)                                                                       |
| 7-8    | Reserved for national assignment                                                                                       |
| 9      | Other                                                                                                                  |

For facility type code 8

| Code   | Code Value                                                                              |
|:-------|:----------------------------------------------------------------------------------------|
| 1      | Hospice (non-hospital based)                                                            |
| 2      | Hospice (hospital based)                                                                |
| 3      | Ambulatory surgical center in hospital outpatient department                            |
| 4      | Freestanding birthing center                                                            |
| 5      | Critical Access Hospital (eff. 10/99) formerly Rural primary care hospital (eff. 10/94) |
| 6-8    | Reserved for national use                                                               |
| 9      | Other                                                                                   |

## [Claim Short Stay Outlier (SSO) Standard Payment Amount](https://www.resdac.org/cms-data/variables/claim-short-stay-outlier-sso-standard-payment-amount)

- Short SAS Name: `CLM_SS_OUTLIER_STD_PYMT_AMT `
- Long SAS Name: `CLM_SS_OUTLIER_STD_PYMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This variable is the standard payment amount for long-term care hospitals (LTCH) under the Medicare prospective payment system (PPS), which is based on the MS-LTC-DRG with the short stay outlier (SSO) adjustment.   

This amount does not include any other applicable outlier payment amount.

Applies only to Inpatient (LTCH) claims.  This field is new in October 2015. 

For a LTCH PPS claim, only one of four fields will be populated (CLM_SITE_NTRL_PYMT_CST_AMT, CLM_SITE_NTRL_PYMT_IPPS_AMT, CLM_FULL_STD_PYMT_AMT, or CLM_SS_OUTLIER_STD_PYMT_AMT) as they are mutually exclusive (i.e., only one of the 4 fields will have a non-zero value). The field with the non-zero value is included in the Claim Payment Amount field.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Site Neutral Payment Based on Cost Amount](https://www.resdac.org/cms-data/variables/claim-site-neutral-payment-based-cost-amount)

- Short SAS Name: `CLM_SITE_NTRL_PYMT_CST_AMT`
- Long SAS Name: `CLM_SITE_NTRL_PYMT_CST_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Under the Long Term Care Hospital (LTCH) prospective payment system (PPS), the payment amount based on estimated cost of the case.

Applies only to Inpatient (LTCH) claims. This field is new in October 2015.
For a LTCH PPS claim, only one of four fields will be populated (CLM_SITE_NTRL_PYMT_CST_AMT, CLM_SITE_NTRL_PYMT_IPPS_AMT, CLM_FULL_STD_PYMT_AMT, or CLM_SS_OUTLIER_STD_PYMT_AMT) as they are mutually exclusive (i.e., only one of the 4 fields will have a non-zero value). The field with the non-zero value is included in the Claim Payment Amount field.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Site Neutral Payment Based on inpatient prospective payment system (IPPS) Amounts](https://www.resdac.org/cms-data/variables/claim-site-neutral-payment-based-inpatient-prospective-payment-system-ipps)

- Short SAS Name: `CLM_SITE_NTRL_PYMT_IPPS_AMT`
- Long SAS Name: `CLM_SITE_NTRL_PYMT_IPPS_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Under the Long Term Care Hospital (LTCH) prospective payment system (PPS), the payment amount based on the inpatient prospective payment system (IPPS) comparable amount. This amount does not include any applicable outlier payment amount.

Applies only to Inpatient (LTCH) claims. This field is new in October 2015.
For a LTCH PPS claim, only one of four fields will be populated (CLM_SITE_NTRL_PYMT_CST_AMT, CLM_SITE_NTRL_PYMT_IPPS_AMT, CLM_FULL_STD_PYMT_AMT, or CLM_SS_OUTLIER_STD_PYMT_AMT) as they are mutually exclusive (i.e., only one of the 4 fields will have a non-zero value). The field with the non-zero value is included in the Claim Payment Amount field.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Source Inpatient Admission Code](https://www.resdac.org/cms-data/variables/Claim-Source-Inpatient-Admission-Code)

- Short SAS Name: `SRC_ADMS`
- Long SAS Name: `CLM_SRC_IP_ADMSN_CD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `src_adms` | `src_adms` | `src_adms` | `src_adms` | `src_adms` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `src_adms` | `src_adms` | `src_adms` | `src_adms` | `src_adms` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `src_adms` | `src_adms` | `madmsrce` | `madmsrce` | `madmsrce` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The code indicating the source of the referral for the admission or visit.



<h3>Values</h3>

For Inpatient/SNF Claims:

| Code   | Code Value                                                                                                                                                                                                                                          |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | ANOMALY: invalid value, if present, translate to '9'                                                                                                                                                                                                |
| 1      | Non-Health Care Facility Point of Origin (Physician Referral) - The patient was admitted to this facility upon an order of a physician.                                                                                                             |
| 2      | Clinic referral - The patient was admitted upon the recommendation of this facility's clinic physician.                                                                                                                                             |
| 3      | HMO referral - Reserved for national assignment. (eff. 3/08) Prior to 3/08, HMO referral - The patient was admitted upon the recommendation of a health maintenance organization (HMO) physician.                                                   |
| 4      | Transfer from hospital (Different Facility) - The patient was admitted to this facility as a hospital transfer from an acute care facility where he or she was an inpatient.                                                                        |
| 5      | Transfer from a skilled nursing facility (SNF) or Intermediate Care Facility (ICF) - The patient was admitted to this facility as a transfer from a SNF or ICF where he or she was a resident.                                                      |
| 6      | Transfer from another health care facility - The patient was admitted to this facility as a transfer from another type of health care facility not defined elsewhere in this code list where he or she was an inpatient.                            |
| 7      | Emergency room - The patient was admitted to this facility after receiving services in this facility's emergency room department. (Obsolete - eff. 7/1/10)                                                                                          |
| 8      | Court/law enforcement - The patient was admitted upon the direction of a court of law or upon the request of a law enforcement agency's representative.                                                                                             |
| 9      | Information not available - The means by which the patient was admitted is not known.                                                                                                                                                               |
| A      | Reserved for National Assignment. (eff. 3/08) Prior to 3/08 defined as: Transfer from a Critical Access Hospital - patient was admitted/referred to this facility as a transfer from a Critical Access Hospital.                                    |
| B      | Transfer from Another Home Health Agency - The patient was admitted to this home health agency as a transfer from another home health agency. (Discontinued July 1, 2010- See Condition Code 47)                                                    |
| C      | Readmission to Same Home Health Agency - The patient was readmitted to this home health agency within the same home health episode period. (Discontinued July 1, 2010)                                                                              |
| D      | Transfer from hospital inpatient in the same facility resulting in a separate claim to the payer - The patient was admitted to this facility as a transfer from hospital inpatient within this facility resulting in a separate claim to the payer. |
| E      | Transfer from Ambulatory Surgical Center - The patient was admitted to this facility as a transfer from an ambulatory surgery center. (eff. 10/1/2007)                                                                                              |
| F      | Transfer from Hospice and is under a Hospice Plan of Care or Enrolled in a Hospice Program - The patient was admitted to this facility as a transfer from a hospice. (eff. 10/1/2007)                                                               |

For Newborn Type of Admission: 

| Code   | Code Value                                                                                                                        |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------|
| 1      | Normal delivery - A baby delivered without complications. (Obsolete eff. 10/1/07)                                                 |
| 2      | Premature delivery - A baby delivered with time and/or weight factors qualifying it for premature status. (Obsolete eff. 10/1/07) |
| 3      | Sick baby - A baby delivered with medical complications, other than those relating to premature status. (Obsolete eff. 10/1/07)   |
| 4      | Extramural birth - A baby delivered in a non-sterile environment. (Obsolete eff. 10/1/07)                                         |
| 5      | Born Inside this Hospital (eff. 10/1/07)                                                                                          |
| 6      | Born Outside of This Hospital (eff. 10/1/07)                                                                                      |
| 7-9    | Reserved for national assignment.                                                                                                 |

## [Claim Through Date](https://www.resdac.org/cms-data/variables/Claim-Through-Date)

- Short SAS Name: `THRU_DT`
- Long SAS Name: `CLM_THRU_DT`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    |           | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` |
| Inpatient  | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` |
| Inpatient  | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` |
| Outpatient | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` | `thru_dt` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    | `thru_dt` | `thru_dt` | `thru_dt` | `sthrudt` | `sthrudt` |
| Inpatient  | `thru_dt` | `thru_dt` | `thru_dt` | `sthrudt` | `sthrudt` |
| Inpatient  | `thru_dt` | `thru_dt` | `thru_dt` | `srev_dt` | `srev_dt` |
| Outpatient | `thru_dt` | `thru_dt` | `thru_dt` | `sthrudt` | `sthrudt` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    | `sthrudt` | `sthrudt` | `thru_dt` | `thru_dt` | `bthrudt` |
| Inpatient  | `sthrudt` | `sthrudt` | `thru_dt` | `thru_dt` | `thru_dt` |
| Inpatient  | `srev_dt` | `srev_dt` | `rev_dt`  | `rev_dt`  | `rev_dt`  |
| Outpatient | `sthrudt` | `sthrudt` | `sthrudt` | `thru_dt` | `thru_dt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The last day on the billing statement covering services rendered to the beneficiary (a.k.a 'Statement Covers Thru Date').

NOTE: For Home Health PPS claims, the 'from' date and the 'thru' date on the RAP (initial claim) must always match.



## [Claim Total Charge Amount](https://www.resdac.org/cms-data/variables/Claim-Total-Charge-Amount)

- Short SAS Name: `TOT_CHRG`
- Long SAS Name: `CLM_TOT_CHRG_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |
| Outpatient | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |
| Outpatient | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |
| Outpatient | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` | `tot_chrg` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version G, the total charges for all services included on the institutional claim. This field is redundant with revenue center code 0001/total charges.

??? limitation
	DESCRIPTION :
	The total charge amount field in the fixed portion was
	truncated on outpatient, hospice and home health claims.
	BACKGROUND :
	For outpatient, hospice and home health claims, the
	total charge amount field in the fixed portion was
	truncated (the cents were dropped off; the decimal
	point was moved, making cents out of dollars) in the
	CWFMQA process beginning with data received from CWF
	1/4/99 through 5/14/99. The problem occurred when
	CWF increased the size of the field.
	CORRECTIVE ACTION :
	The CWFMQA front-end was fixed. The Nearline was patched during the quarterly merge in 7/99 for service years 1998 and 1999. The NCH_PACTCH_CD field will be populated with a value '11'. The 1998 and 1999 SAFs were corrected when finalized in 7/99. The patch involved moving the total charge amount in the revenue center trailer to the total charge amount field in the fixed portion, for records with NCH Daily Process Date 1/4/99 - 5/14/99.
	

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Total PPS Capital Amount](https://www.resdac.org/cms-data/variables/Claim-Total-PPS-Capital-Amount)

- Short SAS Name: `PPS_CPTL`
- Long SAS Name: `CLM_TOT_PPS_CPTL_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `pps_cptl` | `pps_cptl` | `pps_cptl` | `pps_cptl` | `pps_cptl` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `pps_cptl` | `pps_cptl` | `pps_cptl` | `pps_cptl` | `pps_cptl` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `pps_cptl` | `pps_cptl` | `mppscamt` | `mppscamt` | `mppscamt` |

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

The total amount that is payable for capital PPS for the claim. This is the sum of the capital hospital specific portion, federal specific portion, outlier portion, disproportionate share portion, indirect medical education portion, exception payments, and hold harmless payments.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Treatment Authorization Number](https://www.resdac.org/cms-data/variables/claim-treatment-authorization-number)

- Short SAS Name: `CLM_TRTMT_AUTHRZTN_NUM `
- Long SAS Name: `CLM_TRTMT_AUTHRZTN_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

The number assigned by the medical reviewer and reported by the provider to identify the medical review (treatment authorization) action taken after review of the beneficiary's case. It designates that treatment covered by the bill has been authorized by the payer.

This number is used by the fiscal intermediary and the Peer Review Organization.



<h3>Values</h3>

| Code    |
|:--------|
| XXXXXXX |

## [Claim Uncompensated Care Payment Amount](https://www.resdac.org/cms-data/variables/claim-uncompensated-care-payment-amount)

- Short SAS Name: `CLM_UNCOMPD_CARE_PMT_AMT `
- Long SAS Name: `CLM_UNCOMPD_CARE_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field identifies the payment for disproportionate share hospitals (DSH).  It represents the uncompensated care amount of the payment.

This field applies only to inpatient claims. These payments were authorized as part of Section 3133 of the Affordable Care Act (ACA).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Utilization Day Count](https://www.resdac.org/cms-data/variables/Claim-Utilization-Day-Count)

- Short SAS Name: `UTIL_DAY`
- Long SAS Name: `CLM_UTLZTN_DAY_CNT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `util_day` | `util_day` | `util_day` | `util_day` | `util_day` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `util_day` | `util_day` | `util_day` | `util_day` | `util_day` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `util_day` | `util_day` | `util_day` | `util_day` | `util_day` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

On an institutional claim, the number of covered days of care that are chargeable to Medicare facility utilization that includes full days, coinsurance days, and lifetime reserve days. It excludes any days classified as non-covered, leave of absence days, and the day of discharge or death.



## [Claim VBP Adjustment Percent](https://www.resdac.org/cms-data/variables/claim-vbp-adjustment-percent)

- Short SAS Name: `CLM_VBP_ADJSTMT_PCT `
- Long SAS Name: `CLM_VBP_ADJSTMT_PCT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Under the Hospital Value Based Purchasing (HVBP) program, an adjustment is made to the base operating DRG amount for certain Inpatient Prospective Payment System (IPPS) hospitals - based on their Total Performance Score (TPS).

This initiative began in 4th Quarter of 2013 (i.e., beginning of Federal fiscal year 14 [FY14]).   

This field was new in 2013, and is null/missing for all previous years. The HVBP applies only to subsection (d) IPPS hospitals. There is a variable that indicates whether the hospital was excluded from HVBP (see CLM_VBP_PRTCPNT_IND_CD). This percentage reduction is applied  to the base operating DRG amount, depending on their TPS (which is the Value Based Purchasing Score), as required by the Affordable Care Act (ACA). The percentages change each FY.  

Additional information is available on the CMS "Hospital Value-Based Purchasing" website. 

The actual dollar amount of the adjustment that applied to the claim is found in the variable called CLM_VBP_ADJSTMT_PMT_AMT.



<h3>Values</h3>

| Code   |
|:-------|
| X.XX   |

## [Claim Value Amount](https://www.resdac.org/cms-data/variables/Claim-Value-Amount)

- Short SAS Name: `VAL_AMT`
- Long SAS Name: `CLM_VAL_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The amount related to the condition identified in the CLM_VAL_CD which was used by the intermediary to process the institutional claim.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Claim Value Based Purchasing Adjustment Payment Amount](https://www.resdac.org/cms-data/variables/claim-value-based-purchasing-adjustment-payment-amount)

- Short SAS Name: `CLM_VBP_ADJSTMT_PMT_AMT`
- Long SAS Name: `CLM_VBP_ADJSTMT_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Under the Hospital Value Based Purchasing (HVBP) program, an adjustment is made to the base operating DRG amount for certain Inpatient Prospective Payment System (IPPS) hospitals - based on their Total Performance Score (TPS).

This initiative began in 4th Quarter of 2013 (i.e., beginning of Federal fiscal year 14 [FY14]).   

This field was new in 2013, and is null/missing for all previous years. The HVBP applies only to subsection (d) IPPS hospitals. There is a variable that indicates whether the hospital was excluded from HVBP (see CLM_VBP_PRTCPNT_IND_CD). This percentage reduction is applied  to the base operating DRG amount, depending on their TPS (which is the Value Based Purchasing Score), as required by the Affordable Care Act (ACA). The percentages change each FY.  

Additional information is available on the CMS "Hospital Value-Based Purchasing" website. 

The actual dollar amount of the adjustment that applied to the claim is found in the variable called CLM_VBP_ADJSTMT_PMT_AMT.



<h3>Values</h3>

| Code   |
|:-------|
| X.XX   |

## [Claim Value Code](https://www.resdac.org/cms-data/variables/claim-value-code)

- Short SAS Name: `VAL_CD`
- Long SAS Name: `CLM_VAL_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code indicating the value of a monetary condition which was used by the intermediary to process an institutional claim.



<h3>Values</h3>



 Claim Value Table.txt 



## [Claim Value-Based Purchasing (VBP) Participant Indicator Code](https://www.resdac.org/cms-data/variables/claim-value-based-purchasing-vbp-participant-indicator-code)

- Short SAS Name: `CLM_VBP_PRTCPNT_IND_CD `
- Long SAS Name: `CLM_VBP_PRTCPNT_IND_CD`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This field is the code used to identify a reason a hospital is excluded from the Hospital Value Based Purchasing (HVBP) program.

The ACA (Section 3001) excludes from the HVBP hospitals that meet certain conditions.
Additional information is available on the CMS "Hospital Value-Based Purchasing" website.
This initiative began in 4th Quarter of 2013 (i.e., beginning of Federal fiscal year 14).
This field was new in 2013, and is null/missing for all previous years.



<h3>Values</h3>

| Code         | Code Value                                           |
|:-------------|:-----------------------------------------------------|
| Y            | Participating in Hospital Value Based Purchasing     |
| N            | Not participating in Hospital Value Based Purchasing |
| Null/missing | same as 'N'                                          |

## [Claim service facility ZIP code (where service was provided)](https://www.resdac.org/cms-data/variables/claim-service-facility-zip-code-where-service-was-provided)

- Short SAS Name: `CLM_SRVC_FAC_ZIP_CD`
- Long SAS Name: `CLM_SRVC_FAC_ZIP_CD`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

ZIP code where service was provided, as indicated on the claim.



<h3>Values</h3>

| Code      |
|:----------|
| XXXXXXXXX |

## [County Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/County-Code-Claim-SSA)

- Short SAS Name: `CNTY_CD`
- Long SAS Name: `BENE_CNTY_CD`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    |           | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` |
| Inpatient  | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` |
| MedPAR     | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` |
| Outpatient | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` | `cnty_cd` |

| Dataset    | 2008      | 2007      | 2006      | 2005     | 2004     |
|:-----------|:----------|:----------|:----------|:---------|:---------|
| Carrier    | `cnty_cd` | `cnty_cd` | `cnty_cd` | `county` | `county` |
| Inpatient  | `cnty_cd` | `cnty_cd` | `cnty_cd` | `county` | `county` |
| MedPAR     | `cnty_cd` | `cnty_cd` | `cnty_cd` | `county` | `county` |
| Outpatient | `cnty_cd` | `cnty_cd` | `cnty_cd` | `county` | `county` |

| Dataset    | 2003     | 2002     | 2001      | 2000      | 1999      |
|:-----------|:---------|:---------|:----------|:----------|:----------|
| Carrier    | `county` | `county` | `cnty_cd` | `cnty_cd` | `bcounty` |
| Inpatient  | `county` | `county` | `cnty_cd` | `cnty_cd` | `cnty_cd` |
| MedPAR     | `county` | `county` | `mcounty` | `mcounty` | `mcounty` |
| Outpatient | `county` | `county` | `county`  | `cnty_cd` | `cnty_cd` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The SSA standard county code of a beneficiary's residence.



## [Date of Birth from Claim (Date)](https://www.resdac.org/cms-data/variables/Date-Birth-Claim-Date)

- Short SAS Name: `DOB_DT`
- Long SAS Name: `DOB_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The beneficiary's date of birth.



## [Demo information text](https://www.resdac.org/cms-data/variables/demo-information-text)

- Short SAS Name: `DEMO_INFO_TXT`
- Long SAS Name: `DEMO_INFO_TXT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

This is a text field that contains information related to the demonstration.For example, a claim involving a CHOICES demo id `05` would contain the MCO plan contract number in the first five positions of this text field.

When the Demo ID = 01 (RUGS) -- the text field will contain a 2, 3 or 4 to denote the RUGS phase. If RUGS phase is blank or not one of the above the text field will reflect 'INVALID'. NOTE: In Version 'G', RUGS phase was stored in redefined Claim Edit Group, 3rd occurrence, 4th position.
Demo ID = 02 (Home Health demo) -- the text field will contain PROV#. When demo number not equal to 02 then text will reflect 'INVALID'.
Demo ID = 03 (Telemedicine demo) -- text field will contain the HCPCS code. If the required HCPCS is not shown then the text field will reflect 'INVALID'.
Demo ID = 04 (UMWA) -- text field will contain W0 denoting that condition code W0 was present. If condition code W0 not present then the text field will reflect 'INVALID'.
Demo ID = 05 (CHOICES) -- the text field will contain the CHOICES plan number, if both of the following conditions are met: (1) CHOICES plan number present and PPS or Inpatient claim shows that 1st 3 positions of provider number as `210` and the admission date is within HMO effective/termination date; or non-PPS claim and the from date is within HMO effective/termination date and (2) CHOICES plan number matches the HMO plan number. If either condition is not met the text field will reflect 'INVALID CHOICES PLAN NUMBER'. When CHOICES plan number not present, text will reflect 'INVALID'.
Demo ID = 15 (ESRD Managed Care) -- text field will contain the ESRD/MCO plan number. If ESRD/MCO plan number not present the field will reflect 'INVALID'.
Demo ID = 38 (Physician Encounter Claims) -- text field will contain the MCO plan number. When MCO plan number not present the field will reflect 'INVALID'.



## [Demonstration number](https://www.resdac.org/cms-data/variables/demonstration-number)

- Short SAS Name: `DEMO_ID_NUM`
- Long SAS Name: `DEMO_ID_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The number assigned to identify a CMS demonstration project.This field is also used to denote special processing (a.k.a. Special Processing Number, SPN).



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Nursing Home Case-Mix and Quality: NHCMQ (RUGS) Demo – testing PPS for SNFs in 6 states, using a case-mix classification system based on resident characteristics and actual resources used. The claims carry a RUGS indicator and one or more revenue center codes in the 9,000 series.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2      | National HHA Prospective Payment Demo -- testing PPS for HHAs in 5 states, using two alternate methods of paying HHAs: per visit by type of HHA visit and per episode of HH care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 3      | Telemedicine Demo -- testing covering traditionally non-covered physician services for medical consultation furnished via two-way, interactive video systems (i.e. teleconsultation)in 4 states. The claims contain line items with 'QQ' HCPCS code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 4      | United Mine Workers of America (UMWA) Managed Care Demo -- testing risk sharing for Part A services, paying special capitation rates for all UMWA beneficiaries residing in 13 designated counties in 3 states. Under the demo, UMWA will waive the 3-day qualifying hospital stay for a SNF admission. The claims contain TOB '18X','21X','28X' and '51X'; condition code = W0; claim MCO paid switch = not '0'; and MCO contract # = '90091'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 5      | Medicare Choices (MCO encounter data) demo --testing expanding the type of Managed Care plans available and different payment methods at 16 MCOs in 9 states. The claims contain one of the specific MCO Plan Contract # assigned to the Choices Demo site. NOTE - this demonstration was terminated 12/31/2000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 6      | Coronary Artery Bypass Graft (CABG) Demo --testing bundled payment (all-inclusive global pricing) for hospital + physician services related to CABG surgery in 7 hospitals in 7 states. The inpatient claims contain a DRG '106' or '107'. NOTE - this demonstration was terminated in 1998.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 7      | Virginia Cardiac Surgery Initiative (VCSI) (formerly referred to as Medicare Quality Partnerships Demo) -- this is a voluntary consortium of the cardiac surgery Medicare FFS Claims (Version K) Codebook 166 May 2017 physician groups and the non-Veterans Administration hospitals providing open heart surgical services in the Commonwealth of Virginia. The goal of the demo is to share data on quality and process innovations in an attempt to improve the care for all cardiac patients. The demonstration only affects those FIs that process claims from hospitals in Virginia and the carriers that process claims from physicians providing inpatient services at those hospitals. The hospitals will be reimbursed on a global payment basis for selected cardiac surgical diagnosis related groups (DRGs). The inpatient claims will contain a DRG '104', '105', '106', '107', '109'; the related physician/supplier claims will contain the claim payment denial reason code = 'D'. NOTE - The implementation date for this demonstration is 4/1/03. |
| 8      | Provider Partnership Demo -- testing per-case payment approaches for acute inpatient hospitalizations, making a lump-sum payment (combining the normal Part A PPS payment with the Part B allowed charges into a single fee schedule) to a Physician/Hospital Organization for all Part A and Part B services associated with a hospital admission. From 3 to 6 hospitals in the Northeast and Mid-Atlantic regions may participate in the demo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 15     | ESRD Managed Care (MCO encounter data) -- testing open enrollment of ESRD beneficiaries and capitation rates adjusted for patient treatment needs at 3 MCOs in 3 States. The claims contain one of the specific MCO Plan Contract # assigned to the ESRD demo site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 30     | Lung Volume Reduction Surgery (LVRS) or National Emphysema Treatment Trial (NETT) Clinical Study -- evaluating the effectiveness of LVRS and maximum medical therapy (including pulmonary rehab) for Medicare beneficiaries in last stages of emphysema at 18 hospitals nationally, in collaboration with NIH.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 31     | VA Pricing Special Processing (SPN) -- not really a demo but special request from VA due to court settlement; not Medicare services but VA inpatient and physician services submitted to FI 00400 and Carrier 00900 to obtain Medicare pricing -- NCH WILL PROCESS VA CLAIMS ANNOTATED WITH DEMO ID '31', BUT WILL NOT TRANSMIT TO HCFA (CMS) (not in Nearline File).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 37     | Medicare Coordinated Care Demonstration -- to test whether coordinated care services furnished to certain beneficiaries improves outcome of care and reduces Medicare expenditures under Part A and Part B. There will be at least 14 Coordinated Care Entities (CCEs). The selected entities will be assigned a provider number specifically for the demonstration services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 37     | Medicare Disease Management (DMD) -- the purpose of this demonstration is to study the impact on costs and health outcomes of applying disease management services supplemented with coverage for prescription drugs for certain Medicare diagnosed, beneficiaries with advanced-stage congestive heart failure, diabetes, or coronary heart disease. Three demonstration sites will be used for this demonstration and it will last for 3 years. (Effective 4/1/2003).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 38     | Physician Encounter Claims - the purpose of this demo id is to identify the physician encounter claims being processed at the HCFA Data Center (HDC). This number will help EDS in making the claim go through the appropriate processing logic, which differs from that for fee-for-service. **NOT IN NCH.** NOTE - Effective October, 2000. Demo ids will not be assigned to Inpatient and Outpatient encounter claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 39     | Centralized Billing of Flu and PPV Claims -- The purpose of this demo is to facilitate the processing carrier, Trailblazers, paying flu and PPV claims based on payment localities. Providers will be giving the shots throughout the country and transmitting the claims to Trailblazers for processing. NOTE - Effective October, 2000 for carrier claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 40     | Payment of Physician and Non-physician Services in certain Indian Providers -- the purpose of this demo is to extend payment for services of physician and non-physician practitioners furnished in hospitals and ambulatory care clinics. Prior to the legislation change in BIPA, reimbursement for Medicare services provided in IHS facilities was limited to services provided in hospitals and skilled nursing facilities. This change will allow payment for IHS, Tribe and Tribal Organization providers under the Medicare physician fee schedule. NOTE - Effective July 1, 2001 for institutional and carrier claims.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 48     | Medical Adult Day-Care Services -- the purpose of this demonstration is to provide, as part of the episode of care for home health services, medical adult day care services to Medicare beneficiaries as a substitute for a portion of home health services that would otherwise be provided in the beneficiaries home. This demo would last approx. 3 years in not more than 5 sites. Payment for each home health service episode of care will be set at 95% of the amount that would otherwise be paid for home health services provided entirely in the home. NOTE - Effective July 5, 2005 for HHA claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 49     | Hemodialysis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 53     | Extended Stay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 54     | ACE Demo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 58     | used to identify the Multi-payer Advanced Primary Care Practice (MAPCP) demonstration. (eff. 7/2/12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 59     | ACO Pioneer Demonstration (eff. 1/2014)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 61     | CLM-CARE-IMPRVMT-MODEL-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 62     | CLM-CARE-IMPRVMT-MODEL-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 63     | CLM-CARE-IMPRVMT-MODEL-3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 64     | CLM-CARE-IMPRVMT-MODEL-4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 65     | rebilled claims due to auditor denials -- code being implemented for a demonstration to determine the efficiency of allowing providers to rebill for all outpatient services, minus a penalty, when an inpatient claim is denied in full because of medical review because the beneficiary did not require inpatient services. (eff. 7/2/12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 66     | rebilled claims due to provider self-audit after claim submission/payment -- code being implemented for a demonstration to determine the efficiency of allowing providers to rebill for all outpatient services, minus a penalty, when an inpatient claim is denied in full because of medical review because the beneficiary did not require inpatient services. (eff. 7/2/12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 67     | rebilled claims due to provider self-audit after the patient has been discharged, but prior to payment -- code being implemented for a demonstration to determine the efficiency of allowing providers to rebill for all outpatient services, minus a penalty, when an inpatient claim is denied in full because of medical review because the beneficiary did not require inpatient services. (eff. 7/2/12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 68     | NCH will not apply the 3-day hospital stay requirement when processing a SNF claim. (eff. 1/2014)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 70     | used for Electrical Workers Insurance Fund claims. (eff. 7/2/12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 74     | unknown value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 77     | Shared Savings Program (eff. 10/2016)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 78     | Comprehensive Primary Care Plus (CPC+) (eff. 4/2017)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## [Demonstration sequence number](https://www.resdac.org/cms-data/variables/demonstration-sequence-number)

- Short SAS Name: `DEMO_ID_SQNC_NUM`
- Long SAS Name: `DEMO_ID_SQNC_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The number of demonstration identification trailers present on the claim.

The demonstration sequence number is a sequential line number to distinguish distinct demonstration projects that affect the same claim.



## [Encrypted CCW Beneficiary ID](https://www.resdac.org/cms-data/variables/encrypted-ccw-beneficiary-id)

- Short SAS Name: `BENE_ID`
- Long SAS Name: `BENE_ID`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Carrier    |           | `bene_id` | `bene_id` | `bene_id` | `bene_id` |
| Inpatient  | `bene_id` | `bene_id` | `bene_id` | `bene_id` | `bene_id` |
| MedPAR     | `bene_id` | `bene_id` | `bene_id` | `bene_id` | `bene_id` |
| Outpatient | `bene_id` | `bene_id` | `bene_id` | `bene_id` | `bene_id` |

| Dataset    | 2008      | 2007      | 2006      |
|:-----------|:----------|:----------|:----------|
| Carrier    | `bene_id` | `bene_id` | `bene_id` |
| Inpatient  | `bene_id` | `bene_id` | `bene_id` |
| MedPAR     | `bene_id` | `bene_id` | `bene_id` |
| Outpatient | `bene_id` | `bene_id` | `bene_id` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Master Beneficiary Summary File](../mbsf.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The unique CCW indentifier for a beneficiary. The CCW assigns a unique beneficiary identification number to each individual who receives Medicare and/or Medicaid, and uses that number to identify an individual’s records in all CCW data files (e.g., Medicare claims, MAX claims, MDS assessment data). This number does not change during a beneficiary’s lifetime and each number is used only once. The BENE_ID is specific to the CCW and is not applicable to any other identification system or data source.



## [FI Claim Process Date](https://www.resdac.org/cms-data/variables/FI-Claim-Process-Date)

- Short SAS Name: `FI_CLM_PROC_DT`
- Long SAS Name: `FI_CLM_PROC_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The date the fiscal intermediary completes processing and releases the institutional claim to the CWF host.



## [FI Number](https://www.resdac.org/cms-data/variables/fi-number)

- Short SAS Name: `FI_NUM`
- Long SAS Name: `FI_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The identification number assigned by CMS to a fiscal intermediary authorized to process institutional claim records. Effective October 2006, the Medicare Administrative Contractors (MACs) began replacing the existing fiscal intermediaries and started processing institu- tional claim records for states assigned to its jurisdiction. NOTE: The 5-position MAC number will be housed in the existing FI_NUM field. During the transition from an FI to a MAC the FI_NUM field could contain either a FI number or a MAC number. See the FI_NUM table of codes to identify the new MAC numbers and their effective dates.



<h3>Values</h3>

JURISDICTION 3 - Part A MACs

| Code   | Code Value                                                                                                      |
|:-------|:----------------------------------------------------------------------------------------------------------------|
| 10     | Alabama BC - Alabama                                                                                            |
| 11     | Alabama BC - Iowa (replaced by MAC # 03401 -- see below)                                                        |
| 20     | Arkansas BC - Arkansas                                                                                          |
| 21     | Arkansas BC - Rhode Island                                                                                      |
| 30     | Arizona BC (replaced by MAC #03101 -- see below)                                                                |
| 40     | California BC (term. 12/00)                                                                                     |
| 50     | New Mexico BC/CO (term. 06/89)                                                                                  |
| 60     | Connecticut BC (term. 06/99)                                                                                    |
| 70     | Delaware BC - terminated 2/98                                                                                   |
| 80     | Florida BC (term. 03/88)                                                                                        |
| 90     | Florida BC                                                                                                      |
| 101    | Georgia BC                                                                                                      |
| 121    | Illinois - HCSC (term. 08/98)                                                                                   |
| 123    | Michigan - HCSC (term. 08/98)                                                                                   |
| 130    | Indiana BC/Administar Federal                                                                                   |
| 131    | Illinois - Administar                                                                                           |
| 140    | Iowa - Wellmark (term. 6/2000)                                                                                  |
| 150    | Kansas BC (term. 2008) (replaced with MAC # 05201 --see below)                                                  |
| 160    | Kentucky/Administar                                                                                             |
| 180    | Maine BC                                                                                                        |
| 181    | Maine BC - Massachusetts                                                                                        |
| 190    | Maryland BC (term. 9/2005)                                                                                      |
| 200    | Massachusetts BC (term. 7/97)                                                                                   |
| 210    | Michigan BC (term. 9/94)                                                                                        |
| 220    | Minnesota BC (term. 07/99)                                                                                      |
| 230    | Mississippi BC                                                                                                  |
| 231    | Mississippi BC/LA (term. 09/92)                                                                                 |
| 232    | Mississippi BC                                                                                                  |
| 241    | Missouri BC (term. 9/92)                                                                                        |
| 250    | Montana BC (replaced by MAC #03201 -- see below)                                                                |
| 260    | Nebraska BC (term. 2007) (replaced with MAC # 05401 --see below)                                                |
| 270    | New Hampshire BC                                                                                                |
| 280    | New Jersey BC (term. 8/2000)                                                                                    |
| 290    | New Mexico BC - terminated 11/95                                                                                |
| 308    | New York - Empire BC                                                                                            |
| 310    | North Carolina BC (term. 01/02)                                                                                 |
| 320    | North Dakota BC - North Dakota (replaced with MAC # 03301 -- see below)                                         |
| 322    | North Dakota BC - Washington & Alaska                                                                           |
| 323    | North Dakota BC - Idaho, Oregon & Utah (replaced with MAC # 03501 --see below)                                  |
| 332    | Ohio-Administar                                                                                                 |
| 340    | Oklahoma BC (term. 2008) (replaced with MAC # 04301 --see below)                                                |
| 350    | Oregon BC                                                                                                       |
| 351    | Oregon BC/ID. (term. 09/88)                                                                                     |
| 355    | Oregon-CWF                                                                                                      |
| 362    | Independence BC - terminated 8/97                                                                               |
| 363    | Pennsylvania/Highmark - Veritus                                                                                 |
| 366    | Highmark (MD & DC) - Part A (eff. 10/2005)                                                                      |
| 370    | Rhode Island BC                                                                                                 |
| 380    | South Carolina BC - South Carolina                                                                              |
| 382    | South Carolina BC - North Carolina                                                                              |
| 390    | Tennessee BC                                                                                                    |
| 400    | Texas BC                                                                                                        |
| 410    | Utah BC (term. 09/00)                                                                                           |
| 423    | Virginia BC; Trigon (term. 08/99)                                                                               |
| 430    | Washington/Alaska BC                                                                                            |
| 450    | Wisconsin BC - Wisconsin                                                                                        |
| 452    | Wisconsin BC - Michigan                                                                                         |
| 453    | Wisconsin BC - Virginia & West Virginia                                                                         |
| 454    | Wisconsin BC - California                                                                                       |
| 460    | Wyoming BC (replaced by MAC # 03601 -- see below)                                                               |
| 468    | N Carolina BC/CPRTIVA                                                                                           |
| 993    | BC/BS Assoc.                                                                                                    |
| 17120  | Hawaii Medical Service (term. 06/99)                                                                            |
| 50333  | Travelers; Connecticut United Healthcare (terminated - date unknown)                                            |
| 51051  | Aetna California - terminated 6/97                                                                              |
| 51070  | Aetna Connecticut - terminated 6/97                                                                             |
| 51100  | Aetna Florida - terminated 6/97                                                                                 |
| 51140  | Aetna Illinois - terminated 6/97                                                                                |
| 51390  | Aetna Pennsylvania - terminated 6/97                                                                            |
| 52280  | NE - Mutual of Omaha                                                                                            |
| 57400  | Puerto Rico - Cooperativa                                                                                       |
| 61000  | Aetna (term. 06/97)                                                                                             |
| 80883  | Contractor ID for Inpatient & Outpatient Risk Adjustment Data (data not sent through CWF; but through Palmetto) |

JURISDICTION 4 - Part A MACs

| Code   | Code Value                                      |
|:-------|:------------------------------------------------|
| 3101   | Arizona (eff. 10/1/2006) (replaces FI #00030)   |
| 3201   | Montana (eff. 12/1/2006) (replaces FI #00250)   |
| 3301   | N. Dakota (eff. 12/1/2006) (replaces FI #00320) |
| 3401   | S. Dakota (eff. 3/1/2007) (replaces FI #00011)  |
| 3501   | Utah (eff. 12/1/2006) (replaces FI #00323)      |
| 3601   | Wyoming (eff. 11/1/2006) (replaces FI #00460)   |

JURISDICTION 5 - Part A MACs

| Code   | Code Value                                    |
|:-------|:----------------------------------------------|
| 4301   | Oklahoma (eff. 3/1/2008) (replaces FI #00340) |

| Code   | Code Value                                    |
|:-------|:----------------------------------------------|
| 5201   | Oklahoma (eff. 3/1/2008) (replaces FI #00150) |
| 5401   | Oklahoma (eff. 12/1/2007)(replaces FI #00260) |

## [FI or MAC Claim Action Code](https://www.resdac.org/cms-data/variables/FI-Claim-Action-Code)

- Short SAS Name: `ACTIONCD`
- Long SAS Name: `FI_CLM_ACTN_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

The type of action requested by the intermediary to be taken on an institutional claim.



<h3>Values</h3>

ResDAC note: the only values that are actually found in the CCW data are 1, 5, 8. The CMS value for code 3, referred to in code 5 is "Secondary debit adjustment - used only in credit/debit pairs (under HHPPS, would be the final claim or an adjustment on a LUPA)."

| Code   | Code Value                                                                                                     |
|:-------|:---------------------------------------------------------------------------------------------------------------|
| 1      | Original debit action (includes non-adjustment RTI correction items) - it will always be a 1 in regular bills. |
| 5      | Force action code 3                                                                                            |
| 8      | Benefits refused (for inpatient bills, an 'R' nonpayment code must also be present                             |

## [First Claim Diagnosis E Code](https://www.resdac.org/cms-data/variables/First-Claim-Diagnosis-E-Code)

- Short SAS Name: `FST_DGNS_E_CD`
- Long SAS Name: `FST_DGNS_E_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the 1st external cause of injury, poisoning, or other adverse effect This diagnosis E code is also stored as the 1st occurrence of the diagnosis E code trailer.

NOTE: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.



## [Gender Code from Claim](https://www.resdac.org/cms-data/variables/Gender-Code-Claim)

- Short SAS Name: `GNDR_CD`
- Long SAS Name: `GNDR_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The sex of a beneficiary.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 1      | Male         |
| 2      | Female       |
| 0      | Unknown      |

## [HCPCS Third Modifier Code](https://www.resdac.org/cms-data/variables/hcpcs-third-modifier-code)

- Short SAS Name: `MDFR_CD3`
- Long SAS Name: `HCPCS_3RD_MDFR_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

A third modifier to the Healthcare Common Procedure Coding System (HCPCS) procedure code to make it more specific than the first or second modifier codes to identify the revenue center or line item services for the claim.



## [NCH Active or Covered Level Care Thru Date](https://www.resdac.org/cms-data/variables/NCH-Active-or-Covered-Level-Care-Thru-Date)

- Short SAS Name: `CARETHRU`
- Long SAS Name: `NCH_ACTV_OR_CVRD_LVL_CARE_THRU`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The date on a claim for which the covered level of care ended in a general hospital or the active care ended in a psychiatric/TB hospital.

??? derivation
	DERIVED FROM:
	CLM_RLT_OCRNC_CD
	CLM_RLT_OCRNC_DT
	
	DERIVATION RULES:
	Based on the presence of occurrence code 22 move the related occurrence date to NCH_ACTV_CVR_LVL_CARE_THRU_DT.

## [NCH Beneficiary Blood Deductible Liability Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Blood-Deductible-Liability-Amount)

- Short SAS Name: `BLDDEDAM`
- Long SAS Name: `NCH_BENE_BLOOD_DDCTBL_LBLTY_AM`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |
| MedPAR     | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |
| Outpatient | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |
| MedPAR     | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |
| Outpatient | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |
| MedPAR     | `blddedam` | `blddedam` | `mbldded`  | `mbldded`  | `mbldded`  |
| Outpatient | `blddedam` | `blddedam` | `blddedam` | `blddedam` | `blddedam` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The amount of money for which the intermediary determined the beneficiary is liable for the blood deductible.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	DERIVATION RULES:
	Based on the presence of value code equal to '06' move the corresponding value amount to NCH_BENE_BLOOD_DDCTBL_AMT.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Beneficiary Discharge Date](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Discharge-Date)

- Short SAS Name: `DSCHRGDT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dschrgdt` | `dschrgdt` | `dschrgdt` | `dschrgdt` | `dschrgdt` |

| Dataset   | 2008       | 2007       | 2006       | 2005        | 2004        |
|:----------|:-----------|:-----------|:-----------|:------------|:------------|
| MedPAR    | `dschrgdt` | `dschrgdt` | `dschrgdt` | `sdschrgdt` | `sdschrgdt` |

| Dataset   | 2003        | 2002        | 2001      | 2000      | 1999      |
|:----------|:------------|:------------|:----------|:----------|:----------|
| MedPAR    | `sdschrgdt` | `sdschrgdt` | `mdisdte` | `mdisdte` | `mdisdte` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

On an inpatient or Home Health claim, the date the beneficiary was discharged from the facility, or died.

Date matches the "thru" date on the claim (CLM_THRU_DT). When there is a discharge date, the discharge status code (PTNT_DSCHRG_STUS_CD) indicates the final disposition of the patient after discharge.

??? derivation
	DERIVED FROM:
	NCH_PTNT_STUS_IND_CD
	CLM_THRU_DT
	
	DERIVATION RULES:
	Based on the presence of patient discharge status code not equal to 30 (still patient), move the claim thru date to the NCH_BENE_DSCHRG_DT.

## [NCH Beneficiary Inpatient Deductible Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Inpatient-Deductible-Amount)

- Short SAS Name: `DED_AMT`
- Long SAS Name: `NCH_BENE_IP_DDCTBL_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` |
| MedPAR    | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` |
| MedPAR    | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` |

| Dataset   | 2003      | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` | `ded_amt` |
| MedPAR    | `ded_amt` | `ded_amt` | `mpded`   | `mpded`   | `mpded`   |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The amount of the deductible the beneficiary paid for inpatient services, as originally submitted on the institutional claim.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	DERIVATION RULES:
	Based on the presence of value code equal to
	A1, B1, or C1 move the corresponding value
	amount to the NCH_BENE_IP_DDCTBL_AMT.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Beneficiary Medicare Benefits Exhausted Date](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Medicare-Benefits-Exhausted-Date)

- Short SAS Name: `EXHST_DT`
- Long SAS Name: `NCH_BENE_MDCR_BNFTS_EXHTD_DT_I`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The last date for which the beneficiary has Medicare coverage. This is completed only where where benefits were exhausted before the date of discharge and during the billing period covered by this institutional claim.

??? derivation
	DERIVED FROM:
	CLM_RLT_OCRNC_CD
	CLM_RLT_OCRNC_DT
	
	DERIVATION RULES (Effective 10/93):
	Based on the presence of occurrence code A3, B3 or C3 move the related occurrence date to NCH_MDCR_BNFT_EXHST_DT. *NOTE: Prior to 10/93, the date associated with occurrence code 23 was moved to this field.

## [NCH Beneficiary Part A Coinsurance Liability Amount](https://www.resdac.org/cms-data/variables/NCH-Beneficiary-Part-Coinsurance-Liability-Amount)

- Short SAS Name: `COIN_AMT`
- Long SAS Name: `NCH_BENE_PTA_COINSRNC_LBLTY_AM`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` |
| MedPAR    | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` |
| MedPAR    | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` | `coin_amt` |
| MedPAR    | `coin_amt` | `coin_amt` | `mcoinamt` | `mcoinamt` | `mcoinamt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

The amount of money for which the intermediary has determined that the beneficiary is liable for Part A coinsurance on the institutional claim.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	DERIVATION RULES:
	Based on the presence of value code equal to 8, 9, 10 or 11 move the corresponding value amount to the NCH_BENE_IP_PTA_COINSRC_AMT.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Blood Pints Furnished Quantity](https://www.resdac.org/cms-data/variables/NCH-Blood-Pints-Furnished-Quantity)

- Short SAS Name: `BLDFRNSH`
- Long SAS Name: `NCH_BLOOD_PNTS_FRNSHD_QTY`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Number of whole pints of blood furnished to the beneficiary, as reported on the carrier claim (non-DMERC).

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	
	DERIVATION RULES:
	Based on the presence of value code equal to 37 move the related value amount to the NCH_BLOOD_PT_FRNSH_QTY.

## [NCH Claim Type Code](https://www.resdac.org/cms-data/variables/nch-claim-type-code)

- Short SAS Name: `CLM_TYPE`
- Long SAS Name: `NCH_CLM_TYPE_CD`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `clm_type` | `clm_type` | `clm_type` | `clm_type` | `clm_type` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `clm_type` | `clm_type` | `clm_type` | `clm_type` | `clm_type` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `clm_type` | `clm_type` | `clm_type` | `clm_type` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the type of claim record being processed in NCH.

NOTE1: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

NOTE2: During the Version I conversion this field was expanded to include inpatient 'full' encounter claims (for service dates after 6/30/97).

NOTE3: Effective with Version 'J', 3 new code values have been added to include a type code for the Medicare Advantage claims (IME/GME, no-pay and paid as FFS). During the Version 'J' conversion, these type codes were populated throughout history.

??? derivation
	FFS CLAIM TYPE CODES DERIVED FROM:
	NCH CLM_NEAR_LINE_RIC_CD
	NCH PMT_EDIT_RIC_CD
	NCH CLM_TRANS_CD
	NCH PRVDR_NUM
	INPATIENT 'FULL' ENCOUNTER TYPE CODE DERIVED FROM:
	(Pre-HDC processing -- AVAILABLE IN NCH)
	CLM_MCO_PD_SW
	CLM_RLT_COND_CD
	MCO_CNTRCT_NUM
	MCO_OPTN_CD
	MCO_PRD_EFCTV_DT
	MCO_PRD_TRMNTN_DT
	DERIVATION RULES:
	SET CLM_TYPE_CD TO 10 (HHA CLAIM) WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V','W' OR 'U'
	2. PMT_EDIT_RIC_CD EQUAL 'F'
	3. CLM_TRANS_CD EQUAL '5'
	SET CLM_TYPE_CD TO 20 (SNF NON-SWING BED CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V'
	2. PMT_EDIT_RIC_CD EQUAL 'C' OR 'E'
	3. CLM_TRANS_CD EQUAL '0' OR '4'
	4. POSITION 3 OF PRVDR_NUM IS NOT 'U', 'W', 'Y' OR 'Z'
	SET CLM_TYPE_CD TO 30 (SNF SWING BED CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V'
	2. PMT_EDIT_RIC_CD EQUAL 'C' OR 'E'
	3. CLM_TRANS_CD EQUAL '0' OR '4'
	4. POSITION 3 OF PRVDR_NUM EQUAL 'U', 'W', 'Y' OR 'Z'
	SET CLM_TYPE_CD TO 40 (OUTPATIENT CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'W'
	2. PMT_EDIT_RIC_CD EQUAL 'D'
	3. CLM_TRANS_CD EQUAL '6'
	SET CLM_TYPE_CD TO 50 (HOSPICE CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V'
	2. PMT_EDIT_RIC_CD EQUAL 'I'
	3. CLM_TRANS_CD EQUAL 'H'
	SET CLM_TYPE_CD TO 60 (INPATIENT CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V'
	2. PMT_EDIT_RIC_CD EQUAL 'C' OR 'E'
	3. CLM_TRANS_CD EQUAL '1' '2' OR '3'
	SET CLM_TYPE_CD TO 61 (INPATIENT 'FULL' ENCOUNTER CLAIM - PRIOR TO HDC PROCESSING - AFTER 6/30/97 - 12/4/00) WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_MCO_PD_SW = '1'
	2. CLM_RLT_COND_CD = '04'
	3. MCO_CNTRCT_NUM
	MCO_OPTN_CD = 'C'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	SET_CLM_TYPE_CD TO 61 (INPATIENT 'FULL' ENCOUNTER
	CLAIM -- EFFECTIVE WITH HDC PROCESSING) WHERE THE
	FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'V'
	2. PMT_EDIT_RIC_CD EQUAL 'C' OR 'E'
	3. CLM_TRANS_CD EQUAL '1' '2' OR '3'
	4. FI_NUM = 80881
	SET CLM_TYPE_CD TO 62 (Medicare Advantage IME/GME
	CLAIMS - 10/1/05 - FORWARD)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_MCO_PD_SW = '0'
	2. CLM_RLT_COND_CD = '04' & '69'
	3. MCO_CNTRCT_NUM
	MCO_OPTN_CD = 'C'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	SET CLM_TYPE_CD TO 63 (HMO NO-PAY CLAIMS)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	CLAIMS PROCESSED ON OR AFTER 10/6/08
	1. CLM_THRU_DT ON OR AFTER 10/1/06
	2. CLM_MCO_PD_SW = '1'
	3. CLM_RLT_COND_CD = '04'
	4. MCO_CNTRCT_NUM
	MCO_OPTN_CD = 'A', 'B' OR 'C'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	5. ZERO REIMBURSEMENT (CLM_PMT_AMT)
	SET CLM_TYPE_CD TO 63 (HMO NO-PAY CLAIMS)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	CLAIMS PROCESSED PRIOR to 10/6/08
	1. MCO_CNTRCT_NUM
	MCO_OPTN_CD = 'A', 'B' OR 'C'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	2. ZERO REIMBURSEMENT (CLM_PMT_AMT)
	SET CLM_TYPE_CD TO 64 (HMO CLAIMS PAID AS FFS)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	CLAIMS PROCESSED PRIOR to 10/6/08
	1. MCO_CNTRCT_NUM
	MCO_OPTN_CD = '1', '2' OR '4'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	SET CLM_TYPE_CD TO 64 (HMO CLAIMS PAID AS FFS)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	CLAIMS PROCESSED on or after 10/6/08
	1. CLM_RLT_COND_CD = '04'
	2. MCO_CNTRCT_NUM
	MCO_OPTN_CD = '1', '2' OR '4'
	CLM_FROM_DT & CLM_THRU_DT ARE WITHIN THE MCO_PRD_EFCTV_DT & MCO_PRD_TRMNTN_DT ENROLLMENT PERIODS
	SET CLM_TYPE_CD TO 71 (RIC O non-DMEPOS CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'O'
	2. HCPCS_CD not on DMEPOS table
	SET CLM_TYPE_CD TO 72 (RIC O DMEPOS CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'O'
	2. HCPCS_CD on DMEPOS table (NOTE: if one or more line item(s) match the HCPCS on the DMEPOS table).
	SET CLM_TYPE_CD TO 81 (RIC M non-DMEPOS DMERC CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'M'
	2. HCPCS_CD not on DMEPOS table
	SET CLM_TYPE_CD TO 82 (RIC M DMEPOS DMERC CLAIM)
	WHERE THE FOLLOWING CONDITIONS ARE MET:
	1. CLM_NEAR_LINE_RIC_CD EQUAL 'M'
	2. HCPCS_CD on DMEPOS table (NOTE: if one or more line item(s) match the HCPCS on the DMEPOS table).

<h3>Values</h3>

| Code   | Code Value                             |
|:-------|:---------------------------------------|
| 10     | HHA claim                              |
| 20     | Non swing bed SNF claim                |
| 30     | Swing bed SNF claim                    |
| 40     | Outpatient claim                       |
| 50     | Hospice claim                          |
| 60     | Inpatient claim                        |
| 61     | Inpatient 'Full-Encounter' claim       |
| 62     | Medicare Advantage IME/GME claims      |
| 63     | Medicare Advantage (no-pay) claims     |
| 64     | Medicare Advantage (paid as FFS) claim |
| 71     | RIC O local carrier non-DMEPOS claim   |
| 72     | RIC O local carrier DMEPOS claim       |
| 81     | RIC M DMERC non-DMEPOS claim           |
| 82     | RIC M DMERC DMEPOS claim               |

## [NCH DRG Outlier Approved Payment Amount](https://www.resdac.org/cms-data/variables/NCH-DRG-Outlier-Approved-Payment-Amount)

- Short SAS Name: `OUTLRPMT`
- Long SAS Name: `NCH_DRG_OUTLIER_APRVD_PMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

On an institutional claim, the additional payment amount approved by the Peer Review Organization due to an outlier situation for a beneficiary's stay under the prospective payment system, which has been classified into a specific diagnosis related group.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	
	DERIVATION RULES:
	Based on the presence of value code equal to 17 move the related amount to NCH_DRG_OUTLIER_APRV_PMT_AMT.

## [NCH Inpatient Noncovered Charge Amount](https://www.resdac.org/cms-data/variables/NCH-Inpatient-Noncovered-Charge-Amount)

- Short SAS Name: `NCCHGAMT`
- Long SAS Name: `NCH_IP_NCVRD_CHRG_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version H, the noncovered charges for all accommodations and services, reported on an inpatient claim (used for internal CWFMQA editing purposes).

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

??? derivation
	DERIVED FROM:
	REV_CNTR_CD
	REV_CNTR_NCVR_CHRG_AMT
	
	DERVIATION RULES:
	Based on the presence of revenue center code equal to 0001 move the related noncovered charge amount to NCH_IP_NCOV_CHRG_AMT.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Inpatient Total Deduction Amount](https://www.resdac.org/cms-data/variables/NCH-Inpatient-Total-Deduction-Amount)

- Short SAS Name: `TDEDAMT`
- Long SAS Name: `NCH_IP_TOT_DDCTN_AMT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version H, the total Part A deductions reported on the Inpatient claim (used for internal CWFMQA editing purposes).

NOTE: During the Version H conversion this field was populated with data throughout history (back to 1991), but the derivation rule applied was in- complete for claims processed prior to 10/93. Disregard any data present in this field on claims with NCH weekly process date earlier than 10/93.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	
	DERIVATION RULES (Effective 10/93):
	Accumulate the value amounts associated with value codes equal to 06, 08 thru 11 and A1, B1 or C1 and move to IP_TOT_DDCTN_AMT.
	NOTE: Value codes 08-11 did not exist in the NCH prior to 2/93; values codes A1, B1, C1 did not exist prior to 10/93.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Near Line Record Identification Code](https://www.resdac.org/cms-data/variables/NCH-Near-Line-Record-Identification-Code)

- Short SAS Name: `RIC_CD`
- Long SAS Name: `NCH_NEAR_LINE_REC_IDENT_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

A code defining the type of claim record being processed.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                       |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| O      | Part B physician/supplier claim record (processed by local carriers; can include DMEPOS services)                                                |
| V      | Part A institutional claim record (inpatient (IP), skilled nursing facility (SNF), christian science (CS), home health agency (HHA), or hospice) |
| W      | Part B institutional claim record (outpatient (OP), HHA)                                                                                         |
| U      | Both Part A and B institutional home health agency (HHA) claim records -- due to HHPPS and HHA A/B split. (effective 10/00)                      |
| M      | Part B DMEPOS claim record (processed by DME Regional Carrier) (effective 10/93)                                                                 |

## [NCH Patient Status Indicator Code](https://www.resdac.org/cms-data/variables/NCH-Patient-Status-Indicator-Code)

- Short SAS Name: `PTNTSTUS`
- Long SAS Name: `NCH_PTNT_STATUS_IND_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)

Effective with Version H, the code on an inpatient/SNF and Hospice claim, indicating whether the beneficiary was discharged, died or still a patient (used for internal CWFMQA editing purposes.)

NOTE: During the Version H conversion this field was populated throughout history (back to service year 1991).

??? derivation
	DERIVED FROM:
	NCH PTNT_DSCHRG_STUS_CD
	DERIVATION RULES:
	SET NCH_PTNT_STUS_IND_CD TO 'A' WHERE THE
	PTNT_DSCHRG_STUS_CD NOT EQUAL TO '20'- '30'
	OR '40' - '42'.
	SET NCH_PTNT_STUS_IND_CD TO 'B' WHERE THE
	PTNT_DSCHRG_STUS_CD EQUAL TO '20'- '29'
	OR '40' - '42'.
	SET NCH_PTNT_STUS_IND_CD TO 'C' WHERE THE
	PTNT_DSCHRG_STUS_CD EQUAL TO '30'

<h3>Values</h3>

| Code   | Code Value    |
|:-------|:--------------|
| A      | Discharged    |
| B      | Died          |
| C      | Still patient |

## [NCH Primary Payer Claim Paid Amount*](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Claim-Paid-Amount)

- Short SAS Name: `PRPAYAMT`
- Long SAS Name: `NCH_PRMRY_PYR_CLM_PD_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |
| MedPAR     | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |
| Outpatient | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |
| MedPAR     | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |
| Outpatient | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |
| MedPAR     | `prpayamt` | `prpayamt` | `mppamt`   | `mppamt`   | `mppamt`   |
| Outpatient | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` | `prpayamt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version H, the amount of a payment made on behalf of a Medicare bene- ficiary by a primary payer other than Medicare, that the provider is applying to covered Medicare charges on a non-institutional claim.

NOTE: During the Version H conversion, this field was populated with data throughout history (back to service year 1991) by summing up the line item primary payer amounts.



## [NCH Primary Payer Code](https://www.resdac.org/cms-data/variables/NCH-Primary-Payer-Code)

- Short SAS Name: `PRPAY_CD`
- Long SAS Name: `NCH_PRMRY_PYR_CD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prpay_cd` | `prpay_cd` | `prpay_cd` | `prpay_cd` | `prpay_cd` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prpay_cd` | `prpay_cd` | `prpay_cd` | `prpay_cd` | `prpay_cd` |

| Dataset   | 2003       | 2002       | 2001     | 2000     | 1999     |
|:----------|:-----------|:-----------|:---------|:---------|:---------|
| MedPAR    | `prpay_cd` | `prpay_cd` | `mppcde` | `mppcde` | `mppcde` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code, on an institutional claim, specifying a federal non-Medicare program or other source that has primary responsibility for the payment of the Medicare beneficiary's health insurance bills.

??? derivation
	DERIVED FROM:
	CLM_VAL_CD
	CLM_VAL_AMT
	DERIVATION RULES
	SET NCH_PRMRY_PYR_CD TO 'A' WHERE THE
	CLM_VAL_CD = '12'
	SET NCH_PRMRY_PYR_CD TO 'B' WHERE THE
	CLM_VAL_CD = '13'
	SET NCH_PRMRY_PYR_CD TO 'C' WHERE THE
	CLM_VAL_CD = '16' and CLM_VAL_AMT is zeroes
	SET NCH_PRMRY_PYR_CD TO 'D' WHERE THE
	CLM_VAL_CD = '14'
	SET NCH_PRMRY_PYR_CD TO 'E' WHERE THE
	CLM_VAL_CD = '15'
	SET NCH_PRMRY_PYR_CD TO 'F' WHERE THE
	CLM_VAL_CD = '16' (CLM_VAL_AMT not
	equal to zeroes)
	SET NCH_PRMRY_PYR_CD TO 'G' WHERE THE
	CLM_VAL_CD = '43'
	SET NCH_PRMRY_PYR_CD TO 'H' WHERE THE
	CLM_VAL_CD = '41'
	SET NCH_PRMRY_PYR_CD TO 'I' WHERE THE
	CLM_VAL_CD = '42'
	SET NCH_PRMRY_PYR_CD TO 'L' (or prior to 4/97
	set code to 'J') WHERE THE CLM_VAL_CD = '47'

<h3>Values</h3>

Values C, M, N, Y, Z and BLANK indicate Medicare is primary payer.  (values Z and Y were used prior to 12/90.  BLANK was supposed to be effective after 12/90, but may have been used prior to that date.)

| Code   | Code Value                                                                                                                              |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------|
| A      | Working aged bene/spouse with employer group health plan (EGHP)                                                                         |
| B      | End stage renal disease (ESRD) beneficiary in the 18 month coordination period with an employer group health plan                       |
| C      | Conditional payment by Medicare; future reimbursement expected                                                                          |
| D      | Automobile no-fault (eff. 4/97; Prior to 3/94, also included any liability insurance)                                                   |
| E      | Workers' compensation                                                                                                                   |
| F      | Public Health Service or other federal agency (other than Dept. of Veterans Affairs)                                                    |
| G      | Working disabled bene (under age 65 with LGHP)                                                                                          |
| H      | Black Lung                                                                                                                              |
| I      | Dept. of Veterans Affairs                                                                                                               |
| J      | Any liability insurance (eff. 3/94 - 3/97)                                                                                              |
| L      | Any liability insurance (eff. 4/97) (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96)       |
| M      | Override code: EGHP services involved (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96)     |
| N      | Override code: non-EGHP services involved (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96) |
| BLANK  | Medicare is primary payer (not sure of effective date: in use 1/91, if not earlier)                                                     |
| Y      | Other secondary payer investigation shows Medicare as primary payer                                                                     |
| Z      | Medicare is primary payer                                                                                                               |

## [NCH Professional Component Charge Amount](https://www.resdac.org/cms-data/variables/nch-professional-component-charge-amount-0)

- Short SAS Name: `PCCHGAMT`
- Long SAS Name: `NCH_PROFNL_CMPNT_CHRG_AMT`

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

This field is the amount of physician and other professional charges covered under Medicare Part B.

This variable is not populated for Home Health or Hospice claims. This field is used for CMS editing purposes and other internal processes (e.g. if computing interim payments, then these charges are deducted). The source of information for this field for institutional claims is the CLM_VAL_AMT (when the code = 04 or 05, it indicates a professional component charge amount). For Outpatient claims, this information is from the revenue center codes (when the code=096*, 097* or 098*, then the REV_CNTR_TOT_CHRG_AMT indicates a professional component charge amount).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [NCH Provider State Code](https://www.resdac.org/cms-data/variables/nch-provider-state-code)

- Short SAS Name: `PRSTATE`
- Long SAS Name: `PRVDR_STATE_CD`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |
| Outpatient | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |
| Outpatient | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |

| Dataset    | 2003      | 2002      | 2001      | 2000      | 1999      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |
| Outpatient | `prstate` | `prstate` | `prstate` | `prstate` | `prstate` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version H, the two position SSA state code where provider facility is located.

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

??? derivation
	DERIVED FROM:
	NCH PRVDR_NUM
	DERIVATION RULES:
	SET NCH_PRVDR_STATE_CD TO
	PRVDR_NUM POS1-2.
	FOR PRVDR_NUM POS1-2 EQUAL '55' OR '75'
	SET NCH_PRVDR_STATE_CD TO '05'.
	FOR PRVDR_NUM POS1-2 EQUAL '67' OR '74'
	SET NCH_PRVDR_STATE_CD TO '45'.
	FOR PRVDR_NUM POS1-2 EQUAL '68' OR '69'
	SET NCH_PRVDR_STATE_CD TO '10'.
	FOR PRVDR_NUM POS1-2 EQUAL '78'
	SET NCH_PRVDR_STATE_CD TO '14'
	FOR PRVDR_NUM POS1-2 EQUAL TO '76'
	SET NCH_PRVDR_STATE_CD TO '16'
	FOR PRVDR_NUM POS1-2 EQUAL '70'
	SET NCH_PRVDR_STATE_CD TO '17'
	FOR PRVDR_NUM POS1-2 EQUAL '71'
	SET NCH_PRVDR_STATE_CD TO '19'
	FOR PRVDR_NUMBER POS1-2 EQUAL '77'
	SET NCH_PRVDR_STATE_CD TO '24'
	FOR PRVDR_NUM POS1-2 EQUAL TO '72'
	SET NCH_PRVDR_STATE_CD TO '36'
	FOR PRVDR_NUM POS1-2 EQUAL TO '73'
	SET NCH_PRVDR_STATE_CD TO '39'

<h3>Values</h3>

| Code   | Code Value                                                |
|:-------|:----------------------------------------------------------|
| 1      | Alabama                                                   |
| 2      | Alaska                                                    |
| 3      | Arizona                                                   |
| 4      | Arkansas                                                  |
| 5      | California                                                |
| 6      | Colorado                                                  |
| 7      | Connecticut                                               |
| 8      | Delaware                                                  |
| 9      | District of Columbia                                      |
| 10     | Florida                                                   |
| 11     | Georgia                                                   |
| 12     | Hawaii                                                    |
| 13     | Idaho                                                     |
| 14     | Illinois                                                  |
| 15     | Indiana                                                   |
| 16     | Iowa                                                      |
| 17     | Kansas                                                    |
| 18     | Kentucky                                                  |
| 19     | Louisiana                                                 |
| 20     | Maine                                                     |
| 21     | Maryland                                                  |
| 22     | Massachusetts                                             |
| 23     | Michigan                                                  |
| 24     | Minnesota                                                 |
| 25     | Mississippi                                               |
| 26     | Missouri                                                  |
| 27     | Montana                                                   |
| 28     | Nebraska                                                  |
| 29     | Nevada                                                    |
| 30     | New Hampshire                                             |
| 31     | New Jersey                                                |
| 32     | New Mexico                                                |
| 33     | New York                                                  |
| 34     | North Carolina                                            |
| 35     | North Dakota                                              |
| 36     | Ohio                                                      |
| 37     | Oklahoma                                                  |
| 38     | Oregon                                                    |
| 39     | Pennsylvania                                              |
| 40     | Puerto Rico                                               |
| 41     | Rhode Island                                              |
| 42     | South Carolina                                            |
| 43     | South Dakota                                              |
| 44     | Tennessee                                                 |
| 45     | Texas                                                     |
| 46     | Utah                                                      |
| 47     | Vermont                                                   |
| 48     | Virgin Islands                                            |
| 49     | Virginia                                                  |
| 50     | Washington                                                |
| 51     | West Virginia                                             |
| 52     | Wisconsin                                                 |
| 53     | Wyoming                                                   |
| 54     | Africa                                                    |
| 55     | California                                                |
| 56     | Canada & Islands                                          |
| 57     | Central America and West Indies                           |
| 58     | Europe                                                    |
| 59     | Mexico                                                    |
| 60     | Oceania                                                   |
| 61     | Philippines                                               |
| 62     | South America                                             |
| 63     | U.S. Possessions                                          |
| 64     | American Samoa                                            |
| 65     | Guam                                                      |
| 66     | Commonwealth of the Northern Marianas Islands             |
| 67     | Texas                                                     |
| 68     | Florida (eff. 10/2005)                                    |
| 69     | Florida (eff. 10/2005)                                    |
| 70     | Kansas (eff. 10/2005)                                     |
| 71     | Louisiana (eff. 10/2005)                                  |
| 72     | Ohio (eff. 10/2005)                                       |
| 73     | Pennsylvania (eff. 10/2005)                               |
| 74     | Texas (eff. 10/2005)                                      |
| 80     | Maryland (eff. 8/2000)                                    |
| 97     | Northern Marianas                                         |
| 98     | Guam                                                      |
| 99     | With 000 county code is American Samoa; otherwise unknown |

## [NCH Verified Noncovered Stay From Date](https://www.resdac.org/cms-data/variables/NCH-Verified-Noncovered-Stay-Date)

- Short SAS Name: `NCOVFROM`
- Long SAS Name: `NCH_VRFD_NCVRD_STAY_FROM_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version H, the beginning date of the beneficiary's noncovered stay (used for internal CWFMQA editing purposes.)

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

??? derivation
	DERIVED FROM:
	CLM_OCRNC_SPAN_CD
	CLM_OCRNC_SPAN_FROM_DT
	
	DERIVATION RULES:
	Based on the presence of occurrence code 74, 76, 77 or 79 move the related occurrence from date to NCH_VRFY_NCOV_STAY_FROM_DT.

## [NCH Verified Noncovered Stay Through Date](https://www.resdac.org/cms-data/variables/NCH-Verified-Noncovered-Stay-Through-Date)

- Short SAS Name: `NCOVTHRU`
- Long SAS Name: `NCH_VRFD_NCVRD_STAY_THRU_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)

Effective with Version H, the ending date of the beneficiary's noncovered stay (used for internal CWFMQA editing purposes.)

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

??? derivation
	DERIVED FROM:
	CLM_OCRNC_SPAN_CD
	CLM_OCRNC_SPAN_THRU_DT
	
	DERIVATION RULES:
	Based on the presence of occurrence code 74, 76, 77 or 79 move the related occurrence thru date to NCH_VRFY_NCOV_STAY_THRU_DT.

## [NCH Weekly Claim Processing Date](https://www.resdac.org/cms-data/variables/NCH-Weekly-Claim-Processing-Date)

- Short SAS Name: `WKLY_DT`
- Long SAS Name: `NCH_WKLY_PROC_DT`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The date the weekly NCH database load process cycle begins, during which the claim records are loaded into the Nearline file. This date will always be a Friday, although the claims will actually be appended to the database subsequent to the date.



## [Operating Disproportionate Share Amount*](https://www.resdac.org/cms-data/variables/Operating-Disproportionate-Share-Amount)

- Short SAS Name: `DSH_OP`
- Long SAS Name: `DSH_OP_CLM_VAL_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Derived value created on extract from Claim value amount where value code = `18`.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Operating Indirect Medical Education (IME) Amount*](https://www.resdac.org/cms-data/variables/Operating-Indirect-Medical-Education-IME-Amount)

- Short SAS Name: `IME_OP`
- Long SAS Name: `IME_OP_CLM_VAL_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

Derived value created on extract from Claim value amount where value code = `19`.



## [Organization NPI Number](https://www.resdac.org/cms-data/variables/Organization-NPI-Number)

- Short SAS Name: `ORGNPINM`
- Long SAS Name: `ORG_NPI_NUM`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |
| Outpatient | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |
| Outpatient | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |
| Outpatient | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` | `orgnpinm` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [MedPAR RIF](../medpar-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

On an institutional claim, the National Provider Identifier (NPI) number assigned to uniquely identify the institutional provider certified by Medicare to provide services to the beneficiary.

NOTE: Effective May 2007, the NPI will be- come the national standard identifier for covered health care providers. NPIs will replace current OSCAR provider number, UPINs, NSC numbers, and local contractor provider identification numbers (PINs) on standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number (UPIN, PIN, OSCAR provider number, etc.)).

NOTE1: CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available in the NCH. After the 5/07 NPI implelmentation, the standard system main- tainers will add the legacy number to the claim when it is adjudicated. We will continue to receive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no NEW UPINs (legacy number) will be generated for NEW physicians (Part B and outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.



## [Patient Discharge Status Code](https://www.resdac.org/cms-data/variables/patient-discharge-status-code)

- Short SAS Name: `STUS_CD`
- Long SAS Name: `PTNT_DSCHRG_STUS_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the status of the patient as of the CLM_THRU_DT.



<h3>Values</h3>

EXPLANATION OF CLAIM ADJUSTMENT GROUP CODES
POSITIONS 1 & 2 OF ANSI CODE

| Code   | Code Value                                                                                                                                                                                                                                                                                                      |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Unknown Value (but present in data)                                                                                                                                                                                                                                                                             |
| 1      | Discharged to home/self care (routine charge).                                                                                                                                                                                                                                                                  |
| 2      | Discharged/transferred to other short term general hospital for inpatient care.                                                                                                                                                                                                                                 |
| 3      | Discharged/transferred to skilled nursing facility (SNF) with Medicare certification in anticipation of covered skilled care -- (For hospitals with an approved swing bed arrangement, use Code 61 - swing bed. For reporting discharges/transfers to a non-certified SNF, the hospital must use Code 04 - ICF. |
| 4      | Discharged/transferred to intermediate care facility (ICF).                                                                                                                                                                                                                                                     |
| 5      | Discharged/transferred to another type of institution for inpatient care (including distinct parts). NOTE: Effective 1/2005, psychiatric hospital or psychiatric distinct part unit of a hospital will no longer be identified by this code. New code is '65'                                                   |
| 6      | Discharged/transferred to home care of organized home health service organization.                                                                                                                                                                                                                              |
| 7      | Left against medical advice or discontinued care.                                                                                                                                                                                                                                                               |
| 8      | Discharged/transferred to home under care of a home IV drug therapy provider. (discontinued effective 10/1/05)                                                                                                                                                                                                  |
| 9      | Admitted as an inpatient to this hospital (effective 3/1/91). In situations where a patient is admitted before midnight of the third day following the day of an outpatient service, the outpatient services are considered inpatient.                                                                          |
| 20     | Expired (did not recover - Christian Science patient).                                                                                                                                                                                                                                                          |
| 21     | Discharged/transferred to Court/Law Enforcement                                                                                                                                                                                                                                                                 |
| 30     | Still patient                                                                                                                                                                                                                                                                                                   |
| 40     | Expired at home (hospice claims only)                                                                                                                                                                                                                                                                           |
| 41     | Expired in a medical facility such as hospital, SNF, ICF, or freestanding hospice. (Hospice claims only)                                                                                                                                                                                                        |
| 42     | Expired - place unknown (Hospice claims only)                                                                                                                                                                                                                                                                   |
| 43     | Discharged/transferred to a federal hospital (eff. 10/1/03)                                                                                                                                                                                                                                                     |
| 50     | Hospice - home (eff. 10/96)                                                                                                                                                                                                                                                                                     |
| 51     | Hospice - medical facility (eff. 10/96)                                                                                                                                                                                                                                                                         |
| 61     | Discharged/transferred within this institution to a hospital-based Medicare approved swing bed (eff. 9/01)                                                                                                                                                                                                      |
| 62     | Discharged/transferred to an inpatient rehabilitation facility including distinct parts units of a hospital. (eff. 1/2002)                                                                                                                                                                                      |
| 63     | Discharged/transferred to a long term care hospitals. (eff. 1/2002)                                                                                                                                                                                                                                             |
| 64     | Discharged/transferred to a nursing facility certified under Medicaid but not under Medicare (eff. 10/2002)                                                                                                                                                                                                     |
| 65     | Discharged/Transferred to a psychiatric hospital or psychiatric distinct unit of a hospital (these types of hospitals were pulled from patient/discharge status code '05' and given their own code). (eff. 1/2005).                                                                                             |
| 66     | Discharged/transferred to a Critical Access Hospital (CAH) (eff. 1/1/06)                                                                                                                                                                                                                                        |
| 69     | Discharged/transferred to a designated disaster alternative care site (eff. 10/2013)                                                                                                                                                                                                                            |
| 70     | Discharged/transferred to another type of health care institution not defined elsewhere in code list.                                                                                                                                                                                                           |
| 71     | Discharged/transferred/referred to another institution for outpatient services as specified by the discharge plan of care (eff. 9/01) (discontinued effective 10/1/05)                                                                                                                                          |
| 72     | Discharged/transferred/referred to this institution for outpatient services as specified by the discharge plan of care (eff. 9/01) (discontinued effective 10/1/05)                                                                                                                                             |
| 81     | Discharged to home or self-care with a planned acute care hospital readmission (eff. 10/2013)                                                                                                                                                                                                                   |
| 82     | Discharged/transferred to a short term general hospital for inpatient care with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                              |
| 83     | Discharged/transferred to a skilled nursing facility (SNF) with Medicare certification with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                  |
| 84     | Discharged/transferred to a facility that provides custodial or supportive care with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                         |
| 85     | Discharged/transferred to a designated cancer center or children’s hospital with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                             |
| 86     | Discharged/transferred to home under care of organized home health service organization with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                 |
| 87     | Discharged/transferred to court/law enforcement with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                                                         |
| 88     | Discharged/transferred to a federal health care facility with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                                                |
| 89     | Discharged/transferred to a hospital-based Medicare approved swing bed with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                                  |
| 90     | Discharged/transferred to an inpatient rehabilitation facility (IRF) including rehabilitation distinct part units of a hospital with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                         |
| 91     | Discharged/transferred to a Medicare certified long term care hospital (LTCH) with a planned acute care hospital inpatient readmission (eff. 10/2103)                                                                                                                                                           |
| 92     | Discharged/transferred to nursing facility certified under Medicaid but not certified under Medicare with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                    |
| 93     | Discharged/transferred to a psychiatric hospital/distinct part unit of a hospital with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                       |
| 94     | Discharged/transferred to a critical access hospital (CAH) with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                                                                              |
| 95     | Discharged/transferred to another type of health care institution not defined elsewhere in this code list with a planned acute care hospital inpatient readmission (eff. 10/2013)                                                                                                                               |

| Code   | Code Value                                                                                                                                                                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CO     | Contractual Obligations -- this group code should be used when a contractual agreement between the payer and payee, or a regulatory requirement, resulted in an adjustment. Generally, these adjustments are considered a write-off for the provider and are not billed to the patient.                 |
| CR     | Corrections and Reversals - this group code should be used for correcting a prior claim. It applies when there is a change to a previously adjudicated claim.                                                                                                                                           |
| OA     | Other Adjustments - this group code should be used when no other group code applies to the adjustment.                                                                                                                                                                                                  |
| PI     | Payer Initiated Reductions -- this group code should be used when, in the opinion of the payer, the adjustment is not the responsibility of the patient, but there is no supporting contract between the provider and the payer (i.e., medical review or professional review organization adjustments). |
| PR     | Patient Responsibility - this group should be used when the adjustment represents an amount that should be billed to the patient or insured. This group would typically be used for deductible and copay adjustments.                                                                                   |

| Code   | Code Value                                                                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Deductible Amount                                                                                                                                                                    |
| 2      | Coinsurance Amount                                                                                                                                                                   |
| 3      | Co-pay Amount                                                                                                                                                                        |
| 4      | The procedure code is inconsistent with the modifier used or a required modifier is missing.                                                                                         |
| 5      | The procedure code/bill type is inconsistent with the place of service.                                                                                                              |
| 6      | The procedure code is inconsistent with the patient's age.                                                                                                                           |
| 7      | The procedure code is inconsistent with the patient's gender.                                                                                                                        |
| 8      | The procedure code is inconsistent with the provider type.                                                                                                                           |
| 9      | The diagnosis is inconsistent with the patient's age.                                                                                                                                |
| 10     | The diagnosis is inconsistent with the patient's gender.                                                                                                                             |
| 11     | The diagnosis is inconsistent with the procedure.                                                                                                                                    |
| 12     | The diagnosis is inconsistent with the provider type.                                                                                                                                |
| 13     | the date of death precedes the date of service.                                                                                                                                      |
| 14     | The date of birth follows the date of service.                                                                                                                                       |
| 15     | Claim/service adjusted because the submitted authorization number is missing, invalid, or does not apply to the billed services or provider.                                         |
| 16     | Claim/service lacks information which is needed for adjudication.                                                                                                                    |
| 17     | Claim/service adjusted because requested information was not provided or was insufficient/incomplete.                                                                                |
| 18     | Duplicate claim/service.                                                                                                                                                             |
| 19     | Claim denied because this is a work-related injury/illness and thus the liability of the Worker's Compensation Carrier.                                                              |
| 20     | Claim denied because this injury/illness is covered by the liability carrier.                                                                                                        |
| 21     | Claim denied because this injury/illness is the liability of the no-fault carrier.                                                                                                   |
| 22     | Claim adjusted because this care may be covered by another payer per coordination of benefits.                                                                                       |
| 23     | Claim adjusted because charges have been paid by another payer.                                                                                                                      |
| 24     | Payment for charges adjusted. Charges are covered under a capitation agreement/managed care plan.                                                                                    |
| 25     | Payment denied. Your Stop loss deductible has not been met.                                                                                                                          |
| 26     | Expenses incurred prior to coverage.                                                                                                                                                 |
| 27     | Expenses incurred after coverage terminated.                                                                                                                                         |
| 28     | Coverage not in effect at the time the service was provided.                                                                                                                         |
| 29     | The time limit for filing has expired.                                                                                                                                               |
| 30     | Claim/service adjusted because the patient has not met the required eligibility, spend down, waiting, or residency requirements.                                                     |
| 31     | Claim denied as patient cannot be identified as our insured.                                                                                                                         |
| 32     | Our records indicate that this dependent is not an eligible dependent as defined.                                                                                                    |
| 33     | Claim denied. Insured has no dependent coverage.                                                                                                                                     |
| 34     | Claim denied. Insured has no coverage for newborns.                                                                                                                                  |
| 35     | Benefit maximum has been reached.                                                                                                                                                    |
| 36     | Balance does not exceed copayment amount.                                                                                                                                            |
| 37     | Balance does not exceed deductible amount.                                                                                                                                           |
| 38     | Services not provided or authorized by designated (network) providers.                                                                                                               |
| 39     | Services denied at the time authorization/pre-certification was requested.                                                                                                           |
| 40     | Charges do not meet qualifications for emergency/urgent care.                                                                                                                        |
| 41     | Discount agreed to in Preferred Provider contract.                                                                                                                                   |
| 42     | Charges exceed our fee schedule or maximum allowable amount.                                                                                                                         |
| 43     | Gramm-Rudman reduction.                                                                                                                                                              |
| 44     | Prompt-pay discount.                                                                                                                                                                 |
| 45     | Charges exceed your contracted/legislated fee arrangement.                                                                                                                           |
| 46     | This (these) service(s) is(are) not covered.                                                                                                                                         |
| 47     | This (these) diagnosis(es) is(are) not covered, missing, or are invalid.                                                                                                             |
| 48     | This (these) procedure(s) is(are) not covered.                                                                                                                                       |
| 49     | These are non-covered services because this is a routine exam or screening procedure done in conjunction with a routine exam.                                                        |
| 50     | These are non-covered services because this is not deemed a 'medical necessity' by the payer.                                                                                        |
| 51     | These are non-covered services because this a pre existing condition.                                                                                                                |
| 52     | The referring/prescribing/rendering provider is not eligible to refer/prescribe/order/perform the service billed.                                                                    |
| 53     | Services by an immediate relative or a member of the same household are not covered.                                                                                                 |
| 54     | Multiple physicians/assistants are not covered in this case.                                                                                                                         |
| 55     | Claim/service denied because procedure/treatment is deemed experimental/investigational by the payer.                                                                                |
| 56     | Claim/service denied because procedure/treatment has not been deemed 'proven to be effective' by payer.                                                                              |
| 57     | Claim/service adjusted because the payer deems the information submitted does not support this level of service, this many services, this length of service, or this dosage.         |
| 58     | Claim/service adjusted because treatment was deemed by the payer to have been rendered in an inappropriate or invalid place of service.                                              |
| 59     | Charges are adjusted based on multiple surgery rules or concurrent anesthesia rules.                                                                                                 |
| 60     | Charges for outpatient services with the proximity to inpatient services are not covered.                                                                                            |
| 61     | Charges adjusted as penalty for failure to obtain second surgical opinion.                                                                                                           |
| 62     | Claim/service denied/reduced for absence of, or exceeded, precertification/authorization.                                                                                            |
| 63     | Correction to a prior claim. INACTIVE                                                                                                                                                |
| 64     | Denial reversed per Medical Review. INACTIVE                                                                                                                                         |
| 65     | Procedure code was incorrect. This payment reflects the correct code. INACTIVE                                                                                                       |
| 66     | Blood Deductible.                                                                                                                                                                    |
| 67     | Lifetime reserve days. INACTIVE                                                                                                                                                      |
| 68     | DRG weight. INACTIVE                                                                                                                                                                 |
| 69     | Day outlier amount.                                                                                                                                                                  |
| 70     | Cost outlier amount.                                                                                                                                                                 |
| 71     | Primary Payer amount.                                                                                                                                                                |
| 72     | Coinsurance day. INACTIVE                                                                                                                                                            |
| 73     | Administrative days. INACTIVE                                                                                                                                                        |
| 74     | Indirect Medical Education Adjustment.                                                                                                                                               |
| 75     | Direct Medical Education Adjustment.                                                                                                                                                 |
| 76     | Disproportionate Share Adjustment.                                                                                                                                                   |
| 77     | Covered days. INACTIVE                                                                                                                                                               |
| 78     | Non-covered days/room charge adjustment.                                                                                                                                             |
| 79     | Cost report days. INACTIVE                                                                                                                                                           |
| 80     | Outlier days. INACTIVE                                                                                                                                                               |
| 81     | Discharges. INACTIVE                                                                                                                                                                 |
| 82     | PIP days. INACTIVE                                                                                                                                                                   |
| 83     | Total visits. INACTIVE                                                                                                                                                               |
| 84     | Capital adjustments. INACTIVE                                                                                                                                                        |
| 85     | Interest amount. INACTIVE                                                                                                                                                            |
| 86     | Statutory adjustment. INACTIVE                                                                                                                                                       |
| 87     | Transfer amounts.                                                                                                                                                                    |
| 88     | Adjustment amount represents collection against receivable created in prior overpayment.                                                                                             |
| 89     | Professional fees removed from charges.                                                                                                                                              |
| 90     | Ingredient cost adjustment.                                                                                                                                                          |
| 91     | Dispensing fee adjustment.                                                                                                                                                           |
| 92     | Claim paid in full. INACTIVE                                                                                                                                                         |
| 93     | No claim level adjustment. INACTIVE                                                                                                                                                  |
| 94     | Process in excess of charges.                                                                                                                                                        |
| 95     | Benefits adjusted. Plan procedures not followed.                                                                                                                                     |
| 96     | Non-covered charges.                                                                                                                                                                 |
| 97     | Payment is included in allowance for another service/procedure.                                                                                                                      |
| 98     | The hospital must file the Medicare claim for this inpatient non-physician service. INACTIVE                                                                                         |
| 99     | Medicare Secondary Payer Adjustment Amount. INACTIVE                                                                                                                                 |
| 100    | Payment made to patient/insured/responsible party.                                                                                                                                   |
| 101    | Predetermination: anticipated payment upon completion of services or claim ajudication.                                                                                              |
| 102    | Major medical adjustment.                                                                                                                                                            |
| 103    | Provider promotional discount (i.e. Senior citizen discount).                                                                                                                        |
| 104    | Managed care withholding.                                                                                                                                                            |
| 105    | Tax withholding.                                                                                                                                                                     |
| 106    | Patient payment option/election not in effect.                                                                                                                                       |
| 107    | Claim/service denied because the related or qualifying claim/service was not paid or identified on the claim.                                                                        |
| 108    | Claim/service reduced because rent/purchase guidelines were not met.                                                                                                                 |
| 109    | Claim not covered by this payer/contractor. You must send the claim to the correct payer/contractor.                                                                                 |
| 110    | Billing date predates service date.                                                                                                                                                  |
| 111    | Not covered unless the provider accepts assignment.                                                                                                                                  |
| 112    | Claim/service adjusted as not furnished directly to the patient and/or not documented.                                                                                               |
| 113    | Claim denied because service/procedure was provided outside the United States or as a result of war.                                                                                 |
| 114    | Procedure/PRODuct not approved by the Food and Drug Administration.                                                                                                                  |
| 115    | Claim/service adjusted as procedure postponed or canceled.                                                                                                                           |
| 116    | Claim/service denied. The advance indemnification notice signed by the patient did not comply with requirements.                                                                     |
| 117    | Claim/service adjusted because transportation is only covered to the closest facility that can provide the necessary care.                                                           |
| 118    | Charges reduced for ESRD network support.                                                                                                                                            |
| 119    | Benefit maximum for this time period has been reached.                                                                                                                               |
| 120    | Patient is covered by a managed care plan. INACTIVE                                                                                                                                  |
| 121    | Indemnification adjustment.                                                                                                                                                          |
| 122    | Psychiatric reduction.                                                                                                                                                               |
| 123    | Payer refund due to overpayment. INACTIVE                                                                                                                                            |
| 124    | Payer refund amount - not our patient. INACTIVE                                                                                                                                      |
| 125    | Claim/service adjusted due to a submission/billing error(s).                                                                                                                         |
| 126    | Deductible - Major Medical.                                                                                                                                                          |
| 127    | Coinsurance - Major Medical.                                                                                                                                                         |
| 128    | Newborn's services are covered in the mother's allowance.                                                                                                                            |
| 129    | Claim denied - prior processing information appears incorrect.                                                                                                                       |
| 130    | Paper claim submission fee.                                                                                                                                                          |
| 131    | Claim specific negotiated discount.                                                                                                                                                  |
| 132    | Prearranged demonstration project adjustment.                                                                                                                                        |
| 133    | The disposition of this claim/service is pending further review.                                                                                                                     |
| 134    | Technical fees removed from charges.                                                                                                                                                 |
| 135    | Claim denied. Interim bills cannot be processed.                                                                                                                                     |
| 136    | Claim adjusted. Plan procedures of a prior payer were not followed.                                                                                                                  |
| 137    | Payment/Reduction for Regulatory Surcharges, Assessments, Allowances or Health Related Taxes.                                                                                        |
| 138    | Claim/service denied. Appeal procedures not followed or time limits not met.                                                                                                         |
| 139    | Contracted funding agreement - subscriber is employed by the provider of services.                                                                                                   |
| 140    | Patient/Insured health identification number and name do not match.                                                                                                                  |
| 141    | Claim adjustment because the claim spans eligible and ineligible periods of coverage.                                                                                                |
| 142    | Claim adjusted by the monthly Medicaid patient liability amount.                                                                                                                     |
| A0     | Patient refund amount                                                                                                                                                                |
| A1     | Claim denied charges.                                                                                                                                                                |
| A2     | Contractual adjustment.                                                                                                                                                              |
| A3     | Medicare Secondary Payer liability met. INACTIVE                                                                                                                                     |
| A4     | Medicare Claim PPS Capital Day Outlier Amount.                                                                                                                                       |
| A5     | Medicare Claim PPS Capital Cost Outlier Amount.                                                                                                                                      |
| A6     | Prior hospitalization or 30 day transfer requirement not met.                                                                                                                        |
| A7     | Presumptive Payment Adjustment.                                                                                                                                                      |
| A8     | Claim denied; ungroupable DRG.                                                                                                                                                       |
| B1     | Non-covered visits.                                                                                                                                                                  |
| B2     | Covered visits. INACTIVE                                                                                                                                                             |
| B3     | Covered charges. INACTIVE                                                                                                                                                            |
| B4     | Late filing penalty.                                                                                                                                                                 |
| B5     | Claim/service adjusted because coverage/program guidelines were not met or were exceeded.                                                                                            |
| B6     | This service/procedure is adjusted when performed/billed by this type of provider, by this type of facility, or by a provider of this specialty.                                     |
| B7     | This provider was not certified/eligible to be paid for this procedure/service on this date of service.                                                                              |
| B8     | Claim/service not covered/reduced because alternative services were available, and should have been utilized.                                                                        |
| B9     | Services not covered because the patient is enrolled in a Hospice.                                                                                                                   |
| B10    | Allowed amount has been reduced because a component of the basic procedure/test was paid. The beneficiary is not liable for more than the charge limit for the basic procedure/test. |
| B11    | The claim/service has been transferred to the proper payer/processor for processing. Claim/service not covered by this payer/processor.                                              |
| B12    | Services not documented in patients' medical records.                                                                                                                                |
| B13    | Previously paid. Payment for this claim/service may have been provided in a previous payment.                                                                                        |
| B14    | Claim/service denied because only one visit or consultation per physician per day is covered.                                                                                        |
| B15    | Claim/service adjusted because this procedure/service is not paid separately.                                                                                                        |
| B16    | Claim/service adjusted because 'New Patient' qualifications were not met.                                                                                                            |
| B17    | Claim/service adjusted because this service was not prescribed by a physician, not prescribed prior to delivery, the prescription is incomplete, or the prescription is not current. |
| B18    | Claim/service denied because this procedure code/modifier was invalid on the date of service or claim submission.                                                                    |
| B19    | Claim/service adjusted because of the finding of a Review Organization. INACTIVE                                                                                                     |
| B20    | Charges adjusted because procedure/service was partially or fully furnished by another provider.                                                                                     |
| B21    | The charges were reduced because the service/care was partially furnished by another physician. INACTIVE                                                                             |
| B22    | This claim/service is adjusted based on the diagnosis.                                                                                                                               |
| B23    | Claim/service denied because this provider has failed an aspect of a proficiency testing program.                                                                                    |
| W1     | Workers Compensation State Fee Schedule Adjustment.                                                                                                                                  |

## [Provider Number](https://www.resdac.org/cms-data/variables/provider-number)

- Short SAS Name: `PROVIDER`
- Long SAS Name: `PRVDR_NUM`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `provider` | `provider` | `provider` | `provider` | `provider` |
| Outpatient | `provider` | `provider` | `provider` | `provider` | `provider` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `provider` | `provider` | `provider` | `provider` | `provider` |
| Outpatient | `provider` | `provider` | `provider` | `provider` | `provider` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `provider` | `provider` | `provider` | `provider` | `provider` |
| Outpatient | `provider` | `provider` | `provider` | `provider` | `provider` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The identification number of the institutional provider certified by Medicare to provide services to the beneficiary. NOTE: Effective October 1, 2007 the OSCAR Provider Number has been renamed the CMS Certification Number (CCN). The name was changed to avoid confusion with the National Provider Identifier (NPI). The CCN (OSCAR Provider Number) will continue to play a critical role in verifying that a provider has been Medicare certified and for what type of services.



<h3>Values</h3>



 Provider Number Table.txt 



## [Race Code from Claim](https://www.resdac.org/cms-data/variables/Race-Code-Claim)

- Short SAS Name: `RACE_CD`
- Long SAS Name: `BENE_RACE_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The race of a beneficiary.



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 0      | Unknown               |
| 1      | White                 |
| 2      | Black                 |
| 3      | Other                 |
| 4      | Asian                 |
| 5      | Hispanic              |
| 6      | North American Native |

## [Rendering Physician Specialty Code](https://www.resdac.org/cms-data/variables/rendering-physician-specialty-code)

- Short SAS Name: `RNDRNG_PHYSN_SPCLTY_CD`
- Long SAS Name: `REV_CNTR_PHYSN_SPCLTY_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify the CMS specilty code of the rendering physician/practitioner. 

(Revenue Center file)



<h3>Values</h3>

| Code   | Code Value                                                                                                                                              |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00     | Carrier wide                                                                                                                                            |
| 01     | General practice                                                                                                                                        |
| 02     | General surgery                                                                                                                                         |
| 03     | Allergy/immunology                                                                                                                                      |
| 04     | Otolaryngology                                                                                                                                          |
| 05     | Anesthesiology                                                                                                                                          |
| 06     | Cardiology                                                                                                                                              |
| 07     | Dermatology                                                                                                                                             |
| 08     | Family practice                                                                                                                                         |
| 09     | Interventional Pain Management (IPM) (eff. 4/1/03)                                                                                                      |
| 10     | Gastroenterology                                                                                                                                        |
| 11     | Internal medicine                                                                                                                                       |
| 12     | Osteopathic manipulative therapy                                                                                                                        |
| 13     | Neurology                                                                                                                                               |
| 14     | Neurosurgery                                                                                                                                            |
| 15     | Speech/language pathology                                                                                                                               |
| 16     | Obstetrics/gynecology                                                                                                                                   |
| 17     | Hospice and Palliative Care                                                                                                                             |
| 18     | Ophthalmology                                                                                                                                           |
| 19     | Oral surgery (dentists only)                                                                                                                            |
| 20     | Orthopedic surgery                                                                                                                                      |
| 21     | Cardiac Electrophysiology                                                                                                                               |
| 22     | Pathology                                                                                                                                               |
| 24     | Plastic and reconstructive surgery                                                                                                                      |
| 25     | Physical medicine and rehabilitation                                                                                                                    |
| 26     | Physchiatry                                                                                                                                             |
| 27     | General Psychiatry                                                                                                                                      |
| 28     | Colorectal surgery (formerly proctology)                                                                                                                |
| 29     | Pulmonary disease                                                                                                                                       |
| 30     | Diagnostic radiology                                                                                                                                    |
| 31     | Intensive cardiac rehabilitation                                                                                                                        |
| 32     | Anesthesiologist Assistants (eff. 4/1/03--previously grouped with Certified Registered Nurse Anesthetists (CRNA))                                       |
| 33     | Thoracic surgery                                                                                                                                        |
| 34     | Urology                                                                                                                                                 |
| 35     | Chiropractic                                                                                                                                            |
| 36     | Nuclear medicine                                                                                                                                        |
| 37     | Pediatric medicine                                                                                                                                      |
| 38     | Geriatric medicine                                                                                                                                      |
| 39     | Nephrology                                                                                                                                              |
| 40     | Hand surgery                                                                                                                                            |
| 41     | Optometrist                                                                                                                                             |
| 42     | Certified nurse midwife                                                                                                                                 |
| 43     | Certified Registered Nurse Anesthetist (CRNA) (Anesthesiologist Assistants were removed from this specialty 4/1/03)                                     |
| 44     | Infectious disease                                                                                                                                      |
| 45     | Mammography screening center                                                                                                                            |
| 46     | Endocrinology                                                                                                                                           |
| 47     | Independent Diagnostic Testing Facility (IDTF)                                                                                                          |
| 48     | Podiatry                                                                                                                                                |
| 49     | Ambulatory surgical center (formerly miscellaneous)                                                                                                     |
| 50     | Nurse practitioner                                                                                                                                      |
| 51     | Medical supply company with certified orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                            |
| 52     | Medical supply company with certified prosthetist (certified by American Board for Certification in Prosthetics and Orthotics)                          |
| 53     | Medical supply company with certified prosthetist-orthotist (certified by American Board for Certification in Prosthetics and Orthotics)                |
| 54     | Medical supply company for DMERC (and not included in 51-53)                                                                                            |
| 55     | Individual certified orthotist                                                                                                                          |
| 56     | Individual certified prosthetist                                                                                                                        |
| 57     | Individual certified prosthetist-orthotist                                                                                                              |
| 58     | Medical supply company with registered pharmacist                                                                                                       |
| 59     | Ambulance service supplier, (e.g., private ambulance companies, funeral homes, etc.)                                                                    |
| 60     | Public Health or welfare agencies (federal, state, and local)                                                                                           |
| 61     | Voluntary health or charitable agencies (e.g. National Cancer Society, National Heart Association, Catholic Charities)                                  |
| 62     | Psychologist (billing independently)                                                                                                                    |
| 63     | Portable X-ray supplier                                                                                                                                 |
| 64     | Audiologist (billing independently)                                                                                                                     |
| 65     | Physical therapist (private practice added 4/1/03) (independently practicing removed 4/1/03)                                                            |
| 66     | Rheumatology                                                                                                                                            |
| 67     | Occupational therapist (private practice added 4/103) (independently practicing removed 4/1/03)                                                         |
| 68     | Clinical psychologist                                                                                                                                   |
| 69     | Clinical laboratory (billing independently)                                                                                                             |
| 70     | Multispecialty clinic or group practice                                                                                                                 |
| 71     | Registered Dietician/Nutrition Professional (eff.1/1/02)                                                                                                |
| 72     | Pain Management (eff. 1/1/02)                                                                                                                           |
| 73     | Mass Immunization Roster Biller                                                                                                                         |
| 74     | Radiation Therapy Centers (prior to 4/2003 this included Independent Diagnostic Testing Facilities (IDFT))                                              |
| 75     | Slide Preparation Facilities (added to differentiate them from Independent Diagnostic Testing Facilities (IDTFs--eff. 4//1/03))                         |
| 76     | Peripheral vascular disease                                                                                                                             |
| 77     | Vascular surgery                                                                                                                                        |
| 78     | Cardiac surgery                                                                                                                                         |
| 79     | Addiction medicine                                                                                                                                      |
| 80     | Licensed clinical social worker                                                                                                                         |
| 81     | Critical care (intensivists)                                                                                                                            |
| 82     | Hematology                                                                                                                                              |
| 83     | Hematology/oncology                                                                                                                                     |
| 84     | Preventive medicine                                                                                                                                     |
| 85     | Maxillofacial surgery                                                                                                                                   |
| 86     | Neuropsychiatry                                                                                                                                         |
| 87     | All other suppliers (e.g. drug and department stores)                                                                                                   |
| 88     | Unknown supplier/provider specialty                                                                                                                     |
| 89     | Certified clinical nurse specialist                                                                                                                     |
| 90     | Medical oncology                                                                                                                                        |
| 91     | Surgical oncology                                                                                                                                       |
| 92     | Radiation oncology                                                                                                                                      |
| 93     | Emergency medicine                                                                                                                                      |
| 94     | Interventional radiology                                                                                                                                |
| 95     | Competitive Acquisition Program (CAP) Vendor (eff. 07/01/06). Prior to 07/01/06, known as Independent physiological laboratory                          |
| 96     | Optician                                                                                                                                                |
| 97     | Physician assistant                                                                                                                                     |
| 98     | Gynecologist/oncologist                                                                                                                                 |
| 99     | Unknown physician specialty                                                                                                                             |
| A0     | Hospital (DMERCs only)                                                                                                                                  |
| A1     | SNF (DMERCs only)                                                                                                                                       |
| A2     | Intermediate care nursing facility (DMERCs only)                                                                                                        |
| A3     | Nursing facility, other (DMERCs only)                                                                                                                   |
| A4     | Home Health Agency (DMERCs only)                                                                                                                        |
| A5     | Pharmacy (DMERC)                                                                                                                                        |
| A6     | Medical supply company with respiratory therapist (DMERCs only)                                                                                         |
| A7     | Department store (DMERC)                                                                                                                                |
| A8     | Grocery store (DMERC)                                                                                                                                   |
| A9     | Indian Health Service (IHS), tribe and tribal organizations (non-hospital or non-hospital based facilities, eff. 1/2005)                                |
| B1     | Supplier of oxygen and/or oxygen related equipment (eff. 10/2/07)                                                                                       |
| B2     | Pedorthic Personnel (eff. 10/2/07)                                                                                                                      |
| B3     | Medical Supply Company with pedorthic personnel (eff. 10/2/07)                                                                                          |
| B4     | Does not meet definition of health care provider (e.g., Rehabilitation agency, organ procurement organizations, histocompatibility labs) (eff. 10/2/07) |
| B5     | Ocularist                                                                                                                                               |
| C0     | Sleep medicine                                                                                                                                          |
| C1     | Centralized flu                                                                                                                                         |
| C2     | Indirect payment procedure                                                                                                                              |
| C3     | Interventional cardiology                                                                                                                               |
| C5     | Dentist (eff. 7/2016)                                                                                                                                   |

## [Revenue Center Code](https://www.resdac.org/cms-data/variables/revenue-center-code)

- Short SAS Name: `REV_CNTR`
- Long SAS Name: `REV_CNTR`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` |
| Outpatient | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Inpatient  | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` |
| Outpatient | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rev_cntr` |

| Dataset    | 2003       | 2002       | 2001       | 2000     | 1999     |
|:-----------|:-----------|:-----------|:-----------|:---------|:---------|
| Inpatient  | `rev_cntr` | `rev_cntr` | `rvcntr`   | `rvcntr` | `rvcntr` |
| Outpatient | `rev_cntr` | `rev_cntr` | `rev_cntr` | `rvcntr` | `rvcntr` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The provider-assigned revenue code for each cost center for which a separate charge is billed (type of accommodation or ancillary). A cost center is a division or unit within a hospital (e.g., radiology, emergency room, pathology). EXCEPTION: Revenue center code 0001 represents the total of all revenue centers included on the claim.



<h3>Values</h3>



 Revenue Center Table.txt 



## [Revenue Center Deductible Coinsurance Code](https://www.resdac.org/cms-data/variables/Revenue-Center-Deductible-Coinsurance-Code)

- Short SAS Name: `REVDEDCD`
- Long SAS Name: `REV_CNTR_DDCTBL_COINSRNC_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Code indicating whether the revenue center charges are subject to deductible and/or coinsurance



<h3>Values</h3>

For revenue center code 0001, the following MSP override values may be present:

| Code   | Code Value                                                                                                       |
|:-------|:-----------------------------------------------------------------------------------------------------------------|
| 0      | Charges are subject to deductible and coinsurance                                                                |
| 1      | Charges are not subject to deductible                                                                            |
| 2      | Charges are not subject to coinsurance                                                                           |
| 3      | Charges are not subject to deductible or coinsurance                                                             |
| 4      | No charge or units associated with this revenue center code. (For multiple HCPCS per single revenue center code) |

| Code   | Code Value                                                                                                         |
|:-------|:-------------------------------------------------------------------------------------------------------------------|
| M      | Override code; EGHP services involved (eff 12/90 for non-institutional claims; 10/93 for institutional claims)     |
| N      | Override code; non-EGHP services involved (eff 12/90 for non-institutional claims; 10/93 for institutional claims) |
| X      | Override code: MSP cost avoided (eff 12/90 for non-institutional claims; 10/93 for institutional claims)           |

## [Revenue Center HCFA Common Procedure Coding System](https://www.resdac.org/cms-data/variables/Revenue-Center-HCFA-Common-Procedure-Coding-System)

- Short SAS Name: `HCPCS_CD`
- Long SAS Name: `HCPCS_CD`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    |            | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |
| Inpatient  | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |
| Outpatient | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |
| Inpatient  | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |
| Outpatient | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999     |
|:-----------|:-----------|:-----------|:-----------|:-----------|:---------|
| Carrier    | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `bhcpcs` |
| Inpatient  | `hcpcs_cd` | `hcpcs_cd` | `hcpscd`   | `hcpscd`   | `hcpscd` |
| Outpatient | `hcpcs_cd` | `hcpcs_cd` | `hcpcs_cd` | `hcpscd`   | `hcpscd` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The Health Care Common Procedure Coding System (HCPCS) is a collection of codes that represent procedures, supplies, products and services which may be provided to Medicare beneficiaries and to individuals enrolled in private health insurance programs. The codes are divided into three levels, or groups as described below:

Level I: Codes and descriptors copyrighted by the American Medical Association's Current Procedural Terminology, Fourth Edition (CPT-4).  These are 5 position numeric codes representing physician and nonphysician services.

*Note: CPT-4 codes including both long and short descriptions shall be used in accordance with the CMS/AMA agreement.  Any other use violates the AMA copyright.

Level II: Includes codes and descriptors copyrighted by the American Dental Association's Current Dental Terminology, Fifth Edition (CDT-5).  These are 5 position alpha-numeric codes comprising the D series.  All other level II codes and descriptors are approved and maintained jointly by the alpha-numeric editorial panel (consisting of CMS, the Health Insurance Association of America, and the Blue Cross and Blue Shield Association).  These are 5 position alpha-numeric codes representing primarily items and nonphysician services that are not represented in the level I codes.

Level III: Codes and descriptors developed by Medicare carriers for use at the local (carrier) level. These are 5 position alpha-numeric codes in the W, X, Y or Z series representing physician and nonphysician services that are not represented in the level I or level II codes.

HCPCS - General Information (CMS Website)



## [Revenue Center HCPCS Initial Modifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-HCPCS-Initial-Modifier-Code)

- Short SAS Name: `MDFR_CD1`
- Long SAS Name: `HCPCS_1ST_MDFR_CD`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    |            | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` |
| Outpatient | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` |
| Outpatient | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `bhmod1`  |
| Outpatient | `mdfr_cd1` | `mdfr_cd1` | `mdfr_cd1` | `mdfcd1_`  | `mdfcd1_` |

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

A first modifier to the HCPCS procedure code to enable a more specific procedure identification for the line item service on the noninstitutional claim.



## [Revenue Center HCPCS Second Modifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-HCPCS-Second-Modifier-Code)

- Short SAS Name: `MDFR_CD2`
- Long SAS Name: `HCPCS_2ND_MDFR_CD`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    |            | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` |
| Outpatient | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` |
| Outpatient | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` |

| Dataset    | 2003       | 2002       | 2001       | 2000       | 1999      |
|:-----------|:-----------|:-----------|:-----------|:-----------|:----------|
| Carrier    | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `bhmod2`  |
| Outpatient | `mdfr_cd2` | `mdfr_cd2` | `mdfr_cd2` | `mdfcd2_`  | `mdfcd2_` |

Contained in

- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

A second modifier to the HCPCS procedure code to make it more specific than the first modifier code to identify the line item procedures for this claim.



## [Revenue Center IDE, NDC, or UPC Number](https://www.resdac.org/cms-data/variables/revenue-center-ide-ndc-or-upc-number)

- Short SAS Name: `IDENDC`
- Long SAS Name: `REV_CNTR_IDE_NDC_UPC_NUM`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

This field may contain one of three types of identifiers: the National Drug Code (NDC), the Universal Product Code (UPC), or the number assigned by the Food and Drug Administration (FDA) to an investigational device (IDE) after the manufacturer has approval to conduct a clinical trial.The IDEs will have a revenue center code `0624`.

This field was renamed to eventually accommodate the National Drug Code (NDC) and the Universal Product Code (UPC). This field could contain either of these 3 fields (there would never be an instance where more than one would come in on a claim).
The size of this field was expanded to X(24) to accommodate either of the new fields (under Version 'H' it was X(7).



## [Revenue Center NDC Quantity](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity)

- Short SAS Name: `REV_CNTR_NDC_QTY`
- Long SAS Name: `REV_CNTR_NDC_QTY`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version 'J', the quantity dispensed for the drug reflected on the revenue center line item.



## [Revenue Center NDC Quantity Qualifier Code](https://www.resdac.org/cms-data/variables/Revenue-Center-NDC-Quantity-Qualifier-Code)

- Short SAS Name: `REV_CNTR_NDC_QTY_QLFR_CD`
- Long SAS Name: `REV_CNTR_NDC_QTY_QLFR_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate the unit of measurement for the drug that was administered.



<h3>Values</h3>

| Code   | Code Value         |
|:-------|:-------------------|
| F2     | International Unit |
| GR     | Gram               |
| ML     | Milliliter         |
| UN     | Unit               |

## [Revenue Center Non-Covered Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Non-Covered-Charge-Amount)

- Short SAS Name: `REV_NCVR`
- Long SAS Name: `REV_CNTR_NCVRD_CHRG_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_ncvr` | `rev_ncvr` | `rev_ncvr` | `rev_ncvr` | `rev_ncvr` |

| Dataset    | 2008       | 2007       | 2006       | 2000     | 1999     |
|:-----------|:-----------|:-----------|:-----------|:---------|:---------|
| Outpatient | `rev_ncvr` | `rev_ncvr` | `rev_ncvr` | `rvncvr` | `rvncvr` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The charge amount related to a revenue center code for services that are not covered by Medicare.

NOTE: Prior to Version H the field size was S9(7)V99 and the element was only present on the Inpatient/SNF format. As of NCH weekly process date 10/3/97 this field was added to all institutional claim types.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Revenue Center Pricing Indicator Code](https://www.resdac.org/cms-data/variables/revenue-center-pricing-indicator-code-0)

- Short SAS Name: `REV_CNTR_PRCNG_IND_CD`
- Long SAS Name: `REV_PRICNG_IND_CD`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The code used to identify if there was a deviation from the standard method of calculating payment amount.

This field is populated for those claims that are required to process through the Outpatient PPS PRICER software. The type of bills (TOB) required to process through are: 12X,13X, 14X (except Maryland providers, Indian Health Providers, hospitals located in American Samoa, Guam and Saipan and Critical Access Hospitals [CAH]); 76X; 75X and 34X if certain HCPCS are on the bill; and any outpatient type of bill with a condition code `07` and certain HCPCS. These claim types could have lines that are not required to price under OPPS rules so those lines would not have data in this field.
Additional exception: Virgin Island hospitals and hospitals that furnish only inpatient Part B services with dates of service 1/1/02 and forward.
It has been discovered that this field may be populated with data on claims with dates of service prior to 7/00 (implementation of Claim Line Expansion OPPS/HHPPS). The original understanding of the new revenue center fields was that data would be populated on claims with dates of service 7/00 and forward. Data has been found in claims with dates of service prior to 7/00 because the Standard Systems have processed any claim coming in 7/00 and after, meeting the above criteria, through the Outpatient Code Editor (OCE) regardless of the dates of service.
VALUES D, U & T REPRESENT THE FOLLOWING:
D = Discounting fraction (currently 0.5)
U = Number of units
T = Terminated procedure discount (currently 0.5)



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A      | A valid HCPCS code not subject to a fee schedule payment. Reimbursement is calculated on provider submitted charges.                                                                                                                                                                                                                                                                                                                                                                       |
| B      | A valid HCPCS code subject to the fee schedule payment. for the provider billed charges. NOTE: There is an exception for Critical Access Hospitals (provider numbers XX1300-XX1399) with reimbursement method 'J' (all-inclusive method) and dates of service on or after 7/1/01. In these situations, reimbursement for professional services (revenue codes 96X, 97X, 98X) is always at the fee schedule amount of logic is not applicable.                                              |
| C      | Unlisted Rehabilitation Carrier Priced HCPCS                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| D      | A valid radiology HCPCS code subject to the Radiology Pricer and the rate is reflected as zeroes on the HCPCS file and cost report. The Radiology Pricer treats this HCPCS as a non-covered service. Reimbursement is calculated on provider submitted charges.                                                                                                                                                                                                                            |
| E      | A valid ASC HCPCS code subject to the ASC Pricer. The rate is reflected as zeroes on the HCPCS file. The ASC Pricer determines the ASC payment rate and is reported on the cost report.                                                                                                                                                                                                                                                                                                    |
| F      | A valid ESRD HCPCS code subject to the parameter rate. Reimbursement is the lesser of provider submitted charges or the fee schedule amount for non-dialysis HCPCS. Reimbursement is calculated on the provider file rates for dialysis HCPCS. NOTE: The ESRD Pricing Indicator is used when processing the ESRD claim. The non-ESRD pricing indicator is used only for Inpatient claims as follows: valid Hemophilia HCPCS for inpatient claim only and code is summed to parameter rate. |
| G      | A valid HCPCS, code is subject to a fee schedule, but the rate is no longer present on the HCPCS file. Reimbursement is calculated on provider submitted charges.                                                                                                                                                                                                                                                                                                                          |
| H      | A valid DME HCPCS, code is subject to a fee schedule. The rates are reflected under the DME segment. Reimbursement is calculated either on a fee schedule, Medicare FFS Claims (Version K) Codebook 522 May 2017 provider submitted charges or the lesser of provider submitted, or the fee schedule depending on the category of DME.                                                                                                                                                     |
| I      | A valid DME category 5 HCPCS, HCPCS is not found on the DME history record, but a match was found on HIC, category and generic code. Claim must be reviewed by Medical Review before payment can be calculated.                                                                                                                                                                                                                                                                            |
| J      | A valid DME HCPCS, no DME history is present, and a prescription is required before delivery. Claim must be reviewed by Medical Review.                                                                                                                                                                                                                                                                                                                                                    |
| K      | A valid DME HCPCS, prescribed has been reviewed, and fee schedule payment is approved as prescription was present before delivery.                                                                                                                                                                                                                                                                                                                                                         |
| L      | A valid TENS HCPCS, rental period is six months or greater and must be reviewed by Medical Review. This code will be automatically set by the system.                                                                                                                                                                                                                                                                                                                                      |
| M      | A valid TENS HCPCS, Medical Review has approved the rental charge in excess of five months. This must be set by Medical Review. This must be set by Medical Review when approved for payment.                                                                                                                                                                                                                                                                                              |
| N      | Paid based on the fee amount for non ESRD TOB's. NOTE: Fee amount is paid regardless of charges.                                                                                                                                                                                                                                                                                                                                                                                           |
| Q      | Manual pricing                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R      | A valid radiology HCPCS code and is subject to APC. The rate is reported on the cost report. Reimbursement is calculated on provider submitted charges.                                                                                                                                                                                                                                                                                                                                    |
| S      | Valid influenza/PPV HCPCS. A fee amount is not applicable. The amount payable is present in the covered charge field. This amount is not subject to the coinsurance and deductible. This charge is subject to the provider's reimbursement rate.                                                                                                                                                                                                                                           |
| T      | Valid HCPCS. A fee amount is present. The amount payable should be the lower of the billed charge or fee amount. The system should compute the fee amount by multiplying the covered units times the rate. The fee amount is not subject to coinsurance and deductible or provider's reimbursement rate.                                                                                                                                                                                   |
| U      | Valid ambulance HCPCS. A fee amount is present. The amount payable is a blended amount based on a percentage of the fee schedule and a percentage of the reasonable cost. The fee amount is subject to coinsurance and deductible.                                                                                                                                                                                                                                                         |
| X      | Unclassified drug as subject to manual pricing.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## [Revenue Center Rate Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Rate-Amount)

- Short SAS Name: `REV_RATE`
- Long SAS Name: `REV_CNTR_RATE_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_rate` | `rev_rate` | `rev_rate` | `rev_rate` | `rev_rate` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_rate` | `rev_rate` | `rev_rate` | `rev_rate` | `rev_rate` |

| Dataset    | 2003       | 2002       | 2001       | 2000   | 1999   |
|:-----------|:-----------|:-----------|:-----------|:-------|:-------|
| Outpatient | `rev_rate` | `rev_rate` | `rev_rate` | `rvrt` | `rvrt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Charges relating to unit cost associated with the revenue center code. Exception (encounter data only): If plan (e.g. MCO) does not know the actual rate for the accommodations, $1 will be reported in the field.

NOTE1: For SNF PPS claims (when revenue center code equals `0022`), CMS has developed a SNF PRICER to compute the rate based on the provider supplied coding for the MDS RUGS III group and assessment type (HIPPS code, stored in revenue center HCPCS code field).

NOTE2: For OP PPS claims, CMS has developed a PRICER to compute the rate based on the Ambulatory Payment Classification (APC), discount factor, units of service and the wage index.

NOTE3: Under HH PPS (when revenue center code equals `0023`), CMS has developed a HHA PRICER to compute the rate. On the RAP, the rate is determined using the case mix weight associated with the HIPPS code, adjusting it for the wage index for the beneficiary's site of service, then multiplying the result by 60% or 50%, depending on whether or not the RAP is for a first episode.

On the final claim, the HIPPS code could change the payment if the therapy threshold is not met, or partial episode payment (PEP) adjustment or a significant change in condition (SCIC) adjustment. In cases of SCICs, there will be more than one `0023` revenue center line, each representing the payment made at each case-mix level.

NOTE4: For IRF PPS claims (when revenue center code equals `0024`), CMS has developed a PRICER to compute the rate based on the HIPPS/CMG (HIPPS code, stored in revenue center HCPCS code field).



## [Revenue Center Rendering Physician NPI](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-NPI)

- Short SAS Name: `RNDRNG_PHYSN_NPI`
- Long SAS Name: `REV_CNTR_RNDRNG_PHYSN_NPI_NUM`

<h3>Variable Names</h3>

| Dataset    | 2013               | 2012               | 2011               | 2010               |
|:-----------|:-------------------|:-------------------|:-------------------|:-------------------|
| Outpatient | `rndrng_physn_npi` | `rndrng_physn_npi` | `rndrng_physn_npi` | `rndrng_physn_npi` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

Effective with Version 'J', the NPI of the rendering physician who performed the service.



## [Revenue Center Rendering Physician UPIN](https://www.resdac.org/cms-data/variables/Revenue-Center-Rendering-Physician-UPIN)

- Short SAS Name: `RNDRNG_PHYSN_UPIN`
- Long SAS Name: `RNDRNG_PHYSN_UPIN`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Outpatient | `rndrng_physn_upin` | `rndrng_physn_upin` | `rndrng_physn_upin` | `rndrng_physn_upin` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)





## [Revenue Center Therapy Cap Indicator 1 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-1-code)

- Short SAS Name: `THRPY_CAP_IND_CD1`
- Long SAS Name: `THRPY_CAP_IND_CD1`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The field used to identify whether the claim line is subject to a therapy cap.

Details regarding the therapy cap can be found on the CMS website, under the Medicare therapy services web page (see, for example: https://www.cms.gov/Medicare/Billing/TherapyServices/index.html).



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                   |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A      | Hospital outpatient claims are subject to the therapy cap for this date of service (this indicator is used on institutional claims only).                                                                                                                                                                                                                    |
| B      | Critical Access Hospital outpatient claims are subject to the therapy cap for this date of service (this indicator will be used on institutional claims only). Note: Currently, Critical Access Hospital claims are not subject to any therapy cap policies. Indicator B is created here to prepare for possible future legislation to include these claims. |
| C      | The therapy cap exceptions process, as indicated by the submission of the KX modifier, no longer applies for this date of service (this indicator will be used on both institutional and professional claims).                                                                                                                                               |
| D      | The $3,700 threshold for review therapy services no longer applies for this date of service (this indicator will be used on both institutional and professional claims).                                                                                                                                                                                     |

## [Revenue Center Therapy Cap Indicator 2 Code](https://www.resdac.org/cms-data/variables/revenue-center-therapy-cap-indicator-2-code)

- Short SAS Name: `THRPY_CAP_IND_CD2`
- Long SAS Name: `THRPY_CAP_IND_CD2`

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The field used to identify whether the claim line is subject to a therapy cap.

Details regarding the therapy cap can be found on the CMS website, under the Medicare therapy services web page (see, for example: https://www.cms.gov/Medicare/Billing/TherapyServices/index.html).



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                                                                                                                                                                                                                   |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A      | Hospital outpatient claims are subject to the therapy cap for this date of service (this indicator is used on institutional claims only).                                                                                                                                                                                                                    |
| B      | Critical Access Hospital outpatient claims are subject to the therapy cap for this date of service (this indicator will be used on institutional claims only). Note: Currently, Critical Access Hospital claims are not subject to any therapy cap policies. Indicator B is created here to prepare for possible future legislation to include these claims. |
| C      | The therapy cap exceptions process, as indicated by the submission of the KX modifier, no longer applies for this date of service (this indicator will be used on both institutional and professional claims).                                                                                                                                               |
| D      | The $3,700 threshold for review therapy services no longer applies for this date of service (this indicator will be used on both institutional and professional claims).                                                                                                                                                                                     |

## [Revenue Center Total Charge Amount](https://www.resdac.org/cms-data/variables/Revenue-Center-Total-Charge-Amount)

- Short SAS Name: `REV_CHRG`
- Long SAS Name: `REV_CNTR_TOT_CHRG_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_chrg` | `rev_chrg` | `rev_chrg` | `rev_chrg` | `rev_chrg` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_chrg` | `rev_chrg` | `rev_chrg` | `rev_chrg` | `rev_chrg` |

| Dataset    | 2003       | 2002       | 2001       | 2000     | 1999     |
|:-----------|:-----------|:-----------|:-----------|:---------|:---------|
| Outpatient | `rev_chrg` | `rev_chrg` | `rev_chrg` | `rvchrg` | `rvchrg` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

The total charges (covered and non-covered) for all accommodations and services (related to the revenue code) for a billing period before reduction for the deductible and coinsurance amounts and before an adjustment for the cost of services provided. NOTE: For accommodation revenue center total charges must equal the rate times units (days).

EXCEPTIONS:

(1) For SNF RUGS demo claims only (9000 series revenue center codes), this field contains SNF customary accommodation charge, (ie., charges related to the accommodation revenue center code that would have been applicable if the provider had not been participating in the demo).

(2) For SNF PPS (non demo claims), when revenue center code = `0022`, the total charges will be zero.

(3) For Home Health PPS (RAPs), when revenue center code = `0023`, the total charges will equal the dollar amount for the `0023` line.

(4) For Home Health PPS (final claim), when revenue center code = `0023`, the total charges will be the sum of the revenue center code lines (other than `0023`).

(5) For Inpatient Rehabilitation Facility (IFR) PPS, when the revenue center code = `0024`, the total charges will be zero. For accommodation revenue codes (010X - 021X), total charges must equal the rate times the units.

(6) For encounter data, if the plan (e.g. MCO) does not know the actual charges for the accommodations the total charges will be $1 (rate) times units (days).

??? limitation
	DESCRIPTION :
	Multiple total charge '0001' revenue center codes appearing
	on outpatient, hospice and home health claim records.
	BACKGROUND :
	On outpatient, home health and hospice it appears that
	more than one '0001' revenue center code is showing
	up on the claims. The first total charge line adds
	the revenue center codes above it correctly; the
	problem exists below the first total charge line
	where garbage may be present due to the FI Standard
	System not clearing out fields before processing the
	next claim. We believe the error began with the change-
	over to a different claims processing contractor in
	1/98.
	CORRECTIVE ACTION :
	CWF created an edit to reject mulitple '0001' revenue
	center codes, effective 6/28/99. EDG's CWFMQA process
	implemented an edit to drop any revenue center line
	items below the first total charge line. The NCH
	Nearline File, as well as the 1998 Standard Analytic
	Files (SAFs), have been patched/corrected to delete
	the multiple '0001' codes where present on any of the
	institutional claim types. Also, HCIS will be cor-
	recting the revenue center summaries during the next
	refresh.
	The NCH_PATCH_CD field will reflect a value '10'.

<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Revenue Center Unit Count](https://www.resdac.org/cms-data/variables/Revenue-Center-Unit-Count)

- Short SAS Name: `REV_UNIT`
- Long SAS Name: `REV_CNTR_UNIT_CNT`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_unit` | `rev_unit` | `rev_unit` | `rev_unit` | `rev_unit` |

| Dataset    | 2008       | 2007       | 2006       | 2005       | 2004       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Outpatient | `rev_unit` | `rev_unit` | `rev_unit` | `rev_unit` | `rev_unit` |

| Dataset    | 2003       | 2002       | 2001       | 2000    | 1999    |
|:-----------|:-----------|:-----------|:-----------|:--------|:--------|
| Outpatient | `rev_unit` | `rev_unit` | `rev_unit` | `rvunt` | `rvunt` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)

A quantitative measure (unit) of the number of times the service or procedure being reported was performed according to the revenue center/HCPCS code definition as described on an institutional claim.

Depending on type of service, units are measured by number of covered days in a particular accommodation, pints of blood, emergency room visits, clinic visits, dialysis treatments (sessions or days), outpatient therapy visits, and outpatient clinical diagnostic laboratory tests.

NOTE1: When revenue center code = `0022` (SNF PPS) the unit count will reflect the number of covered days for each HIPPS code and, if applicable, the number of visits for each rehab therapy code.

Description of the different unit of service measures by revenue center code beginning on page 18: http://cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c25.pdf



## [Standard Payment Amount](https://www.resdac.org/cms-data/variables/standard-payment-amount)

- Short SAS Name: `PPS_STD_VAL_PYMT_AMT`
- Long SAS Name: `PPS_STD_VAL_PYMT_AMT`

Contained in

- [Inpatient RIF](../ip-rif.md#data-documentation)

This amount identifies the standardized Medicare payment amount.

This is the standardized amount as determined by PRICER software output.  This amount is never used for payments. It is used for comparisons across different regions of the country for the value-based purchasing initiatives and for research. It is a standard amount, without the geographical payment adjustments and some of the other add-on payments that actually go to the hospitals.    

This field is new in October 2014. This field only applies to Inpatient claims. Note that an additional field is available that further adjusts the standard Medicare Payment amount by applying additional standardization requirements (e.g. sequestration).   

Refer to variable called the final standardized amount (FINL_STD_AMT).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [State Code from Claim (SSA)](https://www.resdac.org/cms-data/variables/state-code-claim-ssa)

- Short SAS Name: `STATE_CD`
- Long SAS Name: `BENE_STATE_CD`

<h3>Variable Names</h3>

| Dataset    | 2013       | 2012       | 2011       | 2010       | 2009       |
|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier    |            | `state_cd` | `state_cd` | `state_cd` | `state_cd` |
| Inpatient  | `state_cd` | `state_cd` | `state_cd` | `state_cd` | `state_cd` |
| MedPAR     | `state_cd` | `state_cd` | `state_cd` | `state_cd` | `state_cd` |
| Outpatient | `state_cd` | `state_cd` | `state_cd` | `state_cd` | `state_cd` |

| Dataset    | 2008       | 2007       | 2006       | 2005    | 2004    |
|:-----------|:-----------|:-----------|:-----------|:--------|:--------|
| Carrier    | `state_cd` | `state_cd` | `state_cd` | `state` | `state` |
| Inpatient  | `state_cd` | `state_cd` | `state_cd` | `state` | `state` |
| MedPAR     | `state_cd` | `state_cd` | `state_cd` | `state` | `state` |
| Outpatient | `state_cd` | `state_cd` | `state_cd` | `state` | `state` |

| Dataset    | 2003    | 2002    | 2001       | 2000       | 1999       |
|:-----------|:--------|:--------|:-----------|:-----------|:-----------|
| Carrier    | `state` | `state` | `state_cd` | `state_cd` | `bstate`   |
| Inpatient  | `state` | `state` | `state_cd` | `state_cd` | `state_cd` |
| MedPAR     | `state` | `state` | `mstate`   | `mstate`   | `mstate`   |
| Outpatient | `state` | `state` | `state`    | `state_cd` | `state_cd` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The SSA standard state code of a beneficiary's residence.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 1      | Alabama                         |
| 2      | Alaska                          |
| 3      | Arizona                         |
| 4      | Arkansas                        |
| 5      | California                      |
| 6      | Colorado                        |
| 7      | Connecticut                     |
| 8      | Delaware                        |
| 9      | District of Columbia            |
| 10     | Florida                         |
| 11     | Georgia                         |
| 12     | Hawaii                          |
| 13     | Idaho                           |
| 14     | Illinois                        |
| 15     | Indiana                         |
| 16     | Iowa                            |
| 17     | Kansas                          |
| 18     | Kentucky                        |
| 19     | Louisiana                       |
| 20     | Maine                           |
| 21     | Maryland                        |
| 22     | Massachusetts                   |
| 23     | Michigan                        |
| 24     | Minnesota                       |
| 25     | Mississippi                     |
| 26     | Missouri                        |
| 27     | Montana                         |
| 28     | Nebraska                        |
| 29     | Nevada                          |
| 30     | New Hampshire                   |
| 31     | New Jersey                      |
| 32     | New Mexico                      |
| 33     | New York                        |
| 34     | North Carolina                  |
| 35     | North Dakota                    |
| 36     | Ohio                            |
| 37     | Oklahoma                        |
| 38     | Oregon                          |
| 39     | Pennsylvania                    |
| 40     | Puerto Rico                     |
| 41     | Rhode Island                    |
| 42     | South Carolina                  |
| 43     | South Dakota                    |
| 44     | Tennessee                       |
| 45     | Texas                           |
| 46     | Utah                            |
| 47     | Vermont                         |
| 48     | Virgin Islands                  |
| 49     | Virginia                        |
| 50     | Washington                      |
| 51     | West Virginia                   |
| 52     | Wisconsin                       |
| 53     | Wyoming                         |
| 54     | Africa                          |
| 55     | Asia                            |
| 56     | Canada                          |
| 57     | Central America and West Indies |
| 58     | Europe                          |
| 59     | Mexico                          |
| 60     | Oceania                         |
| 61     | Philippines                     |
| 62     | South America                   |
| 63     | U.S. Possessions                |
| 97     | Saipan - MP                     |
| 98     | Guam                            |
| 99     | American Samoa                  |

## [Zip Code of Residence from Claim](https://www.resdac.org/cms-data/variables/Zip-Code-Residence-Claim)

- Short SAS Name: `ZIP_CD`
- Long SAS Name: `BENE_MLG_CNTCT_ZIP_CD`

<h3>Variable Names</h3>

| Dataset    | 2013     | 2012     | 2011     | 2010     | 2009     |
|:-----------|:---------|:---------|:---------|:---------|:---------|
| Carrier    |          | `zip_cd` | `zip_cd` | `zip_cd` | `zip_cd` |
| Inpatient  | `zip_cd` | `zip_cd` | `zip_cd` | `zip_cd` | `zip_cd` |
| Outpatient | `zip_cd` | `zip_cd` | `zip_cd` | `zip_cd` | `zip_cd` |

| Dataset    | 2008     | 2007     | 2006     | 2005      | 2004      |
|:-----------|:---------|:---------|:---------|:----------|:----------|
| Carrier    | `zip_cd` | `zip_cd` | `zip_cd` | `zipcode` | `zipcode` |
| Inpatient  | `zip_cd` | `zip_cd` | `zip_cd` | `zipcode` | `zipcode` |
| Outpatient | `zip_cd` | `zip_cd` | `zip_cd` | `zipcode` | `zipcode` |

| Dataset    | 2003      | 2002      | 2001       | 2000       | 1999       |
|:-----------|:----------|:----------|:-----------|:-----------|:-----------|
| Carrier    | `zipcode` | `zipcode` | `bene_zip` | `bene_zip` | `bzip`     |
| Inpatient  | `zipcode` | `zipcode` | `bene_zip` | `bene_zip` | `bene_zip` |
| Outpatient | `zipcode` | `zipcode` | `zipcode`  | `bene_zip` | `bene_zip` |

Contained in

- [Skilled Nursing Facility RIF](../snf-rif.md#data-documentation)
- [Outpatient RIF](../op-rif.md#data-documentation)
- [Inpatient RIF](../ip-rif.md#data-documentation)
- [Hospice RIF](../hospice-rif.md#data-documentation)
- [Home Health Agency RIF](../hha-rif.md#data-documentation)
- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The ZIP code of the mailing address where the beneficiary may be contacted.

ResDAC variable note: The zip code variable in the claims data appears as a 9-digit variable. However, the field only presents the 5-digit zip code followed by trailing zeros. For example, a zip code of 55455 would appear as 554550000 in the data.

 

