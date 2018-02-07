# Variable Definitions

!!! note
    These definitions are scraped from ResDAC. Click on the header of a variable description to see the ResDAC page.



## [113 ICD-10 Recodes](https://www.resdac.org/cms-data/variables/113-ICD-10-Recodes)

- Short SAS Name: `ICD_CODE_113`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field groups (or recodes) the NDI ICD-10 code cause of death into 113 categories.



<h3>Values</h3>



Addtional information regarding these categories can be found on the CDC website (see http://www.cdc.gov/nchs/ndi.htm and http://www.cdc.gov/nchs/data/dvs/im9_2002.pdf.pdf).

Available for 1999-2008. Researchers wishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA.  

 



## [1st Occrrnce of Alzheimer's Dsease and Rltd Disorders or Senile Dementia](https://www.resdac.org/cms-data/variables/1st-Occrrnce-Alzheimers-Dsease-and-Rltd-Disorders-or-Senile-Dementia)

- Short SAS Name: `ALZHDMTE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [358 ICD-10 Recodes](https://www.resdac.org/cms-data/variables/358-ICD-10-Recodes)

- Short SAS Name: `ICD_CODE_358`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field groups (or recodes) the NDI ICD-10 code cause of death into 358 categories.



<h3>Values</h3>



Additional information regarding these categories can be found on the CDC website (see http://www.cdc.gov/nchs/ndi.htm and http://www.cdc.gov/nchs/data/dvs/im9_2002.pdf.pdf).

Available for 1999-2008. Researchers wishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA. 



## [5-digit ZIP code for beneficiary](https://www.resdac.org/cms-data/variables/Zip-Code-Residence)

- Short SAS Name: `ZIP_CD`
- Long SAS Name: `ZIP_CD`

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

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the zip code identified as the beneficiary mailing address.

In some cases, the code may not be the actual state where the beneficiary resides. CMS obtains the mailing address used for cash benefits or the mailing address used for other purposes (for example, premium billing) from Social Security Administration (SSA) and Railroad Retirement Board (RRB) Beneficiary Record Systems.



<h3>Values</h3>

| Code        |
|:------------|
| 5-digit zip |

## [ADHD and Other Conduct Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/adhd-and-other-conduct-disorders-medicare-only-claims)

- Short SAS Name: `ACP_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)





<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period). 
		
For ADHD and other conduct disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [ADHD and Other Conduct Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/adhd-and-other-conduct-disorders-first-ever-occurrence-date-medicare-only-claim-0)

- Short SAS Name: `ACP_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the attention deficit hyperactivity disorder (ADHD) or other conduct disorders indicator. The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Acquired Hypothyroidism End Year Flag](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-End-Year-Flag)

- Short SAS Name: `HYPOTH`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for acquired hypothyroidism as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For acquired hypothyroidism, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims with an acquired hypothyroidism code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Acquired Hypothyroidism First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-First-Ever-Occurrence-Date)

- Short SAS Name: `HYPOTH_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) acquired hypothyroidism indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Acquired Hypothyroidism Mid Year Flag](https://www.resdac.org/cms-data/variables/Acquired-Hypothyroidism-Mid-Year-Flag)

- Short SAS Name: `HYPOTH_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for acquired hypothyroidism on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For acquired hypothyroidism, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims with an acquired hypothyroidism code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Acute Inpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Beneficiary-Payments)

- Short SAS Name: `ACUTE_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of Medicare coinsurance and deductible payments in the acute inpatient hospital setting for the year.  The total acute hospitalization beneficiary payments are calculated as the sum of the beneficiary deductible amount and coinsurance amount (variables called NCH_BENE_IP_DDCTBL_AMT and NCH_BENE_PTA_COINSRNC_LBLTY_AM) for all acute inpatient claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Acute inpatient claims are a subset of the claims in the IP data file consisting of data from both acute hospitals and critical access hospitals (CAH). These facilities are those where either the 3rd digit of the provider number (SAS variable PRVDR_NUM) = 0 or the 3rd and 4th digits of PRVDR_NUM = 13. 

There are 2 cost/use categories from the IP data files: Acute and OIP.

Costs to that beneficiaries are liable for are described in detail on the Medicare.gov website. There is a CMS publication called "Your Medicare Benefits", which explains the deductibles and coinsurance amounts.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Acute Inpatient Covered Days](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Covered-Days)

- Short SAS Name: `ACUTE_COV_DAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of Medicare covered days in the acute inpatient hospital setting for the year.  This variable equals the sum of the CLM_UTLZTN_DAY_CNT variables on the source claims.



<h3>Values</h3>



Acute inpatient hospital claims are a subset of the claims in the IP data file consisting of data from both acute hospitals and critical access hospitals (CAH).  These facilities are those where either the 3rd digit of the provider number (SAS variable PRVDR_NUM) = 0 or the 3rd and 4th digits of PRVDR_NUM = 13.  
  
We consider fully-covered days, days where the beneficiary was liable for coinsurance, and lifetime reserve days to all be Medicare-covered days.  Non-covered days, leave of absence days, and the day of discharge or death are not included.

There are 2 cost/use categories from the IP data files: Acute and the OIP.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html) 



## [Acute Inpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Medicare-Payments)

- Short SAS Name: `ACUTE_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of the Medicare claim payment amounts (CLM_PMT_AMT from each claim) in the acute inpatient hospital setting for a given year. To obtain the total acute hospital Medicare payments, take this variable and add in the annual per diem payment amount (ACUTE_MDCR_PMT +  ACUTE_PERDIEM_AMT).



<h3>Values</h3>



Acute inpatient hospital claims are a subset of the claims in the IP data file consisting of data from both acute hospitals and critical access hospitals (CAH). These facilities are those where either the 3rd digit of the provider number (SAS variable PRVDR_NUM) = 0 or the 3rd and 4th digits of PRVDR_NUM = 13.   
		
ACUTE_PERDIEM_PMT must be added to this field to obtain the total acute hospital Medicare payments for the year.  The annual per diem variable was new in 2010; it will always be null/missing in earlier files.

There are 2 cost/use categories from the IP data files: Acute and the OIP.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Acute Inpatient Stays](https://www.resdac.org/cms-data/variables/Acute-Inpatient-Stays)

- Short SAS Name: `ACUTE_STAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of acute inpatient hospital stays (unique admissions, which may span more than one facility) for the year. An acute inpatient stay is defined as a set of one or more consecutive acute inpatient hospital claims where the beneficiary is only discharged on the most recent claim in the set.  If a beneficiary is transferred to a different provider, the acute stay is continued even if there is a discharge date on the claim from which the beneficiary was transferred.



<h3>Values</h3>



The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year. 

Acute inpatient hospital claims are a subset of the claims in the IP data file consisting of data from both acute hospitals and critical access hospitals (CAH). These facilities are those where either the 3rd digit of the provider number (SAS variable PRVDR_NUM) = 0 or the 3rd and 4th digits of PRVDR_NUM = 13.
  
There are 2 cost/use categories from the IP data files: Acute and the OIP.
 



## [Acute Myocardial Infarction End-of-Year Flag](https://www.resdac.org/cms-data/variables/Acute-Myocardial-Infarction-End-Year-Flag)

- Short SAS Name: `AMI`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Acute Myocardial Infarction Mid-Year Flag](https://www.resdac.org/cms-data/variables/Acute-Myocardial-Infarction-Mid-Year-Flag)

- Short SAS Name: `AMIM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Age of beneficiary at end of year](https://www.resdac.org/cms-data/variables/Age-End-Reference-Year)

- Short SAS Name: `AGE`
- Long SAS Name: `AGE_AT_END_REF_YR`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This is the beneficiary’s age, expressed in years and calculated as of the end of the calendar year, or, for beneficiaries that died during the year, age as of the date of death

CCW calculates this variable.



<h3>Values</h3>

MAXIMUM AGE IS 115

CCW calculates this variable.

| Code               |
|:-------------------|
| Maximum age is 115 |

## [Alzheimer's Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-End-Year-Flag)

- Short SAS Name: `ALZH`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Alzheimer's Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-Mid-Year-Flag)

- Short SAS Name: `ALZHM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Alzheimer's Disease and Rltd Disorders or Senile Dementia EOY Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-and-Rltd-Disorders-or-Senile-Dementia-EOY-Flag)

- Short SAS Name: `ALZHDMTA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Alzheimer's Disease and Rltd Disorders or Senile Dementia Mid-Year Flag](https://www.resdac.org/cms-data/variables/Alzheimers-Disease-and-Rltd-Disorders-or-Senile-Dementia-Mid-Year-Flag)

- Short SAS Name: `ALZHDMTM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Ambulatory Surgery Center Beneficiary Payments](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Beneficiary-Payments)

- Short SAS Name: `ASC_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the sum of coinsurance and deductible payments in the part B ambulatory surgery center (ASC) setting for a given year.  The total beneficiary payment is calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for all relevant lines. ASC claims are a subset of the claims in the Part B Carrier data file.  The ASC claims are identified by the claim lines where the LINE_CMS_TYPE_SRVC_CD ='F'.   "



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Ambulatory Surgery Center Events](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Events)

- Short SAS Name: `ASC_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events in the part B ambulatory surgery center (ASC) setting for a given year.  An event is defined as each line item that contains an ASC service.ASC claims are a subset of the claims in the Part B Carrier data file.  The ASC claims are identified by the claim lines where the LINE_CMS_TYPE_SRVC_CD ='F'.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Ambulatory Surgery Center Medicare Payments](https://www.resdac.org/cms-data/variables/Ambulatory-Surgery-Center-Medicare-Payments)

- Short SAS Name: `ASC_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments in the part B ambulatory surgery center (ASC) setting for a given year.   ASC claims are a subset of the claims in the Part B Carrier data file.  The ASC claims are identified by the claim lines where the LINE_CMS_TYPE_SRVC_CD ='F'.  The total ASC Medicare Payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S').



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Anemia End Year Flag](https://www.resdac.org/cms-data/variables/Anemia-End-Year-Flag)

- Short SAS Name: `ANEMIA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for anemia as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For anemia, beneficiaries must have at least one inpatient, SNF, home health, Part B institutional, or Part B non-institutional (carrier) claim with an anemia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Anemia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Anemia-First-Ever-Occurrence-Date)

- Short SAS Name: `ANEMIA_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) anemia indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Anemia Mid Year Flag](https://www.resdac.org/cms-data/variables/Anemia-Mid-Year-Flag)

- Short SAS Name: `ANEMIA_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for anemia on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For anemia, beneficiaries must have at least one inpatient, SNF, home health, Part B institutional, or Part B non-institutional (carrier) claim with an anemia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Anesthesia Beneficiary Payments](https://www.resdac.org/cms-data/variables/Anesthesia-Beneficiary-Payments)

- Short SAS Name: `ANES_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for part B anesthesia services (ANES) for a given year.  The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines. ANES claims are a subset of the claims, and a subset of procedures in the Part B Carrier data file.   ANES claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits = “P0” and the CARR_LINE_MTUS_CD=`2`.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Anesthesia Events](https://www.resdac.org/cms-data/variables/Anesthesia-Events)

- Short SAS Name: `ANES_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the count of events for part B anesthesia services (ANES) for a given year. ANES claims are a subset of the claims, and a subset of procedures in the Part B Carrier data file.   ANES claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits = “P0” and the CARR_LINE_MTUS_CD=`2`. 

An event is defined as each line item that contains the relevant service."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E &M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Anesthesia Medicare Payments](https://www.resdac.org/cms-data/variables/Anesthesia-Medicare-Payments)

- Short SAS Name: `ANES_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for part B anesthesia services (ANES) for a given year.  ANES claims are a subset of the claims, and a subset of procedures in the Part B Carrier data file.   ANES claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits = “P0” and the CARR_LINE_MTUS_CD=`2`.

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Anxiety Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/anxiety-disorders-medicare-only-claims)

- Short SAS Name: `ANXI_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)





<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period). 
		
For anxiety disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Anxiety Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/anxiety-disorders-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `ANXI_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the anxiety disorders indicator. The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Asthma End Year Flag](https://www.resdac.org/cms-data/variables/Asthma-End-Year-Flag)

- Short SAS Name: `ASTHMA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for asthma as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For asthma, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims with an asthma code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Asthma First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Asthma-First-Ever-Occurrence-Date)

- Short SAS Name: `ASTHMA_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) asthma indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Asthma Mid Year Flag](https://www.resdac.org/cms-data/variables/Asthma-Mid-Year-Flag)

- Short SAS Name: `ASTHMA_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for asthma on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For asthma, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims with an asthma code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Atrial Fibrillation End-of-Year Flag](https://www.resdac.org/cms-data/variables/Atrial-Fibrillation-End-Year-Flag)

- Short SAS Name: `ATRIALFB`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Atrial Fibrillation Mid-Year Flag](https://www.resdac.org/cms-data/variables/Atrial-Fibrillation-Mid-Year-Flag)

- Short SAS Name: `ATRIALFM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Autism Spectrum Disorders - Medicare Only Claims](https://www.resdac.org/cms-data/variables/autism-spectrum-disorders-medicare-only-claims)

- Short SAS Name: `AUTISM_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)





<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period). 
		
For autism spectrum disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Autism Spectrum Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/autism-spectrum-disorders-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `AUTISM_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the autism spectrum disorders indicator. The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Beneficiary Race Code](https://www.resdac.org/cms-data/variables/Beneficiary-Race-Code)

- Short SAS Name: `RACE`
- Long SAS Name: `BENE_RACE_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The race of the beneficiary.



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 0      | UNKNOWN               |
| 1      | WHITE                 |
| 2      | BLACK                 |
| 3      | OTHER                 |
| 4      | ASIAN                 |
| 5      | HISPANIC              |
| 6      | NORTH AMERICAN NATIVE |

## [Beneficiary date of birth](https://www.resdac.org/cms-data/variables/Date-Birth)

- Short SAS Name: `BENE_DOB`
- Long SAS Name: `BENE_BIRTH_DT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This is the beneficiary's date of birth.



<h3>Values</h3>

| Code       |
|:-----------|
| MM/DD/YYYY |

## [Benign Prostatic Hyperplasia End Year Flag](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-End-Year-Flag)

- Short SAS Name: `HYPERP`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for benign prostatic hyperplasia as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For benign prostatic hyperplasia, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a benign prostatic hyperplasia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Benign Prostatic Hyperplasia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-First-Ever-Occurrence-Date)

- Short SAS Name: `HYPERP_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) hyperlipidemia indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Benign Prostatic Hyperplasia Mid Year Flag](https://www.resdac.org/cms-data/variables/Benign-Prostatic-Hyperplasia-Mid-Year-Flag)

- Short SAS Name: `HYPERP_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for benign prostatic hyperplasia on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For benign prostatic hyperplasia, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a benign prostatic hyperplasia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Bipolar Disorder - Medicare Only Claims](https://www.resdac.org/cms-data/variables/bipolar-disorder-medicare-only-claims)

- Short SAS Name: `BIPL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)





<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period). 
		
For bipolar disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Bipolar Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/bipolar-disorder-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `BIPL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the bipolar disorders indicator. The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Breast Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Breast-Cancer-End-Year-Flag)

- Short SAS Name: `CNCRBRST`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For breast cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart with a breast cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website:
https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Breast Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Breast-Cancer-Mid-Year-Flag)

- Short SAS Name: `CNCRBRSM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For breast cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart with a breast cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website:
https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Cataract End-of-Year Flag](https://www.resdac.org/cms-data/variables/Cataract-End-Year-Flag)

- Short SAS Name: `CATARACT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Cataract Mid-Year Flag](https://www.resdac.org/cms-data/variables/Cataract-Mid-Year-Flag)

- Short SAS Name: `CATARCTM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Cerebral Palsy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cerebral-palsy-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `CERPAL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for cerebral palsy as of the end of the calendar year.



<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

For cerebral palsy, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Cerebral Palsy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cerebral-palsy-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `CERPAL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the cerebral palsy indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Chronic Kidney Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Kidney-Disease-End-Year-Flag)

- Short SAS Name: `CHRNKIDN`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Chronic Kidney Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Kidney-Disease-Mid-Year-Flag)

- Short SAS Name: `CHRNKDNM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Chronic Obstructive Pulmonary Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Obstructive-Pulmonary-Disease-End-Year-Flag)

