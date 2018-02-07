# Variable Definitions

!!! note
    These definitions are scraped from ResDAC. Click on the header of a variable description to see the ResDAC page.



## [Beneficiary Identification Number](https://www.resdac.org/cms-data/variables/Beneficiary-Identification-Number)

- Short SAS Name: `BENE_ID`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Beneficiary Identification Number for this data request



## [Equated BIC](https://www.resdac.org/cms-data/variables/Equated-BIC)

- Short SAS Name: `EQ_BIC`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code categorizing groups of `BIC`s representing similar relationships between the beneficiary and primary wage earner.

NOTE: The equatable `BIC` module electronically matches two records that contain different `BIC`s where it is apparent both are records for the same beneficiary. It validates the `BIC` and returns a base `BIC` under which to house the record in the National Claims History (NCH) databases. (All records for a beneficiary are stored under a single `BIC`).



<h3>Values</h3>

| Code   | Code Value                                                            |
|:-------|:----------------------------------------------------------------------|
| nan    | SSA Categories                                                        |
| A      | A;J1;J2;J3;J4;M;M1;T;TA                                               |
| B      | B;B2;B6;D;D4;D6;E;E1;K1;K2;K3;K4;W;W6;TB (F);TD (F);TE (F);TW (F)     |
| B1     | B1;BR;BY;D1;D5;DC;E4;E5;W1;WR;TB (M);TD (M);TE (M);TW (M)             |
| B3     | B3;B5;B9;D2;D7;D9;E2;E3;K5;K6;K7;K8;W2;W7;TG (F);TL (F);TR (F);TX (F) |
| B4     | B4;BT;BW;D3;DM;DP;E6;E9;W3;WT;TG (M);TL (M);TR (M);TX (M)             |
| B8     | B8;B7;BN;D8;DA;DV;E7;EB;K9;KA;KB;KC;W4;W8;TH (F);TM (F);TS (F);TY (F) |
| BA     | BA;BK;BP;DD;DL;DW;E8;EC;KD;KE;KF;KG;W9;WC;TJ (F);TN (F);TT (F);TZ (F) |
| BD     | BD;BL;BQ;DG;DN;DY;EA;ED;KH;KJ;KL;KM;WF;WF;TK (F);TP (F);TU (F);TV (F) |
| BG     | BG;DH;DQ;DS;EF;EJ;W5;TH (M);TM (M);TS (M);TY (M)                      |
| BH     | BH;DJ;DR;DX;EG;EK;WB;TJ (M);TN (M);TT (M);TZ (M)                      |
| BJ     | BJ;DK;DT;DZ;EH;EM;WG;TK (M);TP (M);TU (M);TV (M)                      |
| C1     | C1;TC                                                                 |
| C2     | C2;T2                                                                 |
| C3     | C3;T3                                                                 |
| C4     | C4;T4                                                                 |
| C5     | C5;T5                                                                 |
| C6     | C6;T6                                                                 |
| C7     | C7;T7                                                                 |
| C8     | C8;T8                                                                 |
| C9     | C9;T9                                                                 |
| F1     | F1;TF                                                                 |
| F2     | F2;TQ                                                                 |
| F3-F8  | Equatable only to itself (e.g., F3 is equatable to F3)                |
| CA-CZ  | Equatable only to itself (e.g., CA is only equatable to CA)           |
| nan    | RRB Categories                                                        |
| 10     | 10                                                                    |
| 11     | 11                                                                    |
| 13     | 13;17                                                                 |
| 14     | 14;16                                                                 |
| 15     | 15                                                                    |
| 43     | 43                                                                    |
| 45     | 45                                                                    |
| 46     | 46                                                                    |
| 80     | 80                                                                    |
| 83     | 83                                                                    |
| 84     | 84;86                                                                 |
| 85     | 85                                                                    |

## [MEDPAR Active Cross Reference Indicator](https://www.resdac.org/cms-data/variables/medpar-active-cross-reference-indicator-0)

- Short SAS Name: `ACTV_XREF_IND`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Specifies whether the HI claim number originated from a cross-reference.



<h3>Values</h3>

| Code   | Code Value      |
|:-------|:----------------|
| X      | Cross-Reference |
| A      | Active          |

## [MEDPAR Admission Date](https://www.resdac.org/cms-data/variables/MEDPAR-Admission-Date)

- Short SAS Name: `ADMSNDT`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `admsndt` | `admsndt` | `admsndt` | `admsndt` | `admsndt` |

| Dataset   | 2008      | 2007      | 2006      | 2005       | 2004       |
|:----------|:----------|:----------|:----------|:-----------|:-----------|
| MedPAR    | `admsndt` | `admsndt` | `admsndt` | `sadmsndt` | `sadmsndt` |

| Dataset   | 2003       | 2002       | 2001      | 2000      | 1999      |
|:----------|:-----------|:-----------|:----------|:----------|:----------|
| MedPAR    | `sadmsndt` | `sadmsndt` | `madmdte` | `madmdte` | `madmdte` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date the beneficiary was admitted for Inpatient care or the date that care started.

﻿NOTE: This field comes from the admission date that is present on the first claim record included in the stay.



## [MEDPAR Admission Day Code](https://www.resdac.org/cms-data/variables/MEDPAR-Admission-Day-Code)

- Short SAS Name: `ADMSNDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the day of the week on which the beneficiary was admitted to a facility.

??? derivation
	This field is derived from the admission date that is present on the first claim record included in the stay.

<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 1      | Sunday       |
| 2      | Monday       |
| 3      | Tuesday      |
| 4      | Wednesday    |
| 5      | Thursday     |
| 6      | Friday       |
| 7      | Saturday     |

## [MEDPAR Admission Death Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Admission-Death-Day-Count)

- Short SAS Name: `DEATHDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of days from the date the beneficiary was admitted to a facility to the beneficiary's date of death (DOD).

??? derivation
	This field is derived by counting the number of days between the MEDPAR admission date (the admission date present on the first claim record included in the stay) and MEDPAR beneficiary death date (the death date present on the enrollment database, which is accessed prior to creation of the quarterly MEDPAR file).

??? limitation
	DESCRIPTION :
	MEDPAR Admission Death Day Count calculated incorrectly, on both the 3/00 and 6/00 MEDPAR updates.
	BACKGROUND :
	Both the 3/00 and 6/00 MEDPAR updates incorrectly calculated the mortality days; i.e., days between the admission date and the beneficiary date of death. Users of the regular unencrypted MEDPAR file, this is not a problem, as the count can be calculated using the admission date and the date of death.  The problem is with the encrypted file (the expanded modified MEDPAR) because the fields needed to calculate the mortality days are ranged.
	CORRECTIVE ACTION :
	The problem was corrected with the 12/00 MEDPAR update.  NOTE:  For users of the expanded modified MEDPAR file who needs the mortality days, the 12/00 update of the FY1999 file can be given as a replacement.
	SOURCE:
	CONTACT :  OIS/EDG/DMUDD

## [MEDPAR Admitting Diagnosis Code](https://www.resdac.org/cms-data/variables/MEDPAR-Admitting-Diagnosis-Code)

- Short SAS Name: `AD_DGNS`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `ad_dgns` | `ad_dgns` | `ad_dgns` | `ad_dgns` | `ad_dgns` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `ad_dgns` | `ad_dgns` | `ad_dgns` | `ad_dgns` | `ad_dgns` |

| Dataset   | 2003      | 2002      | 2001     | 2000     | 1999     |
|:----------|:----------|:----------|:---------|:---------|:---------|
| MedPAR    | `ad_dgns` | `ad_dgns` | `mdiag0` | `mdiag0` | `mdiag0` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The ICD-9-CM code indicating the beneficiary's initial diagnosis at the time of admission.

NOTE: This field comes from the admitting diagnosis code that is present on the last claim record included in the stay.



## [MEDPAR Admitting Diagnosis Version Code](https://www.resdac.org/cms-data/variables/medpar-admitting-diagnosis-version-code)

- Short SAS Name: `ADMTG_DGNS_VRSN_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10. 

NOTE: With 5010, the diagnosis and procedure codes have been expanded to accommodate ICD-10, even though ICD-10 is not scheduled for implementation until 10/2013.



## [MEDPAR All Accommodations Total Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-All-Accommodations-Total-Charge-Amount)

- Short SAS Name: `ACMDTNS`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The total charge amount (rounded to whole dollars) for all accommodations (routine hospital room and board charges for general care, coronary care and/or intensive care units) related to a beneficiary's stay.

??? derivation
	This field is the sum of MEDPAR private room charge amounts, MEDPAR semiprivate room charge amount, MEDPAR ward charge amount, MEDPAR intensive care charge amount, and MEDPAR coronary care charge amount (i.e., the accumulation of the revenue center total charge amount associated with revenue center codes 0100 - 0219 from all claim records included in the stay).

## [MEDPAR Ambulance Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Ambulance-Charge-Amount)

- Short SAS Name: `AMBLNC`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for ambulance services related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 054x from all claim records included in the stay.

## [MEDPAR Anesthesia Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Anesthesia-Charge-Amount)

- Short SAS Name: `ANSTHSA`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for anesthesia services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 037X from all claim records included in the stay.

## [MEDPAR Base Operating DRG Amount](https://www.resdac.org/cms-data/variables/medpar-base-operating-drg-amount)

- Short SAS Name: `BASE_OPRTG_DRG_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The sum of the claim base operating DRG amounts reported on the claims that comprise the stay. The base operating DRG amount used to identify the wage-adjusted DRG operating payment plus the new technology add-on payment.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the Claim Base Operating DRG amount (CLM-BASE-OPRTG-DRG-AMT) that is present on any of the claim records included in the stay (i.e. the sum of the claim base operating DRG amounts reported on the claims that comprise the stay).

## [MEDPAR Beneficiary Age Count](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Age-Count)

- Short SAS Name: `AGE_CNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The beneficiary’s age as of date of admission.

NOTE: This field is derived by subtracting the bene date of birth from the admission date, present on the first claim record included in the stay. Exception: If the resulting age is 64, and the MSC = 10 or 11, the age is changed to 65.



## [MEDPAR Beneficiary Blood Deductible Liability Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Blood-Deductible-Liability-Amount)

- Short SAS Name: `BLDDEDAM`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of money (rounded to whole dollars) identified as the beneficiary's liability for the blood deductible for the stay.

??? derivation
	This field is derived by accumulating the beneficiary blood deductible liability amount that is present on any of the claim records included in the stay (i.e., the sum of the blood deductibles reported on the claims that comprise the stay).

??? limitation
	DESCRIPTION :
	It was discovered that the blood deductible amounts were incorrect on the Old MEDPAR Files.
	BACKGROUND    :
	Users of the MEDPAR data were comparing money amounts and counts present on the new MEDPAR file (created 6/95 using NCH Nearline File as the source) to that reported on the old MEDPAR File (created 3/95 and prior from claims from the Medicare Quality Assurance System) for Fiscal Year 1994.  They discovered that the blood deductible amount on the new MEDPAR was greater than that of the old MEDPAR.
	
	During NCH's investigation it was determined that the old 500-character MEDPAR incorrectly used a different field to report the blood deductible; specifically the noncovered
	charges derived from blood use Revenue Center codes 0380-0389.  The new program correctly used the NCH field, BENE_BLOOD_DDCTBL_LBLTY_AMT, which is derived from a value code (CLM_VAL_AMT associated with CLM_VAL_CD = '6').
	
	It is believed that all MEDPAR files created prior to 6/95 in the 500 character version are affected. MEDPAR 500 was first available with calendar year and fiscal year 9/91 updates for year 1987 forward.
	
	NOTE:  This anamoly also impacts the DRG Price Amount on the old MEDPAR file because it is calculated from a number of fields including the blood deductible.

## [MEDPAR Beneficiary Death Date](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Death-Date)

- Short SAS Name: `DEATHDT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date the beneficiary died.

??? derivation
	This field comes from the beneficiary death date, if present on the enrollment database, which is accessed prior to creation of the quarterly MEDPAR file.

