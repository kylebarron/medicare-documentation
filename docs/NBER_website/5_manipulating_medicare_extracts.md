# Manipulating the Medicare extracts in SAS

## Overview

Once the claims associated with the index events have been extracted for a given window, there is still some processing of the data which needs to occur before it is ready for analysis. The following sections describes SAS programs which

1. Extract procedures from both the part A and part B claims,
2. Summarize costs for all claims and
3. Extract MedPAR based comorbidities using a 1 year look back.

## Identifying Procedures

Due to the structure of Medicare billing, when looking at procedures it is necessary to look at claims across the MedPAR, Outpatient and Carrier files. Physician services are covered under part B and in most cases are billed by physician/group practices/employers to Carriers regardless of place of service or procedure performed, however it is possible for physician services to appear in the Outpatient file. There are some other cases where physicians may bill Medicare under part A[^33]. The following section outlines an algorithm for capturing procedures across all claims and additionally enforces several checks about the location where physicians files their claims.

[^33]:  Two specific examples I have come across are the following

    1. Since July 2001, critical access hospitals (CAH) have had the option of submitting combined bills with physicians who perform procedure in the CAH, however physicians have the option to opt out of this and
    2. Some services performed by internists and residents in teaching programs may become part of the hospital reimbursement under part A. For more information on the current law, refer [here](http://www.aapa.org/advocacy-and-practice-resources/issue-briefs/505-medicares-final-rule-on-billing-requirements-for-teaching-physicians-the-effect-of-the-rule-on-physician-assistants).

Next some issues with using the MedPAR file to identify procedures are discussed and the algorithm for identifying procedures across all claims files is presented.[^34] Despite the the focus on AMIs, the code can easily be extended to another procedure code grouping of interest.

[^34]:  Based on email correspondence with ResDAC staff. Additional documentation can be found below at: [information on physician billing](http://www.medpac.gov/documents/MedPAC_Payment_Basics_07_Physician.pdf) and also at the [CMS manual for physician billing](http://www.cms.hhs.gov/manuals/downloads/clm104c12.pdf)

Relying on the MedPAR file to identify procedure utilization has a few shortcomings. First, while identifying procedures is relatively straightforward, determining precisely when they occurred is more complicated. The MedPAR records contain a procedure date field corresponding to each procedure code field. Furthermore, McClellan (1993) indicates that even the dates that are present may be unreliable. Consequently, this script follows McClellan (1993) in simply dating procedures to the start of the hospitalization during which it was performed. While this approach should yield dates that are typically correct within a couple of days, it may be problematic for some uses of the data.

Second, relying solely on the MedPAR record will miss any procedures that occur outside a hospital's inpatient department. In recent years, a few percent of catheterization and PCI procedures have occurred in hospital outpatient departments, rather than inpatient departments. [^36]

[^36]: The outpatient records also show a handful of CABG surgeries, which is more surprising. While it is possible that these surgeries reflect coding errors, the claims typically have corresponding physician claims, suggesting that they represent real procedures. In addition, the claim start and end dates are typically a few weeks apart, which is highly atypical for outpatient claims, but consistent with the recovery period from bypass surgery.

As a result, a pair of SAS scripts has been developed to address both of these problems by incorporating outpatient and physician claims data into the MedPAR data. The physician claims data are useful because, when a physician performs a surgical procedure, the physician obtains payment via a Part B physician claim. Physician claims must include the date of the procedure performed and, hence, may provide more precise information on procedure dates than MedPAR (or outpatient) records. In particular, dates are almost never missing on the physician records.

The script [`Step1_tagProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step1_tagProcs.sas) identifies all relevant procedures in the MedPAR, physician, and outpatient claims records. The program reshapes the MedPAR and outpatient claims from a wide, with 6 procedures per observation, into a long format which has one procedure code per observation. The data output from this script can have several procedure types (e.g. cath) tagged for an associated index event since the script simply takes a grouping of procedure codes and then applies a procedure tag. For example, the codes associates several type of ICD-9-CM and HCPCS procedure codes with a "cath" procedure. If an in individual stay has several of these associated "cath" codes, each separate code is tagged as a separate cath procedure in the code.

Another data issue arises for a very small percent of cases where there appears to be a transfer[^37] on the date of the procedure. The result is that there are two claims with the same procedure code and date. We simply drop one of these cases.

[^37]: A transfer in the sense of a separate observation in the MedPAR file, each observation is supposed to capture a hospital or SNF stay. See Section 1 for more information.

Procedures on the MedPAR files are identified using the same set of ICD-9-CM codes described above. Procedures in physician claims are identified using the CPT (HCPCS) codes listed in Lucas et al. (2006) as well as older CPT codes obtained by searching through old CPT manuals. As noted above, the outpatient files report both ICD-9-CM and CPT (HCPCS) procedures codes over much of the period, and neither set of codes seems to provide a comprehensive accounting of the procedures reported on the claim. Consequently, the code uses both ICD-9-CM and CPT codes to identify outpatient procedures.

This script uses ICD-9-CM procedures codes in the MedPAR extract to identify which individuals underwent the following four procedures (or groups of procedures):

1. **Cardiac catheterization and coronary angiography.** Catheterization and angiography are typically part of the same procedure, and precisely which code appears on a record seems to vary arbitrarily, so they are grouped together. For simplicity, the script simply refers to this category as "cath." The script uses the ICD-9-CM codes used in the 2008 [Dartmouth Atlas of Health Care](http://www.dartmouthatlas.org/faq/SxICD9codes.pdf) to identify this group. The script also assumes that catheterization occurred if PCI or CABG occurred, even if the record does not include an explicit code for catheterization.[^40] With PCI, the procedure itself involves catheterization, so this is a safe assumption. In the case of CABG, some type of catheterization typically occurs in advance of or as part of the CABG procedure.

[^40]: This could occur because the hospital did not code all procedures performed or because there was not enough room on the MedPAR record to code all procedures.

2. **Percutaneous coronary interventions (PCI) with or without stent insertion.** This category includes both coronary angioplasty and coronary atherectomy.[^41] Again, the script uses the ICD-9-CM codes from the Dartmouth Atlas for details, see the NHCS ICD-9-CM conversion table referenced in Section 1.

[^41]: It is not possible to focus solely on angioplasty since each ICD-9-CM code for angioplasty also covers atherectomy.

3. **PCI with stent insertion.** To identify stent insertion, the script uses two ICD-9-CM codes: 3606 and 3607.
4. **Coronary artery bypass graft (CABG) surgery.** The script uses the ICD-9-CM codes from the Atlas.

The script [`Step2_matchProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step2_matchProcs.sas) takes the output of this last script and attempts to integrate the physician, MedPAR, and outpatient claims. The SAS program attempts to reconcile all the records by first implementing an exact matching scheme across all the claims. Next a fuzzy match algorithm is used to match carrier procedures which fall within claim end and start date on the institutional claims. The remaining unmatched carrier claims are discarded and any unmatched MedPAR or outpatient procedures are kept in the file.

While the different sources of information match in the sizable majority of cases, there are some inconsistencies. This script generates a variety of information that allows more detailed analysis of these inconsistencies.

Coping with the discrepancies requires understanding why they are occurring. There are a variety of possible explanations[^42]. One possibility is that the set of ICD-9-CM or CPT codes used to identify procedures may be incomplete. Investigating this possibility is the subject of ongoing work, but direct examination of physician and inpatient claims in cases of discrepancies has not yet unearthed obvious additional codes to include. Instead, it appears that there are deficiencies in the claims record themselves.

[^42]: In addition to the explanations given below, a small number of the discrepancies arise from a purely mechanical feature of the data set. Recall that MedPAR claims are included only if the discharge date comes within one year of AMI. Consequently, a procedure conducted during a hospital stay that starts less than a year after AMI but concludes more than a year after AMI will not appear in the MedPAR extract, but may appear in the physician extract. Even after accounting for this mechanical effect, however, the bulk of the discrepancies still remain.

The deficiencies in the underlying claims records may take a variety of forms. One possibility is that institutions or physicians sometimes fail to report all relevant procedure codes. There are, for example, many cases in which MedPAR records fail to list any procedure codes at all, even when it seems likely that some procedure occurred during the stay. Conversely, the six procedure fields on the MedPAR record sometimes fill up completely. In either case, the MedPAR record will not include all procedures that actually occurred during the stay. Similarly, it appears that physicians sometimes fail to file claims for all or part of a procedure. For example, there are a moderately large number of cases where there is MedPAR record showing a bypass surgery and a corresponding physician claim for some related procedure (e.g. heart procedure anesthesia), but no claim for the bypass itself.

Alternatively, providers may be reporting incorrect dates. Even if both the institution and the physician reported the procedure, if one or both of them reports an incorrect date, then it will be difficult or impossible to match the procedures together.

It is probably impossible to perfectly reconcile to the two sets of records. However, the following set of assumptions, allow a reconciliation that is likely approximately correct:

1. All procedures reported actually occurred (with the possible exception of some bypass surgeries reported as occurring in outpatient hospital facilities). That is, in general, they are not the result of coding errors or fraud.
2. Both physicians and institutions sometimes fail to report procedures.
3. All hospital admission and discharge dates reported on MedPAR records are correct, but the procedure dates may be incorrect. (Since admission and discharge dates can factor directly into payment, this seems like a plausible assumption.)
4. Procedure dates reported on physician records are correct, except when there is clear evidence to the contrary (e.g. a patient does not appear to have been hospitalized on a day when he supposedly underwent bypass surgery).
5. Missing procedure dates are assigned to the claim admission date for MedPAR and outpatient cases.

The last portion of [`Step2_matchProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step2_matchProcs.sas) uses these assumptions to generate variables that indicate whether or not an individual has had a given procedure within 1, 3, 7, 30, 90, or 180 days after AMI. The script starts with the universe of physician-reported claims. It then:

1. Keeps any physician-reported procedure that falls between the start and end date of a MedPAR or outpatient claim that also reports that procedure. These procedures are dated at the date reported on the physician claim. This case covers upwards of 90 percent of all procedures.
2. Keeps physician-reported procedures that fall during a period when the individual was hospitalized, even if that hospitalization contains no record of the procedure. These procedures are also dated at the date reported on the physician claim.
3. Drops all other physician-reported claims.
4. Adds on any claims from the outpatient or MedPAR file that were not matched to a physician claim in step #1, with the exception of outpatient claims that report bypass surgery. Where possible, these claims are dated using the procedure date reported on the MedPAR or outpatient record. If this date is not present or falls outside of the period defined by the start and end date of the claim, then the procedure is dated at the start of the claim or hospitalization.

Using the resulting list of procedures and dates, it is then straightforward to compute which individuals have undergone which procedures at various time horizons.

The [`Step1_tagProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step1_tagProcs.sas) program creates the following files, assuming a 5 percent AMI extract was run using `bene_id`s and the principal diagnosis only:

1. `ami05_carpull`: Reshapes the claims from the carrier files, tags all procedures with relevant procedure tag
2. `ami05_mppull`: Reshapes the stays from the MedPAR files, tags all procedures with relevant procedure tag
3. `ami05_oppull`: Reshapes the claims from the OP files, tags all procedures with relevant procedure tag
4. `ami05_oprevpull`: Reshapes the revenue center claims from the OP files, tags all procedures with relevant procedure tag

The [`Step2_matchProcs.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/xday_flag_procedures/Step2_matchProcs.sas) program creates the following files, assuming a 5 percent AMI extract was run using `bene_id`s and the principal diagnosis only:

1. `ami05_procedures`: Aggregates procedure information to the index level and creates index level variable indicating how many days after the index event and individual had a procedure.

## Comorbidities

It is often useful to know whether a patient experiencing an AMI has other conditions, in addition to an AMI. There are several different ways of estimating a comorbidity profile for individuals of interests. Most studies rely on claims from the year preceding the index event in order to avoid incorrectly assigning a complication of the diagnosis as a comorbidity.

Relying on the ~15,000 ICD-9-CM codes is simply not useful from a risk-adjustment perspective because they create relatively flat comorbidity profiles, leaving little variation to risk adjust against. As a result, several disease classifications have been developed over the years to help adjust for other preexisting conditions with respect to some outcome of interest. Although many of these classifications initially were not developed for use with administrative data sets (claims), they have been used or adjusted for such settings. An example of some of the comorbidity classifications available are the Charlson, the Deyo-Klabunde and Romano adaption of the Charlson, CCS codes, the Elixhauser and CMS- Hierarchical Condition Category (HCC).

These groupings often create a risk adjustment index, by using subjectively assigned weights to separate diseases. In many instances the code is available, one such example is the Deyo and Romano adaptation of the Charlson index available here http://healthservices.cancer.gov/seermedicare/program/comorbidity.html.

Risk-adjustment is an important aspect of an objective assessment of health care costs/measures, Klabunde et al. (2000) argue for the case of including part B claims in creating a more complete comorbidity profile of the cohort. The drawback to using part B claims is a result of the inaccuracy of the claims. In addition there is what is known as "rule out" claims, in which doctors bill for tests and time they use to "rule out" a diagnosis. While the included code does not experiment with using the part B claims, a new user should be aware that it is possible to use them as long as these issues are accounted for.

The approach followed is that of Krumholz et al.(2007) which originally made use of the CMS-HCC codes developed by Pope et al. (2004). The HCC is used by the CMS to risk adjust their reimbursements and was originally used by the government's fairly new initiative of creating objective quality risk-adjusted health measures for hospitals found at http://www.qualitynet.org. Full documentation of their methods, ICD-9-CM and procedure code is available on the website. In addition all the code they use can be obtained by requesting the SAS pack from the mortalitymeasures@mathematica-mpr.com.

The HCC aggregates the ICD-9-CM into around 800 DxGroups from which the codes are further aggregated to create the PIP-DCG Clinical Classification, which was CMS's first attempt to risk adjust Medicare payments given the data available (Pope et al.(2004). Using a different aggregation, the DxGroups are used to create the 189 clinically relevant CCs and hierarchies are imposed to create HCCs. CMS currently uses a subset of the HCCs to risk adjust Medicare payments[^43] and originally used the full list of HCC codes to risk adjust different quality measures at http://www.qualitynet.org[^44].

[^43]: [ https://www.cms.gov/MedicareAdvtgSpecRateStats/06_Risk_adjustment.asp]( https://www.cms.gov/MedicareAdvtgSpecRateStats/06_Risk_adjustment.asp)
[^44]: The code can be found on the CMS Risk Adjustment website [here](https://www.cms.gov/MedicareAdvtgSpecRateStats/06_Risk_adjustment.asp). The macro with the code of interest is called `V12H70H` under the 20XX RxHCC model sotfware.

More recently the Krumholz group has updated the methodology used to risk adjust the mortality measures, choosing to use the Condition Categories (CC) without the hierarchies imposed. The hierarchies were not used because they were originally developed to risk adjust expenditures, and ensure that more severe manifestations of a disease cancel the effect of less serious ones.[^45] For studies not interested in costs, imposing these hierarchies causes a loss of information. The current code uses the CC's but also includes the HCC's hierarchies commented out and taken from CMS's risk adjustment software in case an individual is interested in using HCCs.

[^45]: [ 2009 Measures Maintenance Technical Report: Acute Myocardial Infarction, Heart Failure, and Pneumonia 30-Day Risk-Standardized Mortality Measures.](http://www.qualitynet.org/dcs/ContentServer?c=Page&pagename=QnetPublic/Page/QnetTier3&cid=1163010421830)

Use of the CC's allows individuals to aggregate the codes further into comorbidities relevant for the issue at hand. We use the comorbidity aggregations for AMI and CHF events found in Krumholz et al.(2007). Note that the CC to ICD-9-CM crosswalk were downloaded from the http://www.qualitynet.org site by searching for ICD-9-CM to CC crosswalk. A copy of the files used are found here. The SAS program which computes the comorbidities is found here [`ExtComorbidCC.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/last_yr_comorbid/ExtComorbidCC.sas) and classifies the diagnosis codes using the system of CCs. A detailed description of the CC and HCC system is available from Pope et al. (2004) and the code used to risk adjust for outcomes and payment are freely available on the web.

The program processes MedPAR claims although it could easily be extended to deal with Part B claims as well. The program restricts itself to all hospital stays which occur prior to the index event, given the previous caveats. The program does not look to separate the case where an individual occurs twice as an index event. Cases where this does occur results in an instance where some claims occurring after the first index event but before the second index event are interpreted as comorbidities when it is possible that they may be long-term complications.

With that warning, the program proceeds by first transforming the data from a wide format, with ten diagnosis codes per claim, into a long form with one diagnosis per claim. Next the diagnosis codes are merged with the CC crosswalk and the CC's are aggregated into clinically relevant groups. Finally the code aggregates the information to the index level.

The [`ExtComorbidCC.sas`](https://www.nber.org/medicare/public/unzipped/2create_index_level_measures/last_yr_comorbid/ExtComorbidCC.sas) program creates the following files, assuming a five percent AMI extract was run using `bene_id`s and the principal diagnosis only:

1. `ami05_medpar_cc`: Aggregates comorbidity information to the index level and aggregates the CC codes into more general categories. Binary variables are created for the HCC groupings following aggregations used by Krumholz et al (2007)

##  Assigning geographic locations to provider and/or beneficiaries

Assigning locations to provider IDs is not as trivial as one might first suspect. To this avail this section provides code to help individuals assign providers to HRR zones, where only provider zip codes are needed. The second section, takes this process further and provides geocoded data for many of the provider numbers found in the MedPAR data. Geocodes have been assigned through an iterative process fully described in the Appendix C↓. This subsection will give a general overview of the data.

Mapping provider or beneficiaries to the Dartmouth Atlas geography is done through the use of annual crosswalks available on their website which links a zip code to to an HSA or HRR. The difficulty is often in extracting the zip codes from the Medicare data at the provider or beneficiary level in order to be able to apply the crosswalk. The main difficulty is in getting the provider zip codes which are not available in the Medicare claims but are found in the provider of service files (POS). The following 2 sections cover the programs and specific difficulties in much more detail.

For projects interested in geocoded provider information the last section provides a brief overview of the algorithm developed to geocode the provider, along with necessary assumptions imposed. The appendix goes into full detail about the specific programs and each step.

The programs which generate the Dartmouth crosswalk files can be found [here](https://www.nber.org/medicare/public/unzipped/0pre_process/darthmouthHRRxw/MasterHRRCross.do) and require both SAS and Stata to run.

### Assigning beneficiaries to the Dartmouth Atlas Geography

The process of assigning beneficiaries to Dartmouth Atlas geography is done by taking the zip code for each beneficiary found in the annual denominator files and using the Dartmouth crosswalk to code in the correct geography.

Researchers working on the NBER servers can find a file for the population of beneficiaries derived from the denominators files on the servers. These file include annual zip code and demographics along with codes for Dartmouth Atlas geography. Note that the Dartmouth Atlas does not cover foreign countries or commonwealth of the United States. There are also some case for which no zip code match is found.

The program which generates the files can be found at [`CreatePopDenominatorFile.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/enroll_denomFiles/CreatePopDenominatorFile.sas)

### Assigning providers to the Dartmouth Atlas Geography

Provider numbers uniquely identify different types of institutional providers of care (think inpatient or outpatient type setting). The type of entity associated with a provider number are embedded in the last 4 digits of the provider number. Different number ranges are assigned to different provider types, which means that institutions that change provider type correspondingly receive a new provider number. The new and old provider identifiers are cross referenced in the [Provider of Services files](http://www.cms.gov/NonIdentifiableDataFiles/04_ProviderofServicesFile.asp), but the quality of such cross-references has not been verified. Lastly, the physical location associated with provider numbers are not found in the institutional files, but the addresses are found in the provider of service (POS) files and is the main source of all geographic information regarding specific providers.

The POS file is no exception to the quirkiness of working with the Medicare data. Visual inspection of the data identifies some conflicting information and the fact that the POS is updated in a different month relative to the Medicare claims files means that not all providers in a given year will be found in the POS file.

The Dartmouth Health Atlas created a provider ID to HRR crosswalk for 2005 and 2007. The problem with using this crosswalk when claims have been pooled annually into a longitudinal type extract, is that the definition of HRR to zip codes could have changed over time to account for changing population concentrations. Extracts which rely on claims prior to 2005, will need to deal with crosswalks associated with each year.

Individuals working with claims prior to 2005 will need to use the annual zip code to HRR crosswalk available from the Dartmouth Atlas website. The process is complicated by the fact that provider zip codes are not available from the MedPAR files and needs to be merged in from the POS file. Information about the POS is available [here](https://www.cms.gov/NonIdentifiableDataFiles/04_ProviderofServicesFile.asp).

Several programs have been developed to aid in mapping Provider ID to HRRs. The NBER currently holds POS files in a un-harmonized text format which need to be imported into SAS or Stata format before using them. The process is time consuming because it requires looking up the correct variable of interests in the code book and adding them to the dictionaries. Currently a subset of the total variables are being used, although adding extra variables to the extract is straightforward.

In addition, the POS file is updated in a different month then the claim files which leaves the possibility that provider in some years of the claims files are not found in some years of the POS. [`importPOS.sas`](https://www.nber.org/medicare/public/unzipped/Auxiliary/POS/importPOS.sas) is a program which handles many of the problems discussed here while importing the files into SAS. Once the POS file is updated, next the HRR crosswalks are stacked on top of each other and tagged with year in the [`MasterHRRCross.do`](https://www.nber.org/medicare/public/unzipped/Auxiliary/HRR/MasterHRRCross.do) program using HRR crosswalks downloaded from the Dartmouth Atlas web page.

Finally the SAS program [`FixYearDifferencesBetweenMedpar.sas`](https://www.nber.org/medicare/public/unzipped/0pre_process/providerOfService/FixYearDifferencesBetweenMedpar.sas) takes the provider of service files and merges it with the MedPAR file while applying a series of edits to the addresses. Merging the files with the MedPAR files allows for the correction of certain providers for which no POS observation is available in a given year due to a difference in when the survey is given/updated. Lastly this script takes the data set generated by MasterHRRCross.do and merges it with the provider zip codes to create a provider, year crosswalk to HRRs.