- Short SAS Name: `COPD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Chronic Obstructive Pulmonary Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Chronic-Obstructive-Pulmonary-Disease-Mid-Year-Flag)

- Short SAS Name: `COPDM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Colorectal Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Colorectal-Cancer-End-Year-Flag)

- Short SAS Name: `CNCRCLRC`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for colorectal cancer as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For colorectal cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims at least one day apart, with a colorectal cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Colorectal Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Colorectal-Cancer-Mid-Year-Flag)

- Short SAS Name: `CNCRCLRM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [County Code for Beneficiary (SSA code)](https://www.resdac.org/cms-data/variables/County-Code)

- Short SAS Name: `CNTY_CD`
- Long SAS Name: `COUNTY_CD`

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

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the Social Security Administration (SSA) code fopuyypr the county of identified through the benficiary mailing address.



<h3>Values</h3>



Each state has a series of codes beginning with '000' for each county within that state. Certain cities within that state have their own code. County codes must be combined with state codes in order to locate the specific county. The coding system is the SSA system, not the Federal Information Processing Standard (FIPS).

 In some cases, the code may not be the actual county where the beneficairy resides.  CMS obtains the mailing address used for cash benefits or the mailing address used for other purposes (for example, premium billing) from Social Security Administration (SSA) and Railroad Retirement Board (RRB) Beneficiary Record Systems.  



## [Current Beneficiary Identification Code](https://www.resdac.org/cms-data/variables/current-beneficiary-identification-code)

- Short SAS Name: `CRNT_BIC`
- Long SAS Name: `CRNT_BIC_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The current beneficiary identification code (BIC) specifies the basis of the beneficiary's elgibility for cash payment programs, mainly Social Security. When the individual qualifies under another person's account (for example, as a spouse or child), the code identifies the type of relationship between the individual and primary beneficiary.



<h3>Values</h3>



 Beneficiary Identification Code (BIC) Table.txt 



## [Current Reason for Entitlement Code](https://www.resdac.org/cms-data/variables/Current-Reason-Entitlement-Code)

- Short SAS Name: `CREC`
- Long SAS Name: `ENTLMT_RSN_CURR`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Current reason for Medicare entitlement.



<h3>Values</h3>

This variable indicates how the beneficiary currently qualifies for Medicare.

The current reason for entitlement can differ from the original reason that a beneficiary qualified for Medicare (see the OREC variable).

CMS obtains this information from the Social Security Administration (SSA) and Railroad Retirement Board (RRB) record systems.

| Code   | Code Value                             |
|:-------|:---------------------------------------|
| 0      | Old Age and Survivors Insurance (OASI) |
| 1      | Disability Insurance Benefits (DIB)    |
| 2      | End-stage Renal Disease (ESRD)         |
| 3      | Both DIB and ESRD                      |

## [Cystic Fibrosis and Other Metabolic Developmental Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cystic-fibrosis-and-other-metabolic-developmental-disorders-end-year-indicator-0)

- Short SAS Name: `CYSFIB_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for cystic fibrosis and other metabolic developmental disorders as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For cystic fibrosis and other metabolic developmental disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Cystic Fibrosis and Other Metabolic Developmental Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/cystic-fibrosis-and-other-metabolic-developmental-disorders-first-ever-occurren-0)

- Short SAS Name: `CYSFIB_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the cystic fibrosis and other metabolic developmental disorders indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Depression End-of-Year Flag](https://www.resdac.org/cms-data/variables/Depression-End-Year-Flag)

- Short SAS Name: `DEPRESSN`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Depression Mid-Year Flag](https://www.resdac.org/cms-data/variables/Depression-Mid-Year-Flag)

- Short SAS Name: `DEPRSSNM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Diabetes End-of-Year Flag](https://www.resdac.org/cms-data/variables/Diabetes-End-Year-Flag)

- Short SAS Name: `DIABETES`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Diabetes Mid-Year Flag](https://www.resdac.org/cms-data/variables/Diabetes-Mid-Year-Flag)

- Short SAS Name: `DIABTESM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Dialysis Beneficiary Payments](https://www.resdac.org/cms-data/variables/Dialysis-Beneficiary-Payments)

- Short SAS Name: `DIALYS_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for Part B dialysis services (primarily the professional component since treatments are covered in hospital outpatient) for a given year.  The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Dialysis Events](https://www.resdac.org/cms-data/variables/Dialysis-Events)

- Short SAS Name: `DIALYS_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for Part B dialysis services (primarily the professional component since treatments are covered in hospital outpatient) for a given year. An event is defined as each line item that contains the relevant service.  Dialysis claims are a subset of the claims, and a subset of procedures in the Part B Carrier data file. Dialysis claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits =`P9`.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Dialysis Medicare Payments](https://www.resdac.org/cms-data/variables/Dialysis-Medicare-Payments)

- Short SAS Name: `DIALYS_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for Part B dialysis services (primarily the professional component since treatments are covered in hospital outpatient) for a given year.  Dialysis claims are a subset of the claims, and a subset of procedures in the Part B Carrier data file. Dialysis claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits =`P9`.   

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Durable Medical Equipment Beneficiary Payments](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Beneficiary-Payments)

- Short SAS Name: `DME_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for part B durable medical equipment (DME) for a given year.  The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.  

Claims for DME are a subset of the claims in the Part B Carrier and DME data files. These claims are defined as those with a line BETOS code (BETOS_CD) where the first three digits are (`D1A`,`D1B`,`D1C`,`D1D`,`D1E`, or `D1F`.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Durable Medical Equipment Events](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Events)

- Short SAS Name: `DME_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events in the part B durable medical equipment (DME) for a given year. An event is defined as each line item that contains the relevant service.  

Claims for DME are a subset of the claims in the Part B Carrier and DME data files.  These claims are defined as those with a line BETOS code (BETOS_CD) where the first three digits are (`D1A`,`D1B`,`D1C`,`D1D`,`D1E`, or `D1F`).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Durable Medical Equipment Medicare Payments](https://www.resdac.org/cms-data/variables/Durable-Medical-Equipment-Medicare-Payments)

- Short SAS Name: `DME_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for part B durable medical equipment (DME) for a given year.  Claims for DME are a subset of the claims in the Part B Carrier and DME data files. 

These claims are defined as those with a line BETOS code (BETOS_CD) where the first three digits are (`D1A`,`D1B`,`D1C`,`D1D`,`D1E`, or `D1F`). The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



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



## [End-stage Renal Disease (ESRD) Indicator](https://www.resdac.org/cms-data/variables/ESRD-Indicator)

- Short SAS Name: `ESRD_IND`
- Long SAS Name: `ESRD_IND`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies whether a beneficiary is entitled to Medicare benefits due to end stage renal disease (ESRD).

CMS obtains this information from the Social Security Administration (SSA) record system.



<h3>Values</h3>

| Code   | Code Value                         |
|:-------|:-----------------------------------|
| Y      | The beneficiary has ESRD           |
| 0      | The beneficiary does not have ESRD |

## [Endometrial Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Endometrial-Cancer-End-Year-Flag)

- Short SAS Name: `CNCRENDM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for endometrial cancer as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For endometrial cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with an endometrial cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Endometrial Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Endometrial-Cancer-Mid-Year-Flag)

- Short SAS Name: `CNCENDMM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for endometrial cancer on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For endometrial cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with an endometrial cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Enhanced Medicare 5% Sample Indicator](https://www.resdac.org/cms-data/variables/Enhanced-5-Flag)

- Short SAS Name: `EFIVEPCT`
- Long SAS Name: `ENHANCED_FIVE_PERCENT_FLAG`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was ever included in the CCW 5% sample for any year (1999+).

This enhanced 5% sample is broader than the annual 5% sample (variable that was previously called FIVE_PERCENT_FLAG; currently called SAMPLE_GROUP - when value =`01` or `04`) because it includes all beneficiaries who were ever part of the 5% sample but had a HIC change that was not part of the sample. The "enhanced" indicator variable allows for longitudinal study of the 5% sample (i.e., once in, always in).
CCW creates the 5% sample using standard CMS processes. The 5% random sample consists of people who had a Medicare beneficiary Health Insurance Claim number (HIC) equal to the Claim Account Number (CAN) plus Beneficiary Identity Code (BIC) (HIC=CAN+BIC) where the last two digits of the CAN are in the set {05, 20, 45, 70, 95}.



<h3>Values</h3>

| Code   | Code Value                          |
|:-------|:------------------------------------|
| Y      | Yes, included in enhanced 5% sample |
| nan    | Not included in enhanced 5% sample  |

## [Epilepsy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/epilepsy-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `EPILEP_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for epilepsy as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For epilepsy, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Epilepsy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/epilepsy-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `EPILEP_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the epilepsy indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Evaluation and Management Beneficiary Payments](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Beneficiary-Payments)

- Short SAS Name: `EM_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for the part B evaluation and management (E&M) services for a given year. The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.

E & M claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician claims.   The E & M claims are defined as those with a line BETOS code (BETOS_CD) where the first digit ='M' (but is not M1A or M1B – which are categorized as physician office care in this file – see PHYS_MDCR_PMT).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Evaluation and Management Events](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Events)

- Short SAS Name: `EM_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events for the part B evaluation and management (E&M) services for a given year.  An event is defined as each line item that contains the relevant service.

E & M claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician claims.   The E & M claims are defined as those with a line BETOS code (BETOS_CD) where the first digit ='M' (but is not M1A or M1B – which are categorized as physician office care in this file – see PHYS_MDCR_PMT).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Evaluation and Management Medicare Payments](https://www.resdac.org/cms-data/variables/Evaluation-and-Management-Medicare-Payments)

- Short SAS Name: `EM_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for the part B evaluation and management (E&M) services for a given year. E & M claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician claims.   The E & M claims are defined as those with a line BETOS code (BETOS_CD) where the first digit ='M' (but is not M1A or M1B – which are categorized as physician office care in this file – see PHYS_MDCR_PMT).

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Fibromyalgia, Chronic Pain and Fatigue End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/fibromyalgia-chronic-pain-and-fatigue-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `FIBRO_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for fibromyalgia, chronic pain and fatigue as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For fibromyalgia, chronic pain and fatigue, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Fibromyalgia, Chronic Pain and Fatigue First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/fibromyalgia-chronic-pain-and-fatigue-first-ever-occurrence-date-medicare-only-0)

- Short SAS Name: `FIBRO_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the fibromyalgia, chronic pain and fatigue indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [First Occurrence of Acute Myocardial Infarction](https://www.resdac.org/cms-data/variables/First-Occurrence-Acute-Myocardial-Infarction)

- Short SAS Name: `AMIE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the beneficiary met the chronic condition algorithm criteria.  The earliest possible value is 1999MMDD.



## [First Occurrence of Alzheimer's Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Alzheimers-Disease)

- Short SAS Name: `ALZHE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Atrial Fibrillation](https://www.resdac.org/cms-data/variables/First-Occurrence-Atrial-Fibrillation)

- Short SAS Name: `ATRIALFE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Breast Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Breast-Cancer)

- Short SAS Name: `CNCRBRSE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the beneficiary met the chronic condition algorithm criteria.  The earliest possible value is 1999MMDD.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [First Occurrence of Cataract](https://www.resdac.org/cms-data/variables/First-Occurrence-Cataract)

- Short SAS Name: `CATARCTE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Chronic Kidney Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Chronic-Kidney-Disease)

- Short SAS Name: `CHRNKDNE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Chronic Obstructive Pulmonary Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Chronic-Obstructive-Pulmonary-Disease)

- Short SAS Name: `COPDE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Colorectal Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Colorectal-Cancer)

- Short SAS Name: `CNCRCLRE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the beneficiary met the chronic condition algorithm criteria.  The earliest possible value is 1999MMDD.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [First Occurrence of Depression](https://www.resdac.org/cms-data/variables/First-Occurrence-Depression)

- Short SAS Name: `DEPRSSNE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Diabetes](https://www.resdac.org/cms-data/variables/First-Occurrence-Diabetes)

- Short SAS Name: `DIABTESE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Endometrial Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Endometrial-Cancer)

- Short SAS Name: `CNCENDME`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) endometrial cancer indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [First Occurrence of Glaucoma](https://www.resdac.org/cms-data/variables/First-Occurrence-Glaucoma)

- Short SAS Name: `GLAUCMAE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Heart Failure](https://www.resdac.org/cms-data/variables/First-Occurrence-Heart-Failure)

- Short SAS Name: `CHFE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Hip/Pelvic Fracture](https://www.resdac.org/cms-data/variables/First-Occurrence-HipPelvic-Fracture)

- Short SAS Name: `HIPFRACE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Ischemic Heart Disease](https://www.resdac.org/cms-data/variables/First-Occurrence-Ischemic-Heart-Disease)

- Short SAS Name: `ISCHMCHE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Lung Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Lung-Cancer)

- Short SAS Name: `CNCRLNGE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) lung cancer indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).
 



## [First Occurrence of Osteoporosis](https://www.resdac.org/cms-data/variables/First-Occurrence-Osteoporosis)

- Short SAS Name: `OSTEOPRE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [First Occurrence of Prostate Cancer](https://www.resdac.org/cms-data/variables/First-Occurrence-Prostate-Cancer)

- Short SAS Name: `CNCRPRSE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) prostate cancer indicator.  The variable will be blank for beneficiaries that have never had the condition.



## [First Occurrence of Rheumatoid Arthritis / Osteoarthritis](https://www.resdac.org/cms-data/variables/First-Occurrence-Rheumatoid-Arthritis-Osteoarthritis)