??? limitation
	  DESCRIPTION :
	The Date of Death on the MEDPAR files were not up-to-date for four cycles.
	BACKGROUND  :
	 The MEDPAR process pulls in 10 segments of the HISKEW file, to get the date of death.  The HISKEW file names were changed with no notification the change was being made.  Because of this, MEDPAR kept using the HISKEW that was created in June 2000.
	The incomplete MEDPAR cycles are: 12/2000, 3/2001,  6/2001 and 9/2001 (9/2000 MEDPAR was not run).
	CORRECTIVE ACTION :
	Since this anamoly causes no major problem to the prime user of this data, a rerun will not take place.
	NOTE:  The 12/01 quarterly update will access up-to-date information.

## [MEDPAR Beneficiary Death Date Verified Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Death-Date-Verified-Code)

- Short SAS Name: `DEATHCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether the beneficiary's date of death has been verified or originated from a claim record.

??? derivation
	This field is derived from the enrollment database's beneficiary source death date code, or from the presence of a claim status code = '20' (expired) on the last claim record included in the stay.

## [MEDPAR Beneficiary Discharge Status Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Discharge-Status-Code)

- Short SAS Name: `DSCHRGCD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dschrgcd` | `dschrgcd` | `dschrgcd` | `dschrgcd` | `dschrgcd` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dschrgcd` | `dschrgcd` | `dschrgcd` | `dschrgcd` | `dschrgcd` |

| Dataset   | 2003       | 2002       | 2001      | 2000      | 1999      |
|:----------|:-----------|:-----------|:----------|:----------|:----------|
| MedPAR    | `dschrgcd` | `dschrgcd` | `mdistat` | `mdistat` | `mdistat` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify the status of the patient as of the `CLM_THRU_DT`.

??? derivation
	This field is derived from the claim status code that is present on the last claim record included in the stay.

<h3>Values</h3>

| Code   | Code Value                                               |
|:-------|:---------------------------------------------------------|
| A      | Discharged alive (claim status code other than 20 or 30) |
| B      | Discharged dead                                          |
| C      | Still a patient                                          |

## [MEDPAR Beneficiary Identification Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Identification-Code)

- Short SAS Name: `BIC`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The `BIC` reported on the first claim record included in the stay, representing the values existing on the CWF beneficiary master record on the date the CWF host site processed the claim.



## [MEDPAR Beneficiary Inpatient Deductible Liability Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Inpatient-Deductible-Liability-Amount)

- Short SAS Name: `DED_AMT`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of money (rounded to whole dollars) identified as the beneficiary's liability for the Inpatient deductible for the stay.

??? derivation
	This field is derived by accumulating the beneficiary Inpatient deductible amount that is present on any of the claim records included in the stay (i.e., the sum of the Inpatient deductibles reported on the claims that comprise the stay).

## [MEDPAR Beneficiary LRD Used Count](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-LRD-Used-Count)

- Short SAS Name: `LRD_USE`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of lifetime reserve days (LRD) used by the beneficiary for this stay.

??? derivation
	This field is derived by accumulating the lifetime reserve days used count that is present on any of the claim records included in the stay (i.e., the sum of LRD reported on the claims that comprise the stay).

## [MEDPAR Beneficiary Mailing Contact Zip Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Mailing-Contact-Zip-Code)

- Short SAS Name: `BENE_ZIP`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `bene_zip` | `bene_zip` | `bene_zip` | `bene_zip` | `bene_zip` |

| Dataset   | 2008       | 2007       | 2006       | 2005      | 2004      |
|:----------|:-----------|:-----------|:-----------|:----------|:----------|
| MedPAR    | `bene_zip` | `bene_zip` | `bene_zip` | `zipcode` | `zipcode` |

| Dataset   | 2003      | 2002      | 2001   | 2000   | 1999   |
|:----------|:----------|:----------|:-------|:-------|:-------|
| MedPAR    | `zipcode` | `zipcode` | `mzip` | `mzip` | `mzip` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The zip code of the mailing address where the beneficiary may be contacted.

NOTE: This field comes from the zip code that is present on the first claim record included in the stay.



## [MEDPAR Beneficiary Medicare Benefit Exhausted Date](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Medicare-Benefit-Exhausted-Date)

- Short SAS Name: `EXHST_DT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The last date for which the beneficiary had Medicare coverage. This field is completed only where benefits were exhausted before the discharge date and during the period covered by stay.

??? derivation
	This field comes from the highest benefits exhausted date that is present on the claim records included in the stay.

## [MEDPAR Beneficiary Medicare Status Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Medicare-Status-Code)

- Short SAS Name: `MS_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The CWF-derived reason for a beneficiary’s entitlement to Medicare benefits, as of the reference date.

??? derivation
	CWF derives MSC from the following:
	1. Date of birth
	2. Claim through date
	3. Original/Current reasons for entitlement
	4. ESRD indicator
	5. Beneficiary claim number
	Items 1,3,4,5 come from the CWF beneficiary
	master record; Item 2 comes from the FI/Carrier
	claim record. MSC is assigned as follows:
	MSC OASI DIB ESRD AGE BIC
	10 YES N/A NO 65 AND OVER N/A
	11 YES N/A YES 65 AND OVER N/A
	20 NO YES NO UNDER 65 N/A
	21 NO YES YES UNDER 65 N/A
	31 NO NO YES ANY AGE T.

<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [MEDPAR Beneficiary Part A Coinsurance Liability Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Part-Coinsurance-Liability-Amount)

- Short SAS Name: `COIN_AMT`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of money (rounded to whole dollars) identified as the beneficiary's liability for part A coinsurance for the stay.

??? derivation
	This field is derived by accumulating the beneficiary's part a coinsurance liability amount that is present on any of the claim records included in the stay (i.e., the sum of coinsurance amounts reported on the claims that comprise the stay).

## [MEDPAR Beneficiary Primary Payer Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Primary-Payer-Amount)

- Short SAS Name: `PRPAYAMT`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of payment (rounded to whole dollars) made on behalf of the beneficiary by a primary payer other than Medicare, which has been applied to the covered Medicare charges for the stay.

??? derivation
	This field is derived by accumulating the beneficiary primary payer payment amount that is present on any of the claim records included in the stay (i.e., the sum of the primary payer amounts reported on the claims that comprise the stay).

## [MEDPAR Beneficiary Primary Payer Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Primary-Payer-Code)

- Short SAS Name: `PRPAY_CD`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the type of payer who has primary responsibility for the payment of the Medicare beneficiary's claims related to the stay.

??? derivation
	This field comes from the primary payer code that is present on the first claim record included in the stay.

<h3>Values</h3>

| Code    | Code Value                                                        |
|:--------|:------------------------------------------------------------------|
| A       | Working aged bene/spouse with eghp                                |
| B       | ESRD bene in 18-month coordination period with eghp               |
| C       | Conditional Medicare payment; future reimbursement expected       |
| D       | Auto no-fault or any liability insurance                          |
| E       | Worker's compensation                                             |
| F       | Phs or other federal agency (other than dept of veterans affairs) |
| G       | Working disabled                                                  |
| H       | Black lung                                                        |
| I       | Dept of veterans affairs                                          |
| J       | Any liability insurance                                           |
| Z/Blank | Medicare is primary payer                                         |

## [MEDPAR Beneficiary Race Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Race-Code)

- Short SAS Name: `RACE`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The race of the beneficiary.

NOTE: This field comes from the race code that is present on the first claim record included in the stay.

 



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 1      | White                 |
| 2      | Black                 |
| 3      | Other                 |
| 4      | Asian                 |
| 5      | Hispanic              |
| 6      | North American Native |
| 0      | Unknown               |

## [MEDPAR Beneficiary Residence SSA Standard County Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Residence-SSA-Standard-County-Code)

- Short SAS Name: `CNTY_CD`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The SSA standard county code of a beneficiary's residence.

NOTE: This field comes from the state code that is present on the first claim record included in the stay.



## [MEDPAR Beneficiary Residence SSA Standard State Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Residence-SSA-Standard-State-Code)

- Short SAS Name: `STATE_CD`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The SSA standard state code of a beneficiary's residence.

NOTE: This field comes from the state code that is present on the first claim record included in the stay.



<h3>Values</h3>

| Code   | Code Value                    |
|:-------|:------------------------------|
| 1      | Alabama                       |
| 2      | Alaska                        |
| 3      | Arizona                       |
| 4      | Arkansas                      |
| 5      | California                    |
| 6      | Colorado                      |
| 7      | Connecticut                   |
| 8      | Delaware                      |
| 9      | District of Columbia          |
| 10     | Florida                       |
| 11     | Georgia                       |
| 12     | Hawaii                        |
| 13     | Idaho                         |
| 14     | Illinois                      |
| 15     | Indiana                       |
| 16     | Iowa                          |
| 17     | Kansas                        |
| 18     | Kentucky                      |
| 19     | Louisiana                     |
| 20     | Maine                         |
| 21     | Maryland                      |
| 22     | Massachusetts                 |
| 23     | Michigan                      |
| 24     | Minnesota                     |
| 25     | Mississippi                   |
| 26     | Missouri                      |
| 27     | Montana                       |
| 28     | Nebraska                      |
| 29     | Nevada                        |
| 30     | New Hampshire                 |
| 31     | New Jersey                    |
| 32     | New Mexico                    |
| 33     | New York                      |
| 34     | North Carolina                |
| 35     | North Dakota                  |
| 36     | Ohio                          |
| 37     | Oklahoma                      |
| 38     | Oregon                        |
| 39     | Pennsylvania                  |
| 40     | Puerto Rico                   |
| 41     | Rhode Island                  |
| 42     | South Carolina                |
| 43     | South Dakota                  |
| 44     | Tennesee                      |
| 45     | Texas                         |
| 46     | Utah                          |
| 47     | Vermont                       |
| 48     | Virgin Islands                |
| 49     | Virginia                      |
| 50     | Washington                    |
| 51     | West Virginia                 |
| 52     | Wisconsin                     |
| 53     | Wyoming                       |
| 54     | Africa                        |
| 55     | Asia                          |
| 56     | Canada                        |
| 57     | Central America & West Indies |
| 58     | Europe                        |
| 59     | Mexico                        |
| 60     | Oceania                       |
| 61     | Philippines                   |
| 62     | South America                 |
| 63     | U.S. Possessions              |
| 97     | Saipan - MP                   |
| 98     | Guam                          |
| 99     | American Samoa                |

## [MEDPAR Beneficiary Sex Code](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Sex-Code)

- Short SAS Name: `SEX`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The sex of a beneficiary.

NOTE: This field comes from the sex code that is present on the first claim record included in the stay.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 0      | Unknown      |
| 2      | Female       |
| 1      | Male         |

## [MEDPAR Beneficiary Total Coinsurance Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Beneficiary-Total-Coinsurance-Day-Count)

- Short SAS Name: `COIN_DAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the total number of coinsurance days involved with the beneficiary's stay in a facility. For Inpatient services, the beneficiary is liable for a daily coinsurance amount after the 60th day and before the 91st day in a single spell of illness; for SNF services, the beneficiary is liable for a daily coinsurance amount after the 20th day and before the 101st day in a single spell of illness.

??? derivation
	This field is derived by accumulating the coinsurance day count that is present on any of the claim records included in the stay (i.e., the sum of coinsurance days reported on the claims that comprise the stay).

## [MEDPAR Blood Administration Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Blood-Administration-Charge-Amount)

- Short SAS Name: `BLDADMIN`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for blood storage and processing related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 039x from all claim records included in the stay.

## [MEDPAR Blood Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Blood-Charge-Amount)

- Short SAS Name: `BLOODAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for blood provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 038x from all claim records included in the stay.

## [MEDPAR Blood Pints Furnished Quantity](https://www.resdac.org/cms-data/variables/MEDPAR-Blood-Pints-Furnished-Quantity)

- Short SAS Name: `BLDFRNSH`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The quantity of blood (number of whole pints) furnished to the beneficiary during the stay.

Note: this includes blood pints replaced as well as not replaced.

??? derivation
	This field is derived by accumulating the blood pints furnished quantity from all claim records included in the stay.

## [MEDPAR Bundled Model Discount Percent](https://www.resdac.org/cms-data/variables/medpar-bundled-model-discount-percent)

