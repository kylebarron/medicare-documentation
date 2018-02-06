# Glossary

- ASC: Ambulatory Surgical Center
- BSF: [Beneficiary Summary File](resdac/mbsf)
- CCW: Chronic Conditions Data Warehouse
- CMS: Centers for Medicare and Medicaid Services
- CPT: Current Procedural Terminology code set. The CPT is a set of codes used for medical billing and is maintained by the American Medical Association (AMA). Each CPT code has a corresponding short and long description. The codes and short descriptions are distributed by CMS, whereas the AMA holds copyright over the long descriptions. See the codes section of the documentation for more detail.

    The CPT forms "Level 1" of the [Health Care Common Procedure Coding System (HCPCS)](NBER_website/2_Background/#health-care-common-procedure-coding-system-hcpcs).

- CY: Calendar Year
- DME: [Durable Medical Equipment](resdac/dme-rif)
- HCPCS: Healthcare Common Procedure Coding System. The HCPCS is a set of codes used for medical billing. The CPT forms "Level 1" of the HCPCS.

    Datasets with HCPCS codes and short descriptions are freely available on the CMS website in their [Relative Value Files](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/PhysicianFeeSched/PFS-Relative-Value-Files.html). In the `RVU15A.zip` file, for example, the `PPRRVU15_V1223c.csv`, `PPRRVU15_V1223c.txt`, and `PPRRVU15_V1223c.xlsx` files contain an `HCPCS` variable with the code and a `DESCRIPTION` variable with the short description. These CMS files are released under the [End User Point and Click Agreement](https://www.cms.gov/apps/aha/license.asp?file=/Medicare/Medicare-). [^8]

[^8]: [https://github.com/jackwasey/icd/issues/81#issuecomment-217017528](https://github.com/jackwasey/icd/issues/81#issuecomment-217017528)

- HHA: [Home Health Agency](resdac/hha-rif)
- HIPAA: Health Insurance Portability and Accountability Act of 1996
- HISKEW: Health Insurance Skeleton Eligibility Writeoff
- LDS: Limited Data Set
- MA: Medicare Advantage
- MAX: Medicaid Analytic Extract
- MDS: Minimum Data Set
- NCH: National Claims History
- NPI: National Provider Identifier
- PPS: Prospective Payment System
- ResDAC: Research Data Assistance Center. Unit of the University of Minnesota tasked with providing support to the research community using Medicare data.
- RIF: Research Identifiable File
- SNF: [Skilled Nursing Facility](resdac/snf-rif)
- UPIN: Unique Provider Identification Number