- Short SAS Name: `RA_OA_E`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW)rheumatoid arthritis/osteoarthritis indicator.  The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [First Occurrence of Stroke / Transient Ischemic Attack](https://www.resdac.org/cms-data/variables/First-Occurrence-Stroke-Transient-Ischemic-Attack)

- Short SAS Name: `STRKTIAE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the beneficiary met the chronic condition algorithm criteria.  The earliest possible value is 1999MMDD.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Glaucoma End-of-Year Flag](https://www.resdac.org/cms-data/variables/Glaucoma-End-Year-Flag)

- Short SAS Name: `GLAUCOMA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Glaucoma Mid-Year Flag](https://www.resdac.org/cms-data/variables/Glaucoma-Mid-Year-Flag)

- Short SAS Name: `GLAUCMAM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [HMO Coverage Count](https://www.resdac.org/cms-data/variables/HMO-Coverage-Count)

- Short SAS Name: `HMO_MO`
- Long SAS Name: `BENE_HMO_CVRAGE_TOT_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Total number of months of HMO coverage.



<h3>Values</h3>



This variable counts the number of months during the year that the beneficiary received their Part A and Part B benefits through a managed care plan (i.e., a Medicare Advantage [MA] plan) instead of the traditional fee-for-service (FFS) program. Any month where the HMO indicator variable (HMOINDXX) was anything other than a 0 (not a member of an HMO) or a 4 (FFS particpant in a case or disease management demonstration project) is counted as a MA month. 



## [HMO Indicator - April](https://www.resdac.org/cms-data/variables/hmo-indicator-april)

- Short SAS Name: `HMOIND04`
- Long SAS Name: `HMO_IND_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - August](https://www.resdac.org/cms-data/variables/hmo-indicator-august)

- Short SAS Name: `HMOIND08`
- Long SAS Name: `HMO_IND_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - December](https://www.resdac.org/cms-data/variables/hmo-indicator-december)

- Short SAS Name: `HMOIND12`
- Long SAS Name: `HMO_IND_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - February](https://www.resdac.org/cms-data/variables/hmo-indicator-february)

- Short SAS Name: `HMOIND02`
- Long SAS Name: `HMO_IND_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - January](https://www.resdac.org/cms-data/variables/hmo-indicator-january)

- Short SAS Name: `HMOIND01`
- Long SAS Name: `HMO_IND_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - July](https://www.resdac.org/cms-data/variables/hmo-indicator-july)

- Short SAS Name: `HMOIND07`
- Long SAS Name: `HMO_IND_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - June](https://www.resdac.org/cms-data/variables/hmo-indicator-june)

- Short SAS Name: `HMOIND06`
- Long SAS Name: `HMO_IND_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - March](https://www.resdac.org/cms-data/variables/hmo-indicator-march)

- Short SAS Name: `HMOIND03`
- Long SAS Name: `HMO_IND_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - May](https://www.resdac.org/cms-data/variables/hmo-indicator-may)

- Short SAS Name: `HMOIND05`
- Long SAS Name: `HMO_IND_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - November](https://www.resdac.org/cms-data/variables/hmo-indicator-november)

- Short SAS Name: `HMOIND11`
- Long SAS Name: `HMO_IND_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - October](https://www.resdac.org/cms-data/variables/hmo-indicator-october)

- Short SAS Name: `HMOIND10`
- Long SAS Name: `HMO_IND_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [HMO Indicator - September](https://www.resdac.org/cms-data/variables/hmo-indicator-september)

- Short SAS Name: `HMOIND09`
- Long SAS Name: `HMO_IND_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Historically, most Medicare managed care plans have been health maintenance organizations (HMOs), hence the name of the variable. This variable indicates whether the beneficiary was enrolled in a Medicare Advantage (MA) plan during a given month. The 01 through 12 at the end of the variable name correspond with the month (i.e., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                |
|:-------|:----------------------------------------------------------------------------------------------------------|
| 0      | Not a member of an HMO                                                                                    |
| 1      | Non-lock-in, CMS to process provider claims                                                               |
| 2      | Non-lock-in, group health organization (GHO; MA plan) to process in plan Part A and in area Part B claims |
| 4      | Fee-for-service participant in case or disease management demonstration project                           |
| 5      | Not in documentation                                                                                      |
| A      | Lock-in, CMS to process provider claims                                                                   |
| B      | Lock-in, GHO to process in plan Part A and in area Part B claims                                          |
| C      | Lock-in, GHO to process all provider claims                                                               |

## [Heart Failure End-of-Year Flag](https://www.resdac.org/cms-data/variables/Heart-Failure-End-Year-Flag)

- Short SAS Name: `CHF`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Heart Failure Mid-Year Flag](https://www.resdac.org/cms-data/variables/Heart-Failure-Mid-Year-Flag)

- Short SAS Name: `CHFM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Hip/Pelvic Fracture End-of-Year Flag](https://www.resdac.org/cms-data/variables/HipPelvic-Fracture-End-Year-Flag)

- Short SAS Name: `HIPFRAC`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Hip/Pelvic Fracture Mid-Year Flag](https://www.resdac.org/cms-data/variables/HipPelvic-Fracture-Mid-Year-Flag)

- Short SAS Name: `HIPFRACM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Home Health Medicare Payments](https://www.resdac.org/cms-data/variables/Home-Health-Medicare-Payments)

- Short SAS Name: `HH_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments in the home health (HH) setting for a given year.  Calculated as the sum of CLM_PMT_AMT for all HH claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Home Health Visits](https://www.resdac.org/cms-data/variables/Home-Health-Visits)

- Short SAS Name: `HH_VISITS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of home health (HH) visits for a given year.  The CCW variable CLM_HHA_TOT_VISIT_CNT is used to obtain this variable. 



<h3>Values</h3>



The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year.
 



## [Hospice Covered Days](https://www.resdac.org/cms-data/variables/Hospice-Covered-Days)

- Short SAS Name: `HOS_COV_DAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of Medicare covered days in the hospice setting for a given year.   This variable equals the sum of the CLM_UTLZTN_DAY_CNT variables on the source claims.



<h3>Values</h3>



We consider fully-covered days, days where the beneficiary was liable for coinsurance, and lifetime reserve days to all be Medicare-covered days.  Non-covered days, leave of absence days, and the day of discharge or death are not included.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Hospice Medicare Payments](https://www.resdac.org/cms-data/variables/Hospice-Medicare-Payments)

- Short SAS Name: `HOS_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments in the hospice setting for a given year.  The total Medicare payments is calculated as the sum of CLM_PMT_AMT for all hospice claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Hospice Stays](https://www.resdac.org/cms-data/variables/Hospice-Stays)

- Short SAS Name: `HOS_STAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of stays (unique admissions, which may span more than one facility) in the hospice setting for a given year.  A hospice stay is defined as a set of one or more consecutive hospice claims where the beneficiary is only discharged on the most recent claim in the set.



<h3>Values</h3>



The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year. 



## [Hospital Outpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Beneficiary-Payments)

- Short SAS Name: `HOP_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of Medicare coinsurance and deductible payments in the hospital outpatient setting for a given year. Calculated as the sum of DED_AMT and COIN_AMT for all HOP claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Costs to that beneficiaries are liable for are described in detail on the Medicare.gov website.  There is a CMS publication called "Your Medicare Benefits", which explains the deductibles and coinsurance amounts.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Hospital Outpatient Emergency Room Visits](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Emergency-Room-Visits)

- Short SAS Name: `HOP_ER_VISITS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of unique emergency department revenue center dates (as a proxy for an ED visit) in the hospital outpatient data file for a given year.  Revenue centers indicating Emergency Room use were (0450, 0451, 0452, 0456, or 0459). 



<h3>Values</h3>



Note that additional ED  revenue centers are found in the inpatient data files – if the ED visit resulted in an IP admission at the same facility.
  
There are 2 variables that contain counts of  ER visits in different settings: this variable and the Inpatient ER (IP_ER_VISITS)
 



## [Hospital Outpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Medicare-Payments)

- Short SAS Name: `HOP_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments in the hospital outpatient setting for a given year.  Calculated as the sum of CLM_PMT_AMT for all HOP claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Hospital Outpatient Visits](https://www.resdac.org/cms-data/variables/Hospital-Outpatient-Visits)

- Short SAS Name: `HOP_VISITS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of unique revenue center dates (as a proxy for visits) in the hospital outpatient setting for a given year. 



<h3>Values</h3>



The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year.

ER visits in the HOP setting are counted in this variable (also see HOP_ER_VISITS).
 



## [Hospital Readmissions](https://www.resdac.org/cms-data/variables/Hospital-Readmissions)

- Short SAS Name: `READMISSIONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of hospital readmissions in the acute inpatient setting for a given year.  The CLM_FROM_DT for the original admission must have been in the year of the data file, however it was permissible for the readmission claim to have occurred in January of the following year.  A beneficiary is considered to be readmitted when they have an acute inpatient stay with a discharge status that is not expired (DSCHRG_STUS≠20) or left against medical advice (DSCHRG_STUS≠07) within 30 days of a previous acute inpatient stay with a discharge status that is also not expired or left against medical advice.



<h3>Values</h3>



All hospital stays during the year, including readmissions, are counted in the ACUTE_STAYS variable.  Similarly, all acute hospital inpatient payments including payments for readmissions are included in the ACUTE_* payment variables. 
 



## [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-e-0)

- Short SAS Name: `HIVAIDS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for human immunodeficiency virus and/or acquired immunodeficiency syndrom (HIV/AIDS) as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For human immunodeficiency virus and/or acquired immunodeficiency syndrom (HIV/AIDS), beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Human Immunodeficiency Virus and/or Acquired Immunodeficiency Syndrome (HIV/AIDS) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/human-immunodeficiency-virus-andor-acquired-immunodeficiency-syndrome-hivaids-0)

- Short SAS Name: `HIVAIDS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the human immunodeficiency virus and/or acquired immunodeficiency syndrom (HIV/AIDS) indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Hyperlipidemia End Year Flag](https://www.resdac.org/cms-data/variables/Hyperlipidemia-End-Year-Flag)

- Short SAS Name: `HYPERL`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for hyperlipidemia as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For hyperlipidemia, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a hyperlipidemia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Hyperlipidemia First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Hyperlipidemia-First-Ever-Occurrence-Date)

- Short SAS Name: `HYPERL_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the first calendar year, month, and day in which the  beneficiary met the chronic condition algorithm criteria.  The earliest  possible value is 1999MMDD.



## [Hyperlipidemia Mid Year Flag](https://www.resdac.org/cms-data/variables/Hyperlipidemia-Mid-Year-Flag)

- Short SAS Name: `HYPERL_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for hyperlipidemia on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For hyperlipidemia, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a hyperlipidemia code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Hypertension End Year Flag](https://www.resdac.org/cms-data/variables/Hypertension-End-Year-Flag)

- Short SAS Name: `HYPERT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for hypertension (high blood pressure) as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For hypertension, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a hypertension code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Hypertension First Ever Occurrence Date](https://www.resdac.org/cms-data/variables/Hypertension-First-Ever-Occurrence-Date)

- Short SAS Name: `HYPERT_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the chronic condition data warehouse (CCW) hypertension (high blood pressure) indicator.  The variable will be blank for beneficiaries that have never had the condition



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999.  If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Hypertension Mid Year Flag](https://www.resdac.org/cms-data/variables/Hypertension-Mid-Year-Flag)

- Short SAS Name: `HYPERT_MID`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for hypertension (high blood pressure) on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For hypertension, beneficiaries must have at least one inpatient, SNF, or home health claim, or two Part B (institutional or non-institutional) claims, with a hypertension code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [ICD-10 Code](https://www.resdac.org/cms-data/variables/ICD-10-Code)

- Short SAS Name: `ICD_CODE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field identifies only those codes associated with cause of death.



<h3>Values</h3>



All ICD-10 codes begin with an alpha character followed by two or three digits. NDI results do not include decimals in the cause of death codes. The decimal is implied between the second and third digits for ICD-10 codes.

Available for 1999-2008. Researchers whishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA. 



## [ICD-10 Title](https://www.resdac.org/cms-data/variables/ICD-10-Title)

- Short SAS Name: `ICD_TITLE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field is the narrative description of the ICD-10 code value.



<h3>Values</h3>



Available for 1999-2008. Researchers wishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA. 



## [Imaging Beneficiary Payments](https://www.resdac.org/cms-data/variables/Imaging-Beneficiary-Payments)

- Short SAS Name: `IMG_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for imaging services (IMG) for a given year.  The total beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.  

Claims for imaging procedures are a subset of the claims, and a subset of procedures in the Part B Carrier and DME data files. These imaging claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =I (except for `I1E`, or `I1F` – which are considered Part B drugs).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Imaging Events](https://www.resdac.org/cms-data/variables/Imaging-Events)

- Short SAS Name: `IMG_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events for imaging services (IMG) for a given year.  An event is defined as each line item that contains the relevant service. Claims for imaging procedures are a subset of the claims, and a subset of procedures in the Part B Carrier and DME data files. 

These imaging claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =I (except for `I1E`, or `I1F` – which are considered Part B drugs).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Imaging Medicare Payments](https://www.resdac.org/cms-data/variables/Imaging-Medicare-Payments)

- Short SAS Name: `IMG_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for imaging services (IMG) for a given year.  Claims for imaging procedures are a subset of the claims, and a subset of procedures in the Part B Carrier and DME data files. These imaging claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =I (except for `I1E`, or `I1F` – which are considered Part B drugs).

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Inpatient Emergency Room Visits](https://www.resdac.org/cms-data/variables/Inpatient-Emergency-Room-Visits)

- Short SAS Name: `IP_ER_VISITS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of emergency department claims in the inpatient setting for a given year.  The revenue centers indicating Emergency Room use were (0450, 0451, 0452, 0456, 0459).



<h3>Values</h3>



Note that additional ED  revenue centers are found in the HOP data files – if the ED visit did not result in an IP admission at the same facility.  See the variable HOP_ER_VISITS  within this data file).

There are 2 variables that contain counts of  ER visits in different settings: this variable and the Hospital Outpatient ER (HOP_ER_VISITS) 



## [Intellectual Disabilities and Related Conditions End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/intellectual-disabilities-and-related-conditions-end-year-indicator-medicare-on-0)

- Short SAS Name: `INTDIS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for intellectual disabilities and related conditions as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For intellectual disabilities and related conditions, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Intellectual Disabilities and Related Conditions First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/intellectual-disabilities-and-related-conditions-first-ever-occurrence-date-0)

- Short SAS Name: `INTDIS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the intellectual disabilities and related conditions indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Ischemic Heart Disease End-of-Year Flag](https://www.resdac.org/cms-data/variables/Ischemic-Heart-Disease-End-Year-Flag)

- Short SAS Name: `ISCHMCHT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Ischemic Heart Disease Mid-Year Flag](https://www.resdac.org/cms-data/variables/Ischemic-Heart-Disease-Mid-Year-Flag)

- Short SAS Name: `ISCHMCHM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Learning Disabilities End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/learning-disabilities-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `LEADIS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for learning disabilities as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For learning disabilities, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Learning Disabilities First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/learning-disabilities-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `LEADIS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the learning disabilities indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Leukemias and Lymphomas End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/leukemias-and-lymphomas-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `LEUKLYMPH_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for leukemias and lymphomas as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For leukemias and lymphomas, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Leukemias and Lymphomas First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/leukemias-and-lymphomas-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `LEUKLYMPH_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the leukemias and lymphomas indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Liver Disease Cirrhosis and Other Liver Conditions (excluding Hepatitis) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-end-year)

- Short SAS Name: `LIVER_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for liver disease, cirrhosis and other liver conditions (excluding hepatitis) as of the end of the calendar year.



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Liver Disease, Cirrhosis and Other Liver Conditions (excluding Hepatitis) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/liver-disease-cirrhosis-and-other-liver-conditions-excluding-hepatitis-first-ev-0)

- Short SAS Name: `LIVER_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the liver disease, cirrhosis and other liver conditions (excluding hepatitis) indicator.The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Lung Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Lung-Cancer-End-Year-Flag)

- Short SAS Name: `CNCRLUNG`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for lung cancer as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For lung cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with a lung cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Lung Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Lung-Cancer-Mid-Year-Flag)

- Short SAS Name: `CNCRLNGM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for lung cancer on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For lung cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with a lung cancer code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Major Depressive Affective Disorder End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/major-depressive-affective-disorder-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `DEPSN_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for major depressive affective disorder as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For major depressive affective disorder, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Major Depressive Affective Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/major-depressive-affective-disorder-first-ever-occurrence-date-medicare-only-0)

- Short SAS Name: `DEPSN_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the major depressive affective disorder indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Medicare Coverage Start Date](https://www.resdac.org/cms-data/variables/Medicare-Coverage-Start-Date)

- Short SAS Name: `COVSTART`
- Long SAS Name: `COVSTART`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the date when the beneficiary first became eligible for Medicare coverage (Part A or Part B).

Historic date of 1st Medicare coverage (may be prior to 1999, which is the earliest claim files available through CCW)



<h3>Values</h3>



Historic date of 1st Medicare coverage (may be prior to 1999, which is the earliest claim files available through CCW) 



## [Medicare Entitlement/Buy-In Indicator - April](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-april)

- Short SAS Name: `BUYIN04`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - August](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-august)

- Short SAS Name: `BUYIN08`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - December](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-december)

- Short SAS Name: `BUYIN12`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - February](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-february)

- Short SAS Name: `BUYIN02`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - January](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-january)

- Short SAS Name: `BUYIN01`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - July](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-july)

- Short SAS Name: `BUYIN07`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - June](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-june)

- Short SAS Name: `BUYIN06`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - March](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-march)

- Short SAS Name: `BUYIN03`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - May](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-may)

- Short SAS Name: `BUYIN05`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - November](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-november)

- Short SAS Name: `BUYIN11`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value          |
|:-------|:--------------------|
| 0      | Not entitled        |
| 1      | Part A only         |
| 2      | Part B only         |
| 3      | Part A and Part B   |
| A      | Part A state buy-in |
| B      | Part B state buy-in |
| C      | Part C state buy-in |

## [Medicare Entitlement/Buy-In Indicator - October](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-october)

- Short SAS Name: `BUYIN10`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Entitlement/Buy-In Indicator - September](https://www.resdac.org/cms-data/variables/medicare-entitlementbuy-indicator-september)

- Short SAS Name: `BUYIN09`
- Long SAS Name: `MDCR_ENTLMT_BUYIN_IND_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was entitled to Part A, Part B, or both for a given month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). The variable also indicates whether the beneficiary’s state of residence paid his/her monthly premium for Part B coverage (and Part A if necessary). State Medicaid programs can pay those premiums for certain dual eligibles; this action is called “buying in” and so this variable is the “buy-in code.”



