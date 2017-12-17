# Generating costs measures from the claims files

## Overview

Once the initial cohort is extracted, the claims files have been harmonized but are left in a fairly raw form. The next step involves aggregating the raw data into some measures which can be used in the analysis. This section reviews how to use the extracted claims to generate cost of care metrics. There are many important issues which need to be considered before adopting a specific cost measure. For one, provider costs are not reported in the claims data, what are reported are the amount charged and the total amount a provider receives for any given procedure/treatment. Although somewhat imprecise, the amount Medicare reimburses a provider is some time referred to as costs because it is thought to be a fairly good proxy for the actual costs a provider incurs.

Generating cost statistics from the claims data involves ensuring that that the beneficiaries in your sample are enrolled in the medicare part you are interested in and are not in an HMO during the time period your interested in. For example, if you are interested in looking at physician costs in the Carrier files 6 months after a heart attack, you should be sure to only include beneficiaries enrolled in Part B who are not in an HMO during that 6 month period. Failing properly drop individuals who are either not in part B or are serviced by an HMO will result in missing claims at work and mis-reported claims at worst therefore significantly skewing any statistics calculated. The enrollment restriction is taken care of by the software but is worth mentioning because of the complexity and confusion.

This portion of the documentation is devoted to describing the associated code which generates a total reimbursement/cost metric and a cost utilization metric. The following section is split between the two different cost measures. The first section provides a review of the traditional cost measure used in the literature; the total amount reimbursed for a procedure/stay. While the following section documents our 'cost utilization' measurement by providing an overview of the reimbursement systems and documenting the code used to generate the cost utilization metric.

## Cost measure: total reimbursement

The [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) program creates total reimbursement paid to the provider at different day intervals. The cost metrics generated capture total reimbursements which includes the adjustments CMS makes to specific hospital given their characteristics and geographic location. These programs generate cost of care measure which sum reimbursements occurring `X` days from the index event and collapses the data set to the index event level. For example the program generates 30-day costs for Part A and Part B, medPAR, carrier, outpatient and many other sub-classifications of claims.