- Short SAS Name: `BNDLD_MODEL_DSCNT_PCT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The field used to identify the discount percentage that will be applied to the payment for all the hospitals' DRG over the lifetime of the initiative. The hospital must be participating in the Model 1 Bundled Payments for Care Improvement initiative.

??? derivation
	This field comes from the Claim Bundled Model Discount (CLM-BNDLD-MODEL-1-DSCNT-PCT) that is present on the last record included in the stay.

## [MEDPAR Cardiac Catheterization Amount](https://www.resdac.org/cms-data/variables/medpar-cardiac-catheterization-amount)

- Short SAS Name: `CRDC_CATHRZTN_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the cardiac catheterization services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0481' from all claim records included in the stay.

## [MEDPAR Cardiology Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Cardiology-Charge-Amount)

- Short SAS Name: `CRDLGY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for cardiology services and electrocardiogram(s) provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 048X and 073X from all claim records included in the stay.

## [MEDPAR Care Improvement Model Code](https://www.resdac.org/cms-data/variables/medpar-care-improvement-model-code)

- Short SAS Name: `CARE_IMPRVMT_MODEL_{x}_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify that the care improvement model is being used for bundling payments. The valid value for care improvement model 1 is `61`. The valid value for care improvement model 2 is `62`. The valid value for care improvement model 3 is `63`. The valid value for care improvement model 4 is `64`. The value is also reflected in the demonstration trailer.

??? derivation
	This field comes from the Claim Care Improvement Model (CLM-CARE-IMPRVMT-MODEL-{x}-CD) code that is present on the first claim record included in the stay. If there is no Claim Care Improve Model code on the 1st claim then take the first found code on a the other claims that make up the stay.

## [MEDPAR Case or Control Record](https://www.resdac.org/cms-data/variables/medpar-case-or-control-record)

- Short SAS Name: `SLCT_RSN_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Specifies whether this record is a case or control record.



## [MEDPAR Claim Patient Relationship Code](https://www.resdac.org/cms-data/variables/medpar-claim-patient-relationship-code)

- Short SAS Name: `CLM_PTNT_RLTNSHP_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify the patient relationship to the beneficiary.

??? derivation
	This field comes from the patient relationship code (CLM-PTNT-RLTNSHP-CD) that is present on the first claim record included in the stay. If there is no patient relationship code on the 1st claim then take the first found code on any of the other claims that make up the stay.

## [MEDPAR Claim Present on Admission Diagnosis Code Count](https://www.resdac.org/cms-data/variables/medpar-claim-present-admission-diagnosis-code-count)

- Short SAS Name: `POA_DGNS_CD_CNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the count of the number of Present on Admission (POA) codes reported on the Inpatient/SNF claim. The purpose of this count is to indicate how many claim POA diagnosis trailers are present.



## [MEDPAR Claim Present on Admission Diagnosis E Code Count](https://www.resdac.org/cms-data/variables/medpar-claim-present-admission-diagnosis-e-code-count)

- Short SAS Name: `POA_DGNS_E_CD_CNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the count of the number of Present on Admission (POA) codes associated with the diagnosis E codes reported on the Inpatient/SNF claim. The purpose of this count is to indicate how many claim POA diagnosis E trailers are present.



## [MEDPAR Clinic Visit Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Clinic-Visit-Charge-Amount%01)

- Short SAS Name: `CLNC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for clinic visits (e.g., visits to chronic pain or dental centers or to clinics providing psychiatric, ob-gyn, pediatric services) related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 051x from all claim records included in the stay.

## [MEDPAR Coronary Care Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Coronary-Care-Charge-Amount)

- Short SAS Name: `CRNRYAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for coronary care accommodations related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with accommodation revenue center code 021X from all claim records included in the stay.

## [MEDPAR Coronary Care Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Coronary-Care-Day-Count)

- Short SAS Name: `MCCCNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of coronary care days used by the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the revenue center unit count associated with accommodation revenue center code 021x (all six subcategories) from all claim records included in the stay.

??? limitation
	There is approximately a 20% error rate in the revenue center code category 0214 due to coders misunderstanding the term 'post ccu' as including any day after a ccustay rather than just days in a step-down/lower case version of a ccu. 'Post' was removed from the
	revenue center code 0214 description, effective 10/1/96 (12/96 MEDPAR update). 0214 Is now defined as 'intermediate ccu'.

## [MEDPAR Coronary Care Indicator Code](https://www.resdac.org/cms-data/variables/medpar-coronary-care-indicator-code)

- Short SAS Name: `CRNRY_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating that the beneficiary has spent time under coronary care during the stay. It also specifies the type of coronary care unit.

??? derivation
	This field is derived by checking for the presence of coronary care revenue center codes (listed below) on any of the claim records included in the stay. If more than one of the revenue center codes listed below are included on these claims, the code with the highest revenue center total charge amount is used.

??? limitation
	There is approximately a 20% error rate in the revenue center code category 0214 due to coders misunderstanding the term 'post CCU' as including any day after a CCU stay rather than just days in a step-down/lower case version of a CCU. 'Post' was removed from the revenue center code 0214 description, effective 10/1/96 (12/96 MEDPAR update). 0214 Is now defined as 'intermediate CCU'.

<h3>Values</h3>

| Code   | Code Value                              |
|:-------|:----------------------------------------|
| Blank  | No coronary care indication             |
| 0      | General (revenue code 0210)             |
| 1      | Myocardial (revenue code 0211)          |
| 2      | Pulmonary care (revenue code 0212)      |
| 3      | Heart transplant (revenue code 0213)    |
| 4      | Intermediate CCU (revenue code 0214)    |
| 9      | Other Coronary Care (revenue code 0219) |

## [MEDPAR Covered Level Care Thru Date](https://www.resdac.org/cms-data/variables/MEDPAR-Covered-Level-Care-Thru-Date)

- Short SAS Name: `CVRLVLDT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date on which a covered level of care ended in a SNF.

??? derivation
	This field comes from the date associated with occurrence code = 22 if present on any of the claims included in the stay. If multiple dates, the highest date is used. This field is only applicable to SNF claims.

## [MEDPAR Credit Received Replaced Device Switch](https://www.resdac.org/cms-data/variables/medpar-credit-received-replaced-device-switch)

- Short SAS Name: `CRED_RCVD_RPLCD_DVC_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch used to identify whether the provider received a credit from the Manufacturer for a replaced medical device.

??? derivation
	If any claim that comprises the Stay has a value code (CLM-VAL-CD) equal to 'FD' populate the MEDPAR Credit Received from Manufacturer for Replaced Medical Device Switch with a 'Y'. If no 'FD' value code, populate field with an 'N'.

## [MEDPAR DME Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-DME-Charge-Amount)

- Short SAS Name: `DME_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for DME (purchase of new DME and rentals) related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 0290, 0291, 0292, and 0294 - 0299 from all claim records included in the stay.

## [MEDPAR DRG Code](https://www.resdac.org/cms-data/variables/MEDPAR-DRG-Code)

- Short SAS Name: `DRG_CD`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the DRG to which the claims that comprise the stay belong for payment purposes.

??? derivation
	This field comes from the actual DRG code that is present on the last claim record included in the stay. 
	Exception: If the DRG code is not present (e.g., claims from Maryland and PPS-exempt hospital units do not have a DRG), a valid DRG is obtained using the grouper software and is moved to this field.

## [MEDPAR DRG Outlier Approved Payment Amount](https://www.resdac.org/cms-data/variables/MEDPAR-DRG-Outlier-Approved-Payment-Amount)

- Short SAS Name: `OUTLRAMT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlramt` | `outlramt` | `outlramt` | `outlramt` | `outlramt` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlramt` | `outlramt` | `outlramt` | `outlramt` | `outlramt` |

| Dataset   | 2003       | 2002       | 2001      | 2000      | 1999      |
|:----------|:-----------|:-----------|:----------|:----------|:----------|
| MedPAR    | `outlramt` | `outlramt` | `moutamt` | `moutamt` | `moutamt` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of additional payment (rounded to whole dollars) approved due to an outlier situation over the DRG allowance for the stay.

??? derivation
	This field is derived by accumulating the DRG outlier approved payment amount (value code = 17 amount) that is present on any of the claim records included in the stay (i.e., the sum of outlier amounts reported on the claims that comprise the stay).

## [MEDPAR DRG Price Amount](https://www.resdac.org/cms-data/variables/MEDPAR-DRG-Price-Amount)

- Short SAS Name: `DRGPRICE`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `drgprice` | `drgprice` | `drgprice` | `drgprice` | `drgprice` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `drgprice` | `drgprice` | `drgprice` | `drgprice` | `drgprice` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `drgprice` | `drgprice` | `mdrgpric` | `mdrgpric` | `mdrgpric` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount (called the 'DRG price' for purposes of MEDPAR analysis) that would have been paid if no deductibles, coinsurance, primary payers, or outliers were involved (rounded to whole dollars).

??? derivation
	This field is derived by accumulating the following amounts: MEDPAR Medicare payment amount, MEDPAR beneficiary primary payer payment amount, MEDPAR beneficiary coinsurance liability amount, MEDPAR beneficiary Inpatient deductible liability amount, MEDPAR beneficiary blood deductible amount; and then subtracting from the sum the MEDPAR DRG outlier approved payment amount.

??? limitation
	DESCRIPTION :
	IT WAS DISCOVERED THAT THE DRG PRICE AMOUNT WSA INCORRECT ON THE OLD MEDPAR FILES.
	BACKGROUND  :
	Users of the MEDPAR data were comparing money amounts and counts present on the new MEDPAR file (created 6/95 using NCH Nearline File as the source) to that reported on the old MEDPAR File (created 3/95 and prior from claims from the Medicare Quality Assurance System) for Fiscal Year 1994.  They discovered that the DRG price amount on the new MEDPAR contained incorrect amounts.
	
	NOTE:  This anamoly occurs because the DRG price amount is calculated from a number of fields including the blood deductible amount, which was discovered to be populated incorrectly.
	
	During NCH's investigation it was determined that the old 500-character MEDPAR incorrectly used a different field to report the blood deductible; specifically the noncovered charges derived from blood use Revenue Center codes 0380-0389.  The new program correctly used the NCH field, BENE_BLOOD_DDCTBL_LBLTY_AMT, which is derived from a value code (CLM_VAL_AMT associated with CLM_VAL_CD = '6').
	
	It is believed that all MEDPAR files created prior to 6/95 in the 500 character version were affected. MEDPAR 500 was first available with calendar year and fiscal year 9/91  updates for year 1987 forward.

## [MEDPAR DRG/Outlier Stay Code](https://www.resdac.org/cms-data/variables/MEDPAR-DRGOutlier-Stay-Code)

- Short SAS Name: `OUTLR_CD`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code identifying (1) for PPS providers if the stay has an unusually long length (day outlier) or high cost (cost outlier); or (2) for non-PPS providers the source for developing the DRG.

??? derivation
	This field is the actual DRG outlier stay code that is present on the last claim record included in the stay.

<h3>Values</h3>

Applicable to PPS providers:

| Code   | Code Value   |
|:-------|:-------------|
| 0      | No Outlier   |
| 1      | Day Outlier  |
| 2      | Cost Outlier |

Applicable to Non-PPS Providers:

| Code   | Code Value                                 |
|:-------|:-------------------------------------------|
| 6      | Valid DRG Received From Intermediary       |
| 7      | HCFA-Developed DRG                         |
| 8      | HCFA-Developed DRG Using Claim Status Code |
| 9      | Not Groupable                              |

## [MEDPAR Departmental Total Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Departmental-Total-Charge-Amount)

- Short SAS Name: `DPRTMNTL`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The total charge amount (rounded to whole dollars) for all ancillary departments (other than routine room and board, CCU, and ICU) related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 0220 - 0999 from all claim records included in the stay (i.e., the sum of charges for all revenue centers other than accommodations 0100 - 0219).

## [MEDPAR Diagnosis Code](https://www.resdac.org/cms-data/variables/MEDPAR-Diagnosis-Code)