<h3>Values</h3>

| Code   | Code Value                     |
|:-------|:-------------------------------|
| 0      | Not entitled                   |
| 1      | Part A only                    |
| 2      | Part B only                    |
| 3      | Part A and Part B              |
| A      | Part A state buy-in            |
| B      | Part B state buy-in            |
| C      | Part A and Part B state buy-in |

## [Medicare Sample Group Indicator](https://www.resdac.org/cms-data/variables/Strict-5-Flag)

- Short SAS Name: `SAMPLE_GROUP`
- Long SAS Name: `SAMPLE_GROUP`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Medicare 1, 5, or 20% strict sample group indicator.

CCW creates the sample values using standard CMS processes to identify the random 1, 5, 15, and 20 percent samples of Medicare beneficiaries.
The sample groups are based on a random 20 percent sample that is split into three mutually exclusive groups of 1 percent, 4 percent, and 15 percent.
To use the 1 percent sample, specify that SAMPLE_GRP equals “01”.
To use the 5 percent sample, specify that SAMPLE_GRP equals “01” or “04”.
To use the 15 percent sample, specify that SAMPLE_GRP equals “15”.
To use the 20 percent sample, specify that SAMPLE_GRP equals “01”, “04”, or “15”.
Beneficiaries are assigned to sample groups each year based on the last two digits of their Medicare Claim Account Numbers (CANs). Since CANs can change over time (e.g., in the case of remarriage), new beneficiaries are becoming eligible for Medicare, and existing beneficiaries are dying, the sample is cross-sectional. There is no guarantee that the exact same beneficiaries are represented in the same sample group from one year to the next (i.e., this is the strict sampling).



<h3>Values</h3>

| Code                                                               |
|:-------------------------------------------------------------------|
| 01, 04, 15, null/missing (not included in 20% sample for the year) |

## [Medicare Status Code - April](https://www.resdac.org/taxonomy/term/5196)

- Short SAS Name: `MDCR_STUS_CD_04`
- Long SAS Name: `MDCR_STATUS_CODE_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in April.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - August](https://www.resdac.org/taxonomy/term/5216)

- Short SAS Name: `MDCR_STUS_CD_08`
- Long SAS Name: `MDCR_STATUS_CODE_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in August.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - December](https://www.resdac.org/taxonomy/term/5236)

- Short SAS Name: `MDCR_STUS_CD_12`
- Long SAS Name: `MDCR_STATUS_CODE_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in December.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - February](https://www.resdac.org/taxonomy/term/5186)

- Short SAS Name: `MDCR_STUS_CD_02`
- Long SAS Name: `MDCR_STATUS_CODE_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in February.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - January](https://www.resdac.org/cms-data/variables/Medicare-Status-Code)

- Short SAS Name: `MDCR_STUS_CD_01`
- Long SAS Name: `MDCR_STATUS_CODE_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in January.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - July](https://www.resdac.org/taxonomy/term/5211)

- Short SAS Name: `MDCR_STUS_CD_07`
- Long SAS Name: `MDCR_STATUS_CODE_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in July.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - June](https://www.resdac.org/taxonomy/term/5206)

- Short SAS Name: `MDCR_STUS_CD_06`
- Long SAS Name: `MDCR_STATUS_CODE_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in June.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - March](https://www.resdac.org/taxonomy/term/5191)

- Short SAS Name: `MDCR_STUS_CD_03`
- Long SAS Name: `MDCR_STATUS_CODE_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in March.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - May](https://www.resdac.org/taxonomy/term/5201)

- Short SAS Name: `MDCR_STUS_CD_05`
- Long SAS Name: `MDCR_STATUS_CODE_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in May.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - November](https://www.resdac.org/taxonomy/term/5231)

- Short SAS Name: `MDCR_STUS_CD_11`
- Long SAS Name: `MDCR_STATUS_CODE_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in November.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - October](https://www.resdac.org/taxonomy/term/5226)

- Short SAS Name: `MDCR_STUS_CD_10`
- Long SAS Name: `MDCR_STATUS_CODE_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in October.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare Status Code - September](https://www.resdac.org/taxonomy/term/5221)

- Short SAS Name: `MDCR_STUS_CD_09`
- Long SAS Name: `MDCR_STATUS_CODE_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates how a beneficiary currently qualifies for Medicare - in September.

Analysts can use this variable to quickly distinguish between the aged, disabled, and ESRD populations.
This field is coded from age, original reason for entitlement, current reason for entitlement and ESRD indicator contained in the enrollment data base at CMS.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value            |
|:-------|:----------------------|
| 10     | Aged without ESRD     |
| 11     | Aged with ESRD        |
| 20     | Disabled without ESRD |
| 21     | Disabled with ESRD    |
| 31     | ESRD only             |

## [Medicare-Medicaid dual eligibility code - April](https://www.resdac.org/taxonomy/term/5636)

- Short SAS Name: `DUAL_04`
- Long SAS Name: `DUAL_STUS_CD_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (April).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - August](https://www.resdac.org/taxonomy/term/5656)

- Short SAS Name: `DUAL_08`
- Long SAS Name: `DUAL_STUS_CD_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (August).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - December](https://www.resdac.org/taxonomy/term/5676)

- Short SAS Name: `DUAL_12`
- Long SAS Name: `DUAL_STUS_CD_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (December).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - February](https://www.resdac.org/taxonomy/term/5626)

- Short SAS Name: `DUAL_02`
- Long SAS Name: `DUAL_STUS_CD_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (February).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - July](https://www.resdac.org/taxonomy/term/5651)

- Short SAS Name: `DUAL_07`
- Long SAS Name: `DUAL_STUS_CD_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (July).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - June](https://www.resdac.org/taxonomy/term/5646)

- Short SAS Name: `DUAL_06`
- Long SAS Name: `DUAL_STUS_CD_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (June).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - March](https://www.resdac.org/taxonomy/term/5631)

- Short SAS Name: `DUAL_03`
- Long SAS Name: `DUAL_STUS_CD_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (March).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - May](https://www.resdac.org/taxonomy/term/5641)

- Short SAS Name: `DUAL_05`
- Long SAS Name: `DUAL_STUS_CD_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (May).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - November](https://www.resdac.org/taxonomy/term/5671)

- Short SAS Name: `DUAL_11`
- Long SAS Name: `DUAL_STUS_CD_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (November).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - October](https://www.resdac.org/taxonomy/term/5666)

- Short SAS Name: `DUAL_10`
- Long SAS Name: `DUAL_STUS_CD_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (October).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Medicare-Medicaid dual eligibility code - September](https://www.resdac.org/taxonomy/term/5661)

- Short SAS Name: `DUAL_09`
- Long SAS Name: `DUAL_STUS_CD_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether the beneficiary was eligible for both Medicare and Medicaid in a given month (September).

The original source for this variable is the State Medicare Modernization Act (MMA) files that states submit to CMS. Those files are considered the “gold standard” for identifying dual eligibles because the information in them is used to determine the level of Medicare Part D low-income subsidies. Dual eligibles are often divided into “full duals” and “partial duals” based on the level of Medicaid benefits they receive. CMS generally considers beneficiaries to be full duals if they have values of 02, 04, or 08, and to be partial duals if they have values of 01, 03, 05, or 06. Partial duals sometimes divided into the QMB-only population (01) and all other partial duals (03, 05, or 06). There are
CMS Chronic Conditions Data Warehouse (CCW) – Codebook
Master Beneficiary Summary File (MBSF) with Medicare Part A, B, C & D
May 2017 – Version 1.0 Page 56 of 225
different ways to classify dually eligible beneficiaries. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles". There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                            |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **     | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'XX' for 2006-2009) |
| nan    | Non-Medicaid                                                                                                                          |
| 00     | Not Medicare enrolled for the month                                                                                                   |
| 01     | Qualified Medicare Beneficiary (QMB)-only                                                                                             |
| 02     | QMB and full Medicaid coverage, including prescription drugs                                                                          |
| 03     | Specified Low-Income Medicare Beneficiary (SLMB)-only                                                                                 |
| 04     | SLMB and full Medicaid coverage, including prescription drugs                                                                         |
| 05     | Qualified Disabled Working Individual (QDWI)                                                                                          |
| 06     | Qualifying individuals (QI)                                                                                                           |
| 08     | Other dual eligible (not QMB, SLMB, QWDI, or QI) with full Medicaid coverage, including prescription drugs                            |
| 09     | Other dual eligible, but without Medicaid coverage                                                                                    |
| 99     | Unknown                                                                                                                               |

## [Migraine and other Chronic Headache End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/migraine-and-other-chronic-headache-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `MIGRAINE_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for migraine and other chronic headache as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For migraine and other chronic headache, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Migraine and other Chronic Headache First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/migraine-and-other-chronic-headache-first-ever-occurrence-date-medicare-only-0)

- Short SAS Name: `MIGRAINE_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the migraine and other chronic headache indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Mobility Impairments End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/mobility-impairments-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `MOBIMP_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for mobility impairments as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For mobility impairments, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Mobility Impairments First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/mobility-impairments-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `MOBIMP_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the mobility impairments indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Months of Dual Eligibility](https://www.resdac.org/cms-data/variables/Dual-Eligible-Months-Number)

- Short SAS Name: `DUAL_MO`
- Long SAS Name: `DUAL_ELGBL_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the number of months during the year that the beneficiary was dually eligible (i.e., he/she was also eligible for Medicaid benefits).

CCW derived this variable by counting the number of months where the beneficiary had dual eligibility (DUAL_STUS_CD_XX not equal to `00` or '**').
There are different ways to classify dually eligible beneficiaries - in terms of whether he/she is enrolled in full or partial benefits. Additional information regarding various ways to identify dually enrolled populations, refer to a CCW Technical Guidance document entitled: "Options in Determining Dual Eligibles"



<h3>Values</h3>

| Code                                                  |
|:------------------------------------------------------|
| The value in this field is between '00' through '12'. |

## [Months of Part D Coverage](https://www.resdac.org/cms-data/variables/Plan-Coverage-Months-Number)

- Short SAS Name: `PTD_MO`
- Long SAS Name: `PTD_PLAN_CVRG_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the number of months during the year that the beneficiary had Medicare Part D coverage. CCW derives this variable by counting the number of months where the beneficiary had Part D coverage.

A Part D covered month is one where the first value of the monthly PTD_CNTRCT_ID_XX variable equaled H, R, S, or E or the value was X followed by 4 alphanumeric characters.



<h3>Values</h3>




| Code                                                  |
|:------------------------------------------------------|
| The value in this field is between '00' through '12'. |

## [Months of Retiree Drug Subsidy Coverage](https://www.resdac.org/cms-data/variables/Retiree-Drug-Subsidy-Coverage-Months-Number)

- Short SAS Name: `RDS_MO`
- Long SAS Name: `RDS_CVRG_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the number of months during the year that the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS). CCW derives this variable by counting the number of months where the beneficiary had retiree drug subsidy.

A month of RDS is when the RDS_IND_XX for the month = Y.
Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.



<h3>Values</h3>

| Code                                                  |
|:------------------------------------------------------|
| The value in this field is between '00' through '12'. |

## [Multiple Sclerosis and Transverse Myelitis End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/multiple-sclerosis-and-transverse-myelitis-end-year-indicator-medicare-only-0)