The documentation proceeds as follows; first the different entities which submit payment to providers is reviewed. Since the claims files are billing records, each cost related variable in the data can be grouped into payment from one of these entities. The final section concludes with an overview of the [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) program which creates the costs statistics and the different types of files it creates. A useful report about the different reimbursement systems can be found [here](http://aging.senate.gov/crs/medicare7.pdf).

### Defining total costs as payments made to providers

Providers can be thought of receiving payment for care from three separate entities in the claims files:

1. **Medicare reimbursement**: The primary payment comes from Medicare and is equal to the amount which Medicare decides to reimburse.
2. **Beneficiary payment**:  Beneficiaries are the second entity contributing to the payments made to providers.
3. **Secondary payers**:  In some instances an individual may have more than one insurance policy or coverage through some other organization. When an individuals has this type of coverage there are a set of rules which determine who pays first. Secondary payers refers to these other types health coverage which are responsible for part of the bill before Medicare is.

In turn each of these entities has separate associated variables found in the Medicare claims files. In some instances these variables are different across the different claims files. ResDAC provides (upon request) several different worksheets which describe which variables found in the claims files need to be aggregated to obtain the payment to a provider. The following table provides links to these tables. Some care should be taken when applying these definitions to the older claims files as these files are created for the most recent files. This is especially important in the Outpatient and Carrier files where new payment systems were implemented 2000.

|           Claim Files           |   PDF    | Received from ResDAC |
|---------------------------------|----------|----------------------|
| MedPAR (Inpatient)              | [link](https://www.nber.org/medicare/public/unzipped/Auxiliary/WorkshopMedparFilePaymentCalculation.pdf) | June 2011            |
| Carrier                         | [link](https://www.nber.org/medicare/public/unzipped/Auxiliary/WorkshopCarrierFilePaymentCalculation.pdf) | June 2011            |
| Outpatient                      | [link](https://www.nber.org/medicare/public/unzipped/Auxiliary/WorkshopHospitalOutpatientFilePaymentCalculation.pdf) | June 2011            |
| Durable Medical Equipment (DME) | [link](https://www.nber.org/medicare/public/unzipped/Auxiliary/WorkshopDMEFilePaymentCalculation.pdf) | June 2011            |
| Home Health Agencies (HHA)      | [link](https://www.nber.org/medicare/public/unzipped/Auxiliary/WorkshopHHAFilePaymentCalculation.pdf) | June 2011            |

Table 6.1 ResDAC's Medicare variable aggregations for different costs

### Carrier costs extraction program/claim specific information

It is useful to review the structure of the files prior to working with them. Recall that each claim present in the Carrier files is made up of several line items. The NBER SAS extraction code extracts information for index events at the line item level because it allows researchers to dis-aggregate costs and other information at the smallest level possible. However, some variables are only available on the claims for a group of associated 'line items'. In these cases the code merges claim level information to the line item level, creating some redundancy.

In calculating reimbursements (according to correspondence with ResDAC) users can sum variables which covers payments from the 3 entities described in the previous section, see ResDAC documentation. The documentation recommends using the line allowed charge amount (`lalowchg`) in order to get a measure of total reimbursement. The latter is used in the cost programs because it is available for all years (see `stayCost` variable). Lastly, because some claims or line items maybe denied, ResDAC also suggests dropping all denied claims and line items before calculating costs as is done in the SAS code.

### Outpatient cost extraction program/claim specific information

Similar to the Carrier files the Outpatient files provide a claim and revenue center level observations. The revenue centers can be thought of as the analog of the line item and provide much more detailed information about the specific claim of interest. However, the code does not extract the outpatient files at the revenue center level, instead it leaves the claims in its 'relational' form. Note that for total costs purposes, the variable `pmt_amt`, found on the claims files, is used because it includes total payments for both the associated revenue center and claims files. Therefore the code does not need to use revenue center level claims when constructing costs as the total amount reimbursed.

### [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) costs programs

The goal of the [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) program is to aggregate the claims and create X-day cost measures relative to the index event date. The final data set will have several variables describing costs at the index event level, which can be merged with an other file by using the `diag_id` variable. Note that the program looks to estimates all-payment received by the provider , equal to all payment made from the three groups `MEDICARE REIMB + BENE PAYMENT + SECONDARY PAY`. Embedded in the code, comments document the exact variables used to generate a measure of spending.

The code assumed that costs in claims are linear over time in the case where a length of stay is longer then the `X` days cost metric being constructed. For example if a claim started on the 26th day after the index event and lasted through the 35th day after the index event, 30 days costs would include 50% $((30-26+1)/(35-26+1))$ of the associated costs for that claim.

In addition to information on the actual amount a provider is payed, the bill or charge amount a provider sends to Medicare is also available in the claims files. For the most part we extract information regarding expenditures in the code, however it is just as easy to move forward and extract charge information if one was so inclined by adding the variables of interest to the extraction programs.

Lastly, the code goes ahead and splits costs in the MedPAR file by provider type using the provider numbers. The different grouping in part reflect the different type of PPS systems found in the MedPAR file.

The [`CumulativeCostsPerIndx.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_costs_raw/CumulativeCostsPerIndx.sas) program creates the following files, assuming a five percent extract was run:

1. `ami05_alldcost`: Combines cost/reimbursement information from the MedPAR, Carrier and OP files. Output at to the index level.
2. `ami05_carcost`: Creates reimbursement/costs measures for index events at different day levels using the Carrier files - erased.
3. `ami05_mparcost`: Creates reimbursement/costs measures for index events at different day levels using the MedPAR files - erased.
4. `ami05_opcost`: Creates reimbursement/costs measures for index events at different day levels using the OP files - erased.

##  Cost measure: cost of health care utilization & Medicare payment system overview

This section turns to the more involved task of separating payments made to providers based for the amount of care provider or utilized from the reimbursement made to providers based on non-utilization factors. In order to do so an understanding of the different payment systems is needed. The following subsections will be broken down by Medicare claim type (MedPAR, Carrier or Outpatient), each section will review the different payment systems found within each claim file noting that not all payment systems have a cost-utilization measure created for them. Each section will provide an overview of the payment systems found in each claim file and will close with describing how the cost utilization measure for the given payment system is constructed in the code.

Generally, each payment system follows a similar formula where a weight, assigned to the care received, describes the intensity of care relative to some average level of care. However converting this level of care into a dollar amount requires a base dollar amount CMS refers to as a conversion factor, which is updated annually. The weight and conversion factor determine the reimbursement a provider receives for the services rendered to a patient, however their are additional multipliers or add-ons specific to different payment systems which compensate a provider for non-utilization characteristics.

One notable exception exists for these payment systems exists in the case of Maryland. [^48] The programs presented in this section do not attempt to account for Maryland specific reimbursement rules or exclude claims occurring in Maryland. Researchers should be aware of this issue.

[^48]: [ http://www.commonwealthfund.org/Innovations/State-Profiles/2010/Jan/Maryland-All-Payer.aspx]( http://www.commonwealthfund.org/Innovations/State-Profiles/2010/Jan/Maryland-All-Payer.aspx)

As a general rule of thumb, users looking for more in-depth descriptions of payment systems should first check the MedPAC site for information regarding reimbursement systems, then look through CMS published final rules and finally move onto the internet-only manuals (IOM). Each resource goes into much more detail then the previous and its advisable to try to get a top down understanding before moving into too fine of detail on the reimbursement systems. It is worth noting that while the formulas appear straightforward, in practice they may lack many important details. In order to truly capture the reimbursement system with greater accuracy would in some cases involve a level of granularity which is difficult to attain. Furthermore, the changing reimbursement policies over time would also need to be replicated. With these warning in mind, the following section provides an overview of how the current reimbursement systems function. Information on final rules as well as a short overview of the different formulas CMS uses in calculating the reimbursement are discussed. In addition to the final rules, a direct link to the current regulations is available [here](http://ecfr.gpoaccess.gov/cgi/t/text/text-idx?type=simple;c=ecfr;cc=ecfr;idno=42;region=DIV1;q1=410;rgn=div5;sid=50998e57993a19624a6462a55d28f150;view=text;node=42%3A2.0.1.2.10).

Finally, users looking to run the `costutilization` programs should note that there are several SAS programs which provide the cost utilization code, however the structure is different then some of the other programs included in the main extraction portion of the code. All programs used are controlled by a master program which calls all of the subprograms for the different reimbursement systems. The program is called [`CallAllCostUtilizationPrgms.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/CallAllCostUtilizationPrgms.sas). The code used is nested according to the payment system used. Individuals need only run this program and comment out what parts of the program they do not want to run.

### Difference between Dartmouth index and cost utilization measure developed here

Researchers at Dartmouth developed a cost utilization index, described in detail by Gottlieb et al. (2010), and made the index available to the public. While the methodology used in many instance is close, the Dartmouth index and the cost utilization measures defined here do have several substantial differences which we believe make our measure more flexible. The first major difference is that the Dartmouth index only goes back to 2003 and is only made available at the state and HRR level. The geographic level of aggregation would not be adequate in studies concentrating on provider level outcomes. The index is also aggregated across several different payment systems which may or may not be a problem for some studies. However, the largest difference between these measures is in how Dartmouth multiplies their index by a constant every year to ensure that cost utilization measures equal total cost. We do not do this with our measures because it would make comparing them over time difficult, since the constant would change annually therefore potentially biasing longitudinal comparisons[^49].

[^49]: Thanks to Jonathan Holmes for pointing this out.

### MedPAR cost utilization measures (AIPPS only)

The MedPAR file is generated from the inpatient and skilled nursing facility claims files. While the largest payment system, in terms of expenditures, is the Acute Inpatient Prospective Payment System (IPPS) which deals with short-term inpatient facilities their are several other reimbursement systems found in the MedPAR claims files for which no cost-utilization measure was constructed. Specifically the following table documents the payment systems and whether a cost-utilization measure has been constructed for them. However it is worth noting that many of the other payment systems use the hospital wage index to adjust prices, and adjusting these other systems by the wage index would help get closer to the amount reimbursed for the care given by a provider.

|        Payment System        | Year Implemented | Cost-utilization Measure |
|------------------------------|------------------|--------------------------|
| Acute Inpatient PPS (AIPPS)  | 1984             | Yes                      |
| Inpatient Rehab PPS          | January 2002     | No                       |
| Long-Term Inp Care PPS       | October 2002     | No                       |
| Psychiatric Inpatient PPS    | January 2005     | No                       |
| Critical Access Hospitals    | 1998?            | No                       |
| Skilled Nursing Facility PPS | 1998             | No                       |

Table 6.2 Payment systems found in the MedPAR file

CMS describes in complete detail any changes made to their reimbursement policy in an annual document published August 1st, effective October 1st. The document known as the Acute IPPS final rule is updated on a fiscal year basis. Therefore researchers interested in studying changes to the Acute IPPS may yield cleaner results, with respect to the impact of reimbursement changes, if they work with fiscal as opposed to calendar years.

!!! note
    It is important for a researcher to realize that skilled nursing facilities and long-term care inpatient stays are also found in the MedPAR file but are reimbursed under a different payment system.

#### Overview of CMS Acute Inpatient Prospective Payment System (IPPS) reimbursement policy

Lincoln,New Hampshire

The Social Security Amendments of 1983 established the prospective payment system (PPS) for inpatient hospital services. The PPS established excludes children and cancer hospitals, as well as hospitals located outside of the 50 states. In addition, the statute allows for other exclusions like hospitals that are covered under state reimbursement control systems. These hospitals are paid on the basis of reasonable costs (IOM, Chapter 3 Inpatient Billing, Section 20).

Provider numbers 21000-21099 in Maryland are paid 94% of submitted charges subject to any unmet Part B deductible and coinsurance. (IOM, Chapter 3 Inpatient Billing, Section 20).

CMS reimburses individuals based on standardized capital and operating base amounts. Several adjustments are applied to the base amounts which account for wage differentials, urban/rural settings, teaching hospitals, disproportionate share and several other policy type adjustments. For a useful graphic of the costs refer to [MedPAC's hospital payment basics overview](http://www.medpac.gov/documents/MedPAC_Payment_Basics_10_hospital.pdf).

$$
TotalReimbursement = Operating + Capital
$$

$$
Operating = DRG_{hps}
\left( 1 + dish_h^{op} + teach_h^{op} \right)
\left( B_h^{NL} + B_h^L \cdot W_h^L \right)
$$

$$
Capital = DRG_{hps}
\left( 1 + dish_h^{cap}  + teach_h^{cap} \right)
\left( B_h^{NL} + B_h^L \cdot W_h^K \right)
$$

CMS reimburses inpatient providers on operating and capital expenses each of which are based on the $DRG_{hps}$ assigned to the $s$th stay of the $p$th patient in the $h$th hospital. DRGs are assigned on discharge from an inpatient facility and are therefore associated with a specific stay (not claim). Since they are assigned on discharge the MedPAR and Inpatient files can be thought of as being equivalent when summarizing DRGs for an associated event.

CMS reimbursement calculations begin with an adjusted base labor $B_h^L$ and non-labor $B_h^{NL}$ amount. These base amounts depend on whether the location of the $h$th hospital has an associated wage index which is less then or greater than 1. Next a geographic wage adjustment is applied to the $B_h^L$ in the form of a wage index dependent on the location of the hospital. Once the $B_h^L$ is adjusted, $B_h^{NL}$ is added to it a series of policy adjustments scale the reimbursement amount for different hospital specific factors. Finally this scaled amount is further multiplied by the DRG weight. The process is applied to both operating and capital amounts. Note that in the case of the capital amount it is adjusted by a geographic adjustment (GAF), $W_h^K$, which is not equal to the wage index used in the operating amount.

#### Other factors impacting DRG reimbursement

In addition to the generic DRG based reimbursement there are several other factors which may determine different reimbursement amount which include but are not limited to the following:

1. Transfer cases or cases with a length of stay less then the geometric mean
2. Outlier payments
3. Add on payments for new technology
4. Other provider specific adjustments

More information can be found at MedPAC's payment overview, ResDAC's [DRG payment document](http://www.resdac.org/Tools/TBs/TN-004_CalculatingHospitalDRG_508.pdf), CMS's Internet Only Manuals, Chapter 3 and also American Health Information Management Association's (AHIMA) Coding and Reimbursement for Hospital Inpatient Services, see [here](https://www.nber.org/medicare/public/unzipped/AHIMA_ch1INPATIENT_PPS.pdf) for chapter 1 from an old version of the book.

#### DRG weights

DRG weights are not available in the Medicare claims data, and need to be merged in from the annual DRG weight files. For recent regulation CMS has made the historical DRG weight file available.

#### Acute IPPS cost-utilization program

Program: [`InpatientPPS_calc.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/inpAcutePPS/InpatientPPS_calc.sas)

Equation (4) describes the cost-utilization measure constructed from the IAPPS and generated in the code. Note that the base payment amount, which can be thought of as the conversion factor ($/DRG weight) is taken from the Table 1A/B in the Appendix of the IAPPS final rules. One complication is that the final rule reports two base payments depending on the whether the hospital location has a wage adjustment factor greater then or equal to 1 (urban) or less then 1 (rural). The difference is small between the two amounts and we choose to first add the non-labor and labor amount together then take the average between the urban and rural quantities as defined in equation 4. See [`ImportDRGinfo.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/inpAcutePPS/ImportDRGinfo.sas) for exact labor/non-labor amount and in some instance capital amounts in the urban/rural setting. The quantities used as the conversion factor are displayed in 6.3↓.

$$
operatingcost_{utilization} = DRG_{hps}
\left[
\frac{
    \left( B_{w \geq 1}^{NL} + B_{w \geq 1}^L \right)
     + \left( B_{w < 1}^{NL} + B_{w < 1}^L \right)}{2}
\right]
$$

| Fiscal Year | Conversion Factor ($/DRG weight) | Reference rule |
|--|--|--|
| 1992 | 3443.236  | FR:: Aug 30,1991 pg 43249 |
| 1993 | 3662.173  |FR:: Sep 1,1992 pg 39845 |
| 1994 | 3660.383  | FR:: Sep 1,1993 pg 46362 |
| 1995 | 3764.665  | FR:: Sep 1,1994 |
| 1996 | 3809.090  | FR:: Sep 1,1995 |
| 1997 | 3877.550  | FR:: August 30,1996 |
| 1998 | 3873.745  |  |
| 1999 | 3974.830  |  |
| 2000 | 3919.745  |  |
| 2001 | 3996.515  |  |
| 2002 | 4123.830  |  |
| 2003 | 4217.550  | CMS-1470-CN |
| 2004 | 4377.820  |  |
| 2005 | 4554.255  | CMS-1482-F2: pg 23483 |
| 2006 | 4714.690  |  |
| 2007 | 4874.490  | CMS-1488-N |
| 2008 | 4960.640  | CMS-1533-CN2 |
| 2009 | 5097.460  |  |
| 2010 | 5128.560  |  |

Table 6.3 Historical IAPPS base payment/conversion factors ($/DRG weight)

1. `ami05_claimsDRGQ`: Generates medpar stay level cost utilization measure - `inpatient_Q` . Only defined for claims occuring at a short-term inpatient facility.

### Carrier cost-utilization metric

Not all services in the carrier files are paid by the physician fee schedule (PFS), which began in 1992. Some examples include ambulatory claims and clinical laboratory claims. Additionally, some services are priced regionally by the organizations which process the claims, referred to as Carriers, while other services are paid on a "reasonable charge" basis. Still some services which are covered can be bundled together. The cost-utilization measure developed here for use with the carrier files, covers all line items for the PFS. For line items with no RVU found in the PFS, the median reimbursement amount is used as the cost utilization measure.

#### Overview of CMS PFS reimbursement policy

The PFS was originally developed by Hsiao and Braun at the Harvard School of Public Health in the late 1980s. However as part of the maintenance of the PFS, the American Medical Association (AMA) offered to take on the role of updating the PFS to account for differences in payment structures and began to do so in 1992 as part of the 5-year maintenance review. Conversion factors are updated annually to account for increases in cost, where as RVU weights are updated annually to account for new codes with a more general review occuring every five-years, is a more in depth review which looks to make sure that the RVU weights keep pace with changes in the way medicine is practiced.

Historically, the RVU where calculated using charges from past claims, although beginning in 1999 the transition from a charge based to a resource based RVU methodology was fully implemented in 2002. The following provides a brief overview of the general formula CMS uses to calculate reimbursements. For further information refer to the IOM, CMS published final rules or [this MedPAC document](http://www.medpac.gov/documents/MedPAC_Payment_Basics_10_Physician.pdf).

The physician fee schedule maps HCPCS codes to relative value unit ($RVU$) weights associated with three different costs associated with physician providing care. Practice expense RVUs ( $RVU^{PE}$ ) capture the costs associated with renting office space, buying supplies and hiring non-physician clinical and administrative staff. Work RVUs ( $RVU^W$) capture the costs associated with physicians time for providing a service to a patient. Professional liability insurance RVUs ( $RVU^{PLI}$) capture the costs associated with the premium a physician pays for liability insurance. As the following formula shows, each of these components are adjusted by a specific geographic practice cost index ($GPCI$) relevant to each component. Note that the RVU weights are defined for the $l$th line items associated with the $c$th claim and $p$th patients treated at the $h$th hospital.

$$
C^{CAR} \left(
RVU_{hpcl}^W \cdot GPCI_h^W +
RVU_{hpcl}^{PE} \cdot GPCI_h^{PE} +
RVU_{hpcl}^{PLI} \cdot GPCI_h^{PLI}
\right)
+ Policy_h
$$

Once the RVUs have been adjusted for geographic costs and then summed together a conversion factor is used to transform the RVU weights into an associated dollar amount meant to capture the intensity of a specific procedure. Additionally, the physician fee schedule is adjusted based on the whether the physician provides the care in facility or non-facility setting. Finally, line items occurring during or after 2007 use the transitional PE RVU, rather then the implemented PE RVU which is used before 2007.

#### Merging in the physician fee schedule

RVU weights are not available in the Medicare claims data, and need to be merged in from the physician fee schedule. The physician fee schedule is identified at the HCPCS code and for some HCPCS code modifiers. While the physician fee schedule only has `TC`, `26`, and `53` modifier codes, the Medicare claims files have many more modifier codes. The reason for this disconnect is that not all modifier codes are of importance in determining the amount a code is reimbursed [^50]. In order to merge the claims and fee schedule, first merge on calendar year, HCPCS code and modifier code (only the first modifier). For all non matching merges, merge on calendar year and HCPCS code. A small percent of claims is not matched and are dropped from the sample.

[^50]: A modifier is shown if there is a technical component (modifier `TC`) and a professional component (PC) (modifier `-26`) for the service. If there is a PC and a `TC` for the service, Addendum B contains three entries for the code: One for the global values (both professional and technical); one for modifier `-26` (PC); and one for modifier `TC`. The global service is not designated by a modifier, and physicians must bill using the code without a modifier if the physician furnishes both the PC and the `TC` of the service. Modifier `-53` is shown for a discontinued procedure. There will be RVUs for the code (CPT code 45378) with this modifier - Federal Register Vol. 66 No. 212/Thursday, November 1, 2001/Rules and Regulations pg. 55295-55503

For the most part the file weights are updated annually with the exception of certain new technology which is deemed important enough for Medicare to start reimbursement. In order to be able to adapt to these instances, Medicare publishes the fee schedule quarterly. For most purposes using the last quarter, the "D" files, will suffice. The "D" files are used by the programs.

| Source | Calendar Year |
|-|-|
| Federal Register Vol. 64 No. 211 / Tuesday, November 2, 1999 / Rules and Regulations pg. 59429-59590 | 2000  |
| Federal Register Vol. 65 No. 212 / Wednesday, November 1, 2000/Rules and Regulations pg. 65425-65603 |  2001 |
| Federal Register Vol. 66 No. 212 / Thursday, November 1, 2001/Rules and Regulations pg. 55295-55503 |  2002 |
| CMS webpage --valid only for March 1, 2003 – Dec 31,	 |  2003 |
| CMS webpage  |  2004 forward |

Table 6.4 Annual Physician Fee Schedules Files

#### Status Indicators in the Physician Fee Schedule and Claims file

The status indicators in the PFS describes how the HCPCS code is reimbursed and what class it falls into. They are useful for figuring out how CMS reimburses a HCPCS code and are included in the final data set for this reason.

#### Conversion Factors

The conversion factors which translate RVU weights into dollar amounts are published and updated annually in the final rules. The conversion factors, CCAR can be found in the 6.5↓. Note that in 2008 the conversion factor was updated half-way through the year in a proposed rule but the change was never finalized and as a result never materialized. Determining the conversion factor in recent years can be tricky because CMS reports conversion factor that the sustainable growth factor (SGR) rule requires, even though congress has voided the rule every year since 2003.

In 2010, the conversion factor and the physician fee schedule were updated halfway through the year. On May 10, 2010 CMS released revised physician payment files to Medicare Contractors necessary to reflect changes to payments as a result of the CY 2010 correction notice published in the Federal Register on May 11, 2010 and changes resulting from the Patient Protection and Affordable Health Care Act. This fee schedule also reflects the Department of Defense Appropriations Act of 2010, the Temporary Extension Act of 2010, and the Continuing Extension Act of 2010 which have provided for a zero percent update to the 2010 Medicare Physician Fee Schedule and is effective for claims with dates of service from January 1, 2010 through May 31, 2010. These fees reflect a change in the conversion factor as a result of the Preservation of Access to Care for Medicare Beneficiaries and Pension Relief Act of 2010, which President Obama signed into law on June 25, 2010. This legislation provides for a 2.2 percent update to the 2010 Medicare Physician Fee Schedule (MPFS), effective for dates of service June 1, 2010, through November 30, 2010. Revised payment files were posted by CMS on July 1, 2010 [^51].

[^51]: This paragraph was taken from the following websitehttp://www.ahcancal.org/facility_operations/medicare/Pages/2010MedicarePartBFeeSchedule.aspx. The statements were verified. The following document also http://www.gpo.gov/fdsys/pkg/PLAW-111publ192/pdf/PLAW-111publ192.pdf explains the 2.2% uprate.

Note that the conversion factors are available from the AMA at http://www.ama-assn.org/resources/doc/rbrvs/cf-history.pdf. Chapter 12 of the internet only manuals (IOM) published by CMS also have historical conversion factors.

| source | Calendar Year | $C^{CAR}$ ($) |
|-|-|-|
| Chapter 12 - IOM - CMS  | 1998  |  36.6873 |
| Chapter 12 - IOM - CMS  | 1999  | 34.7315  |
| Federal Register Vol. 64 No. 211/ Tuesday, November 2, 1999/Rules and Regulations pg. 59429-59590  | 2000 | 36.6137  |
| Federal Register Vol. 65 No. 212/ Wednesday, November 1, 2000/Rules and Regulations pg. 65425-65603  | 2001 | 38.2581  |
| Federal Register Vol. 66 No. 212/Thursday, November 1, 2001/Rules and Regulations pg. 55295-55503  | 2002 | 36.1992  |
| CMS Webpage | 2003  | 36.7856  |
| CMS Webpage | 2004  | 37.3374  |
| CMS Webpage | 2005  | 37.8975  |
| CMS Webpage | 2006  | 37.8975  |
| CMS Webpage | 2007  | 37.8975  |
| CMS Webpage | 2008  | 38.0870  |
| CMS Webpage | 2009  | 36.0666  |
| CMS Webpage | January to May 2010  |  36.0791 |
| CMS Webpage | June to December 2010  |  36.8729 |

Table 6.5 Annual Physician Fee Schedules RVU conversion factor amounts--Carrier ($)

#### Carrier Cost Utilization Program

The program begins by merging in the physician fee schedule and adding RVU weights. About 25% of the claims are associated with a total RVU of 0. These are largely associated with Status Codes indicating statutory exclusions, excluded from physician fee schedule by regulation, or that the carriers themselves are supposed to price the code. For these HCPCS codes a weight is calculated as follows:

1. Calculate the median cost by HCPCS, HCPCS modifier code and year.
2. Divide that median amount by that years conversion factor to get a weight for the HCPCS, modifier, year combination
3. Assign that weight to the missing data

Also note that line items classified as facility/non-facility based are determined from the place of service codes where the values are defined at [this link](https://www.cms.gov/manuals/downloads/clm104c26.pdf).

The cost utilization amounts can now be defined by multiplying the conversion factor by the total RVU weight in the case where the RVU is not equal to zero. Cases where the RVU is equal to zero are set equal to the median reimbursement amount for the HCPCS/modifier code in a given year, as defined above. The following equation re-iterate this process.

$$
cost_{util} =
\begin{cases}
C^{CAR} \left( RVU_{hpcl}^W + RVU_{hpcl}^{PE} + RVU_{hpcl}^{PLI} \right) & if RVU \not = 0 \\
reimbursement_{year}^{median} & if RVU = 0
\end{cases}
$$

1. `ami05_RVUratio`: Generates line item levels cost utilization measure - `physician_cf_Q` corresponding to the cost utilization metric created using the conversion factor. Note that `physician_Q&los.` is generated by estimating a ratio for the conversion factor an is only included for checking purposes.
2. `ami05_HCPCS2costutil`: Generates a crosswalk file with all the relevant information. To assign physician_Q costs to any carrier extracts, first take all modifier codes that are not equal to `TC`, `53` or `26` and assign them a `MI` code. Next merge this file with the claims files based on the year of the second line item date (`sexpend2`), HCPCS code, modifier and place of service (`plcsvrvc`).

### Outpatient cost-utilization metric

Beginning in 2001, the Outpatient Prospective Payment System (OPPS) was introduced by CMS which uses a similar weight/conversion factor approach. The OPPS covers the outpatient hospital setting and covers a large amount of the claims in the outpatient claims file but there are still a significant amount of claims which the OPPS does not cover.

Some of the other payment systems/services found in the outpatient file but not covered by OPPS are described in the following list, a more complete description can be found in [AHIMA's Coding and Reimbursement for Hospital Outpatient Services](https://www.nber.org/medicare/public/unzipped/Auxiliary/AHIMA_ch1_OPPS.pdf) (the following list is based on the descriptions given there).

1. **Maryland Hospital Costs Containment Services**
2. **Indian Health Service Hospital Outpatient Services**: paid under separately established rates and are paid in the Federal register annually
3. **Critical Access Hospital (CAH) Outpatient Services**: They are paid under a reasonable cost-system
4. **Ambulance Services and Physical/Occupational/Speech Therapy** (status indicator=`A`): paid under a fee-schedule
5. **Services Already Paid For under Fee Schedule or Other Payment Systems** (status indicator=`A`): screening mammography, services for patients with end-stage renal disease (ESRD) that are paid for under the ESRD composite rate, laboratory services paid for under the clinical diagnostic laboratory fee schedule, and DME, prosthetics, orthotics, and supplies (DMEPOS), including prosthetic devices and implants, paid for under the DMEPOS fee schedule when the hospital is acting as a supplier of these items. See (AHIMA, 2005) for examples.
6. **Outpatients services furnished to SNF Inpatients**: If the care is part of their comprehensive care plan then SNF PPS covers these costs
7. **Inpatient Procedures**: procedures which CMS will only reimburse if they have occurred in an inpatient setting. CMS chooses these procedures because the it is not appropriate to preform them in an outpatients setting or because they are almost done in an inpatient setting. Inpatients of a Skilled Nursing Facility. See AHIMA documents for a full list of criteria CMS uses.
8. **Pre-admission Diagnostic and non-diagnostic Services**: Beginning January 1,1991 diagnostic and non-diagnostic outpatient services provided to a Medicare beneficiary by an admitting hospital within three days of admission are covered by Part A
9. **Ambulatory Surgery Centers (ASC)**[^52]

[^52]: A summary of changes to ASC payment rates made prior to CY 1998 may be found in the June 12, 1998 proposed rule (63 FR 32292). The 1998 rule proposed to rebase the ASC payment rates using cost, charge, and utilization data collected by a 1994 survey of ASCs. In that proposed rule, we also proposed to refine the rate setting methodology that was implemented in the February 8, 1990 Federal Register

The cost-utilization metric generated only covers the OPPS portion of the claims, the importance of the other payments systems will depend on the specifics of the study in question. For example, a researchers studying heart attacks and looking at 3 day costs will see that the ambulatory fee schedule plays an important role in describing total costs, and therefore the cost utilization metric created below, which only covers the OPPS, will miss a large portion of costs. Similarly, users looking at trends before 2001, should note that the OPPS started in 2001 and therefore our cost-utilization measure only starts in 2001.

#### Prospective Payment System (OPPS)

The mandate for an outpatient PPS systems can be found in the Omnibus Budget Reconciliation Act of 1986 (OBRA 1986) and the Omnibus Budget Reconciliation Act of 1990 (OBRA 1990). Over the next 14 years a series of different regulations were passed which prepared the the outpatient system for a PPS. The Balanced Budget Act of 1997 provided the implementation for such a system beginning January 1,1999. The Balanced Budget Refinement Act of 1999 made further changes to the impending OPPS system. However due to the concern around the Y2K computer bug, the implementation was pushed back to late 2000.(AHIMA, 2005).

Before the OPPS was implemented in late 2000, the outpatient claims were reimbursed using a charge based method, a fee-schedule or some blend of the two. The use of provider specific charges complicates estimating a utilization specific cost amount because geographic and provider specific differences in treatment and billing are mixed in the charges, leaving the researcher with the task of developing a method for separating the two. The methods discuses in the following section for separating policy adjustments from utilization costs are not valid for pre-OPPS data and is not covered by the methods discussed here. For more information about the OPPS and the the reimbursement systems used before the implementation of OPPS in the Outpatient files refer to the following RAND documentWynn (2005) . The remainder of the section will focus on the OPPS which was implemented in 2001.

An outpatient claim can be reimbursed through more then one Medicare payment system because Medicare reimburses for services in the outpatient files at the revenue center level, not the claim level. Since medicare reimburses at the revenue center levels, generating a cost utilization measure specific to a Medicare payment system requires working with costs and procedures codes (HCPCS) at the revenue center level.

The OPPS is reviewed in the following sections, broadly characterizing how reimbursements are calculated. The sections will describe specific aspects of the OPPS like identifying which claims fall under the OPPS and which do not. The OPPS analog to the Inpatient PPS DRGs are the ambulatory patient groups (APCs), a brief overview of APCs are also provided. Finally a general formula used to calculate OPPS reimbursements are reviewed.

RESOURCES ON OPPS:

- http://www.irp.com/apc/training/oppchap5.html#_Toc487605397
- Wynn (2005)
- AHIMA's Coding and Reimbursement for Hospital Outpatient Services
- MedPAC's OPPS payment basics documentation.
- CMS Internet Only Manuals (IOM)
- Grimaldi, Paul(2002). Medicare's Fee Schedule Hospital Outpatient Care. J Health Care Finance. 28(3) pg 14-31

Supplies	Critical care	Distinct parts of hospitals that are excluded under inpatient PPS	Implantable items	Limited follow-up services	Services furnished to SNF patients that are not packaged into SNF consolidated billing	Drugs, pharmaceuticals, and biologicals	Diagnostic services and other diagnostic tests	Certain preventive services furnished to healthy persons	Surgical procedures	Surgical pathology	Antigens, vaccines, splints, and casts	Radiology, including radiation therapy	Cancer chemotherapy	Partial hospitalization for the mentally ill	Clinic visits	Cancer hospitals	Inpatient procedures for patients who expire	Scheduled interdisciplinary team conferences	Cancer hospitals that are excluded from inpatient PPS	Observation services	Emergency department visits	Services for patients who have exhausted their Part A benefits

Table 6.6 Services covered by OPPS

For a list of services which are covered by OPPS, including a brief overview of the services please refer to AHIMA's Coding and Reimbursement for Hospital Outpatient Services. The regulation can also be referenced at the following link 42 CFR 419.22 - Hospital outpatient services excluded from payment under the hospital outpatient prospective payment system.

#### Overview of OPPS reimbursement policy

The OPPS calculates reimbursements by applying a conversion factor to the associated APC weights found in a HCPCS to APC crosswalk (Addendum B) [^53] The following equation describes the OPPS reimbursement policy where an $APC_{hpcr}$ occur at the $h$th hospital treating the $p$th patient corresponding to the $c$th claim and $r$th revenue center.

[^53]:  The APCs were created by 3M-Health Information Systems using a sample of Medicare outpatient claims. Using these claims, 3M aggregated codes into clinically related groupings which are also similar in cost intensiveness. For a more in-depth review of the particulars of how the APCs are constructed and the specific criteria used to create APC groups refer to AHIMA's Coding and Reimbursement for Hospital Outpatient Services.
Each APC is assigned a relative weight which represents the intensity of a specified treatment. The relative weights use a mid-level clinic visit (APC 601) as the denominator because it is one of the most frequently preformed services.

$$
\left( .60 \cdot C^{OPPS} \cdot W_h^L + .40 \cdot C^{OPPS} \right)
\cdot APCh_{hpcr} + Policy_{h}
$$

CMS assumes that 60% of the OPPS conversion factor, COPPS is associated with the labor portion of expenses. They apply a wage index associated with where the hospital is located,W Lh , to the labor portion of the conversion factor which depends on the specific hospital's geography. Next the adjusted conversion factor is multiplied by the APC weight. The conversion factor transforms the APC weight into a dollar amount. The last step is to add in any additional policy adjustments related to hospital specific characteristic, $Policy_h$. For more information see MedPAC's OPPS payment basics documentation and CMS Internet Only Manuals (IOM).

Note that the COPPS is updated on an annual basis in the OPPS Final Rule. The annual uprate is based on the inpatients market basket percentage increase applicable to hospital discharges and further adjusted to ensure budget neutrality.

While the reimbursement equation is fairly straightforward, there are various different rules which determine how exactly a procedure is reimbursed. The first complication involves determining which claims are covered by OPPS. The "status indicator" does this by classifying claims into categories explaining how they are reimbursed.

There are various places where the status indicator is available. The outpatient claims have a status indicator variable. CMS also publishes an annual HCPCs to APC crosswalk in the final rule under Addendum B. The crosswalk is useful in that it also includes status indicator codes as well as copayment amounts for every HCPCS code.

Coinsurance is another major portion of the OPPS which may be of interest in determining total costs. As of 2005, the standard 20% Medicare copayment amount was gradually applied to the OPPS copayment rates. For certain APC groups with a relatively high copayment compared to total payment, the policy was particularly worrisome for some outpatient facilities. As a result, CMS has established national copayment amount for each APC, as well as a minimum or floor price (equal to 20% of total payment). Hospitals are allowed to set the copayment amount between these two rates once a year and advertise these reduced rates. Note prior to the OPPS, coinsurance rates were based on charges not the actual amount reimbursed which lead to coinsurance rates making up a large portion of the total payment to providers.

In some cases, the OPPS has changed the way it reimburses for services which were qualified to receive transitional pass through payments, certain drugs which meet a cost threshold and for new technology where no charge/cost data is available to assign it to an APC. In most of these cases no relative weight is assigned to the appropriate HCPCS code in Addendum A or B. Instead a dollar amount is simply stated for that payment amount.

| Payment Type | Description |
|-|-|
| discount eligible HCPCS  |  Discount applied if several HCPCS codes which are eligible for a discount appear on the same revenue center.	 |
| pass-through payments HCPCS  | Implemented to ensure the transition to OPPS did not adversely impact providers, pass-through payments set to expire. DME and prescription drugs.  |
| average sales price   | Drugs which crossed a cost threshold were reimbursed according to the average sales price.	  |
| packaged HCPCS codes	  | A key feature of the OPPS is the use of packaging services to gain efficiencies. When an HCPCS code is packaged no weight is assigned.  |

Table 6.7 Payment type found in the claims files

#### Identifying OPPS claims, APC weights and conversion factors in the claims file

Determining which claims are covered by the OPPS is the first step to creating the cost utilization metric. CMS does this through the use of what they call status indicators. A status indicator is mapped to the claims files through the use Addendum B which is part of every final rule. The file is basically a crosswalk between HCPCS codes and APC codes with all of the relevant information.

Note that the outpatient claims have a variable “apchipps“ which should provide an APC for each revenue center observation. However in practice I have found that these variables are not very consistent with what is found in Addendum B. More specifically, the APCs found in `apchipps` and those found by merging Addendum B only have 60% correlation between 2001 and 2008. Looking at the annual correlations shows extremely inconsistent results. In addition, CMS also includes a variable for status indicators - `pmtmthd` - which shows several different status indicators for APCs found in `apchipps`. It appears that `apchipps` has a large majority of claims with a `0000` code which indicates that these revenue centers have been packaged — a `N` status indicator.

Addendum B is the key file necessary for identifying outpatient claims covered by the OPPS and also for defining the associated payment weight or payment amount for each APC. The file need only be merged with the HCPCS codes, a crosswalk from HCPCS code to relevant APC code, weight and payment rate. These files are used with the code provided for the OPPS to map HCPCS codes to APCs and status indicators.

In addition to Addendum B, the final rule published annually provides a complete description of the reimbursement changes in it entirety. Of specific interest are the conversion factors, COPPS 4↑, which are published annually in the final rules. However some caution needs to be used to ensure that the last final rule is used as they often go through several revisions which can be major[^54].

[^54]: One year Addendum B was miscalculated due to a programming error

Starting in 2009 CMS implemented the Hospital Outpatient Quality Data Reporting Program, which granted outpatient hospitals successfully reporting quality measures an additional reimbursement in the form of a higher conversion factor. We decided to use the unadjusted (reduced) conversion factor in the 2009 and 2010 years because our interest is in cost utilization, not in the added incentives in place.

| Source | Calendar Year | $C^{OPPS}$ ($)
|-|-|-|
| April 7, 2000 OPPS Final Rule  | 2000 | 47.583  |
| November 13, 2000 Interim Final Rule | 2001 | 49.596  |
| November 30, 2001 Final Rule | 2002 | 50.904  |
| CMS Website  | 2003  | 52.151  |
| CMS Website  | 2004  | 54.561  |
| CMS Website  | 2005  | 56.983  |
| CMS Website  | 2006  | 59.511  |
| CMS Website  | 2007  | 61.468  |
| CMS Website  | 2008  | 63.694  |
| CMS Website  | 2009  | 64.784  |
| CMS Website  | 2010  | 66.086  |

Table 6.8 Annual OPPS conversion factor amounts ($)

Also note that the status indicators descriptions are published annually under Addendum D.

#### SAS Program: Generating OPPS cost-utilization measures

A SAS program is included in the pack at [`CombineOPclms_revcenter.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_cost_utiladj/outpatient/calledMacroLib/CombineOPclms_revcenter.sas) to combine the claims and revenue center items. Next Addendum B is merged in with the HCPCS codes found in the outpatient file. Note that due to copyright restrictions placed on CPT codes used in Addendum B, the APCS weights are not redistributed as part of this code. Users need to download them from the CMS website.

In addition to importing Addendum B into a SAS file, the program also goes through and groups the HCPCS codes using the associated status indicator variables found in Addendum B into four categories indicated by the `costutiltype` variable. The following section describes how the cost-utilization measure is constructed for each group.
"Other payment system" HCPCS codes (`costutiltype = 0`)

As already discussed, the outpatient files have several different payment systems which reimburse revenue center claims. While the OPPS is the largest reimbursement system, this category deals with the costs which are not covered by the OPPS. It is defined as HCPCS code with an associated status indicator (variable name `si`) not in (`G`, `H`, `K`,`S`,`P`,`Q`,`T`,`V`,`X`,`N`). No cost adjustment is made of these type of claims and costs are used as is.
"Standard weight" HCPCS codes (`costutiltype = 1`)

HCPCS codes with a "standard weight" describe HCPCS codes for which a relative APC weight exists. Calculating cost-utilization measure for these claims is straightforward for the most part, with the exception of discounted claims discussed next. For non-discounted claims, the cost-utilization measure is calculated as follows
(6.9) costutil = COPPS⋆APChhpcr

One measure constructed `outpatient_Q`, ignore the discounting discused next and basically applies equation 9 to all the relevant claims. There are a handful of cases whose status indicator falls into this group but for which there are no relative weights or payment rates for these groups. These claims have a missing value assigned to the variables. The majority of these revenue centers do not report costs in the claims files.

The standard weight group also includes HCPCS codes which are eligible for a discount, indicated by a status indicator `T` code or by the `discountPossilbe` dummy variable. A discount only occurs if several HCPCS codes which are eligible for a discount appear on the same claim. In these cases, the APC weight is discounted per the OPPS rules which indicate that of all `T` HCPCS codes, the code with the max weight is reimbursed in full and the remaining HCPCS codes are reimbursed at 50% of the APC weight. The adjusted weight is stored in the `updatewght` variable and the unadjusted weight is stored in the `relwght` variable. These are coded into the program as outpatient_QTcode to allow user to compare the cost-utilization measures.
"Standard pay amount" HCPCS codes (`costutiltype = 2`)
"Standard pay amount" HCPCS codes have no relative weight, but do have a dollar amount associated with them which are still adjusted for geography. New technology is eligible to apply for pass-though status. In addition when technology first enters the OPPS, it is assigned to and APC within a given cost band. No relative weight is associated with this APC because not enough claims data has been collected for the given technology. As more information is gathered the technology is moved from the new technology cost band and placed in an appropriate APC category.

The new technology appears to be geographically adjusted upon comparison in the claims files. The new technology APCS are between the following number 0970-0997 before 2004, 1501 to 1574 between 2004 and 2005 and 1492 to 1574 in 2006 and beyond. . In these instances no estimated conversion factor is used, rather the payment rate amount found on Addendum B is used.
(6.10) costutil = payamount OPPShpcr
"unadjusted payment" HCPCS codes (`costutiltype = 3`)

Some HCPCS codes are "unadjusted" and cover prescription drugs and some pass-through payments. Prescription drugs are based on wholesale index and not wage adjusted. Some pass-through amounts are included in this category, however pass-through payments lie in a grayer area then prescription drugs in the sense that they are often cost-based, which means that their maybe some implicit geographic variation in these amounts. Codes falling into this category are not adjusted for cost utilization, some examples include new technology which is eligible for pass-through status. The actual amount reimbursed is used.

Initially prescription drugs were assigned there own relative weights in Addendum A and Addendum B, however in 2004 the PDMI was passed which changed the way in which reimbursement were calculated. Drugs which crossed a cost threshold were reimbursed according to the average sales price.

Prescription drugs do not receive a wage index adjustment but their administration does because they are coded and reimbursed separately. In addition prescription drugs do not receive an adjustment for a rural location. Note that the administration of a drug does not fall in this category. The following paper provides a good overview of recent changes http://www.nejm.org/doi/pdf/10.1056/NEJMp1110117. Note that the payment for drugs are not adjusted
$$
cost_{util} = fullreimb_{reported}^{OPPS}
$$
“Packaged Incidental service“ (`costutiltype = 4`)

These are revenue centers with a status indicator of `N` which means that their costs have been packaged into other revenue centers observations. Addendum B provides no relative weights for these HCPCS codes and in many cases these correspond to revenue centers found in the claims files with no HCPCS code. These are identified by using the status indicator variable `pmtmthd` found in the claims files. In some cases the claims do have an associated cost for the given, revenue centers. These costs are ignored in the `outpatient_Q` variable, its set to missing, because these costs are assumed to be some non-utilization costs as the documentation would suggest. Nonetheless this separate group is defined in the case an individual is interested in further looking into this group.
$$
cost_{util} = fullreimb_{reported}^{OPPS}
$$
“Inconsistent HCPCS codes “ (`costutiltype = 5`)

These codes are inconsistent in the sense that the revenue center claims files `pmtmthd` indicator variables denotes these claims as being covered by OPPS although their is no match for the HCPCS code in Addendum B. Closer inspection of the HCPCS codes shows that they are mostly C and G HCPCS codes. The C codes are temporary HCPCS codes and the G codes are for voluntary reporting of quality codes. This group makes up less then 1% of the claims and the total unadjusted costs are included in the `outpatient_Q` measures.
$$
cost_{util} = fullreimb_{reported}
$$
“No map from HCPCS codes to status indicator“ (`costutiltype = 6`)

These HCPCS codes have no status indicator in the claims files and also do not match to Addendum B and are therefore unsure how to deal with these claims. This group is only a handful of claims and is mostly made of HCPCS X codes. The total unadjusted costs are included in the `outpatient_Q` measures.
$$
cost_{util} = fullreimb_{reported}
$$

#### Final data sets

The final data set is created at the revenue center level and contains a variable `outpatient_Q` and `outpatient_QTcode`. Each variable is defined as described for each of the groupings above, with the exception the the latter is defined with discounted weights and the former does not account for discounted weights (`si = T`).

1. `ami05_OPPSq`: Generates revenue center level cost utilization measure - `outpatient_Q` corresponding to the cost utilization metric created using the conversion factor. Note that `costutiltype` variable defines how the `outpatient_Q` variable is defined.