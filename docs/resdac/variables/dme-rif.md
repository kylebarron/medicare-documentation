# Variable Definitions

!!! note
    These definitions are scraped from ResDAC. Click on the header of a variable description to see the ResDAC page.



## [Carrier Claim Beneficiary Paid Amount](https://www.resdac.org/cms-data/variables/carrier-claim-beneficiary-paid-amount)

- Short SAS Name: `CLM_BENE_PD_AMT`
- Long SAS Name: `CLM_BENE_PD_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The amount paid by the beneficiary for the non-institutional Part B (carrier, or DMERC) claim.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Carrier Claim Cash Deductible Applied Amount*](https://www.resdac.org/cms-data/variables/Carrier-Claim-Cash-Deductible-Applied-Amount)

- Short SAS Name: `DEDAPPLY`
- Long SAS Name: `CARR_CLM_CASH_DDCTBL_APLD_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the amount of the cash deductible as submitted on the claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [Carrier Claim Entry Code](https://www.resdac.org/cms-data/variables/Carrier-Claim-Entry-Code)

- Short SAS Name: `ENTRY_CD`
- Long SAS Name: `CARR_CLM_ENTRY_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Carrier-generated code describing whether the Part B claim is an original debit, full credit, or replacement debit.



## [Carrier Claim HCPCS Year Code](https://www.resdac.org/cms-data/variables/Carrier-Claim-HCPCS-Year-Code)

- Short SAS Name: `HCPCS_YR`
- Long SAS Name: `CARR_CLM_HCPCS_YR_CD`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` | `hcpcs_yr` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the terminal digit of HCPCS version used to code the claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [Carrier Claim Payment Denial Code](https://www.resdac.org/cms-data/variables/Carrier-Claim-Payment-Denial-Code)

- Short SAS Name: `PMTDNLCD`
- Long SAS Name: `CARR_CLM_PMT_DNL_CD`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` |

| Dataset   | 2002       | 2001       | 2000       |
|:----------|:-----------|:-----------|:-----------|
| Carrier   | `pmtdnlcd` | `pmtdnlcd` | `pmtdnlcd` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code on a noninstitutional claim indicating to whom payment was made or if the claim was denied.

NOTE1: Effective with Version 'J', the field has been expanded on the NCH record to 2 bytes, With this expansion, the NCH will no longer use the character values to represent the official two byte values sent in by CWF since 4/2002. During the Version J conversion, all character values were converted to the two byte values.

NOTE2: Effective 4/1/02, this field was expanded to two bytes to accommodate new values. The NCH Nearline file did not expand the current 1-byte field but instituted a crosswalk of the 2-byte field to the 1-byte character value. See table of code for the crosswalk.



<h3>Values</h3>



 [Carrier Claim Payment Denial Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/Carrier%20Claim%20Payment%20Denial%20Table_0.txt) 



## [Carrier Claim Primary Payer Paid Amount*](https://www.resdac.org/cms-data/variables/Carrier-Claim-Primary-Payer-Paid-Amount)

- Short SAS Name: `PRPAYAMT`
- Long SAS Name: `CARR_CLM_PRMRY_PYR_PD_AMT`

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

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the amount of a payment made on behalf of a Medicare bene- ficiary by a primary payer other than Medicare, that the provider is applying to covered Medicare charges on a non-institutional claim.

NOTE: During the Version H conversion, this field was populated with data throughout history (back to service year 1991) by summing up the line item primary payer amounts.



## [Carrier Claim Provider Assignment Indicator Switch](https://www.resdac.org/cms-data/variables/Carrier-Claim-Provider-Assignment-Indicator-Switch)

- Short SAS Name: `ASGMNTCD`
- Long SAS Name: `CARR_CLM_PRVDR_ASGNMT_IND_SW`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

A switch indicating whether or not the provider accepts assignment for the noninstitutional claim.



<h3>Values</h3>

| Code   | Code Value         |
|:-------|:-------------------|
| A      | Assigned claim     |
| N      | Non-assigned claim |

## [Carrier Number](https://www.resdac.org/cms-data/variables/Carrier-Number)

- Short SAS Name: `CARR_NUM`
- Long SAS Name: `CARR_NUM`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The identification number assigned by CMS to a carrier authorized to process claims from a physician or supplier. Effective July 2006, the Medicare Administrative Contractors (MACs) began replacing the existing carriers and started processing physician or supplier claim records for states assigned to its jurisdiction.

NOTE: The 5-position MAC number will be housed in the existing `CARR_NUM` field. During the transi- tion from a carrier to a MAC the `CARR_NUM` field could contain either a Carrier number or a MAC number. See the `CARR_NUM` table of codes to identify the new MAC numbers and their effective dates.



<h3>Values</h3>



 [Carrier Number-MAC Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/Carrier%20Number-MAC%20Table.txt) 



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



## [Claim Diagnosis Code I Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-I-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD1`
- Long SAS Name: `ICD_DGNS_VRSN_CD1`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` |                     |
| Inpatient  | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` |
| Outpatient | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` | `icd_dgns_vrsn_cd1` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10.

NOTE: With 5010, the diagnosis and procedure codes have bee expanded to accommodate ICD-10, even though ICD-10 is not scheduled for implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code II Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-II-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD2`
- Long SAS Name: `ICD_DGNS_VRSN_CD2`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` |                     |
| Inpatient  | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` |
| Outpatient | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` | `icd_dgns_vrsn_cd2` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10.

NOTE: With 5010, the diagnosis and procedure codes have bee expanded to accommodate ICD-10, even though ICD-10 is not scheduled for implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code III Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-III-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD3`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` |                     |
| Inpatient  | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` |
| Outpatient | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` | `icd_dgns_vrsn_cd3` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code IV Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IV-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD4`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` |                     |
| Inpatient  | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` |
| Outpatient | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` | `icd_dgns_vrsn_cd4` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code IX Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-IX-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD9`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` |                     |
| Inpatient  | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` |
| Outpatient | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` | `icd_dgns_vrsn_cd9` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code V Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-V-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD5`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` |                     |
| Inpatient  | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` |
| Outpatient | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` | `icd_dgns_vrsn_cd5` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code VI Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VI-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD6`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` |                     |
| Inpatient  | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` |
| Outpatient | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` | `icd_dgns_vrsn_cd6` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code VII Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VII-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD7`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` |                     |
| Inpatient  | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` |
| Outpatient | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` | `icd_dgns_vrsn_cd7` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code VIII Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-VIII-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD8`

<h3>Variable Names</h3>

| Dataset    | 2013                | 2012                | 2011                | 2010                |
|:-----------|:--------------------|:--------------------|:--------------------|:--------------------|
| Carrier    |                     | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` |                     |
| Inpatient  | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` |
| Outpatient | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` | `icd_dgns_vrsn_cd8` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code X Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-X-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD10`

<h3>Variable Names</h3>

| Dataset    | 2013                 | 2012                 | 2011                 | 2010                 |
|:-----------|:---------------------|:---------------------|:---------------------|:---------------------|
| Carrier    |                      | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` |                      |
| Inpatient  | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` |
| Outpatient | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` | `icd_dgns_vrsn_cd10` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code XI Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XI-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD11`

<h3>Variable Names</h3>

| Dataset    | 2013                 | 2012                 | 2011                 | 2010                 |
|:-----------|:---------------------|:---------------------|:---------------------|:---------------------|
| Carrier    |                      | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` |                      |
| Inpatient  | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` |
| Outpatient | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` | `icd_dgns_vrsn_cd11` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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



## [Claim Diagnosis Code XII Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Claim-Diagnosis-Code-XII-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `ICD_DGNS_VRSN_CD12`

<h3>Variable Names</h3>

| Dataset    | 2013                 | 2012                 | 2011                 | 2010                 |
|:-----------|:---------------------|:---------------------|:---------------------|:---------------------|
| Carrier    |                      | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` |                      |
| Inpatient  | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` |
| Outpatient | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` | `icd_dgns_vrsn_cd12` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the  diagnosis code is ICD-9 or ICD-10.

NOTE:  With 5010, the diagnosis and procedure codes have bee   expanded to accommodate ICD-10, even though ICD-10 is not  scheduled for  implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

## [Claim Disposition Code](https://www.resdac.org/cms-data/variables/Claim-Disposition-Code)

- Short SAS Name: `DISP_CD`
- Long SAS Name: `CLM_DISP_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Code indicating the disposition or outcome of the processing of the claim record.



<h3>Values</h3>

| Code   | Code Value                                                                                                   |
|:-------|:-------------------------------------------------------------------------------------------------------------|
| 1      | Debit accepted                                                                                               |
| 2      | Debit accepted (automatic adjustment) applicable through 4/4/93                                              |
| 3      | Cancel accepted                                                                                              |
| 61     | Conversion code used only during conversion period - 1/1/91 - 2/21/91: debit accepted                        |
| 62     | Conversion code used only during conversion period - 1/1/91 - 2/21/91: debit accepted (automatic adjustment) |
| 63     | Conversion code used only during conversion period - 1/1/91 - 2/21/91: cancel accepted                       |

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



## [Clinical Trial Number](https://www.resdac.org/cms-data/variables/Clinical-Trial-Number)

- Short SAS Name: `CCLTRNUM`
- Long SAS Name: `CLM_CLNCL_TRIL_NUM`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective September 1, 2008 with the implementation of CR#3, the number used to identify all items and services provided to a beneficiary during their participation in a clinical trial.

NOTE: CMS is requesting the clinical trial number be voluntarily reported. The number is assigned by the National Library of Medicine (NLM) Clinical Trials Data Bank when a new study is registered.



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



## [DMERC Claim Ordering Physician NPI Number](https://www.resdac.org/cms-data/variables/DMERC-Claim-Ordering-Physician-NPI-Number)

- Short SAS Name: `RFR_NPI`
- Long SAS Name: `RFR_PHYSN_NPI`

<h3>Variable Names</h3>

| Dataset   | 2012      | 2011      | 2010      | 2009      | 2008      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `rfr_npi` | `rfr_npi` | `rfr_npi` | `rfr_npi` | `rfr_npi` |

| Dataset   | 2007      | 2006      | 2005      | 2004      | 2003      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `rfr_npi` | `rfr_npi` | `rfr_npi` | `rfr_npi` | `rfr_npi` |

| Dataset   | 2002      | 2001      | 2000      |
|:----------|:----------|:----------|:----------|
| Carrier   | `rfr_npi` | `rfr_npi` | `rfr_npi` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

A placeholder field (effective with Version H) for storing the NPI assigned to the physician ordering the Part B services/DMEPOS item.



## [DMERC Claim Ordering Physician UPIN Number](https://www.resdac.org/cms-data/variables/DMERC-Claim-Ordering-Physician-UPIN-Number)

- Short SAS Name: `RFR_UPIN`
- Long SAS Name: `RFR_PHYSN_UPIN`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `rfr_upin` | `rfr_upin` | `rfr_upin` | `rfr_upin` | `rfr_upin` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `rfr_upin` | `rfr_upin` | `rfr_upin` | `rfr_upin` | `rfr_upin` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `rfr_upin` | `rfr_upin` | `rfr_upin` | `brfrupin` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Effective with Version G, the unique physician identification number (UPIN) of the physician ordering the Part B services/DMEPOS item.



## [DMERC Line HCPCS Fourth Modifier Code](https://www.resdac.org/cms-data/variables/DMERC-Line-HCPCS-Fourth-Modifier-Code)

- Short SAS Name: `MDFR_CD4`
- Long SAS Name: `HCPCS_4TH_MDFR_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Prior to Version H this field was named: `HCPCS_4TH_MDFR_CD`.



## [DMERC Line HCPCS Third Modifier Code](https://www.resdac.org/cms-data/variables/DMERC-Line-HCPCS-Third-Modifier-Code)

- Short SAS Name: `MDFR_CD3`
- Long SAS Name: `HCPCS_3RD_MDFR_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Prior to Version H this field was named: `HCPCS_3RD_MDFR_CD`.



## [DMERC Line Item Supplier NPI Number](https://www.resdac.org/cms-data/variables/DMERC-Line-Item-Supplier-NPI-Number)

- Short SAS Name: `SUP_NPI`
- Long SAS Name: `PRVDR_NPI`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

The National Provider Identifier (NPI) assigned to the supplier of the Part B service/DMEPOS line item.

NOTE: Effective May 2007, the NPI will become the national standard identifier for covered health care providers. NPIs will replace the current legacy provider numbers (UPINs, PINs, OSCAR provider numbers, etc.) on the standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capa- bility was there for the NCH to receive NPIs along with an existing legacy number (UPIN, NPIs OSCAR provider numbers, etc.).

NOTE1: CMS has determined that dual provider identifiers (legacy numbers and NPIs) must be available on the NCH. After the 5/07 NPI implementation, the standard system maintainers will add the legacy number to the claim when it is adjudicated. Effective May 2007, no NEW UPINs will be generated for NEW physicians (Part B and Outpatient claims) so there will only be NPIs sent in to the NCH for those phy- sicians.



## [DMERC Line Pricing State Code](https://www.resdac.org/cms-data/variables/DMERC-Line-Pricing-State-Code)

- Short SAS Name: `PRCNG_ST`
- Long SAS Name: `DMERC_LINE_PRCNG_STATE_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Prior to Version H this field was named: CWFB_DME_PRCNG_STATE_CD.



<h3>Values</h3>



 [State Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/State%20Table_0.txt) 



## [DMERC Line Provider State Code](https://www.resdac.org/cms-data/variables/DMERC-Line-Provider-State-Code)

- Short SAS Name: `PRVSTATE`
- Long SAS Name: `PRVDR_STATE_CD`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `prvstate` | `prvstate` | `prvstate` | `prvstate` | `prvstate` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `prvstate` | `prvstate` | `prvstate` | `prvstate` | `prvstate` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `prvstate` | `prvstate` | `prvstate` | `prvstate` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Effective with Version H, the two-digit numeric social security administration (SSA) state code where provider or facility is located.

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).



<h3>Values</h3>



 [State Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/State%20Table_1.txt) 



## [DMERC Line Screen Savings Amount](https://www.resdac.org/cms-data/variables/DMERC-Line-Screen-Savings-Amount)

- Short SAS Name: `SCRNSVGS`
- Long SAS Name: `DMERC_LINE_SCRN_SVGS_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Prior to Version H this field was named: CWFB_DME_SCRN_SVGS_AMT and the field size was S9(5)V99.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [DMERC Line Supplier Provider Number](https://www.resdac.org/cms-data/variables/DMERC-Line-Supplier-Provider-Number)

- Short SAS Name: `SUPLRNUM`
- Long SAS Name: `PRVDR_NUM`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Effective with Version 'G', billing number assigned to the supplier of the Part B service/DMEPOS by the National Supplier Clearinghouse, as reported on the line item for the DMERC claim.

Different types of identifiers may be used.Refer to the variable called `DMERC_LINE_SUPPLR_TYPE_CD` to determine the type used for each line.



## [DMERC Line Supplier Type Code](https://www.resdac.org/cms-data/variables/DMERC-Line-Supplier-Type-Code)

- Short SAS Name: `SUP_TYPE`
- Long SAS Name: `DMERC_LINE_SUPPLR_TYPE_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Prior to Version H this field on the DMERC claim was named: CWFB_PRVDR_TYPE_CD.



<h3>Values</h3>

| Code   | Code Value                                                                                                                                                          |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Clinics, groups, associations, partnerships, or other entities for whom the carrier's own ID number has been assigned.                                              |
| 1      | Physicians or suppliers billing as solo practitioners for who SSN's are shown in the physician ID code field.                                                       |
| 2      | Physicians or suppliers billing as solo practitioners for who the carrier's own physician ID code is shown.                                                         |
| 3      | Suppliers (other than sole proprietorship) or whom employer identification (EI) numbers are used in coding the ID field.                                            |
| 4      | Suppliers (other than sole proprietorship) for who the carrier's own code has been shown.                                                                           |
| 5      | Institutional providers and independent laboratories for whom employer identification (EI) numbers are used in coding the ID field.                                 |
| 6      | Institutional providers and independent laboratories for whom the carrier's own ID number is shown.                                                                 |
| 7      | Clinics, groups, associations, or partnerships for whom employer identification (EI) numbers are used in coding the ID field.                                       |
| 8      | Other entities for whom employer identification (EI) numbers are used in coding the ID field or proprietorship for whom EI numbers are used in coding the ID field. |

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

The unique CCW indentifier for a beneficiary. The CCW assigns a unique beneficiary identification number to each individual who receives Medicare and/or Medicaid, and uses that number to identify an individual’s records in all CCW data files (e.g., Medicare claims, MAX claims, MDS assessment data). This number does not change during a beneficiary’s lifetime and each number is used only once. The `BENE_ID` is specific to the CCW and is not applicable to any other identification system or data source.



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

## [Health Care Common Procedure Coding System](https://www.resdac.org/cms-data/variables/Line-HCFA-Common-Procedure-Coding-System)

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

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The Health Care Common Procedure Coding System (HCPCS) is a collection of codes that represent procedures, supplies, products and services which may be provided to Medicare beneficiaries and to individuals enrolled in private health insurance programs. The codes are divided into three levels, or groups as described below.

In the Institutional Claim Revenue Center Files, this variable can indicate the specific case-mix grouping that Medicare used to pay for skilled nursing facility (SNF), home health, or inpatient rehabilitation facility (IRF) services (see Note 2 below).

Level I

Codes and descriptors copyrighted by the American Medical Association's Current Procedural Terminology, Fourth Edition (CPT-4). These are 5-position numeric codes representing physician and non-physician services.

**** Note 1: **** CPT-4 codes including both long and short descriptions shall be used in accordance with the CMS/AMA agreement. Any other use violates the AMA copyright.

Level II

Includes codes and descriptors copyrighted by the American Dental Association's Current Dental Terminology, Fifth Edition (CDT-5). These are 5-position alpha-numeric codes comprising the D series. All other level II codes and descriptors are approved and maintained jointly by the alpha- numeric editorial panel (consisting of CMS, the Health Insurance Association of America, and the Blue Cross and Blue Shield Association). These are 5-position alpha-numeric codes representing primarily items and non-physician services that are not represented in the level I codes.

Level III

Codes and descriptors developed by Medicare carriers (currently known as Medicare Administrative Contractors; MACs) for use at the local (MAC) level. These are 5-position alpha-numeric codes in the W, X, Y or Z series representing physician and non-physician services that are not represented in the level I or level II codes.

**** Note 2: ****

This field may contain information regarding case-mix grouping that Medicare used to pay for SNF, home health, or IRF services. These groupings are sometimes known as Health Insurance Prospective Payment System (HIPPS) codes. This field will contain a HIPPS code if the revenue center code (`REV_CNTR`) equals 0022 for SNF care, 0023 for home health, or 0024 for IRF care. For home health claims, please also see the revenue center APC/HIPPS code variable (``REV_CNTR`_APC_HIPPS_CD`).



## [Hematocrit/Hemoglobin Test Results](https://www.resdac.org/cms-data/variables/HematocritHemoglobin-Test-Results)

- Short SAS Name: `HCTHGBRS`
- Long SAS Name: `LINE_HCT_HGB_RSLT_NUM`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective September 1, 2008, with the implementation of CR#3, the number used to identify the most recent hematocrit or hemoglobin reading on the noninstitutional claim.

NOTE: The hematocrit/hemoglobin test result field is a redefined field. The field is being defined as X(3) and redefined as numeric (99V9). A numeric test on the alphanumeric field is needed. Whenever a user wants to use the field they must test the alphanumeric field for numerics and if it is numeric then the 99V9 definition would be used. The older data will cause an abend if trying to process numeric data with characters.



## [Hematocrit/Hemoglobin Test Type Code](https://www.resdac.org/cms-data/variables/HematocritHemoglobin-Test-Type-Code)

- Short SAS Name: `HCTHGBTP`
- Long SAS Name: `LINE_HCT_HGB_TYPE_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective September 1, 2008 with the implementation of CR#3, the code used to identify which reading is reflected in the hematocrit/hemoglobin result number field on the noninstitutional claim.



<h3>Values</h3>

| Code   | Code Value      |
|:-------|:----------------|
| R1     | Hemoglobin Test |
| R2     | Hematocrit Test |

## [Line Allowed Charge Amount](https://www.resdac.org/cms-data/variables/Line-Allowed-Charge-Amount)

- Short SAS Name: `LALOWCHG`
- Long SAS Name: `LINE_ALOWD_CHRG_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lalowchg` | `lalowchg` | `lalowchg` | `lalowchg` | `lalowchg` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lalowchg` | `lalowchg` | `lalowchg` | `lalowchg` | `lalowchg` |

| Dataset   | 2002       | 2001       | 2000       | 1999     |
|:----------|:-----------|:-----------|:-----------|:---------|
| Carrier   | `lalowchg` | `lalowchg` | `lalowchg` | `ballow` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The amount of allowed charges for the line item service on the noninstitutional claim. This charge is used to compute pay to providers or reimbursement to beneficiaries. **NOTE: The

Note1: The amount includes beneficiary-paid amounts (i.e., deductible and coinsurance).

Note2: The allowed charge is determined by the lower of three charges: prevailing, customary or actual.



## [Line Beneficiary Part B Deductible Amount](https://www.resdac.org/cms-data/variables/Line-Beneficiary-Part-B-Deductible-Amount)

- Short SAS Name: `LDEDAMT`
- Long SAS Name: `LINE_BENE_PTB_DDCTBL_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012      | 2011      | 2010      | 2009      | 2008      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `ldedamt` | `ldedamt` | `ldedamt` | `ldedamt` | `ldedamt` |

| Dataset   | 2007      | 2006      | 2005      | 2004      | 2003      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `ldedamt` | `ldedamt` | `ldedamt` | `ldedamt` | `ldedamt` |

| Dataset   | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `ldedamt` | `ldedamt` | `ldedamt` | `blnbded` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The amount of money for which the carrier has determined that the beneficiary is liable for the Part B cash deductible for the line item service on the noninstitutional claim.



## [Line Beneficiary Payment Amount](https://www.resdac.org/cms-data/variables/Line-Beneficiary-Payment-Amount)

- Short SAS Name: `LBENPMT`
- Long SAS Name: `LINE_BENE_PMT_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the payment (reim- bursement) made to the beneficiary related to the line item service on the noninstitu- tional claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [Line Beneficiary Primary Payer Code](https://www.resdac.org/cms-data/variables/Line-Beneficiary-Primary-Payer-Code)

- Short SAS Name: `LPRPAYCD`
- Long SAS Name: `LINE_BENE_PRMRY_PYR_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code specifying a federal non-Medicare program or other source that has primary responsibility for the payment of the Medicare beneficiary's medical bills relating to the line item service on the noninstitutional claim.



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

 ***Prior to 12/90***

| Code   | Code Value                                                          |
|:-------|:--------------------------------------------------------------------|
| Y      | Other secondary payer investigation shows Medicare as primary payer |
| Z      | Medicare is primary payer                                           |

## [Line Beneficiary Primary Payer Paid Amount](https://www.resdac.org/cms-data/variables/Line-Beneficiary-Primary-Payer-Paid-Amount)

- Short SAS Name: `LPRPDAMT`
- Long SAS Name: `LINE_BENE_PRMRY_PYR_PD_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lprpdamt` | `lprpdamt` | `lprpdamt` | `lprpdamt` | `lprpdamt` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lprpdamt` | `lprpdamt` | `lprpdamt` | `lprpdamt` | `lprpdamt` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lprpdamt` | `lprpdamt` | `lprpdamt` | `PRPAYAMT` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The amount of a payment made on behalf of a Medicare beneficiary by a primary payer other than Medicare, that the provider is applying to covered Medicare charges for to the line ITEM SERVICE ON THE NONINSTITUTIONAL.



## [Line Coinsurance Amount](https://www.resdac.org/cms-data/variables/Line-Coinsurance-Amount)

- Short SAS Name: `COINAMT`
- Long SAS Name: `LINE_COINSRNC_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012      | 2011      | 2010      | 2009      | 2008      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `coinamt` | `coinamt` | `coinamt` | `coinamt` | `coinamt` |

| Dataset   | 2007      | 2006      | 2005      | 2004      | 2003      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `coinamt` | `coinamt` | `coinamt` | `coinamt` | `coinamt` |

| Dataset   | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `coinamt` | `coinamt` | `coinamt` | `COINAMT` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the beneficiary coinsurance liability amount for this line item service on the noninstitutional claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [Line DME Purchase Price Amount](https://www.resdac.org/cms-data/variables/Line-DME-Purchase-Price-Amount)

- Short SAS Name: `DME_PURC`
- Long SAS Name: `LINE_DME_PRCHS_PRICE_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Effective 5/92, the amount representing the lower of fee schedule for purchase of new or used DME, or actual charge. In case of rental DME, this amount represents the purchase cap; rental payments can only be made until the cap is met. This line item field is applicable to non-institutional claims involving DME, prosthetic, orthotic and supply items, immunosuppressive drugs, pen, ESRD and oxygen items referred to as DMEPOS.



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Diagnosis Code](https://www.resdac.org/cms-data/variables/Line-Diagnosis-Code)

- Short SAS Name: `LINE_ICD_DGNS_CD`
- Long SAS Name: `LINE_ICD_DGNS_CD`

<h3>Variable Names</h3>

| Dataset   | 2012               | 2011               | 2010               | 2009       | 2008       |
|:----------|:-------------------|:-------------------|:-------------------|:-----------|:-----------|
| Carrier   | `line_icd_dgns_cd` | `line_icd_dgns_cd` | `line_icd_dgns_cd` | `linedgns` | `linedgns` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `linedgns` | `linedgns` | `linedgns` | `linedgns` | `linedgns` |

| Dataset   | 2002       | 2001       | 2000       | 1999    |
|:----------|:-----------|:-----------|:-----------|:--------|
| Carrier   | `linedgns` | `linedgns` | `linedgns` | `blndx` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code indicating the diagnosis supporting this line item procedure/service on the noninstitutional claim.



## [Line Diagnosis Code Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Line-Diagnosis-Code-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `LINE_ICD_DGNS_VRSN_CD`
- Long SAS Name: `LINE_ICD_DGNS_VRSN_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis code is ICD-9 or ICD-10.

NOTE: With 5010, the diagnosis and procedure codes have been expanded to accomodate ICD-10, even though ICD-10 is not scheduled for implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

## [Line First Expense Date](https://www.resdac.org/cms-data/variables/Line-First-Expense-Date)

- Short SAS Name: `EXPNSDT1`
- Long SAS Name: `LINE_1ST_EXPNS_DT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `expnsdt1` | `expnsdt1` | `expnsdt1` | `expnsdt1` | `expnsdt1` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `expnsdt1` | `expnsdt1` | `sexpndt1` | `sexpndt1` | `sexpndt1` |

| Dataset   | 2002       | 2001       | 2000       | 1999      |
|:----------|:-----------|:-----------|:-----------|:----------|
| Carrier   | `sexpndt1` | `expnsdt1` | `expnsdt1` | `bexpdt1` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Beginning date (1st expense) for this line item service on the noninstitutional claim.



## [Line HCFA Provider Specialty Code](https://www.resdac.org/cms-data/variables/Line-HCFA-Provider-Specialty-Code)

- Short SAS Name: `HCFASPCL`
- Long SAS Name: `PRVDR_SPCLTY`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` |

| Dataset   | 2002       | 2001       | 2000       | 1999    |
|:----------|:-----------|:-----------|:-----------|:--------|
| Carrier   | `hcfaspcl` | `hcfaspcl` | `hcfaspcl` | `bspec` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

CMS specialty code used for pricing the line item service on the noninstitutional claim.



<h3>Values</h3>



 [HCFA Provider Specialty Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/HCFA%20Provider%20Specialty%20Table.txt) 



## [Line HCFA Type Service Code](https://www.resdac.org/cms-data/variables/Line-HCFA-Type-Service-Code)

- Short SAS Name: `TYPSRVCB`
- Long SAS Name: `LINE_CMS_TYPE_SRVC_CD`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `typsrvcb` | `typsrvcb` | `typsrvcb` | `typsrvcb` | `typsrvcb` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `typsrvcb` | `typsrvcb` | `typsrvcb` | `typsrvcb` | `typsrvcb` |

| Dataset   | 2002       | 2001       | 2000       | 1999   |
|:----------|:-----------|:-----------|:-----------|:-------|
| Carrier   | `typsrvcb` | `typsrvcb` | `typsrvcb` | `btos` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Code indicating the type of service, as defined in the CMS Medicare Carrier Manual, for this line item on the non-institutional claim.



<h3>Values</h3>



 [CMS Type of Service Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/CMS%20Type%20of%20Service%20Table.txt) 



## [Line HCPCS Initial Modifier Code](https://www.resdac.org/cms-data/variables/Line-HCPCS-Initial-Modifier-Code)

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

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

A first modifier to the HCPCS procedure code to enable a more specific procedure identification for the line item service on the noninstitutional claim.



## [Line HCPCS Second Modifier Code](https://www.resdac.org/cms-data/variables/Line-HCPCS-Second-Modifier-Code)

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

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

A second modifier to the HCPCS procedure code to make it more specific than the first modifier code to identify the line item procedures for this claim.



## [Line Last Expense Date](https://www.resdac.org/cms-data/variables/Line-Last-Expense-Date)

- Short SAS Name: `EXPNSDT2`
- Long SAS Name: `LINE_LAST_EXPNS_DT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `expnsdt2` | `expnsdt2` | `expnsdt2` | `expnsdt2` | `expnsdt2` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `expnsdt2` | `expnsdt2` | `sexpndt2` | `sexpndt2` | `sexpndt2` |

| Dataset   | 2002       | 2001       | 2000       | 1999      |
|:----------|:-----------|:-----------|:-----------|:----------|
| Carrier   | `sexpndt2` | `expnsdt2` | `expnsdt2` | `bexpdt2` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The ending date (last expense) for the line item service on the noninstitutional claim.



## [Line NCH BETOS Code](https://www.resdac.org/cms-data/variables/Line-NCH-BETOS-Code)

- Short SAS Name: `BETOS`
- Long SAS Name: `BETOS_CD`

<h3>Variable Names</h3>

| Dataset   | 2012    | 2011    | 2010    | 2009    | 2008    |
|:----------|:--------|:--------|:--------|:--------|:--------|
| Carrier   | `betos` | `betos` | `betos` | `betos` | `betos` |

| Dataset   | 2007    | 2006    | 2005    | 2004    | 2003    |
|:----------|:--------|:--------|:--------|:--------|:--------|
| Carrier   | `betos` | `betos` | `betos` | `betos` | `betos` |

| Dataset   | 2002    | 2001    | 2000    | 1999    |
|:----------|:--------|:--------|:--------|:--------|
| Carrier   | `betos` | `betos` | `betos` | `betos` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the Berenson-Eggers type of service (`BETOS`) for the procedure code based on generally agreed upon clinically meaningful groupings of procedures and services. This field is included as a line item on the noninstitutional claim.

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).

??? derivation
	 Match the HCPCS on the claim to the HCPCS on the HCPCS Master File to obtain the BETOS code.
	

<h3>Values</h3>



 [`BETOS` Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/`BETOS`%20Table.txt) 



## [Line National Drug Code](https://www.resdac.org/cms-data/variables/Line-National-Drug-Code)

- Short SAS Name: `LNNDCCD`
- Long SAS Name: `LINE_NDC_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective 1/1/94 on the DMERC claim, the National Drug Code identifying the oral anti-cancer drugs. Effective with Version H, this line item field was added as a placeholder on the carrier claim.



## [Line Other Applied Amount for 1st Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-1st-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT1`
- Long SAS Name: `LINE_OTHR_APLD_AMT1`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 2nd Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-2nd-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT2`
- Long SAS Name: `LINE_OTHR_APLD_AMT2`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 3rd Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-3rd-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT3`
- Long SAS Name: `LINE_OTHR_APLD_AMT3`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 4th Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-4th-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT4`
- Long SAS Name: `LINE_OTHR_APLD_AMT4`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 5th Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-5th-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT5`
- Long SAS Name: `LINE_OTHR_APLD_AMT5`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 6th Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-6th-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT6`
- Long SAS Name: `LINE_OTHR_APLD_AMT6`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Amount for 7th Code](https://www.resdac.org/cms-data/variables/line-other-applied-amount-7th-code)

- Short SAS Name: `LINE_OTHR_APLD_AMT7`
- Long SAS Name: `LINE_OTHR_APLD_AMT7`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The field used to identify amounts that were used to adjust the amount payable when processing the line item.

See the associated line other applied indicator code in the LINE_OTHR_APLD_IND_CD{#} field.
There are up to 7 of these line applied amount fields (`LINE_OTHR_APLD_AMT1` - `LINE_OTHR_APLD_AMT7`).



<h3>Values</h3>

| Code   |
|:-------|
| XXX.XX |

## [Line Other Applied Indicator 1st Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-1st-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD1`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD1`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_1.txt) 



## [Line Other Applied Indicator 2nd Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-2nd-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD2`
- Long SAS Name: `LINE_OTHER_APLD_IND_CD2`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_0.txt) 



## [Line Other Applied Indicator 3rd Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-3rd-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD3`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD3`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB.txt) 



## [Line Other Applied Indicator 4th Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-4th-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD4`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD4`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_2.txt) 



## [Line Other Applied Indicator 5th Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-5th-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD5`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD5`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_3.txt) 



## [Line Other Applied Indicator 6th Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-6th-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD6`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD6`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_4.txt) 



## [Line Other Applied Indicator 7th Code](https://www.resdac.org/cms-data/variables/line-other-applied-indicator-7th-code)

- Short SAS Name: `LINE_OTHR_APLD_IND_CD7`
- Long SAS Name: `LINE_OTHR_APLD_IND_CD7`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code used to identify the reason the claim payment amount was adjusted during claims processing.

See the associated amounts in the LINE_OTHR_APLD_AMT{#} field.
There are up to 7 of these line applied indicator fields (`LINE_OTHR_APLD_IND_CD1` - `LINE_OTHR_APLD_IND_CD7`).



<h3>Values</h3>



 [LINE_OTHR_APLD_IND_CD_TB.txt](https://www.resdac.org/sites/resdac.umn.edu/files/LINE_OTHR_APLD_IND_CD_TB_5.txt) 



## [Line Payment 80%/100% Code](https://www.resdac.org/cms-data/variables/Line-Payment-80100-Code)

- Short SAS Name: `PMTINDSW`
- Long SAS Name: `LINE_PMT_80_100_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code indicating that the amount shown in the payment field on the noninstitutional line item represents either 80% or 100% of the allowed charges less any deductible, or 100% limitation of liability only.



## [Line Place Of Service Code](https://www.resdac.org/cms-data/variables/line-place-service-code)

- Short SAS Name: `PLCSRVC`
- Long SAS Name: `LINE_PLACE_OF_SRVC_CD`

<h3>Variable Names</h3>

| Dataset   | 2012      | 2011      | 2010      | 2009      | 2008      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `plcsrvc` | `plcsrvc` | `plcsrvc` | `plcsrvc` | `plcsrvc` |

| Dataset   | 2007      | 2006      | 2005      | 2004      | 2003      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `plcsrvc` | `plcsrvc` | `plcsrvc` | `plcsrvc` | `plcsrvc` |

| Dataset   | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `plcsrvc` | `plcsrvc` | `plcsrvc` | `bplacsv` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code indicating the place of service, as defined in the Medicare Carrier Manual, for this line item on the noninstitutional claim.



<h3>Values</h3>



 [List obtained from [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set.html) Place of Service Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/Place%20of%20Service%20Table.txt) 



## [Line Primary Payer Allowed Charge Amount](https://www.resdac.org/cms-data/variables/Line-Primary-Payer-Allowed-Charge-Amount)

- Short SAS Name: `PRPYALOW`
- Long SAS Name: `LINE_PRMRY_ALOWD_CHRG_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)

Effective with Version H, the primary payer allowed charge amount for the line item service on the noninstitutional claim. 

If there is a primary payer other than Medicare, there may be an allowed payment for the provider; if so, this field is populated. 

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [Line Processing Indicator Code](https://www.resdac.org/cms-data/variables/Line-Processing-Indicator-Code)

- Short SAS Name: `PRCNGIND`
- Long SAS Name: `LINE_PRCSG_IND_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The code on a noninstitutional claim indicating to whom payment was made or if the claim was denied.

NOTE1: Effective with Version 'J', the field has been expanded on the NCH record to 2 bytes, With this expansion, the NCH will no longer use the character values to represent the official two byte values sent in by CWF since 4/2002. During the Version J conversion, all character values were converted to the two byte values.

NOTE2: Effective 4/1/02, this field was expanded to two bytes to accommodate new values. The NCH Nearline file did not expand the current 1-byte field but instituted a crosswalk of the 2-byte field to the 1-byte character value. See table of code for the crosswalk.



<h3>Values</h3>



 [Line Processing Indicator Table.txt](https://www.resdac.org/sites/resdac.umn.edu/files/Line%20Processing%20Indicator%20Table.txt) 



## [Line Provider Participating Indicator Code](https://www.resdac.org/cms-data/variables/Line-Provider-Participating-Indicator-Code)

- Short SAS Name: `PRTCPTG`
- Long SAS Name: `PRTCPTNG_IND_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Code indicating whether or not a provider is participating or accepting assignment for this line item service on the noninstitutional claim.



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 1      | Participating                                                                                             |
| 2      | All or some covered and allowed expenses applied to deductible Participating                              |
| 3      | Assignment accepted/non-participating                                                                     |
| 4      | Assignment not accepted/non-participating                                                                 |
| 5      | Assignment accepted but all or some covered and allowed expenses applied to deductible Non-participating. |
| 6      | Assignment not accepted and all covered and allowed expenses applied to deductible non-participating.     |
| 7      | Participating provider not accepting assignment.                                                          |

## [Line Provider Tax Number](https://www.resdac.org/cms-data/variables/Line-Provider-Tax-Number)

- Short SAS Name: `TAX_NUM`
- Long SAS Name: `TAX_NUM`

<h3>Variable Names</h3>

| Dataset   | 2012      | 2011      | 2010      | 2009      | 2008      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `tax_num` | `tax_num` | `tax_num` | `tax_num` | `tax_num` |

| Dataset   | 2007      | 2006      | 2005      | 2004      | 2003      |
|:----------|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `tax_num` | `tax_num` | `tax_num` | `tax_num` | `tax_num` |

| Dataset   | 2002      | 2001      | 2000      | 1999      |
|:----------|:----------|:----------|:----------|:----------|
| Carrier   | `tax_num` | `tax_num` | `tax_num` | `bprovid` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Social security number or employee identification number of physician/supplier used to identify to whom payment is made for the line item service on the noninstitutional claim.



## [Line Service Count](https://www.resdac.org/cms-data/variables/Line-Service-Count)

- Short SAS Name: `SRVC_CNT`
- Long SAS Name: `LINE_SRVC_CNT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` |

| Dataset   | 2002       | 2001       | 2000       | 1999     |
|:----------|:-----------|:-----------|:-----------|:---------|
| Carrier   | `srvc_cnt` | `srvc_cnt` | `srvc_cnt` | `bsrvct` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The count of the total number of services processed for the line item on the non-institutional claim.



## [Line Service Deductible Indicator Switch](https://www.resdac.org/cms-data/variables/Line-Service-Deductible-Indicator-Switch)

- Short SAS Name: `DED_SW`
- Long SAS Name: `LINE_SERVICE_DEDUCTIBLE`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Switch indicating whether or not the line item service on the noninstitutional claim is subject to a deductible.



<h3>Values</h3>

| Code   | Code Value                        |
|:-------|:----------------------------------|
| 0      | SERVICE SUBJECT TO DEDUCTIBLE     |
| 1      | SERVICE NOT SUBJECT TO DEDUCTIBLE |

## [Line Submitted Charge Amount](https://www.resdac.org/cms-data/variables/Line-Submitted-Charge-Amount)

- Short SAS Name: `LSBMTCHG`
- Long SAS Name: `LINE_SBMTD_CHRG_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` |

| Dataset   | 2002       | 2001       | 2000       | 1999      |
|:----------|:-----------|:-----------|:-----------|:----------|
| Carrier   | `lsbmtchg` | `lsbmtchg` | `lsbmtchg` | `bsubchg` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

The amount of submitted charges for the line item service on the noninstitutional claim.



## [NCH Carrier Claim Allowed Charge Amount*](https://www.resdac.org/cms-data/variables/NCH-Carrier-Claim-Allowed-Charge-Amount)

- Short SAS Name: `ALOWCHRG`
- Long SAS Name: `NCH_CARR_CLM_ALOWD_AMT`

<h3>Variable Names</h3>

| Dataset   | 2012       | 2011       | 2010       | 2009       | 2008       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `alowchrg` | `alowchrg` | `alowchrg` | `alowchrg` | `alowchrg` |

| Dataset   | 2007       | 2006       | 2005       | 2004       | 2003       |
|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `alowchrg` | `alowchrg` | `alowchrg` | `alowchrg` | `alowchrg` |

| Dataset   | 2002       | 2001       | 2000       | 1999       |
|:----------|:-----------|:-----------|:-----------|:-----------|
| Carrier   | `alowchrg` | `alowchrg` | `alowchrg` | `alowchrg` |

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the total allowed charges on the claim (the sum of line item allowed charges).

NOTE1: The amount includes beneficiary-paid amounts (i.e., deductible and coinsurance).

NOTE2: During the Version H conversion this field was populated with data throughout history (back to service year 1991).



## [NCH Carrier Claim Submitted Charge Amount*](https://www.resdac.org/cms-data/variables/NCH-Carrier-Claim-Submitted-Charge-Amount)

- Short SAS Name: `SBMTCHRG`
- Long SAS Name: `NCH_CARR_CLM_SBMTD_CHRG_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the total submitted charges on the claim (the sum of line item submitted charges).

NOTE: During the Version H conversion this field was populated with data throughout history (back to service year 1991).



## [NCH Claim Beneficiary Payment Amount*](https://www.resdac.org/cms-data/variables/NCH-Claim-Beneficiary-Payment-Amount)

- Short SAS Name: `BENE_PMT`
- Long SAS Name: `NCH_CLM_BENE_PMT_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the total payments made to the beneficiary for this claim (sum of line payment amounts to the beneficiary.)

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



## [NCH Claim Provider Payment Amount*](https://www.resdac.org/cms-data/variables/NCH-Claim-Provider-Payment-Amount)

- Short SAS Name: `PROV_PMT`
- Long SAS Name: `NCH_CLM_PRVDR_PMT_AMT`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version H, the total payments made to the provider for this claim (sum of line item provider payment amounts.) 

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.



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



## [Primary Claim Diagnosis Code Diagnosis Version Code (ICD-9 or ICD-10)](https://www.resdac.org/cms-data/variables/Primary-Claim-Diagnosis-Code-Diagnosis-Version-Code-ICD-9-or-ICD-10)

- Short SAS Name: `PRNCPAL_DGNS_VRSN_CD`
- Long SAS Name: `PRNCPAL_DGNS_VRSN_CD`

Contained in

- [Durable Medical Equipment RIF](../dme-rif.md#data-documentation)
- [Carrier RIF](../carrier-rif.md#data-documentation)

Effective with Version 'J', the code used to indicate if the diagnosis is ICD-9 or ICD-10.

NOTE: With 5010, the diagnosis and procedure codes have been expanded to accommodate ICD-10, even though ICD-10 is not scheduled for implementation until 10/2013.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 9      | ICD-9        |
| 0      | ICD-10       |

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

 