- Short SAS Name: `MULSCL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for multiple sclerosis and transverse myelitis as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For multiple sclerosis and transverse myelitis, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Multiple Sclerosis and Transverse Myelitis First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/multiple-sclerosis-and-transverse-myelitis-first-ever-occurrence-date-medicare-0)

- Short SAS Name: `MULSCL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the multiple sclerosis and transverse myelitis indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Muscular Dystrophy End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/muscular-dystrophy-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `MUSDYS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for muscular dystrophy as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For muscular dystrophy, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Muscular Dystrophy First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/muscular-dystrophy-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `MUSDYS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the muscular dystrophy indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [NDI Date of Death](https://www.resdac.org/taxonomy/term/586)

- Short SAS Name: `NDI_DOD`
- Long SAS Name: `NDI_DOD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field indicates that an enrollee's date of death has been verified as the exact date of becoming deceased, according to a death certificate.



<h3>Values</h3>



Formatted as YYYYMMDD 



## [NDI Death Certificate Number](https://www.resdac.org/cms-data/variables/NDI-Death-Certificate-Number)

- Short SAS Name: `DEATH_CERT_NUM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field represents the death certificate number of the beneficiary.



<h3>Values</h3>



Numbers are not unique across years.

Available for 1999-2008/ Rsearchers wishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA. 



## [NDI Entity Axis Cause of Death - Condition](https://www.resdac.org/cms-data/variables/NDI-Entity-Axis-Cause-Death-Condition)

- Short SAS Name: `ENTITY_COND_1 (through ENTITY_COND_8)`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field identifies the first eight underlying causes of death codes as listed by the certifier of death (formatted but not audited).



<h3>Values</h3>

Each condition takes 7 positions in the record
Position1: Part/line number on certificate

| Code   | Code Value         |
|:-------|:-------------------|
| 1      | Part I, line 1 (a) |
| 2      | Part I, line 2 (b) |
| 3      | Part I, line 3 (c) |
| 4      | Part I, line 4 (d) |
| 5      | Part I, line 5 (e) |
| 6      | Part II            |

Position 2: Sequence of condition within
part/line Code range:1-7   

Position 3-6: Condition code (See ICD-9 or ICD-10 codes)
Whenever there is a 4-position code, there is always an implied decimal after the 3rd position.   

Position 7: Nature of Injury flag (only for ICD-9 codes)

| Code   | Code Value                                                 |
|:-------|:-----------------------------------------------------------|
| 1      | the code in positions 3-6 is a Nature of Injury ICD-9 code |
| 0      | all other codes                                            |

## [NDI Record Axis Cause of Death - Condition](https://www.resdac.org/cms-data/variables/NDI-Record-Axis-Cause-Death-Condition)

- Short SAS Name: `RECORD_COND_1 (through RECORD_COND_8)`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field identifies the first eight underlying causes of death codes as edited and audited by National Center for Health Statistics (NCHS).



<h3>Values</h3>

Each condition takes 5 positions in the record.

Positions 1-4: Condition Code (See ICD-9 or ICD-10 codes)  
Note: Whenever there is a 4-position code, there is always an implied decimal after the 3rd position.

Position 5: Nature of Injury Flag (only for ICD-9 codes)

| Code   | Code Value                                                |
|:-------|:----------------------------------------------------------|
| 1      | the code in position 1-4 is a Nature of Injury ICD-9 code |
| 0      | all other codes                                           |

## [NDI State of Death](https://www.resdac.org/cms-data/variables/NDI-State-Death)

- Short SAS Name: `NDI_STATE_DEATH_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field identifies the state where the beneficiary death occurred.



<h3>Values</h3>

Centers for Disease Control and Prevention (CDC) National Death Index (NDI)

Recoded to SSA codes by CCW.

Available for 1999-2008. Researchers wishing to obtain this NDI segment of the MBSF must obtain an additional approval beyond the CMS DUA.

| Code   | Code Value           |
|:-------|:---------------------|
| 1      | Alabama              |
| 2      | Alaska               |
| 3      | Arizona              |
| 4      | Arkansas             |
| 5      | California           |
| 6      | Colorado             |
| 7      | Connecticut          |
| 8      | Delaware             |
| 9      | District of Colombia |
| 10     | Florida              |
| 11     | Georgia              |
| 12     | Hawaii               |
| 13     | Idaho                |
| 14     | Illinois             |
| 15     | Indiana              |
| 16     | Iowa                 |
| 17     | Kansas               |
| 18     | Kentucky             |
| 19     | Louisiana            |
| 20     | Maine                |
| 21     | Maryland             |
| 22     | Massachusetts        |
| 23     | Michigan             |
| 24     | Minnesota            |
| 25     | Mississippi          |
| 26     | Missouri             |
| 27     | Montana              |
| 28     | Nebraska             |
| 29     | Nevada               |
| 30     | New Hampshire        |
| 31     | New Jersey           |
| 32     | New Mexico           |
| 33     | New York             |
| 34     | North Carolina       |
| 35     | North Dakota         |
| 36     | Ohio                 |
| 37     | Oklahoma             |
| 38     | Oregon               |
| 39     | Pennsylvania         |
| 40     | Puerto Rico          |
| 41     | Rhode Island         |
| 42     | South Carolina       |
| 43     | South Dakota         |
| 44     | Tennessee            |
| 45     | Texas                |
| 46     | Utah                 |
| 47     | Vermont              |
| 48     | Virgin Islands       |
| 49     | Virginia             |
| 50     | Washington           |
| 51     | West Virgina         |
| 52     | Wisconsin            |
| 53     | Wyoming              |

## [Obesity End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/obesity-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `OBESITY_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for obesity as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For obesity, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Obesity First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/obesity-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `OBESITY_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the obesity indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Original Reason for Entitlement Code](https://www.resdac.org/cms-data/variables/Original-Reason-Entitlement-Code)

- Short SAS Name: `OREC`
- Long SAS Name: `ENTLMT_RSN_ORIG`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Original reason for Medicare entitlement.



<h3>Values</h3>

CMS obtains this information from the Social Security Administration (SSA) and Railroad Retirement Board (RRB) record systems.

| Code   | Code Value                             |
|:-------|:---------------------------------------|
| 0      | OLD AGE AND SURVIVORS INSURANCE (OASI) |
| 1      | DISABILITY INSURANCE BENEFITS (DIB)    |
| 2      | ESRD                                   |
| 3      | BOTH DIB AND ESRD                      |

## [Osteoporosis End-of-Year Flag](https://www.resdac.org/cms-data/variables/Osteoporosis-End-Year-Flag)

- Short SAS Name: `OSTEOPRS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Osteoporosis Mid-Year Flag](https://www.resdac.org/cms-data/variables/Osteoporosis-Mid-Year-Flag)

- Short SAS Name: `OSTEOPRM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Other Developmental Delays End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/other-developmental-delays-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `OTHDEL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for other developmental delays as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For other developmental delays, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Other Developmental Delays First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/other-developmental-delays-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `OTHDEL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the other developmental delays indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Other Inpatient Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Inpatient-Beneficiary-Payments)

- Short SAS Name: `OIP_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of Medicare coinsurance and deductible payments in the non-acute inpatient hospital setting for the year.  The total “other” inpatient (OIP) beneficiary payments are calculated as the sum of NCH_BENE_IP_DDCTBL_AMT and NCH_BENE_PTA_COINSRNC_LBLTY_AM for all relevant claims where the CLM_PMT_AMT >= 0.  

These OIP claims are a subset of the claims in the IP data file consisting of data from IP settings such as long-term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other types of IP facilities such as children’s hospitals or cancer centers.



<h3>Values</h3>



There are 2 cost/use categories from the IP data files: Acute and the OIP.

Costs to that beneficiaries are liable for are described in detail on the Medicare.gov website. There is a CMS publication called "Your Medicare Benefits", which explains the deductibles and coinsurance amounts.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Other Inpatient Covered Days](https://www.resdac.org/cms-data/variables/Other-Inpatient-Covered-Days)

- Short SAS Name: `OIP_COV_DAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of covered days in the non-acute inpatient setting for a given year.  The CCW variable CLM_UTLZTN_DAY_CNT is used to obtain this variable.   These “other” inpatient (OIP) claims are a subset of the claims in the IP data file consisting of data from IP settings such as long-term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other types of IP facilities such as children’s hospitals or cancer centers.



<h3>Values</h3>



We consider fully-covered days, days where the beneficiary was liable for coinsurance, and lifetime reserve days to all be Medicare-covered days.  Non-covered days, leave of absence days, and the day of discharge or death are not included.

There are 2 cost/use categories from the IP data files: Acute and the OIP.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html) 



## [Other Inpatient Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Inpatient-Medicare-Payments)

- Short SAS Name: `OIP_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of the Medicare claim payment amounts (CLM_PMT_AMT from each claim) in the other inpatient (OIP) settings for a given year.  To obtain the total OIP Medicare payments, take this variable and add in the annual per diem payment amount (OIP_MDCR_PMT +  OIP_PERDIEM_AMT).
.

These OIP claims are a subset of the claims in the IP data file consisting of data from IP settings such as long-term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other types of IP facilities such as children’s hospitals or cancer centers.



<h3>Values</h3>



There are 2 cost/use categories from the IP data files: Acute and the OIP.

OIP_PERDIEM_PMT must be added to this field to obtain the total Medicare payments. The annual per diem variable was new in 2010; it will always be null/missing in earlier files.

Costs to that beneficiaries are liable for are described in detail on the Medicare.gov website. There is a CMS publication called "Your Medicare Benefits", which explains the deductibles and coinsurance amounts.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Other Inpatient Stays](https://www.resdac.org/cms-data/variables/Other-Inpatient-Stays)

- Short SAS Name: `OIP_STAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of hospital stays (unique admissions, which may span more than one facility) in the non-acute inpatient setting for a given year.  A non-acute inpatient stay is defined as a set of one or more consecutive non-acute inpatient claims where the beneficiary is only discharged on the most recent claim in the set.  The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year. These “other” inpatient (OIP) claims are a subset of the claims in the IP data file consisting of data from IP settings such as long-term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other types of IP facilities such as children’s hospitals or cancer centers.



<h3>Values</h3>



There are 2 cost/use categories from the IP data files: Acute and the OIP
 



## [Other Part B Carrier Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Beneficiary-Payments)

- Short SAS Name: `OTHC_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments from Part B Carrier and DME claims which appear in settings other than the 10 specific categories which are part of this file for a given year. The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.  

Claims for other carrier/DME claims are a subset of the claims in the Part B Carrier and DME data files.  Types of services which may have been summarized in this other carrier category (OTHC) include ambulance, chiropractor, chemotherapy, vision, hearing and speech services, etc.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Other Part B Carrier Events](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Events)

- Short SAS Name: `OTHC_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the count of events in the part B other setting for a given year, which includes Part B Carrier and DME claims which appear in settings other than the 10 specific categories which are part of this file for a given year.  Claims for other carrier/DME claims are a subset of the claims in the Part B Carrier and DME data files.  Types of services which may have been summarized in this other carrier category (OTHC) include ambulance, chiropractor, chemotherapy, vision, hearing and speech services, etc.

An event is defined as each line item that contains the relevant service."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims. 



## [Other Part B Carrier Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Part-B-Carrier-Medicare-Payments)

- Short SAS Name: `OTHC_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments from Part B Carrier and DME claims which appear in settings other than the 10 specific categories which are part of this file for a given year.  Claims for other carrier/DME claims are a subset of the claims in the Part B Carrier and DME data files.  Types of services which may have been summarized in this other carrier category (OTHC) include ambulance, chiropractor, chemotherapy, vision, hearing and speech services, etc.

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Other Procedures Beneficiary Payments](https://www.resdac.org/cms-data/variables/Other-Procedures-Beneficiary-Payments)

- Short SAS Name: `OPROC_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for services considered part B other procedures (i.e., not anesthesia or dialysis) for a given year. The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.  

Claims for other procedures are a subset of the claims in the Part B Carrier data file. These other procedure claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits are (`P1`,`P2`,`P3`,`P4`,`P5`,`P6`,`P7`, or `P8`).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Other Procedures Events](https://www.resdac.org/cms-data/variables/Other-Procedures-Events)

- Short SAS Name: `OPROC_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the count of events for part B other procedures for a given year. Claims for other procedures are a subset of the claims in the Part B Carrier data file. These other procedure claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits are (`P1`,`P2`,`P3`,`P4`,`P5`,`P6`,`P7`, or `P8`). 

An event is defined as each line item that contains the relevant service."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Other Procedures Medicare Payments](https://www.resdac.org/cms-data/variables/Other-Procedures-Medicare-Payments)

- Short SAS Name: `OPROC_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for services considered part B other procedures (i.e., not anesthesia or dialysis) for a given year.  Claims for other procedures are a subset of the claims, and a subset of procedures in the Part B Carrier data file. These other procedure claims are defined as those with a line BETOS code (BETOS_CD) where the first 2 digits are (`P1`,`P2`,`P3`,`P4`,`P5`,`P6`,`P7`, or `P8`). The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part A Months Count](https://www.resdac.org/cms-data/variables/part-months-count)

- Short SAS Name: `A_MO_CNT`
- Long SAS Name: `BENE_HI_CVRAGE_TOT_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Months of Part A coverage

This variable is the number of months during the year that the beneficiary had Medicare Part A coverage. (This is sometimes referred to as health insurance coverage - or Medicare HI coverage).

??? derivation
	CCW derives this variable by counting the number of months where the beneficiary had Part A coverage (i.e., the BUYINXX variable equaled 1, A, 3, or C).

<h3>Values</h3>

| Code   |
|:-------|
| 0-12   |

## [Part A Termination Code](https://www.resdac.org/cms-data/variables/Part-Termination-Code)

- Short SAS Name: `A_TRM_CD`
- Long SAS Name: `BENE_PTA_TRMNTN_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code Specifies the reason Part A entitlement was terminated.



<h3>Values</h3>

| Code   | Code Value             |
|:-------|:-----------------------|
| 0      | Not terminated         |
| 1      | Dead                   |
| 2      | Non-payment of premium |
| 3      | Voluntary withdrawl    |
| 9      | Other termination      |

## [Part B Drug Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-B-Drug-Beneficiary-Payments)

- Short SAS Name: `PTB_DRUG_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the sum of coinsurance and deductible payments for part B drugs for a given year. Part B drug claims are a subset of the claims in the Part B Carrier and DME data files. The Part B drug claims are identified by BETOS codes (CCW variable BETOS_CD with values of `D1G`,`O1D`,`O1E`,`O1G`,`I1E`, or `I1F`). 

The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.  "



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Drug Events](https://www.resdac.org/cms-data/variables/Part-B-Drug-Events)

- Short SAS Name: `PTB_DRUG_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events in the part B drug setting for a given year.  Part B drug claims are a subset of the claims in the Part B Carrier and DME data files. The Part B drug claims are identified by BETOS codes (CCW variable BETOS_CD with values of `D1G`,`O1D`,`O1E`,`O1G`,`I1E`, or `I1F`).  An event is defined as each line item that contains the relevant service.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Drug Medicare Payments](https://www.resdac.org/cms-data/variables/Part-B-Drug-Medicare-Payments)

- Short SAS Name: `PTB_DRUG_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for Part B drugs for a given year. Part B drug claims are a subset of the claims in the Part B Carrier and DME data files.  The Part B drug claims are identified by BETOS codes (CCW variable BETOS_CD with values of `D1G`,`O1D`,`O1E`,`O1G`,`I1E`, or `I1F`).  

Total Part B drug payments are calculated as sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S')."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Months Count](https://www.resdac.org/cms-data/variables/part-b-months-count)

- Short SAS Name: `B_MO_CNT`
- Long SAS Name: `BENE_SMI_CVRAGE_TOT_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Months of Part B coverage

This variable is the number of months during the year that the beneficiary had Medicare Part B coverage. (This is sometimes referred to as supplemental medical insurance coverage - or SMI coverage.) CCW derives this variable by counting the number of months where the beneficiary had Part B coverage (i.e., the BUYINXX variable equaled 2, B, 3, or C).



<h3>Values</h3>

| Code   |
|:-------|
| 0-12   |

## [Part B Physician Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-B-Physician-Beneficiary-Payments)

- Short SAS Name: `PHYS_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for the part B physician office services (PHYS) for a given year. The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines. 

Physician office claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician evaluation and management claims (note that E&M are tabulated separately in this data file).  The PHYS claims are defined as those with a line BETOS code (BETOS_CD) where the first three digits =M1A or M1B (the remainder of physician services which occur in different settings appear in  EM_MDCR_PMT).



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Physician Events](https://www.resdac.org/cms-data/variables/Part-B-Physician-Events)

- Short SAS Name: `PHYS_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the count of events in the part B physician office services (PHYS) for a given year. Physician office claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician evaluation and management claims (note that E&M are tabulated separately in this data file).   The PHYS claims are defined as those with a line BETOS code (BETOS_CD) where the first three digits =M1A or M1B (the remainder of physician services which occur in different settings appear in  EM_MDCR_PMT).

An event is defined as each line item that contains the relevant service."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Physician Medicare Payments](https://www.resdac.org/cms-data/variables/Part-B-Physician-Medicare-Payments)

- Short SAS Name: `PHYS_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments for the part B physician office services (PHYS) for a given year. Physician office claims are a subset of the claims in the Part B Carrier and DME data files, and a subset of physician evaluation and management claims (note that E&M are tabulated separately in this data file).

The physician claims are defined as those with a line BETOS code (BETOS_CD) where the first 3 digits = M1A or M1B (note that all other BETOS_CD that begin with "M" are categorized as other evluation & managment services in this file – see EM_MDCR_PMT). The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Part B Termination Code](https://www.resdac.org/cms-data/variables/Part-B-Termination-Code)

- Short SAS Name: `B_TRM_CD`
- Long SAS Name: `BENE_PTB_TRMNTN_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies the reason Part B entitlement was terminated.



<h3>Values</h3>

| Code   | Code Value             |
|:-------|:-----------------------|
| 0      | Not terminated         |
| 1      | Dead                   |
| 2      | Non-payment of premium |
| 3      | Voluntary withdrawl    |
| 9      | Other termination      |

## [Part C Contract Number - April](https://www.resdac.org/cms-data/variables/part-c-contract-number-april)

- Short SAS Name: `PTC_CNTRCT_ID_04`
- Long SAS Name: `PTC_CNTRCT_ID_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (April).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - August](https://www.resdac.org/cms-data/variables/part-c-contract-number-august)

- Short SAS Name: `PTC_CNTRCT_ID_08`
- Long SAS Name: `PTC_CNTRCT_ID_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (August).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - December](https://www.resdac.org/cms-data/variables/part-c-contract-number-december)

- Short SAS Name: `PTC_CNTRCT_ID_12`
- Long SAS Name: `PTC_CNTRCT_ID_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (December).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - February](https://www.resdac.org/cms-data/variables/part-c-contract-number-february)

- Short SAS Name: `PTC_CNTRCT_ID_02`
- Long SAS Name: `PTC_CNTRCT_ID_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (February).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - January](https://www.resdac.org/cms-data/variables/part-c-contract-number-january)

- Short SAS Name: `PTC_CNTRCT_ID_01`
- Long SAS Name: `PTC_CNTRCT_ID_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (January).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.

You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - July](https://www.resdac.org/cms-data/variables/part-c-contract-number-july)

- Short SAS Name: `PTC_CNTRCT_ID_07`
- Long SAS Name: `PTC_CNTRCT_ID_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (July).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - June](https://www.resdac.org/cms-data/variables/part-c-contract-number-june)

- Short SAS Name: `PTC_CNTRCT_ID_06`
- Long SAS Name: `PTC_CNTRCT_ID_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (June).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - March](https://www.resdac.org/cms-data/variables/part-c-contract-number-march)

- Short SAS Name: `PTC_CNTRCT_ID_03`
- Long SAS Name: `PTC_CNTRCT_ID_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (March).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - May](https://www.resdac.org/cms-data/variables/part-c-contract-number-may)

- Short SAS Name: `PTC_CNTRCT_ID_05`
- Long SAS Name: `PTC_CNTRCT_ID_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (May).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - November](https://www.resdac.org/cms-data/variables/part-c-contract-number-november)

- Short SAS Name: `PTC_CNTRCT_ID_11`
- Long SAS Name: `PTC_CNTRCT_ID_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (November).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - October](https://www.resdac.org/cms-data/variables/part-c-contract-number-october)

- Short SAS Name: `PTC_CNTRCT_ID_10`
- Long SAS Name: `PTC_CNTRCT_ID_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (October).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C Contract Number - September](https://www.resdac.org/cms-data/variables/part-c-contract-number-september)

- Short SAS Name: `PTC_CNTRCT_ID_09`
- Long SAS Name: `PTC_CNTRCT_ID_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Medicare Part C contract number for the beneficiary’s Medicare Advantage (MA) plan for a given month (September).CMS assigns an identifier to each contract that a managed care plan has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



## [Part C PBP Number - April](https://www.resdac.org/cms-data/variables/part-c-pbp-number-april)

- Short SAS Name: `PTC_PBP_ID_04`
- Long SAS Name: `PTC_PBP_ID_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (April).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - August](https://www.resdac.org/cms-data/variables/part-c-pbp-number-august)

- Short SAS Name: `PTC_PBP_ID_08`
- Long SAS Name: `PTC_PBP_ID_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (August).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - December](https://www.resdac.org/cms-data/variables/part-c-pbp-number-december)

- Short SAS Name: `PTC_PBP_ID_12`
- Long SAS Name: `PTC_PBP_ID_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (December).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - February](https://www.resdac.org/cms-data/variables/part-c-pbp-number-february)

- Short SAS Name: `PTC_PBP_ID_02`
- Long SAS Name: `PTC_PBP_ID_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (February).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - January](https://www.resdac.org/cms-data/variables/part-c-pbp-number-january)

- Short SAS Name: `PTC_PBP_ID_01`
- Long SAS Name: `PTC_PBP_ID_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (January).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - July](https://www.resdac.org/cms-data/variables/part-c-pbp-number-july)

- Short SAS Name: `PTC_PBP_ID_07`
- Long SAS Name: `PTC_PBP_ID_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (July).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - June](https://www.resdac.org/cms-data/variables/part-c-pbp-number-june)

- Short SAS Name: `PTC_PBP_ID_06`
- Long SAS Name: `PTC_PBP_ID_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (June).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - March](https://www.resdac.org/cms-data/variables/part-c-pbp-number-march)

- Short SAS Name: `PTC_PBP_ID_03`
- Long SAS Name: `PTC_PBP_ID_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (March).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - May](https://www.resdac.org/cms-data/variables/part-c-pbp-number-may)

- Short SAS Name: `PTC_PBP_ID_05`
- Long SAS Name: `PTC_PBP_ID_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (May).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - November](https://www.resdac.org/cms-data/variables/part-c-pbp-number-november)

- Short SAS Name: `PTC_PBP_ID_11`
- Long SAS Name: `PTC_PBP_ID_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (November).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - October](https://www.resdac.org/cms-data/variables/part-c-pbp-number-october)

- Short SAS Name: `PTC_PBP_ID_10`
- Long SAS Name: `PTC_PBP_ID_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (October).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C PBP Number - September](https://www.resdac.org/cms-data/variables/part-c-pbp-number-september)

- Short SAS Name: `PTC_PBP_ID_09`
- Long SAS Name: `PTC_PBP_ID_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Medicare Part C plan benefit package (PBP) for the beneficiary’s Medicare Advantage (MA) plan for a given month (September).CMS assigns an identifier to each PBP within a contract that a Part C plan sponsor has with CMS.

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month.
You need to know both the Part C contract number (PTC_CNTRCT_ID_XX) and plan benefit package (PBP) in order to identify the specific plan in which a beneficiary was enrolled.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part C Plan Type Code - April](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-april)

- Short SAS Name: `PTC_PLAN_TYPE_CD_04`
- Long SAS Name: `PTC_PLAN_TYPE_CD_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (April).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - August](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-august)