- Short SAS Name: `DGNSCD{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The diagnosis code identifying the beneficiary's principal or other diagnosis (including E code).

NOTE: Prior to Version H, the principal diagnosis code was not stored with the 'OTHER' diagnosis codes. During the Version H conversion the CLM_PRNCPAL_DGNS_CD was added as the first occurrence.NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.NOTE2: Effective with Version 'J', the diagnosis E codes are stored in a separate trailer (CLM_DGNS_E_GRP).

 

??? derivation
	This field is the actual principal diagnosis code (1st occurrence) or one of up to 9 other diagnosis codes that are present on the last claim record included in the stay.

## [MEDPAR Diagnosis Code Count](https://www.resdac.org/cms-data/variables/MEDPAR-Diagnosis-Code-Count)

- Short SAS Name: `DGNSCNT`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `dgnscnt` | `dgnscnt` | `dgnscnt` | `dgnscnt` | `dgnscnt` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `dgnscnt` | `dgnscnt` | `dgnscnt` | `dgnscnt` | `dgnscnt` |

| Dataset   | 2003      | 2002      | 2001       | 2000       | 1999       |
|:----------|:----------|:----------|:-----------|:-----------|:-----------|
| MedPAR    | `dgnscnt` | `dgnscnt` | `mdiagnum` | `mdiagnum` | `mdiagnum` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of diagnosis codes included in the stay.

??? derivation
	This field is derived by adding '1' to the count of the other diagnosis codes reported on the last claim record included in the stay. The '1' represents the principal diagnosis code, which is reported separately from the other diagnosis.

## [MEDPAR Diagnosis Code POA Array](https://www.resdac.org/cms-data/variables/medpar-diagnosis-code-poa-array)

- Short SAS Name: `DGNS_POA`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Diagnosis code POA array.

??? derivation
	This field is the actual principal diagnosis code (1st occurrence) or one of up to 9 other diagnosis codes that are present on the last claim record included in the stay.

## [MEDPAR Diagnosis E Code Count](https://www.resdac.org/cms-data/variables/medpar-diagnosis-e-code-count)

- Short SAS Name: `DGNS_E_CD_CNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the count of the number of diagnosis E codes
 reported on the Inpatient/SNF claim. The purpose of this count is to 
indicate how many diagnosis E trailers are present.



## [MEDPAR Diagnosis E Code Present on Admission Indicator](https://www.resdac.org/cms-data/variables/medpar-diagnosis-e-code-present-admission-indicator)