- Short SAS Name: `PTC_PLAN_TYPE_CD_08`
- Long SAS Name: `PTC_PLAN_TYPE_CD_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (August).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - December](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-december)

- Short SAS Name: `PTC_PLAN_TYPE_CD_12`
- Long SAS Name: `PTC_PLAN_TYPE_CD_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (December).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - February](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-february)

- Short SAS Name: `PTC_PLAN_TYPE_CD_02`
- Long SAS Name: `PTC_PLAN_TYPE_CD_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (February).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - January](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-january)

- Short SAS Name: `PTC_PLAN_TYPE_CD_01`
- Long SAS Name: `PTC_PLAN_TYPE_CD_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (January).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - July](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-july)

- Short SAS Name: `PTC_PLAN_TYPE_CD_07`
- Long SAS Name: `PTC_PLAN_TYPE_CD_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (July).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - June](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-june)

- Short SAS Name: `PTC_PLAN_TYPE_CD_06`
- Long SAS Name: `PTC_PLAN_TYPE_CD_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (June).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - March](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-march)

- Short SAS Name: `PTC_PLAN_TYPE_CD_03`
- Long SAS Name: `PTC_PLAN_TYPE_CD_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (March).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - May](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-may)

- Short SAS Name: `PTC_PLAN_TYPE_CD_05`
- Long SAS Name: `PTC_PLAN_TYPE_CD_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (May).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - November](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-november)

- Short SAS Name: `PTC_PLAN_TYPE_CD_11`
- Long SAS Name: `PTC_PLAN_TYPE_CD_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (November).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - October](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-october)

- Short SAS Name: `PTC_PLAN_TYPE_CD_10`
- Long SAS Name: `PTC_PLAN_TYPE_CD_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (October).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part C Plan Type Code - September](https://www.resdac.org/cms-data/variables/part-c-plan-type-code-september)

- Short SAS Name: `PTC_PLAN_TYPE_CD_09`
- Long SAS Name: `PTC_PLAN_TYPE_CD_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the type of Medicare Part C plan for the beneficiary for a given month (September).

If the beneficiary was not enrolled in a managed care plan for a given month, this variable will be null/missing for that month. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>



 Part C Plan Type Code.txt 



## [Part D Beneficiary Payments](https://www.resdac.org/cms-data/variables/Part-D-Beneficiary-Payments)

- Short SAS Name: `PTD_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the dollar amount that the beneficiary paid for all PDEs for a given year, without being reimbursed by a third party.  The amount includes all copayments, coinsurance, deductible, or other patient payment amounts, and comes directly from the source Prescription Drug Events (PDEs).  

The total beneficiary payments are calculated as the sum of three CCW variables: patient pay amount (PTNT_PAY_AMT), other troop amount (OTHER_TROOP_AMT), and patient liability reduction due to other payer amount (PLRO_AMT) for Part D drugs for the relevant PDEs.



<h3>Values</h3>



This amount contributes to a beneficiary's true out-of-pocket (TrOOP) costs, but only if it is for a Part D-covered drug (i.e., spending on non-covered drugs does not count toward the TrOOP amount).

Note that another PDE variable called the low-income cost sharing (LIS) amount (variable name LICS_AMT), indicates the amount paid by Part D low-income subsidy for the PDE. Although this is sometimes considered a beneficiary payment (since it is made on behalf of a beneficiary), we have included the LIS payments in the Part D Medicare Payment amount (see variable called PTD_MDCR_PMT).

The value will be null if the beneficiary was not enrolled in Part D or did not use any Part D drugs during the year.
 



## [Part D Contract Number - April](https://www.resdac.org/taxonomy/term/5416)

- Short SAS Name: `PTDCNTRCT04`
- Long SAS Name: `PTD_CNTRCT_ID_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (April). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - August](https://www.resdac.org/taxonomy/term/5436)

- Short SAS Name: `PTDCNTRCT08`
- Long SAS Name: `PTD_CNTRCT_ID_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (August). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - December](https://www.resdac.org/taxonomy/term/5456)

- Short SAS Name: `PTDCNTRCT12`
- Long SAS Name: `PTD_CNTRCT_ID_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (December). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - February](https://www.resdac.org/taxonomy/term/5406)

- Short SAS Name: `PTDCNTRCT02`
- Long SAS Name: `PTD_CNTRCT_ID_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (February). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - January](https://www.resdac.org/cms-data/variables/Encrypted-Contract-ID-occurs-12-times)

- Short SAS Name: `PTDCNTRCT01`
- Long SAS Name: `PTD_CNTRCT_ID_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (January). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - July](https://www.resdac.org/taxonomy/term/5431)

- Short SAS Name: `PTDCNTRCT07`
- Long SAS Name: `PTD_CNTRCT_ID_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (July). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - June](https://www.resdac.org/taxonomy/term/5426)

- Short SAS Name: `PTDCNTRCT06`
- Long SAS Name: `PTD_CNTRCT_ID_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (June). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - May](https://www.resdac.org/taxonomy/term/5421)

- Short SAS Name: `PTDCNTRCT05`
- Long SAS Name: `PTD_CNTRCT_ID_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (May). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - November](https://www.resdac.org/taxonomy/term/5451)

- Short SAS Name: `PTDCNTRCT11`
- Long SAS Name: `PTD_CNTRCT_ID_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (November). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - October](https://www.resdac.org/taxonomy/term/5446)

- Short SAS Name: `PTDCNTRCT10`
- Long SAS Name: `PTD_CNTRCT_ID_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (October). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Contract Number - September](https://www.resdac.org/taxonomy/term/5441)

- Short SAS Name: `PTDCNTRCT09`
- Long SAS Name: `PTD_CNTRCT_ID_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the Part D contract number for the beneficiary’s Part D plan for a given month (September). CMS assigns an identifier to each contract that a Part D plan has with CMS.

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).
If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

The first character of the contract ID is a letter that indicates the type of plan (for July 2009 and later, when X is followed by additional numbers/characters, it indicates Part D enrollment; for 2006-2009 the 'X' appeared without any other digits and indicated the beneficiary was not enrolled in Part D).

If the beneficiary did not have a Part D plan for a given month, this variable will have a value of X, N, 0, or *, or be null/missing for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled contract number.

For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.

There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).

You need to know both the Part D contract number and plan benefit package (PTD_PBP_ID_XX) in order to identify the specific plan in which a beneficiary was enrolled.

| Code   | Code Value                                                                                                                                                                                                                 |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E      | Employer direct plan (starting January 2007)                                                                                                                                                                               |
| H      | Managed care organizations other than a regional PPO (i.e., local MA-PDs, 1876 cost plans, Program of All-Inclusive Care for the Elderly (PACE) plans, private fee-for-service plans, or demonstration organization plans) |
| R      | Regional preferred provider organization (PPO)                                                                                                                                                                             |
| S      | Stand-alone prescription drug plan (PDP)                                                                                                                                                                                   |
| X      | Limited Income Newly Eligible Transition plan (LINET, starting July 2009)                                                                                                                                                  |
| N      | Not Part D Enrolled                                                                                                                                                                                                        |
| 0      | Not Medicare enrolled for the month                                                                                                                                                                                        |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009)                                                                                       |

## [Part D Events](https://www.resdac.org/cms-data/variables/Part-D-Events)

- Short SAS Name: `PTD_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of events for Part D drugs for a given year (i.e., a unique count of the PDE_IDs). An event is a dispensed (filled) drug prescription that appears in the Prescription Drug Event (PDE) file.



<h3>Values</h3>



The value will be null if the beneficiary was not enrolled in Part D or did not use any Part D drugs during the year.

PDEs consist of highly variable days supply of the medication.  We also create a derived variable that counts a standard 30 day supply of a filled Part D prescription (see PTD_FILL_CNT). 



## [Part D Fill Count](https://www.resdac.org/cms-data/variables/Part-D-Fill-Count)

- Short SAS Name: `PTD_FILL_CNT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Part D prescribing events consist of highly variable days supply of the medication.  This derived variable creates a standard 30 days supply of a filled Part D prescription, and counts this as a “fill”.   The Part D fill count does not indicate the number of different drugs the person is using, only the total months covered by a medication (e.g., if a patient is receiving a full year supply of a medication, whether this occurs in one transaction or 12 monthly transactions, the fill count = 12; if the patient is taking three such medications, the fill count=36).  



<h3>Values</h3>



The value will be null if the beneficiary was not enrolled in Part D or did not use any Part D drugs during the year.

We also calaculate the acutal number of prescription drug fill events for Part D drugs for a given year (i.e., a unique count of the PDE_IDs); see variable PTD_EVENTS.
 



## [Part D Medicare Payments](https://www.resdac.org/cms-data/variables/Part-D-Medicare-Payments)

- Short SAS Name: `PTD_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the dollar amount that the Part D plan covered for all covered drugs for a given year. The variable is calculated as the sum of the plan payments for covered PDEs (CVRD_D_PLAN_PD_AMT) and the low income cost sharing subsidy amount (LICS_AMT) during the year.



<h3>Values</h3>



This variable does not include all costs to Medicare for the Part D benefit; it does not include non-covered drugs (PDE variable called NCVRD_PLAN_PD_AMT) also does not consider include any applicable rebate amounts or other discounts).

Plans may choose to provide enhanced benefits that pay for some non-covered drugs.

The value will be null if the beneficiary was not enrolled in Part D or did not use any Part D drugs during the year. 



## [Part D PBP Number - April](https://www.resdac.org/cms-data/variables/part-d-pbp-number-april)

- Short SAS Name: `PTDPBPID04`
- Long SAS Name: `PTD_PBP_ID_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (April). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - August](https://www.resdac.org/cms-data/variables/part-d-pbp-number-august)

- Short SAS Name: `PTDPBPID08`
- Long SAS Name: `PTD_PBP_ID_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (August). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - December](https://www.resdac.org/cms-data/variables/part-d-pbp-number-december)

- Short SAS Name: `PTDPBPID12`
- Long SAS Name: `PTD_PBP_ID_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (December). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - February](https://www.resdac.org/cms-data/variables/part-d-pbp-number-february)

- Short SAS Name: `PTDPBPID02`
- Long SAS Name: `PTD_PBP_ID_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (February). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - January](https://www.resdac.org/cms-data/variables/part-d-pbp-number-january)

- Short SAS Name: `PTDPBPID01`
- Long SAS Name: `PTD_PBP_ID_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (January). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - July](https://www.resdac.org/cms-data/variables/part-d-pbp-number-july)

- Short SAS Name: `PTDPBPID07`
- Long SAS Name: `PTD_PBP_ID_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (July). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - June](https://www.resdac.org/cms-data/variables/part-d-pbp-number-june)

- Short SAS Name: `PTDPBPID06`
- Long SAS Name: `PTD_PBP_ID_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (June). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - March](https://www.resdac.org/cms-data/variables/part-d-pbp-number-march)

- Short SAS Name: `PTDPBPID03`
- Long SAS Name: `PTD_PBP_ID_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (March). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - May](https://www.resdac.org/cms-data/variables/part-d-pbp-number-may)

- Short SAS Name: `PTDPBPID05`
- Long SAS Name: `PTD_PBP_ID_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (May). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - November](https://www.resdac.org/cms-data/variables/part-d-pbp-number-november)

- Short SAS Name: `PTDPBPID11`
- Long SAS Name: `PTD_PBP_ID_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (November). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - October](https://www.resdac.org/cms-data/variables/part-d-pbp-number-october)

- Short SAS Name: `PTDPBPID10`
- Long SAS Name: `PTD_PBP_ID_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (October). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D PBP Number - September](https://www.resdac.org/cms-data/variables/part-d-pbp-number-september)

- Short SAS Name: `PTDPBPID09`
- Long SAS Name: `PTD_PBP_ID_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The variable is the Part D plan benefit package (PBP) for the beneficiary’s Part D plan for a given month (September). CMS assigns an identifier to each PBP within a contract that a Part D plan sponsor has with CMS.

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates the final, reconciled PBP number.
For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December). You need to know both the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package in order to identify the specific plan in which a beneficiary was enrolled.



<h3>Values</h3>

| Code                                                 |
|:-----------------------------------------------------|
| 3-digit alphanumeric that can include leading zeros. |

## [Part D Retiree Drug Subsidy Indicator - April](https://www.resdac.org/taxonomy/term/5581)

- Short SAS Name: `RDSIND04`
- Long SAS Name: `RDS_IND_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (April).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - August](https://www.resdac.org/taxonomy/term/5601)

- Short SAS Name: `RDSIND08`
- Long SAS Name: `RDS_IND_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (August).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - December](https://www.resdac.org/taxonomy/term/5621)

- Short SAS Name: `RDSIND12`
- Long SAS Name: `RDS_IND_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (December).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - February](https://www.resdac.org/taxonomy/term/5571)

- Short SAS Name: `RDSIND02`
- Long SAS Name: `RDS_IND_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (February).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - January](https://www.resdac.org/cms-data/variables/RDS-Code-Retiree-Drug-Subsidy-Code-occurs-12-times)

- Short SAS Name: `RDSIND01`
- Long SAS Name: `RDS_IND_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (January).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - July](https://www.resdac.org/taxonomy/term/5596)

- Short SAS Name: `RDSIND07`
- Long SAS Name: `RDS_IND_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (July).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - June](https://www.resdac.org/taxonomy/term/5591)

- Short SAS Name: `RDSIND06`
- Long SAS Name: `RDS_IND_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (June).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - March](https://www.resdac.org/taxonomy/term/5576)

- Short SAS Name: `RDSIND03`
- Long SAS Name: `RDS_IND_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (March).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - May](https://www.resdac.org/taxonomy/term/5586)

- Short SAS Name: `RDSIND05`
- Long SAS Name: `RDS_IND_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (May).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - November](https://www.resdac.org/taxonomy/term/5616)

- Short SAS Name: `RDSIND11`
- Long SAS Name: `RDS_IND_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (November).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - October](https://www.resdac.org/taxonomy/term/5611)

- Short SAS Name: `RDSIND10`
- Long SAS Name: `RDS_IND_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (October).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Retiree Drug Subsidy Indicator - September](https://www.resdac.org/taxonomy/term/5606)

- Short SAS Name: `RDSIND09`
- Long SAS Name: `RDS_IND_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates if the beneficiary was enrolled in an employer-sponsored prescription drug plan that qualified for Part D’s retiree drug subsidy (RDS) for a given month (September).

Some employers offer prescription drug plans to their retirees, and Part D pays a subsidy to plans that offer coverage that is equivalent to (or better than) conventional Part D benefits.
CMS does not collect PDEs for beneficiaries that are enrolled in RDS-eligible plans.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code   | Code Value                                                                                                                           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Y      | Employer subsidized for the retired beneficiary                                                                                      |
| N      | No employer subsidization for the retired beneficiary                                                                                |
| 0      | Not Medicare enrolled for the month                                                                                                  |
| *      | Enrolled in Medicare A and/or B, but no Part D enrollment data for the beneficiary. (This status was indicated as 'X' for 2006-2009) |

## [Part D Segment Number - April](https://www.resdac.org/taxonomy/term/5526)

- Short SAS Name: `SGMTID04`
- Long SAS Name: `PTD_SGMT_ID_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (April).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - August](https://www.resdac.org/taxonomy/term/5546)

- Short SAS Name: `SGMTID08`
- Long SAS Name: `PTD_SGMT_ID_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (August).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - December](https://www.resdac.org/taxonomy/term/5566)

- Short SAS Name: `SGMTID12`
- Long SAS Name: `PTD_SGMT_ID_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (December).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - February](https://www.resdac.org/taxonomy/term/5516)

- Short SAS Name: `SGMTID02`
- Long SAS Name: `PTD_SGMT_ID_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (February).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - January](https://www.resdac.org/cms-data/variables/Encrypted-Segment-ID-occurs-12-times)

- Short SAS Name: `SGMTID01`
- Long SAS Name: `PTD_SGMT_ID_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (January).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - July](https://www.resdac.org/taxonomy/term/5541)

- Short SAS Name: `SGMTID07`
- Long SAS Name: `PTD_SGMT_ID_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (July).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - June](https://www.resdac.org/taxonomy/term/5536)

- Short SAS Name: `SGMTID06`
- Long SAS Name: `PTD_SGMT_ID_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (June).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - March](https://www.resdac.org/taxonomy/term/5521)

- Short SAS Name: `SGMTID03`
- Long SAS Name: `PTD_SGMT_ID_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (March).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - May](https://www.resdac.org/taxonomy/term/5531)

- Short SAS Name: `SGMTID05`
- Long SAS Name: `PTD_SGMT_ID_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (May).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - November](https://www.resdac.org/taxonomy/term/5561)

- Short SAS Name: `SGMTID11`
- Long SAS Name: `PTD_SGMT_ID_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (November).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - October](https://www.resdac.org/taxonomy/term/5556)

- Short SAS Name: `SGMTID10`
- Long SAS Name: `PTD_SGMT_ID_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (October).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Segment Number - September](https://www.resdac.org/taxonomy/term/5551)

- Short SAS Name: `SGMTID09`
- Long SAS Name: `PTD_SGMT_ID_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the segment number that CMS assigns to identify a geographic market segment or subdivision of a Part D plan; the segment number allows you to determine the market area covered by the plan. The variable describes the market segment for a given month (September).

If the beneficiary did not have a Part D plan for a given month, this variable will have null/missing value for that month. If the beneficiary changed plans during the year, the value indicates market segment identifier for the final, reconciled PBP. For 2006 - 2012, this variable was always encrypted to comply with CMS privacy rules.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).
You need to know the Part D contract number (PTD_CNTRCT_ID_XX) and plan benefit package (PTD_PBP_ID_XX) in order to determine the geographic market areas where the particular PBP was offered. Premiums may vary by market segment.



<h3>Values</h3>

| Code                                                                 |
|:---------------------------------------------------------------------|
| Null/missing or a 3-digit numeric value that includes leading zeros. |

## [Part D Total Prescription Costs](https://www.resdac.org/cms-data/variables/Part-D-Total-Prescription-Costs)

- Short SAS Name: `PTD_TOTAL_RX_CST`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the gross drug cost (TOT_RX_CST_AMT) of all Part D drugs for a given year. This value includes the ingredient cost, dispensing fee, sales tax (if applicable), and vaccine administration fee (if any, 2010+ only).



<h3>Values</h3>



This is the price paid for the drug at the point of sale (i.e., the pharmacy counter), and it does not include any rebates or discounts that the drug manufacturer provides directly to the Part D plan sponsor. 

The value will be null if the beneficiary was not enrolled in Part D or did not use any Part D drugs during the year. 



## [Part D low-income cost share group code - April](https://www.resdac.org/taxonomy/term/5691)

- Short SAS Name: `CSTSHR04`
- Long SAS Name: `CST_SHR_GRP_CD_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (April). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - August](https://www.resdac.org/taxonomy/term/5711)

- Short SAS Name: `CSTSHR08`
- Long SAS Name: `CST_SHR_GRP_CD_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (August). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - December](https://www.resdac.org/taxonomy/term/5731)

- Short SAS Name: `CSTSHR12`
- Long SAS Name: `CST_SHR_GRP_CD_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (December). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - February](https://www.resdac.org/taxonomy/term/5681)

- Short SAS Name: `CSTSHR02`
- Long SAS Name: `CST_SHR_GRP_CD_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (February). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - January](https://www.resdac.org/cms-data/variables/Cost-Share-Group-Code-occurs-12-times)

- Short SAS Name: `CSTSHR01`
- Long SAS Name: `CST_SHR_GRP_CD_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (January). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - July](https://www.resdac.org/taxonomy/term/5706)

- Short SAS Name: `CSTSHR07`
- Long SAS Name: `CST_SHR_GRP_CD_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (July). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - June](https://www.resdac.org/taxonomy/term/5701)

- Short SAS Name: `CSTSHR06`
- Long SAS Name: `CST_SHR_GRP_CD_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (June). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - March](https://www.resdac.org/taxonomy/term/5686)

- Short SAS Name: `CSTSHR03`
- Long SAS Name: `CST_SHR_GRP_CD_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (March). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - May](https://www.resdac.org/taxonomy/term/5696)

- Short SAS Name: `CSTSHR05`
- Long SAS Name: `CST_SHR_GRP_CD_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (May). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - November](https://www.resdac.org/taxonomy/term/5726)

- Short SAS Name: `CSTSHR11`
- Long SAS Name: `CST_SHR_GRP_CD_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (November). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - October](https://www.resdac.org/taxonomy/term/5721)

- Short SAS Name: `CSTSHR10`
- Long SAS Name: `CST_SHR_GRP_CD_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (October). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Part D low-income cost share group code - September](https://www.resdac.org/taxonomy/term/5716)

- Short SAS Name: `CSTSHR09`
- Long SAS Name: `CST_SHR_GRP_CD_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the beneficiary’s Part D low-income subsidy cost sharing group for a given month (September). The Part D benefit requires enrollees to pay both premiums and cost-sharing, but the program also has a low-income subsidy (LIS) that covers some or all of those costs for certain low-income individuals, including deductibles and cost-sharing during the coverage gap.

CMS identifies beneficiaries with fully-subsidized Part D coverage by looking for individuals that have a 01, 02, or 03 for the month. Other beneficiaries who are eligible for the LIS but do not receive a full subsidy have a 04, 05, 06, 07, or 08. The remaining values indicate that the individual is not eligible for subsidized Part D coverage. There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December)



<h3>Values</h3>



 Part D low-income cost share group code .txt 



## [Peripheral Vascular Disease End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/peripheral-vascular-disease-end-year-indicator-medicare-only-claims)

- Short SAS Name: `PVD_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for peripheral vascular disease as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For peripheral vascular disease, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Peripheral Vascular Disease First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/peripheral-vascular-disease-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `PVD_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the peripheral vascular disease indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Personality Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/personality-disorders-end-year-indicator-medicare-only-claims)

- Short SAS Name: `PSDS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for personality disorders as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For personality disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Personality Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/personality-disorders-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `PSDS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the personality disorders indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Post-Traumatic Stress Disorder End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/post-traumatic-stress-disorder-end-year-indicator-medicare-only-claims)

- Short SAS Name: `PTRA_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for post-traumatic stress disorder as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For post-traumatic stress disorder, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Post-Traumatic Stress Disorder First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/post-traumatic-stress-disorder-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `PTRA_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the post-traumatic stress disorder indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Pressure Ulcers and Chronic Ulcers End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/pressure-ulcers-and-chronic-ulcers-end-year-indicator-medicare-only-claims)

- Short SAS Name: `ULCERS_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for pressure ulcers and chronic ulcers as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For pressure ulcers and chronic ulcers, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Pressure Ulcers and Chronic Ulcers First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/pressure-ulcers-and-chronic-ulcers-first-ever-occurrence-date-medicare-only)

- Short SAS Name: `ULCERS_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the pressure ulcers and chronic ulcers indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Prostate Cancer End-of-Year Flag](https://www.resdac.org/cms-data/variables/Prostate-Cancer-End-Year-Flag)

- Short SAS Name: `CNCRPRST`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for prostate cancer as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For prostate cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with a prostate cancer code, on any diagnosis, within the last year. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Prostate Cancer Mid-Year Flag](https://www.resdac.org/cms-data/variables/Prostate-Cancer-Mid-Year-Flag)

- Short SAS Name: `CNCRPRSM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for prostate cancer on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For prostate cancer, beneficiaries must have at least one inpatient or SNF claim, or two Part B (institutional or non-institutional) claims that are at least one day apart, with a prostate cancer code, on any diagnosis, within the last year. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Reference Year](https://www.resdac.org/cms-data/variables/reference-year)

- Short SAS Name: `RFRNC_YR`
- Long SAS Name: `BEN_ENROLLMT_REF_YR`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field indicates the reference year of the enrollment data. NOTE: The data files are partitioned into calendar year files.



## [Research Triangle Institute (RTI) Race Code](https://www.resdac.org/cms-data/variables/Research-Triangle-Institute-RTI-Race-Code)

- Short SAS Name: `RTI_RACE_CD`
- Long SAS Name: `RTI_RACE_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Beneficiary race code (modified using RTI algorithm). Enhanced race/ethnicity designation based on first and last name algorithms.



<h3>Values</h3>

This variable is created by taking the beneficiary race code that has historically been used by the Social Security Administration (and is in turn used in CMS’s enrollment data base) and applying an algorithm that identifies more beneficiaries as Hispanic or Asian. This algorithm was developed by the Research Triangle Institute (RTI) and is thus often referred to as the “RTI race code”. The algorithm classifies beneficiaries as Hispanic or Asian if their SSA race code equals 4 (Asian) or 5 (Hispanic), or if they have a first or last name that RTI determined was likely Hispanic or Asian in origin.

The variable also incorporates CCW enhancements that reduce the number of beneficiaries with missing information.


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | UNKNOWN                         |
| 1      | NON-HISPANIC WHITE              |
| 2      | BLACK (OR AFRICAN-AMERICAN)     |
| 3      | OTHER                           |
| 4      | ASIAN/PACIFIC ISLANDER          |
| 5      | HISPANIC                        |
| 6      | AMERICAN INDIAN / ALASKA NATIVE |

## [Rheumatoid Arthritis / Osteoarthritis End-of-Year Flag](https://www.resdac.org/cms-data/variables/Rheumatoid-Arthritis-Osteoarthritis-End-Year-Flag)

- Short SAS Name: `RA_OA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the chronic condition data warehouse (CCW) criteria for rheumatoid arthritis/osteoarthritis as of the end of the calendar year.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For rheumatoid arthritis/osteoarthritis, beneficiaries must have at least two inpatient, SNF, home health, or Part B (institutional or non-institutional) claims that are at least one day apart with a rheumatoid arthritis/osteoarthritis code in any position during the 2-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website:
https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                                                                                 |
|:-------|:-------------------------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient fee-for-service (FFS) coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage                   |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage                   |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage                            |

## [Rheumatoid Arthritis / Osteoarthritis Mid-Year Flag](https://www.resdac.org/cms-data/variables/Rheumatoid-Arthritis-Osteoarthritis-Mid-Year-Flag)

- Short SAS Name: `RA_OA_M`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For rheumatoid arthritis/osteoarthritis, beneficiaries must have at least two inpatient, SNF, home health, or Part B (institutional or non-institutional) claims that are at least one day apart with a rheumatoid arthritis/osteoarthritis code in any position during the 2-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Schizophrenia End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-end-year-indicator-medicare-only-claims)

- Short SAS Name: `SCHI_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for schizophrenia as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For schizophrenia, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Schizophrenia First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `SCHI_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the schizophrenia indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Schizophrenia and Other Psychotic Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-and-other-psychotic-disorders-end-year-indicator-medicare-only)

- Short SAS Name: `SCHIOT_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for schizophrenia and other psychotic disorders as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For schizophrenia and other psychotic disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Schizophrenia and Other Psychotic Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/schizophrenia-and-other-psychotic-disorders-first-ever-occurrence-date-medicare)