- Short SAS Name: `POA_DGNS_E_{x}_IND_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the Present on Admission (POA) indicator code associated with the diagnosis E codes.



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

## [MEDPAR Diagnosis E Version Code](https://www.resdac.org/cms-data/variables/medpar-diagnosis-e-version-code)

- Short SAS Name: `DGNS_E_VRSN_CD_{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10.



## [MEDPAR Diagnosis Present on Admission Indicator Code](https://www.resdac.org/cms-data/variables/medpar-diagnosis-present-admission-indicator-code)

- Short SAS Name: `POA_DGNS_{x}_IND_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to identify the Present on Admission (POA) indicator code associated with the diagnosis codes (principal and secondary). The present on admission indicators for the diagnosis E codes are stored in the present on admission diagnosis E trailer.



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

## [MEDPAR Diagnosis Version Code](https://www.resdac.org/cms-data/variables/medpar-diagnosis-version-code)

- Short SAS Name: `DGNS_VRSN_CD_{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10.



## [MEDPAR Discharge Date](https://www.resdac.org/cms-data/variables/MEDPAR-Discharge-Date)

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date on which the beneficiary was discharged or died.

NOTE: This field comes from the highest claim thru date that is present on the claim records included in the stay, where the claim status code is other than `30` (still patient)on the last claim record included in the stay. Inpatient claims will always have a discharge date; SNF claims could have a zero date.



## [MEDPAR Discharge Destination Code](https://www.resdac.org/cms-data/variables/medpar-discharge-destination-code%01)

- Short SAS Name: `DSTNTNCD`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dstntncd` | `dstntncd` | `dstntncd` | `dstntncd` | `dstntncd` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dstntncd` | `dstntncd` | `dstntncd` | `dstntncd` | `dstntncd` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `dstntncd` | `dstntncd` | `mdisdest` | `mdisdest` | `mdisdest` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code primarily indicating the destination of the beneficiary upon discharge from a facility; also denotes death or SNF/still patient situations.

??? derivation
	This field comes from the claim status code that is present on the last claim record included in the stay.

<h3>Values</h3>

| Code   | Code Value                                                                                           |
|:-------|:-----------------------------------------------------------------------------------------------------|
| 70     | Discharged/transferred to another type of health care institution not defined elsewhere in code list |

## [MEDPAR ESRD Condition Code](https://www.resdac.org/cms-data/variables/MEDPAR-ESRD-Condition-Code)

- Short SAS Name: `ESRD_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating if the beneficiary had an ESRD condition reported during the stay.

??? derivation
	This field is derived by checking for condition codes 70 - 76 on any of the claim records included in the stay.

## [MEDPAR ESRD Revenue Setting Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-ESRD-Revenue-Setting-Charge-Amount)

- Short SAS Name: `ESRDSETG`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the type of dialysis received by the beneficiary during the stay. Up to 5 2-position codes may be present.

??? derivation
	This field is derived from the presence of the dialysis revenue center codes listed below on any of the claim records included in the stay.

## [MEDPAR ESRD Setting Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-ESRD-Setting-Indicator-Code)

- Short SAS Name: `ESRDSTG{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the type of dialysis received by the beneficiary during the stay. Up to 5 2-position codes may be present.

??? derivation
	This field is derived from the presence of the dialysis revenue center codes listed below on any of the claim records included in the stay.

<h3>Values</h3>



 Medpar_ESRD_SETG_IND_TB.txt 



## [MEDPAR Emergency Room Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Emergency-Room-Charge-Amount)

- Short SAS Name: `ER_AMT`

<h3>Variable Names</h3>

| Dataset   | 2013     | 2012     | 2011     | 2010     | 2009     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| MedPAR    | `er_amt` | `er_amt` | `er_amt` | `er_amt` | `er_amt` |

| Dataset   | 2008     | 2007     | 2006     | 2005     | 2004     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| MedPAR    | `er_amt` | `er_amt` | `er_amt` | `er_amt` | `er_amt` |

| Dataset   | 2003     | 2002     | 2001     | 2000     | 1999     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| MedPAR    | `er_amt` | `er_amt` | `merchg` | `merchg` | `merchg` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for emergency room services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 045X from all claim records included in the stay.

## [MEDPAR Fiscal Intermediary/Carrier Identification Number](https://www.resdac.org/cms-data/variables/MEDPAR-Fiscal-IntermediaryCarrier-Identification-Number)

- Short SAS Name: `FICARR`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The identification of the intermediary processing the beneficiary's claims related to the stay.

NOTE: This field comes from the intermediary number that is present on the first claim record included in the stay.



## [MEDPAR GHO Paid Code](https://www.resdac.org/cms-data/variables/MEDPAR-GHO-Paid-Code)

- Short SAS Name: `GHOPDCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether or not a GHO has paid the provider for the claim(s).

NOTE: This field comes from the GHO-paid indicator that is present on the first claim record included in the stay.



<h3>Values</h3>

| Code       | Code Value                    |
|:-----------|:------------------------------|
| 1          | GHO has paid the provider     |
| 0 or Blank | GHO has not paid the provider |

## [MEDPAR HRR Adjustment Percent](https://www.resdac.org/cms-data/variables/medpar-hrr-adjustment-percent)

- Short SAS Name: `HRR_ADJSTMT_PCT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Under the Hospital Readmission Reduction (HRR) Program, the percent used to identify the readmission adjustment factor that will be applied in determining a subsection (d) hospital's operating IPPS payment amount in accordance with Section 3025 of the Affordable Care Act (ACA).

??? derivation
	This field comes from the Claim HRR Adjustment Percent (CLM-HRR-ADJSTMT-PCT) that is present on the last claim record included in the stay.

## [MEDPAR HRR Participant Indicator Code](https://www.resdac.org/cms-data/variables/medpar-hrr-participant-indicator-code)

- Short SAS Name: `HRR_PRTCPNT_IND_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify whether the facility is participating in the Hospital Readmission Reduction Program.

??? derivation
	This field comes from the Claim HRR Participant Indicator code (CLM-HRR-PRTCPNT-IND-CD) that is present on the first claim record included in the stay. If there is no Claim HRR Participant Indicator code on the first claim then take the first found code on any of the other claims that make up the stay.

## [MEDPAR Incident to Other Diagnostic Services Amount](https://www.resdac.org/cms-data/variables/medpar-incident-other-diagnostic-services-amount)

- Short SAS Name: `INCDNT_DGNSTC_SRVCS_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical supplies incident to other diagnostic services related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0622' from all claim records included in the stay.

## [MEDPAR Incident to Radiology Amount](https://www.resdac.org/cms-data/variables/medpar-incident-radiology-amount)

- Short SAS Name: `INCDNT_RDLGY_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical supplies incident to radiology related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0621' from all claim records included in the stay.

## [MEDPAR Indirect Medical Education (IME) Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Indirect-Medical-Education-IME-Amount)

- Short SAS Name: `IME_AMT`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of additional payment (rounded to whole dollars) made to teaching hospitals for IME for the stay.

??? derivation
	This field is derived by accumulating the value amount associated with value code = 19 that is present on any of the claim records included in the stay (i.e., the sum of IME amounts - value code 19 amounts - reported on the claims that comprise the stay).

## [MEDPAR Informational Encounter Indicator Switch](https://www.resdac.org/cms-data/variables/medpar-informational-encounter-indicator-switch)

- Short SAS Name: `INFRMTL_ENCTR_IND_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch used to identify if a beneficiary is enrolled in a Managed Care Organization.

??? derivation
	If any claim that comprises the Stay has a condition code (CLM RLT COND CD) equal to '04' populate the MEDPAR Informational Encounter Switch with a 'Y'. If no '04' condition code, populate field with an 'N'.

## [MEDPAR Inhalation Therapy Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Inhalation-Therapy-Charge-Amount)

- Short SAS Name: `INHLTAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for inhalation therapy services (respiratory and pulmonary function) provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 041x and 046x from all claim records included in the stay.

## [MEDPAR Inpatient Admission Type Code](https://www.resdac.org/cms-data/variables/MEDPAR-Inpatient-Admission-Type-Code)

- Short SAS Name: `TYPE_ADM`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the type and priority of the beneficiary's admission to a facility for the Inpatient hospital stay.

??? derivation
	This field comes from the Inpatient admission type code that is present on the last claim record included in the stay.

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

## [MEDPAR Inpatient Disproportionate Share Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Inpatient-Disproportionate-Share-Amount)

- Short SAS Name: `DISP_SHR`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount paid over the DRG amount (rounded to whole dollars) for the disproportionate share hospital for the stay.

??? derivation
	This field is derived by accumulating the value amount associated with value code = 18 that is present on any of the claim records included in the stay (i.e., the sum of value code 18 amounts reported on the claims that comprise the stay).

## [MEDPAR Inpatient Low Volume Payment Amount](https://www.resdac.org/cms-data/variables/medpar-inpatient-low-volume-payment-amount)

- Short SAS Name: `IP_LOW_VOL_PYMT_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount field used to identify a payment adjustment given to hospitals to account for the higher costs per discharge for low income hospitals under the Inpatient Prospective Payment System (IPPS).

??? derivation
	This field is derived by accumulating the IP Low Volume Amount that is present on any of the claim records included in the stay (i.e. the sum of the low volume amounts re-ported on the claims that comprise the stay).

## [MEDPAR Intensive Care Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Intensive-Care-Charge-Amount)

- Short SAS Name: `ICAREAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for intensive care accommodations related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with accommodation revenue center code 020x from all claim records included in the stay.

## [MEDPAR Intensive Care Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Intensive-Care-Day-Count)

- Short SAS Name: `ICARECNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of intensive care days used by the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the revenue center unit count associated with accommodation revenue center codes 020X (all 9 subcategories) from all claims included in the stay.

??? limitation
	There is approximately a 20% error rate in the revenue center code category 0206 due to coders misunderstanding the term 'post ICU' as including any day after an ICU stay rather than just days in a step-down/lower case version of an ICU. 'Post' was removed from the revenue center code 0206 description, effective 10/1/96 (12/96 MEDPAR update). 0206 Is now defined as 'intermediate ICU'.

## [MEDPAR Intensive Care Unit (ICU) Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Intensive-Care-Unit-ICU-Indicator-Code)

- Short SAS Name: `ICUINDCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating that the beneficiary has spent time under intensive care during the stay. It also specifies the type of ICU.

??? derivation
	This field is derived by checking for the presence of icu revenue center codes (listed below) on any of the claim records included in the stay. If more than one of the revenue center codes listed below are included on these claims, the code with the highest revenue center total charge amount is used.

??? limitation
	There is approximately a 20% error rate in the revenue center code category 0206 due to coders misunderstanding the term 'post ICU' as including any day after an ICU stay rather than just days in a step-down/lower case version of an ICU. 'Post' was removed from the revenue center code 0206 description, effective 10/1/96 (12/96 MEDPAR update). 0206 Is now defined as 'intermediate ICU'.

<h3>Values</h3>

| Code   | Code Value                                                                   |
|:-------|:-----------------------------------------------------------------------------|
| 0      | General (revenue center 0200)                                                |
| 1      | Surgical (revenue center 0201)                                               |
| 2      | Medical (revenue center 0202)                                                |
| 3      | Pediatric (revenue center 0203)                                              |
| 4      | Psychiatric (revenue center 0204)                                            |
| 6      | Intermediate IOU; (revenue center 0209) prior to 12/96 update was 'post ICU' |
| 7      | Burn care (revenue center 0207)                                              |
| 8      | Trauma (revenue center 0208)                                                 |
| 9      | Other intensive care (revenue code 0209)                                     |

## [MEDPAR Internal Use (By IPSB) Code](https://www.resdac.org/cms-data/variables/MEDPAR-Internal-Use-IPSB-Code)

- Short SAS Name: `IPSBCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Limited availability; for internal use only. Where not available, this field will contain zeroes.



## [MEDPAR Internal Use File Date Code](https://www.resdac.org/cms-data/variables/MEDPAR-Internal-Use-File-Date-Code)

- Short SAS Name: `FILDTCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Limited availability; for internal use only to to identify fiscal year/calendar year segments. Where not available, this field will contain a zero.



## [MEDPAR Internal Use SSI Data](https://www.resdac.org/cms-data/variables/medpar-internal-use-ssi-data)

- Short SAS Name: `INTRNL_USE_SSI_DATA`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Internal use SSI data.



## [MEDPAR Internal Use SSI Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Internal-Use-SSI-Day-Count)

- Short SAS Name: `SSIDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Internal use SSI Day count.



## [MEDPAR Internal Use SSI Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Internal-Use-SSI-Indicator-Code)

- Short SAS Name: `SSICD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Internal use SSI Indicator code.



## [MEDPAR Internal Use Sample Size Code](https://www.resdac.org/cms-data/variables/MEDPAR-Internal-Use-Sample-Size-Code)

- Short SAS Name: `SMPLSIZE`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Limited availability; for internal use only to identify the MEDPAR sample size: 20% (HIC 9th digit = 0, 5); 20% (HIC 9th digit = 4, 8; 60% (remainder). Where not available, this field will contain a zero.



## [MEDPAR Intraocular Lens Amount](https://www.resdac.org/cms-data/variables/medpar-intraocular-lens-amount)

- Short SAS Name: `INTRAOCULAR_LENS_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical intraocular lens supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0276' from all claim records included in the stay.

## [MEDPAR Investigational Device Amount](https://www.resdac.org/cms-data/variables/medpar-investigational-device-amount)

- Short SAS Name: `INVSTGTNL_DVC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical investigational devices supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0624' from all claim records included in the stay.

## [MEDPAR Laboratory Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Laboratory-Charge-Amount)

- Short SAS Name: `LAB_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for laboratory costs related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 030x, 031x, 074x, and 075x from all claim records included in the stay.

## [MEDPAR Latest Claim Accretion Date](https://www.resdac.org/cms-data/variables/MEDPAR-Latest-Claim-Accretion-Date)

- Short SAS Name: `ACRTNDT`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `acrtndt` | `acrtndt` | `acrtndt` | `acrtndt` | `acrtndt` |

| Dataset   | 2008      | 2007      | 2006      | 2005       | 2004       |
|:----------|:----------|:----------|:----------|:-----------|:-----------|
| MedPAR    | `acrtndt` | `acrtndt` | `acrtndt` | `sacrtndt` | `sacrtndt` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `sacrtndt` | `sacrtndt` | `maccrdte` | `maccrdte` | `maccrdte` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date the latest claim record included in the stay was accreted (posted/processed) to the beneficiary master record at the CWF host.

??? derivation
	This field comes from the highest accretion date that is present on the claim records included in the stay.

## [MEDPAR Length of Stay Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Length-Stay-Day-Count)

- Short SAS Name: `LOSCNT`

<h3>Variable Names</h3>

| Dataset   | 2013     | 2012     | 2011     | 2010     | 2009     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| MedPAR    | `loscnt` | `loscnt` | `loscnt` | `loscnt` | `loscnt` |

| Dataset   | 2008     | 2007     | 2006     | 2005     | 2004     |
|:----------|:---------|:---------|:---------|:---------|:---------|
| MedPAR    | `loscnt` | `loscnt` | `loscnt` | `loscnt` | `loscnt` |

| Dataset   | 2003     | 2002     | 2001   | 2000   | 1999   |
|:----------|:---------|:---------|:-------|:-------|:-------|
| MedPAR    | `loscnt` | `loscnt` | `mlos` | `mlos` | `mlos` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count in days of the total length of a beneficiary's stay in a hospital or SNF.

??? derivation
	This field is derived by subtracting the date of discharge (or thru date in SNF cases where beneficiary is still a patient) from the date of admission. If difference is '0,' the value becomes a '1.'

## [MEDPAR Lithotripsy Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Lithotripsy-Charge-Amount)

- Short SAS Name: `LTHTRPSY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for lithotripsy services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 079X from all claim records included in the stay.

## [MEDPAR MA Teaching Indicator Switch](https://www.resdac.org/cms-data/variables/medpar-ma-teaching-indicator-switch)

- Short SAS Name: `MA_TCHING_IND_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify whether the claim contains any request for supplemental IME/DGME/N&AH payment.

??? derivation
	If any claim that comprises the Stay has a condition code (CLM-RLT-COND-CD) equal to '69' populate the MEDPAR MA Teaching Indicator Switch with a 'Y'. If no '69' condition code, populate field with an 'N'.

## [MEDPAR MRI Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-MRI-Charge-Amount)

- Short SAS Name: `MRI_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for MRI services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center 061x from all claim records included in the stay.

## [MEDPAR Medical Surgical Dressing Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-dressing-amount)

- Short SAS Name: `MDCL_SRGCL_DRSNG_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical dressing supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV CNTR CD) '0623' from all claim records included in the stay.

## [MEDPAR Medical Surgical General Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-general-amount)

- Short SAS Name: `MDCL_SRGCL_GNRL_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical general supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV CNTR CD) '0270' from all claim records included in the stay.

## [MEDPAR Medical Surgical Miscellaneous Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-miscellaneous-amount)

- Short SAS Name: `MDCL_SRGCL_MISC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical miscellaneous supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0620', '0625', '0626', '0627', '0628' & '0629' from all claim records included in the stay.

## [MEDPAR Medical Surgical Non-Sterile Supplies Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-non-sterile-supplies-amount)

- Short SAS Name: `MDCL_SRGCL_NSTRL_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical nonsterile supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0271' from all claim records included in the stay.

## [MEDPAR Medical Surgical Pacemaker Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-pacemaker-amount)

- Short SAS Name: `MDCL_SRGCL_PCMKR_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical pacemaker supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0275' from all claim records included in the stay.

## [MEDPAR Medical Surgical Sterile Supplies Amount](https://www.resdac.org/cms-data/variables/medpar-medical-surgical-sterile-supplies-amount)

- Short SAS Name: `MDCL_SRGCL_STRL_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical sterile supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRGAMT) associated with revenue center code (REV-CNTRCD) '0272' from all claim records included in the stay.

## [MEDPAR Medical/Surgical Supplies Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-MedicalSurgical-Supplies-Charge-Amount)

- Short SAS Name: `SUPLYAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for medical/surgical supplies related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 027x and 062x from all claim records included in the stay.

## [MEDPAR Medicare Payment Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Medicare-Payment-Amount)

- Short SAS Name: `PMT_AMT`

<h3>Variable Names</h3>

| Dataset    | 2013      | 2012      | 2011      | 2010      | 2009      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |
| MedPAR     | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |
| Outpatient | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |

| Dataset    | 2008      | 2007      | 2006      | 2005      | 2004      |
|:-----------|:----------|:----------|:----------|:----------|:----------|
| Inpatient  | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |
| MedPAR     | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |
| Outpatient | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` | `pmt_amt` |

| Dataset    | 2003      | 2002      | 2001       | 2000       | 1999       |
|:-----------|:----------|:----------|:-----------|:-----------|:-----------|
| Inpatient  | `pmt_amt` | `pmt_amt` | `pmt_amt`  | `pmt_amt`  | `pmt_amt`  |
| MedPAR     | `pmt_amt` | `pmt_amt` | `mintreim` | `mintreim` | `mintreim` |
| Outpatient | `pmt_amt` | `pmt_amt` | `pmt_amt`  | `pmt_amt`  | `pmt_amt`  |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Amount of payment made from the Medicare trust fund for the services covered by the claim record. Generally, the amount is calculated by the fi; and represents what was paid to the institutional provider, with the exceptions noted below.

NOTE: In some situations, a negative claim payment amount may be present; e.g., (1) when a beneficiary is charged the full deductible during a short stay and the deductible exceeded the amount Medicare pays; or (2) when a beneficiary is charged a coinsurance amount during a long stay and the coinsurance amount exceeds the amount Medicare pays (most prevalent situation involves psych hospitals who are paid a daily per diem rate no matter what the charges are.)

Under IP PPS, Inpatient hospital services are paid based on a predetermined rate per discharge, using the DRG patient classification system and the pricer program. On the IP PPS claim, the payment amount includes the DRG outlier approved payment amount, disproportionate share (since 05/1/86), in- direct medical education (since 10/1/88), total PPS capital (since 10/1/91). It does not include the pass thru amounts (i.e., capital-related costs, direct medical education costs, kidney acquisition costs, bad debts); or any beneficiary-paid amounts (i.e., deductibles and coinsurance); or any other payer reimbursement.

Under SNF PPS, SNFs will classify beneficiaries using the patient classification system known as rugs III. For the SNF PPS claim, the SNF pricer will calculate/return the rate for each revenue center line item with revenue center code = `0022`; multiply the rate times the units count; and then sum the amount payable for all lines with revenue center code `0022` to determine the total claim payment amount.

Exceptions: For claims involving demos and BBA encounter data, the amount reported in this field May not just represent the actual provider payment.

For demo ids `01`,`02`,`03`,`04` -- claims contain amount paid to the provider, except that special 'differentials' paid outside the normal payment system are not included.

For demo ids `05`,`15` -- encounter data 'claims'contain amount Medicare would have paid under FFS, instead of the actual payment to the MCO.

For demo ids `06`,`07`,`08` -- claims contain actual provider payment but represent a special negotiated bundled payment for both part a and part B services. To identify what the conventional provider part a payment would have been, check value code = `y4`.

For BBA encounter data (non-demo) -- 'claims' contain amount Medicare would have paid under FFS, instead of the actual payment to the BBA plan.

 

??? derivation
	This field is derived by accumulating the payment amount that is present on all of the claim records included in the stay (i.e, the sum of payment (reimbursement) reported on the claims that comprise the stay).

## [MEDPAR NCH Claim Type Code](https://www.resdac.org/cms-data/variables/medpar-nch-claim-type-code)

- Short SAS Name: `CLM_TYPE`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

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
	
	INPATIENT 'FULL' ENCOUNTER TYPE CODE DERIVED FROM: (Pre-HDC processing --AVAILABLE IN NCH) 
	CLM_MCO_PD_SW 
	CLM_RLT_COND_CD 
	MCO_CNTRCT_NUM 
	MCO_OPTN_CD 
	MCO_PRD_EFCTV_DT 
	MCO_PRD_TRMNTN_DT

<h3>Values</h3>

In the data element `NCH_CLM_TYPE_CD` (derivation rules) the numbers for these claim types need to be changed - dictionary reflects 61 for all three.

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

## [MEDPAR New Technology Add On Amount](https://www.resdac.org/cms-data/variables/medpar-new-technology-add-amount)

- Short SAS Name: `NEW_TCHNLGY_ADD_ON_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The amount of payments made for discharges involving approved new technologies. If the total covered costs of the discharge exceeds the DRG payment for the case (including adjustments for IME and disproportionate share hospitals (DSH) but excluding outlier payments) an add-on amount is made indicating a new technology was used in the treatment of the beneficiary.

??? derivation
	This field is derived by accumulating the amount field (CLM-VAL-AMT) found in the value code trailer for value code (CLM-VAL-CD) equal to '77' for any claim records included in the stay.

## [MEDPAR Observation Switch](https://www.resdac.org/cms-data/variables/medpar-observation-switch)

- Short SAS Name: `OBSRVTN_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch used to identify whether the claim involves treatment or observation in an observation room.

??? derivation
	If any claim that comprises the Stay has a revenue center code (REV-CNTR-CD) equal to '0762' populate the MEDPAR Observation Switch with a 'Y'. If no '0762' revenue center code populate field with an 'N'.

## [MEDPAR Occupational Therapy Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Occupational-Therapy-Charge-Amount)

- Short SAS Name: `OCPTLAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for occupational therapy services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 043x from all claims records included in the stay.

## [MEDPAR Operating Hospital Amount](https://www.resdac.org/cms-data/variables/medpar-operating-hospital-amount)

- Short SAS Name: `OPRTG_HSP_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The sum of the claim operating HSP amounts reported on the claims that comprise the stay. The operating HSP amount is used to identify the difference between the HSP rate payment (updated HSP x DRG weight) and the federal rate payment (includes DSH, IME, outliers, etc. as applicable) when HSP rate payment exceeds Federal rate payment (otherwise $0).

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9).

??? derivation
	This field is derived by accumulating the Claim Operating HSP Amount (CLM_OPRTG_HSP_AMT) that is present on any of the claim records included in the stay (i.e. the sum of the claim operating HSP amounts reported on the claims that comprise the stay).

## [MEDPAR Operating Room Amount](https://www.resdac.org/cms-data/variables/medpar-operating-room-amount)

- Short SAS Name: `OPRTG_ROOM_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the operating room services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0360', '0361', '0362', '0363', '0364', '0365', '0366', '0367', '0368', '0369', '0710', '0711', '0712', '0713', '0714', '0715', '0717', '0718' & '0719' from all claim records included in the stay.

## [MEDPAR Operating Room Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Operating-Room-Charge-Amount)

- Short SAS Name: `OROOMAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the operating room, recovery room, and labor room delivery used by the beneficiary during the stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 036X, 071X, and 072X from all claim records included in the stay.

## [MEDPAR Operating Room Labor and Delivery Amount](https://www.resdac.org/cms-data/variables/medpar-operating-room-labor-and-delivery-amount)

- Short SAS Name: `OR_LABOR_DLVRY_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the labor room/delivery services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0720', '0721', '0722', '0723', '0724', '0725', '0726', '0727', '0728' & '0729' from all claim records included in the stay.

## [MEDPAR Organ Acquisition Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Organ-Acquisition-Charge-Amount-0)

- Short SAS Name: `ORGNAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for organ acquisition or other donor bank services related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 081x and 089x from all claim records included in the stay.

## [MEDPAR Organ Acquisition Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Organ-Acquisition-Indicator-Code)

- Short SAS Name: `ORGNCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the type of organ acquisition received by the beneficiary during the stay.

??? derivation
	This field is derived by checking for the presence of the organ acquisition indicator revenue center codes listed below on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                             |
|:-------|:-------------------------------------------------------|
| K1     | General classification (revenue code 0810)             |
| K2     | Living donor kidney (revenue code 0811)                |
| K3     | Cadaver donor kidney (revenue code 0812)               |
| K4     | Unknown donor kidney (revenue code 0813)               |
| K5     | Other kidney acquisition (revenue code 0814)           |
| H1     | Cadaver donor heart (revenue code 0815)                |
| H2     | Other heart acquisition (revenue code 0816)            |
| L1     | Donor liver (revenue code 0817)                        |
| 01     | Other organ acquisition (revenue code 0819)            |
| 02     | General acquisition (revenue code 0890)                |
| B1     | Bone donor bank (revenue code 0891)                    |
| 03     | Organ donor bank other than kidney (revenue code 0892) |
| S1     | Skin donor bank (revenue code 0893)                    |
| 04     | Other donor bank (revenue code 0899)                   |
| BLANK  | No organ acquisition indication                        |

## [MEDPAR Other Implants Amount](https://www.resdac.org/cms-data/variables/medpar-other-implants-amount)

- Short SAS Name: `OTHR_IMPLANTS_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical other implant supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0278' from all claim records included in the stay.

## [MEDPAR Other Service Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Other-Service-Charge-Amount)

- Short SAS Name: `OTHRAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for other services (revenue centers that do not fit into other categories) related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with the 'other' revenue center codes from all claim records included in the stay. The 'other' codes include 0002-0099, 022x, 023x, 024x, 052x, 053x, 055x - 060x, 064x - 070x, 076x - 078x, 090x - 095x, and 099x. (Some of these codes are not yet assigned.)

## [MEDPAR Other Supplies Device Amount](https://www.resdac.org/cms-data/variables/medpar-other-supplies-device-amount)

- Short SAS Name: `OTHR_SUPLIES_DVC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical other devices supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0279' from all claim records included in the stay.

## [MEDPAR Outlier Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Outlier-Day-Count)

- Short SAS Name: `OUTLRDAY`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlrday` | `outlrday` | `outlrday` | `outlrday` | `outlrday` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlrday` | `outlrday` | `outlrday` | `outlrday` | `outlrday` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `outlrday` | `outlrday` | `moutdys2` | `moutdys2` | `moutdys2` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of days paid as outliers (either a day or cost outlier) under PPS beyond the DRG threshold.

??? derivation
	This field is derived by checking the MEDPAR utilization day count against the DRG threshold table (DRG weightsfile).

## [MEDPAR Outpatient Service Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Outpatient-Service-Charge-Amount)

- Short SAS Name: `OPSRVC`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for outpatient services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 049x and 050x from all claim records included in the stay.

## [MEDPAR Outpatient Services Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Outpatient-Services-Indicator-Code)

- Short SAS Name: `OPSRVCCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether or not the beneficiary has received outpatient services, ambulatory surgical care, or both.

??? derivation
	This field is derived by checking for the presence of the outpatient services revenue center codes listed below on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                                                           |
|:-------|:-------------------------------------------------------------------------------------|
| 0      | No outpatient services/ambulatory surgical care (revenue code other than 049X, 050X) |
| 1      | Outpatient services (revenue code 050X)                                              |
| 2      | Ambulatory surgical care (revenue code 049X)                                         |
| 3      | Outpatient services and ambulatory surgical care (revenue codes 049X and 050X)       |

## [MEDPAR Oxygen Take Home Amount](https://www.resdac.org/cms-data/variables/medpar-oxygen-take-home-amount)

- Short SAS Name: `OXYGN_TAKE_HOME_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical oxygen take home supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0277' from all claim records included in the stay.

## [MEDPAR PPS Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-PPS-Indicator-Code)

- Short SAS Name: `PPS_IND`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether or not the facility is being paid under the prospective payment system (PPS).

??? derivation
	If the condition code not equal 65 on all of the claims included in the stay and the third position of the provider number is numeric set MEDPAR_PPS_IND_CD to 2 (PPS). Otherwise set it to 0 (Non PPS.)

<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 0      | Non PPS      |
| 2      | PPS          |

## [MEDPAR Pharmacy Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Pharmacy-Charge-Amount)

- Short SAS Name: `PHRMCAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for pharmaceutical costs related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 025x, 026x, and 063x from all claims records included in the stay.

## [MEDPAR Pharmacy Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Pharmacy-Indicator-Code)

- Short SAS Name: `PHRMCYCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether or not the beneficiary received drugs during the stay. It also specifies the type of drugs.

??? derivation
	This field is derived by checking for the presence of drug-specific revenue center codes (listed below) on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                                                                |
|:-------|:------------------------------------------------------------------------------------------|
| 0      | No drugs (revenue code other than those listed below)                                     |
| 1      | General drugs and/pr IV therapy (revenue code 025x, 026x)                                 |
| 2      | Erythropoietin (epoetin: revenue code 0630, 0635, 0637, 0639)                             |
| 3      | Blood clotting drugs (revenue code 0636)                                                  |
| 4      | General drugs and/or IV therapy; and epoetin (combination of values 1 and 2)              |
| 5      | General drugs and/or IV therapy; and blood clotting drugs (combination of values 1 and 3) |

## [MEDPAR Physical Therapy Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Physical-Therapy-Charge-Amount)

- Short SAS Name: `PHYTHAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for physical therapy services provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 042x from all claims records included in the stay.

## [MEDPAR Private Room Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Private-Room-Charge-Amount%01)

- Short SAS Name: `PRVTAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for private room accommodations related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 011x and 014x from all claim records included in the stay.
	
	Exception for SNF rugs demo effective 3/96 SNF update: this field is derived from revenue center codes in the 9033-9044 series.

## [MEDPAR Private Room Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Private-Room-Day-Count)

- Short SAS Name: `PRVTDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of private room days used by the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the revenue center unit count associated with accommodation revenue center codes 011x and 014x from all claim records included in the stay.
	Exception for SNF rugs demo effective 3/96 SNF update: field is derived from revenue center codes in the 9033-9044 series.

## [MEDPAR Product Replacement for known Recall of Product Switch](https://www.resdac.org/cms-data/variables/medpar-product-replacement-known-recall-product-switch)

- Short SAS Name: `PROD_RPLCMT_RCLL_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch used to identify whether a claim involves the replacement of a product as a result of the Manufacturer or FDA having identified the product for recall and therefore a replacement.

??? derivation
	If any claim that comprises the Stay has a Condition code (CLM-RLT-COND-CD) equal to '50' populate the MEDPAR Product Replacement Recall Switch with a 'Y'. If no '50' condition code, populate field with an 'N'.

## [MEDPAR Product Replacement within Product Lifecycle Switch](https://www.resdac.org/cms-data/variables/medpar-product-replacement-within-product-lifecycle-switch)

- Short SAS Name: `PROD_RPLCMT_LIFECYC_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch used to identify whether a claim involves the replacement of a product earlier than the anticipated lifecycle due to an indication the product is not functioning properly.

??? derivation
	If any claim that comprises the Stay has a condition code (CLM-RLT-COND-CD) equal to '49' populate the MEDPAR Product Replacement within Product Lifecycle Switch with a 'Y'. If no '49' condition code, populate field with an 'N'.

## [MEDPAR Professional Fees Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Professional-Fees-Charge-Amount)

- Short SAS Name: `PROFFEES`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for professional fees related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 096x, 097x, and 098x from all claims records included in the stay.

## [MEDPAR Prosthetic Orthotic Amount](https://www.resdac.org/cms-data/variables/medpar-prosthetic-orthotic-amount)

- Short SAS Name: `PRSTHTC_ORTHTC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical prosthetic/orthotic supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center code (REV-CNTR-CD) '0274' from all claim records included in the stay.

## [MEDPAR Provider Number](https://www.resdac.org/cms-data/variables/MEDPAR-Provider-Number)

- Short SAS Name: `PRVDRNUM`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prvdrnum` | `prvdrnum` | `prvdrnum` | `prvdrnum` | `prvdrnum` |

| Dataset   | 2008       | 2007       | 2006       | 2005        | 2004        |
|:----------|:-----------|:-----------|:-----------|:------------|:------------|
| MedPAR    | `prvdrnum` | `prvdrnum` | `prvdrnum` | `prvnumgrp` | `prvnumgrp` |

| Dataset   | 2003        | 2002        | 2001      | 2000      | 1999      |
|:----------|:------------|:------------|:----------|:----------|:----------|
| MedPAR    | `prvnumgrp` | `prvnumgrp` | `mprovno` | `mprovno` | `mprovno` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

MEDPAR provider number.



<h3>Values</h3>



 Provider Number Table.txt 



## [MEDPAR Provider Number Special Unit Code](https://www.resdac.org/cms-data/variables/MEDPAR-Provider-Number-Special-Unit-Code)

- Short SAS Name: `SPCLUNIT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `spclunit` | `spclunit` | `spclunit` | `spclunit` | `spclunit` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `spclunit` | `spclunit` | `spclunit` | `spclunit` | `spclunit` |

| Dataset   | 2003       | 2002       | 2001      | 2000      | 1999      |
|:----------|:-----------|:-----------|:----------|:----------|:----------|
| MedPAR    | `spclunit` | `spclunit` | `mfaclty` | `mfaclty` | `mfaclty` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code identifying the special numbering system for units of hospitals that are excluded from PPS or hospitals with SNF swing-bed designation.

??? derivation
	If the third position of the provider number from the first claim record included in the stay equals 'M', 'R', 'S', 'T', 'U', 'W', 'Y' OR 'Z', it is moved to this field, otherwise it is blank.

<h3>Values</h3>

| Code   | Code Value                                                                            |
|:-------|:--------------------------------------------------------------------------------------|
| M      | PPS-exempt psychiatric unit in CAH                                                    |
| R      | PPS-exempt rehabilitation unit in CAH                                                 |
| S      | PPS-exempt psychiatric unit                                                           |
| T      | PPS-exempt rehabilitation unit                                                        |
| U      | Swing-bed short-term/acute care hospital                                              |
| W      | Swing-bed long-term hospital                                                          |
| Y      | Swing-bed rehabilitation hospital                                                     |
| Z      | Swing-bed rural primary care hospital; eff 10/97 changed to critical access hospitals |
| Blanks | Not PPS-exempt or swing-bed designation                                               |

## [MEDPAR Radiology CT Scan Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-ct-scan-amount)

- Short SAS Name: `RDLGY_CT_SCAN_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the Computed Tomographic (CT) services related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0350', '0351', '0352', '0353', '0354', '0355', '0356', 0357', '0358' & '0359' from all claim records included in the stay.

## [MEDPAR Radiology CT Scan Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-CT-Scan-Indicator-Switch)

- Short SAS Name: `CTSCANSW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology computed tomographic (CT) scan services during the stay.

??? derivation
	This field is derived by checking for revenue center code 035X on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                   |
|:-------|:---------------------------------------------|
| 0      | No radiology CT scan (revenue code not 035X) |
| 1      | Yes radiology CT scan (revenue code 035X)    |

## [MEDPAR Radiology Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Charge-Amount)

- Short SAS Name: `RDLGYAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for radiology costs (including oncology, excluding MRI) related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating revenue center total charge amount associated with revenue center codes 028x, 032x, 033x, 034x, 035x, and 040x from all claim records included in the stay.

## [MEDPAR Radiology Diagnostic Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-diagnostic-amount)

- Short SAS Name: `RDLGY_DGNSTC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the radiology diagnostic services related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0320', '0321', '0322','0323', '0324', '0325', '0326', 0327', '0328' & '0329' from all claim records included in the stay.

## [MEDPAR Radiology Diagnostic Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Diagnostic-Indicator-Switch)

- Short SAS Name: `DGNSTCSW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology diagnostic services during the stay.

??? derivation
	This field is derived by checking for revenue center code 032x on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                      |
|:-------|:------------------------------------------------|
| 0      | No radiology-diagnostic (revenue code not 032x) |
| 1      | Yes radiology-diagnostic (revenue code 032x)    |

## [MEDPAR Radiology Nuclear Medicine Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-nuclear-medicine-amount)

- Short SAS Name: `RDLGY_NUCLR_MDCN_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the nuclear medicine services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0340', '0341', '0342', '0343', '0344', '0345', '0346', '0347', '0348' & '0349' from all claim records included in the stay.

## [MEDPAR Radiology Nuclear Medicine Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Nuclear-Medicine-Indicator-Switch)

- Short SAS Name: `NUCLR_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology nuclear medicine services during the stay.

??? derivation
	This field is derived by checking for revenue center code 034x on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                  |
|:-------|:--------------------------------------------|
| 0      | No nuclear medicine (revenue code not 034x) |
| 1      | Yes nuclear medicine (revenue code 034x)    |

## [MEDPAR Radiology Oncology Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-oncology-amount)

- Short SAS Name: `RDLGY_ONCOLOGY_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the oncology services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0280', '0281', '0282', '0283', '0284', '0285', '0286', '0287', '0288' & '0289' from all claim records included in the stay.

## [MEDPAR Radiology Oncology Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Oncology-Indicator-Switch)

- Short SAS Name: `ONCLGYSW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology oncology services during the stay.

??? derivation
	This field is derived by checking for revenue center code 028X on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                    |
|:-------|:----------------------------------------------|
| 0      | No radiology-oncology (revenue code not 028x) |
| 1      | Yes radiology-oncology (revenue code 028x)    |

## [MEDPAR Radiology Other Imaging Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-other-imaging-amount)

- Short SAS Name: `RDLGY_OTHR_IMGNG_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the radiology other imaging services related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0400', '0401', '0402', '0403', '0404', '0405', '0406', '0407', '0408' & '0409' from all claim records included in the stay.

## [MEDPAR Radiology Other Imaging Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Other-Imaging-Indicator-Switch)

- Short SAS Name: `IMGNG_SW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology other imaging services during the stay.

??? derivation
	This field is derived by checking for revenue center code 040X on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                        |
|:-------|:--------------------------------------------------|
| 0      | No other imaging services (revenue code not 040x) |
| 1      | Yes other imaging services (revenue code 040x)    |

## [MEDPAR Radiology Therapeutic Amount](https://www.resdac.org/cms-data/variables/medpar-radiology-therapeutic-amount)

- Short SAS Name: `RDLGY_THRPTC_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the radiology therapeutic services/supplies related to the beneficiary's stay.

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9)

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRG-AMT) associated with revenue center codes (REV-CNTR-CD) '0330', '0331', '0332', '0333', '0334', '0335', '0336', '0337', '0338' & '0339' from all claim records included in the stay.

## [MEDPAR Radiology Therapeutic Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Radiology-Therapeutic-Indicator-Switch)

- Short SAS Name: `THRPTCSW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not the beneficiary received radiology therapeutic services during the stay.

??? derivation
	This field is derived by checking for revenue center code 033X on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                       |
|:-------|:-------------------------------------------------|
| 0      | No radiology-therapeutic (revenue code not 033X) |
| 1      | Yes radiology-therapeutic (revenue code 033X)    |

## [MEDPAR SNF Qualification From Date](https://www.resdac.org/cms-data/variables/MEDPAR-SNF-Qualification-Date)

- Short SAS Name: `QLFYFROM`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The beginning date of the beneficiary's qualifying stay. For Inpatient claims, the date relates to the PPS portion of the inlier for which there is no utilization to benefits. For SNF claims, the date relates to the qualifying stay from a hospital that is at least two days in a row if the source of admission is an 'a', or at least three days in a row if the source of admission is other than an 'a'.

??? derivation
	This field comes from occurrence span code = 70 and related occurrence span from date, if present on any of the claim records included in the stay. If more than one record has an occurrence span code = 70, with different span dates, the date from the last claim record included in the stay is used.

## [MEDPAR SNF Qualification Through Date](https://www.resdac.org/cms-data/variables/MEDPAR-SNF-Qualification-Through-Date)

- Short SAS Name: `QLFYTHRU`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The ending date of the beneficiary's qualifying stay. For Inpatient claims, the date relates to the PPS portion of the inlier for which there is no utilization to benefits. For SNF claims, the date relates to the qualifying stay from a hospital that is at least two days in a row if the source of admission is an 'A', or at least three days in a row if the source of admission is other than an 'A'.

??? derivation
	This field comes from the occurrence span code = 70 and related occurrence span thru date, if present on any of the claims included in the stay. If more than one record has an occurrence span code = 70, with different span dates, the date from the last claim record included in the stay is used.

## [MEDPAR Semi-Private Room Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Semi-Private-Room-Charge-Amount)

- Short SAS Name: `SPRVTAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for semi-private room accommodations related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center codes 010x, 012x, 013x, and 016x - 019x from all claim records included in the stay.
	
	Exception for SNF rugs demo effective 03/96 SNF update: field is derived from revenue center codes in the 9019-9032 series.

## [MEDPAR Semiprivate Room Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Semiprivate-Room-Day-Count%01)

- Short SAS Name: `SPRVTDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of semi-private room days used by the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the revenue center unit count associated with accommodation revenue center codes 010X, 012X, 013X, 016X - 019X from all claim records included in the stay.

## [MEDPAR Short Stay/Long Stay/SNF Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Short-StayLong-StaySNF-Indicator-Code)

- Short SAS Name: `SSLSSNF`

<h3>Variable Names</h3>

| Dataset   | 2013      | 2012      | 2011      | 2010      | 2009      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `sslssnf` | `sslssnf` | `sslssnf` | `sslssnf` | `sslssnf` |

| Dataset   | 2008      | 2007      | 2006      | 2005      | 2004      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| MedPAR    | `sslssnf` | `sslssnf` | `sslssnf` | `sslssnf` | `sslssnf` |

| Dataset   | 2003      | 2002      | 2001    | 2000    | 1999    |
|:----------|:----------|:----------|:--------|:--------|:--------|
| MedPAR    | `sslssnf` | `sslssnf` | `mstay` | `mstay` | `mstay` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether the stay is a short stay, long stay, or SNF.

??? derivation
	This field is derived from the third position of the provider number that is present on the first claim record included in the stay.

<h3>Values</h3>

| Code   | Code Value                              |
|:-------|:----------------------------------------|
| N      | SNF Stay (Prvdr3 = 5, 6, U, W, Y, or Z) |
| S      | Short-Stay (Prvdr3 = 0, M, R, S, T)     |
| L      | Long-Stay (All Others)                  |

## [MEDPAR Source Inpatient Admission Code](https://www.resdac.org/cms-data/variables/MEDPAR-Source-Inpatient-Admission-Code)

- Short SAS Name: `SRC_ADMS`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating the source of the beneficiary's admission to an Inpatient facility or, for newborn admission, the type of delivery.

??? derivation
	This field comes from the source Inpatient admission code that is present on the last claim record included in the stay.

<h3>Values</h3>

For Inpatient/SNF Claims:

| Code   | Code Value                                                                                                                                                                                                                                          |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | ANOMALY: invalid value, if present, translate to '9'                                                                                                                                                                                                |
| 1      | Non-Health Care Facility Point of Origin (Physician Referral) - The patient was admitted to this facility upon an order of a physician.                                                                                                             |
| 2      | Clinical referral - The patient was admitted upon the recommendation of this facility's clinic physician.                                                                                                                                           |
| 3      | HMO referral - Reserved for national assignment. (eff. 3/08) Prior to 3/08, HMO referral - The patient was admitted upon the recommendation of a health maintenance organization (HMO) physician.                                                   |
| 4      | Transfer from hospital (Different Facility) - The patient was admitted to this facility as a hospital transfer from an acute care facility where he or she was an inpatient.                                                                        |
| 5      | Transfer from a skilled nursing facility (SNF) or Intermediate Care Facility (ICF) - The patient was admitted to this facility as a transfer from a SNF or ICF where he or she was a resident.                                                      |
| 6      | Transfer from another health care facility - The patient was admitted to this facility as a transfer from another type of health care facility not defined elsewhere in this code list where he or she was an inpatient.                            |
| 7      | Emergency room - The patient was admitted to this facility after receiving services in this facility's emergency room department. (Obsolete - eff. 7/1/10)                                                                                          |
| 8      | Court/law enforcement - The patient was admitted upon the direction of a court of law or upon the request of a law enforcement agency's representative. Includes transfers from incarceration facilities.                                           |
| 9      | Information not available - The means by which the patient was admitted is not known.                                                                                                                                                               |
| A      | Reserved for National Assignment. (eff. 3/08) Prior to 3/08 defined as: Transfer from a Critical Access Hospital - patient was admitted/referred to this facility as a transfer from a Critical Access Hospital.                                    |
| B      | Transfer from Another Home Health Agency - The patient was admitted to this home health agency as a transfer from another home health agency. (Discontinued July 1, 2010 - See Condition Code 47)                                                   |
| C      | Readmission to Same Home Health Agency - The patient was readmitted to this home health agency within the same home health episode period. (Discontinued July 1, 2010)                                                                              |
| D      | Transfer from hospital inpatient in the same facility resulting in a separate claim to the payer - The patient was admitted to this facility as a transfer from hospital inpatient within this facility resulting in a separate claim to the payer. |
| E      | Transfer from Ambulatory Surgery Center - The patient was admitted to this facility as a transfer from an ambulatory surgery center. (eff. 10/1/2007)                                                                                               |
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

## [MEDPAR Speech Pathology Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Speech-Pathology-Charge-Amount)

- Short SAS Name: `SPCH_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for speech pathology services (speech, language, audiology) provided during the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 044x and 047x from all claim records included in the stay.

## [MEDPAR Stay Final Action Claims Count](https://www.resdac.org/cms-data/variables/MEDPAR-Stay-Final-Action-Claims-Count)

- Short SAS Name: `FACLMCNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of claim records (final action) included in the stay.

??? derivation
	This field is derived by counting the number of final action claims used to create the stay.

## [MEDPAR Surgical Procedure Code](https://www.resdac.org/cms-data/variables/MEDPAR-Surgical-Procedure-Code)

- Short SAS Name: `PRCDRCD{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The ICD-9-CM code identifying the principal or other surgical procedure performed during the beneficiary's stay. This element is part of the MEDPAR surgical procedure group. It may occur up to 25 times.

NOTE1: Effective with Version 'J', this field has been expanded from 5 bytes to 7 bytes to accommodate the future implementation of ICD-10.

??? derivation
	This field is the actual principal surgical procedure code (1st occurrence) or one of up to 24 other surgical procedure codes that may be present on the last claim record included in the stay.

## [MEDPAR Surgical Procedure Code Count](https://www.resdac.org/cms-data/variables/MEDPAR-Surgical-Procedure-Code-Count)

- Short SAS Name: `PRCDRCNT`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` | `prcdrcnt` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `prcdrcnt` | `prcdrcnt` | `msurgnum` | `msurgnum` | `msurgnum` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of surgical procedure codes included in the stay.

??? derivation
	This field is derived by counting the procedure codes that are reported on the last claim record included in the stay.

## [MEDPAR Surgical Procedure Indicator Switch](https://www.resdac.org/cms-data/variables/MEDPAR-Surgical-Procedure-Indicator-Switch)

- Short SAS Name: `PRCDRSW`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The switch indicating whether or not there were any surgical procedures performed during the beneficiary's stay.

??? derivation
	This field is derived by checking for the presence of procedure codes on the last claim record included in the stay.

<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 0      | No surgery indicated  |
| 1      | Yes surgery indicated |

## [MEDPAR Surgical Procedure Performed Date](https://www.resdac.org/cms-data/variables/MEDPAR-Surgical-Procedure-Performed-Date)

- Short SAS Name: `PRCDRDT{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The date on which the icd-9-cm surgical procedure was performed during the beneficiary's stay. This element is part of the MEDPAR surgical procedure group. It can occur up to 25 times.

??? derivation
	This field is the actual date associated with the principal or one of up to 24 other surgical procedure codes that is present on the last claim record included in the stay.

## [MEDPAR Surgical Procedure Performed Date Count](https://www.resdac.org/cms-data/variables/MEDPAR-Surgical-Procedure-Performed-Date-Count)

- Short SAS Name: `PRCDTCNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of dates associated with the surgical procedures included in the stay.

??? derivation
	This field is derived by counting the surgical procedures dates that are reported on the last claim record included in the stay.

## [MEDPAR Surgical Procedure Version Code](https://www.resdac.org/cms-data/variables/medpar-surgical-procedure-version-code)

- Short SAS Name: `SRGCL_PRCDR_VRSN_CD_{x}`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the surgical procedure code is ICD-9 or ICD-10.



## [MEDPAR Take Home Amount](https://www.resdac.org/cms-data/variables/medpar-take-home-amount)

- Short SAS Name: `TAKE_HOME_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for the medical/surgical take home supplies related to the beneficiary's stay. 

NOTE: Effective with MEDPAR2000 expansion, all amount fields were expanded from S9(7) to S9(9).

??? derivation
	This field is derived by accumulating the revenue center total charge amount (REV-CNTR-TOT-CHRGAMT) associated with revenue center code (REV-CNTRCD) '0273' from all claim records included in the stay.

## [MEDPAR Total Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Total-Charge-Amount)

- Short SAS Name: `TOTCHRG`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The total amount (rounded to whole dollars) of all charges (covered and non-covered) for all services provided to the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the total charge amount from all claim records included in the stay (i.e., the sum of total charges reported on the claims that comprise the stay).

## [MEDPAR Total Covered Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Total-Covered-Charge-Amount)

- Short SAS Name: `CVRCHRG`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The portion of the total charges amount (rounded to wholedollars) that is covered by Medicare for the stay.

??? derivation
	This field is derived by calculating the covered charges from all claim records included in the stay (i.e.,subtract the revenue center non-covered charge amount from the revenue center total charge amount for revenue center code = 0001 that is reported on the claims that comprise the stay; sum the results). Exception: if there exists an erroneous condition relative to revenue center code 0001, the calculation will be made for each revenue center code included on the claims that comprise the stay with the results summed to create the total.

## [MEDPAR Total PPS Capital Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Total-PPS-Capital-Amount)

- Short SAS Name: `PPS_CPTL`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The total amount (rounded to whole dollars) that is payable for capital PPS (e.g., reimbursement for depreciation, rent, certain interest, real estate taxes for hospital buildings/equipment subject to PPS).

??? derivation
	This field is derived by accumulating the total PPS capital amount that is present on any of the claim records included in the stay (i.e., the sum of total PPS capital amounts reported on the claims that comprise the stay).

## [MEDPAR Total Pass Through Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Total-Pass-Through-Amount)

- Short SAS Name: `PASSTHRU`

<h3>Variable Names</h3>

| Dataset   | 2013       | 2012       | 2011       | 2010       | 2009       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `passthru` | `passthru` | `passthru` | `passthru` | `passthru` |

| Dataset   | 2008       | 2007       | 2006       | 2005       | 2004       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `passthru` | `passthru` | `passthru` | `passthru` | `passthru` |

| Dataset   | 2003       | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| MedPAR    | `passthru` | `passthru` | `mbtpdiem` | `mbtpdiem` | `mbtpdiem` |

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The total of all claim pass through amounts (rounded to whole dollars) for the stay.

??? derivation
	This field is derived by multiplying the pass thru per diem amount that is present on the last claim record included in the stay times the MEDPAR utilization day count (the sum of the utilization (covered) days reported on the claims that comprise the stay).

## [MEDPAR Transplant Indicator Code](https://www.resdac.org/cms-data/variables/MEDPAR-Transplant-Indicator-Code)

- Short SAS Name: `TRNSPLNT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code indicating whether or not the beneficiary received a organ transplant during the stay.

??? derivation
	This field is derived by checking for the presence of the transplant revenue center code (listed below) on any of the claim records included in the stay.

<h3>Values</h3>

| Code   | Code Value                                                    |
|:-------|:--------------------------------------------------------------|
| 0      | No organ or kidney transplant (revenue code not 0362 or 0367) |
| 2      | Organ transplant other than kidney (revenue code 0362)        |
| 7      | Kidney transplant (revenue code 0367)                         |

## [MEDPAR Used DME Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Used-DME-Charge-Amount)

- Short SAS Name: `UDME_AMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for used DME (purchase of used DME) related to the beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 0293 from all claim records included in the stay.

## [MEDPAR Utilization Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Utilization-Day-Count%18)

- Short SAS Name: `UTIL_DAY`

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

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of covered days of care that are chargeable to Medicare utilization for the stay.

??? derivation
	This field is derived by accumulating the utilization day count that is present on any of the claim records included in the stay (i.e., the sum of utilization days reported on the claims that comprise the stay).

## [MEDPAR VBP Adjustment Percent](https://www.resdac.org/cms-data/variables/medpar-vbp-adjustment-percent)

- Short SAS Name: `VBP_ADJSTMT_PCT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Under the Hospital Value Based Purchasing (HVBP) program, the percent used to identify an adjustment made to certain subsection (d) IPPS hospital's base operating DRG amount, in accordance with their Total Performance Score (TPS) as required by the Affordable Care Act (ACA). This is the Value Based Purchasing Score.

??? derivation
	This field comes from the Claim VBP Adjustment Percent (CLM-VBP-CLM-ADJSTMT-PCT) that is present on the last claim record included in the stay.

## [MEDPAR VBP Participant Indicator Code](https://www.resdac.org/cms-data/variables/medpar-vbp-participant-indicator-code)

- Short SAS Name: `VBP_PRTCPNT_IND_CD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The code used to identify a reason a hospital is excluded from the Hospital Value Based Purchasing (HVBP) program. The ACA (Section 3001) excludes from HVBP program hospitals that meet certain conditions.

??? derivation
	This field comes from the Claim VBP Participant Indicator code (CLM-VBP-PRTCPNT-IND-CD) that is present on the first claim record included in the stay. If there is no Claim VBP Participant Indicator code on the first claim then take the first found code on any of the other claims that make up the stay.

## [MEDPAR Ward Charge Amount](https://www.resdac.org/cms-data/variables/MEDPAR-Ward-Charge-Amount)

- Short SAS Name: `WARDAMT`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The charge amount (rounded to whole dollars) for ward accommodations related to a beneficiary's stay.

??? derivation
	This field is derived by accumulating the revenue center total charge amount associated with revenue center code 015x from all claim records included in the stay.
	
	Exception for SNF rugs demo effective 03/96 SNF update: this field is derived from revenue center codes in the 9000-9018 series.

## [MEDPAR Ward Day Count](https://www.resdac.org/cms-data/variables/MEDPAR-Ward-Day-Count)

- Short SAS Name: `WARDDAY`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The count of the number of ward days used by the beneficiary for the stay.

??? derivation
	This field is derived by accumulating the revenue center unit count associated with accommodation revenue center code 015x from all claim records included in the stay.
	
	Exception for SNF rugs demo eff 3/96 SNF update: field is derived from revenue center codes in the 9000-9018 series.

## [MEDPAR Warning Indicators Code](https://www.resdac.org/cms-data/variables/MEDPAR-Warning-Indicators-Code)

- Short SAS Name: `WRNGCD`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

The codes (commonly called warning indicators) specifying detailed billing information obtained from the claims analyzed for the stay process. The purpose of these codes is to provide additional information for the MEDPAR user; i.e., let the user know whether or not the stay included adjustments, a single claim or multiple claims, any error conditions, etc.

??? derivation
	This field is packed. Each of the digits identify a specific item of interest to users of the MEDPAR file. Warning indicators 1 and 6, and the first two values of indicator 8, are set early in the process – while processing all claims through the final action algorithm, prior to the creation of the stay record. The other indicators are derived from the claims remaining after the final action processing, which are used to created the stay record.

<h3>Values</h3>



 MEDPAR Warning Indicators Code Table.txt 



## [MEDPAR Year of Record](https://www.resdac.org/cms-data/variables/medpar-year-record)

- Short SAS Name: `MEDPAR_YR_NUM`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Year of the MedPAR Record.



## [MedPAR ID Number](https://www.resdac.org/cms-data/variables/MedPAR-ID-Number)

- Short SAS Name: `MEDPARID`

Contained in

- [MedPAR RIF](../medpar-rif.md#data-documentation)

Unique key for MEDPAR claim.



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