- Short SAS Name: `SCHIOT_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the schizophrenia and other psychotic disorders indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Sensory - Blindness and Visual Impairment End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-blindness-and-visual-impairment-end-year-indicator-medicare-only-claims)

- Short SAS Name: `VISUAL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for sensory (blindness and visual) impairment as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For sensory (blindness and visual) impairment, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Sensory - Blindness and Visual Impairment First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-blindness-and-visual-impairment-first-ever-occurrence-date-medicare-only)

- Short SAS Name: `VISUAL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the sensory (blindness and visual) impairment indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Sensory - Deafness and Hearing Impairment End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-deafness-and-hearing-impairment-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `HEARIM_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for a sensory (deafness and hearing) impairment as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For sensory (deafness and hearing) impairment, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Sensory - Deafness and Hearing Impairment First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/sensory-deafness-and-hearing-impairment-first-ever-occurrence-date-medicare-onl-0)

- Short SAS Name: `HEARIM_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for a sensory (deafness and hearing) impairment. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Sex](https://www.resdac.org/cms-data/variables/Sex)

- Short SAS Name: `SEX`
- Long SAS Name: `SEX_IDENT_CD`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the sex of the beneficiary.



<h3>Values</h3>

| Code   | Code Value   |
|:-------|:-------------|
| 0      | UNKNOWN      |
| 1      | MALE         |
| 2      | FEMALE       |

## [Skilled Nursing Facility Beneficiary Payments](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Beneficiary-Payments)

- Short SAS Name: `SNF_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of Medicare coinsurance and deductible payments in the skilled nursing facility (SNF) setting for a given year.  The total beneficiary payment is calculated as the sum of DED_AMT and COIN_AMT for all SNF claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Costs to that beneficiaries are liable for are described in detail on the Medicare.gov website. There is a CMS publication called "Your Medicare Benefits", which explains the deductibles and coinsurance amounts.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Skilled Nursing Facility Covered Days](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Covered-Days)

- Short SAS Name: `SNF_COV_DAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of Medicare covered days in the skilled nursing facility (SNF) setting for the year.  This variable equals the sum of the CLM_UTLZTN_DAY_CNT variables on the source claims.



<h3>Values</h3>



We consider fully-covered days, days where the beneficiary was liable for coinsurance, and lifetime reserve days to all be Medicare-covered days.  Non-covered days, leave of absence days, and the day of discharge or death are not included.

Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html) 



## [Skilled Nursing Facility Medicare Payments](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Medicare-Payments)

- Short SAS Name: `SNF_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the total Medicare payments in the skilled nursing facility (SNF) setting for a given year.  The total Medicare payments for SNF are calculated as the sum of CLM_PMT_AMT for all SNF claims where the CLM_PMT_AMT >= 0.



<h3>Values</h3>



Medicare payments are described in detail in a series of Medicare Payment Advisory Commission (MedPAC) documents called “Payment Basics” (see: http://www.medpac.gov/-documents-/payment-basics).

Also in the Medicare Learning Network (MLN) “Payment System Fact Sheet Series” (see the list of MLN publications at: http://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/MLN-Publications.html)
 



## [Skilled Nursing Facility Stays](https://www.resdac.org/cms-data/variables/Skilled-Nursing-Facility-Stays)

- Short SAS Name: `SNF_STAYS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the count of skilled nursing facility setting (SNF) stays (unique admissions, which may span more than one facility) for a given year.  A SNF stay is defined as a set of one or more consecutive skilled nursing facility claims where the beneficiary is only discharged on the most recent claim in the set.



<h3>Values</h3>



The CLM_FROM_DT for the first claim associated with the stay must have been in the year of the data file, however it was permissible for the CLM_THRU_DT to have occurred in January of the following year. 



## [Source of enrollment data](https://www.resdac.org/cms-data/variables/source-enrollment-data)

- Short SAS Name: `ENRL_SRC`
- Long SAS Name: `ENRL_SRC`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates the source of enrollment data.

The Centers for Medicare & Medicaid Services (CMS) has updated the Medicare enrollment source data for the Master Beneficiary Summary File (MBSF). As of March 2017, the MBSF includes Medicare enrollment information from the CMS Common Medicare Environment (CME) rather than the CMS Enrollment Database (EDB). Data from the two sources was nearly identical. The CME improves the identification of Medicare Part B enrollment and also allows for more timely release of the MBSF. The universe of beneficiaries in the CME versus the EDB version of the MBSF are only slightly different.



<h3>Values</h3>

| Code   | Code Value                  |
|:-------|:----------------------------|
| EDB    | Enrollment Database         |
| CME    | Common Medicare Environment |

## [Spina Bifida and Other Congenital Anomalies of the Nervous System End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spina-bifida-and-other-congenital-anomalies-nervous-system-end-year-indicator)

- Short SAS Name: `SPIBIF_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for spina bifida and other congenital anomalies of the nervous system as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For spina bifida and other congenital anomalies of the nervous system, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Spina Bifida and Other Congenital Anomalies of the Nervous System First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spina-bifida-and-other-congenital-anomalies-nervous-system-first-ever-occurrence)

- Short SAS Name: `SPIBIF_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the spina bifida and other congenital anomalies of the nervous system indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Spinal Cord Injury End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spinal-cord-injury-end-year-indicator-medicare-only-claims)

- Short SAS Name: `SPIINJ_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for spinal cord injury as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For spinal cord injury, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Spinal Cord Injury First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/spinal-cord-injury-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `SPIINJ_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the spinal cord injury indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [State Buy-In Coverage Count](https://www.resdac.org/cms-data/variables/State-Buy-Coverage-Count)

- Short SAS Name: `BUYIN_MO`
- Long SAS Name: `BENE_STATE_BUYIN_TOT_MONS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

Total number of months of state buy-in.



<h3>Values</h3>



This variable counts the total number of months during the year when the beneficiary premium was paid by the state. State Medicaid programs can pay Medicare premiums for certain dual eligibles (i.e., for beneficiaries also enrolled in a state Medicaid program); this action is called “buying in” and so this variable is the “buy-in code.”  Any month where the BUYINXX variable was: A (Part A state buy-in), B (Part B state buy-in), or C(Part A and Part B state buy-in) is counted.
 



## [State and county FIPS code - April](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-april)

- Short SAS Name: `STATE_CNTY_FIPS_CD_04`
- Long SAS Name: `STATE_CNTY_FIPS_CD_04`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in April.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - August](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-august)

- Short SAS Name: `STATE_CNTY_FIPS_CD_08`
- Long SAS Name: `STATE_CNTY_FIPS_CD_08`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in August.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - December](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-december)

- Short SAS Name: `STATE_CNTY_FIPS_CD_12`
- Long SAS Name: `STATE_CNTY_FIPS_CD_12`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in December.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - February](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-february)

- Short SAS Name: `STATE_CNTY_FIPS_CD_02`
- Long SAS Name: `STATE_CNTY_FIPS_CD_02`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in February.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - January](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-january)

- Short SAS Name: `STATE_CNTY_FIPS_CD_01`
- Long SAS Name: `STATE_CNTY_FIPS_CD_01`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in January.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - July](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-july)

- Short SAS Name: `STATE_CNTY_FIPS_CD_07`
- Long SAS Name: `STATE_CNTY_FIPS_CD_07`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in July.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - June](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-june)

- Short SAS Name: `STATE_CNTY_FIPS_CD_06`
- Long SAS Name: `STATE_CNTY_FIPS_CD_06`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in June.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - March](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-march)

- Short SAS Name: `STATE_CNTY_FIPS_CD_03`
- Long SAS Name: `STATE_CNTY_FIPS_CD_03`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in March.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - May](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-may)

- Short SAS Name: `STATE_CNTY_FIPS_CD_05`
- Long SAS Name: `STATE_CNTY_FIPS_CD_05`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in May.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - November](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-november)

- Short SAS Name: `STATE_CNTY_FIPS_CD_11`
- Long SAS Name: `STATE_CNTY_FIPS_CD_11`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in November.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - October](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-october)

- Short SAS Name: `STATE_CNTY_FIPS_CD_10`
- Long SAS Name: `STATE_CNTY_FIPS_CD_10`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in October.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State and county FIPS code - September](https://www.resdac.org/cms-data/variables/state-and-county-fips-code-september)

- Short SAS Name: `STATE_CNTY_FIPS_CD_09`
- Long SAS Name: `STATE_CNTY_FIPS_CD_09`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This field specifies the monthly the concatenated state/county Federal Information Processing Standard (FIPS) code for the beneficiary - in September.

The first 2 digits specify the state; the last 3 digits specify the county.
This variable is derived by taking the SSA state/county code on record for the beneficiary in the CMS enrollment database and linking it to the corresponding FIPS state/county code.
There are 12 monthly variables - where the 01 through 12 at the end of the variable name correspond with the month (e.g., 01 is January and 12 is December).



<h3>Values</h3>

| Code                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------|
| 5-digit numeric value, which can include leading zeros, or null (if there is no crosswalk from the SSA code to the FIPS code) |

## [State code for beneficiary (SSA code)](https://www.resdac.org/cms-data/variables/State-Code)

- Short SAS Name: `STATE_CD`
- Long SAS Name: `STATE_CODE`

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

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

The social security administration (SSA) standard 2-digit state code of a beneficiary's residence. 

 ResDAC data variable alert:Invalid beneficiary resident state codes are being sent to CMS from SSA.    -SSA has not identified a timeframe for resolution but the two agencies are addressing the issue.    -CMS notes the invalid codes as: 67, 68, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 96 and 97.    - ResDAC is aware that redundant code values exist in the table:        -64, 99 resolve to American Samoa;        -65, 98 resolve to Guam;        -66, 97 resolve to Northern Marianas. As noted above, 97 is an invalid code.



<h3>Values</h3>



 State SSA codes_GDIT_05182017.txt 



## [Stroke / Transient Ischemic Attack End-of-Year Flag](https://www.resdac.org/cms-data/variables/Stroke-Transient-Ischemic-Attack-End-Year-Flag)

- Short SAS Name: `STRKETIA`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria within the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For stroke/TIA, beneficiaries must have at least one inpatient claim or two Part B (institutional or non-institutional) claims with a stroke/TIA code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories


| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Stroke / Transient Ischemic Attack Mid-Year Flag](https://www.resdac.org/cms-data/variables/Stroke-Transient-Ischemic-Attack-Mid-Year-Flag)

- Short SAS Name: `STRKTIAM`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This code specifies whether the beneficiary met the chronic condition algorithm criteria on July 1 of the specified reference period.



<h3>Values</h3>

The CCW’s chronic condition flags require beneficiaries to satisfy both claims criteria (a minimum number/type of claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (FFS Part A and Part B coverage during the entire specified time period). For stroke/TIA, beneficiaries must have at least one inpatient claim or two Part B (institutional or non-institutional) claims with a stroke/TIA code in any position during the 1-year reference period. The CCW’s criteria were developed after reviewing validated algorithms from the research literature and criteria used by other federal data sources.  You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                      |
|:-------|:--------------------------------|
| 0      | Neither claims nor coverage met |
| 1      | Claims met, coverage not met    |
| 2      | Claims not met, coverage met    |
| 3      | Claims and coverage met         |

## [Tests Beneficiary Payments](https://www.resdac.org/cms-data/variables/Tests-Beneficiary-Payments)

- Short SAS Name: `TEST_BENE_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable is the sum of coinsurance and deductible payments for part B tests for a given year. The total Beneficiary payments are calculated as the sum of LINE_COINSRNC_AMT + LINE_BENE_PTB_DDCTBL_AMT for the relevant lines.   

Claims for tests are a subset of the claims in the Part B Carrier data file. These claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =T.



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Tests Events](https://www.resdac.org/cms-data/variables/Tests-Events)

- Short SAS Name: `TEST_EVENTS`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the count of events in for part B tests for a given year.  Claims for tests are a subset of the claims in the Part B Carrier data file. These claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =T.

An event is defined as each line item that contains the relevant service."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Anesthesia, Part B Drug, Physician, E & M, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Tests Medicare Payments](https://www.resdac.org/cms-data/variables/Tests-Medicare-Payments)

- Short SAS Name: `TEST_MDCR_PMT`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

"This variable is the total Medicare payments for part B tests for a given year.  Claims for tests are a subset of the claims in the Part B Carrier data file. These claims are defined as those with a line BETOS code (BETOS_CD) where the first digit =T.

The total Medicare payments are calculated as the sum of LINE_NCH_PMT_AMT where the LINE_PRCSG_IND_CD was ('A','R', or 'S') - for all relevant lines."



<h3>Values</h3>



There are 11 cost/use categories from the Carrier Part B and DME data files – the ASC, Part B Drug, Physician, E &M, anesthesia, dialysis, imaging, tests, other procedures, DME and other carrier claims.
 



## [Tobacco Use Disorders End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/tobacco-use-disorders-end-year-indicator-medicare-only-claims)

- Short SAS Name: `TOBA_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for tobacco use disorders as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE: For tobacco use disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Tobacco Use Disorders First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/tobacco-use-disorders-first-ever-occurrence-date-medicare-only-claims)

- Short SAS Name: `TOBA_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the tobacco use disorders indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).



## [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-brain-damage-end-0)

- Short SAS Name: `BRAINJ_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for traumatic brain injury and nonpsychotic mental disorders as of the end of the calendar year.



<h3>Values</h3>

The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period). 
		
For traumatic brain injury and nonpsychotic mental disorders, beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Traumatic Brain Injury and Nonpsychotic Mental Disorders due to Brain Damage First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/traumatic-brain-injury-and-nonpsychotic-mental-disorders-due-brain-damage-first-0)

- Short SAS Name: `BRAINJ_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the traumatic brain injury and nonpsychotic mental disorders indicator. The variable will be blank for beneficiaries that have never had the condition.



<h3>Values</h3>



The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File). 



## [Viral Hepatitis (General) End-of-Year Indicator - Medicare Only Claims](https://www.resdac.org/cms-data/variables/viral-hepatitis-general-end-year-indicator-medicare-only-claims-0)

- Short SAS Name: `HEPVIRAL_MEDICARE`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable indicates whether a beneficiary met the condition criteria for viral hepatitis (general) as of the end of the calendar year.

NOTE: The condition variable requires beneficiaries to satisfy both claims criteria (a minimum number/type of Medicare claims that have the proper diagnosis codes and occurred within a specified time period) and coverage criteria (Medicare FFS Part A and Part B coverage during the entire specified time period).

NOTE1: For viral hepatitis (general), beneficiaries must have at least one Medicare inpatient claim or two other non-drug claims of any service type with a related code in any position during the 2-year reference period. You can find more detailed information on the criteria on the CCW website: https://www.ccwdata.org/web/guest/condition-categories



<h3>Values</h3>

| Code   | Code Value                                                               |
|:-------|:-------------------------------------------------------------------------|
| 0      | Beneficiary did not meet claims criteria or have sufficient FFS coverage |
| 1      | Beneficiary met claims criteria but did not have sufficient FFS coverage |
| 2      | Beneficiary did not meet claims criteria but had sufficient FFS coverage |
| 3      | Beneficiary met claims criteria and had sufficient FFS coverage          |

## [Viral Hepatitis (General) First Ever Occurrence Date - Medicare Only Claims](https://www.resdac.org/cms-data/variables/viral-hepatitis-general-first-ever-occurrence-date-medicare-only-claims-0)

- Short SAS Name: `HEPVIRAL_MEDICARE_EVER`

Contained in

- [Master Beneficiary Summary File](../mbsf.md#data-documentation)

This variable shows the date when the beneficiary first met the criteria for the viral hepatitis (general) indicator. The variable will be blank for beneficiaries that have never had the condition.

NOTE: The earliest possible date for anyone in the CCW is January 1, 1999. If the beneficiary became eligible for Medicare after that, the earliest possible date will be some time after his/her coverage start date (i.e., the COVSTART variable in the Beneficiary File).

