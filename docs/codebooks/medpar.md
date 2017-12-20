# MedPAR file


`desc using medpar01_raw_2011`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `bene_id` | str15 | %15s | Beneficiary encrypted id number (new individual unique identifier) |
| `state_med`       | str2   | %2s        | Patient state of residence at admission|
| `county_med`      | str3   | %3s        | Patient county of residence at admission|
| `zip_med`         | str5   | %5s        | Patient zip of residence at admission|
| `src_adms`        | str1   | %1s        | Source of admissions|
| `type_adm`        | str1   | %1s        | Type of admissions|
| `sslssnf`         | str1   | %1s        | Short stay/long stay/SNF indicator|
| `dschrgcd`        | str1   | %1s        | Discharge status code|
| `dstntncd`        | str2   | %2s        | Discharge destination code|
| `pps_ind`         | str1   | %1s        | Prospective payment status|
| `ad_dgns`         | str6   | %6s        | Admitting diagnosis|
| `dgnscd1`-`25`      |    str5 | %5s     | Diagnosis code #1|
| `dgns_vrsn_cd_1`-`25`|  str1 | %1s     | Flag icd-9 or icd-10|
| `prcdrcd1`-`6`      |   str4  | %4s      | Procedure code #1|
| `drg_cd`          | str3   | %3s        | DRG code|
| `outlr_cd`        | str1   | %1s        | Outlier status code|
| `prpay_cd`        | str1   | %1s        | Type of primary payer|
| `prvnumgrp`       | str6   | %6s        | Institution provider identifier number|
| `spclunit`        | str1   | %1s        | Institution type alpha-numeric code|
| `admsndt`         | long   | %tdD_m_Y   | Admission date|
| `dschrgdt`        | long   | %tdD_m_Y   | Discharge date (missing values filled with LOS+admit)|
| `acrtndt`         | long   | %tdD_m_Y   | Date claim was added to CMS master file|
| `outlrday`        | byte   | %8.0g      | Number of outlier days|
| `loscnt`          | int    | %8.0g      | Length of stay|
| `coin_amt`        | long   | %12.0g     | Patient coinsurance amount|
| `ded_amt`         | int    | %8.0g      | Patient deductible amount|
| `blddedam`        | int    | %8.0g      | Patient blood deductible amount|
| `prpayamt`        | long   | %12.0g     | Non-Medicare primary payer amount|
| `outlramt`        | long   | %12.0g     | Outlier payment amount|
| `disp_shr`        | long   | %12.0g     | Disproportionate share payment|
| `ime_amt`         | long   | %12.0g     | Indirect medical education amount|
| `pps_cptl`        | long   | %12.0g     | PPS capital payment|
| `passthru`        | long   | %12.0g     | Bill pass-through payment amount|
| `pmt_amt`         | long   | %12.0g     | Total Medicare payment|
| `drgprice`        | long   | %12.0g     | Total all-payer payment w/o outlier payments|
| `dgnscnt`         | byte   | %8.0g      | Number of diagnosis code on record|
| `prcdrcnt`        | byte   | %8.0g      | Number of procedure codes on record|
| `prcdrdt1`-`6`      |   long  | %tdD_m_Y | Procedure date #1|
| `er_amt`          | long   | %12.0g     | Emergency room charge amount|
| `ehic`            | str1   | %1s        | Encrypted health insurance claim number|
| `outlrday_new`    | str1   | %1s        | Number of outlier days|
| `drg_cd_new`      | str1   | %1s        | DRG code|
| `mperdiem`        | byte   | %8.0g      | Cost report pass-through/per diem|
| `medrawindx`      | long   | %12.0g     | MedPAR raw indx unique with fileyear|
| `fileyear`        | int    | %8.0g      | Year of MedPAR file containing claim|
| `is_longhosp`     | byte   | %8.0g      | Long-term care inpatient facility|
| `is_shorthosp`    | byte   | %8.0g      | Short-term inpatient facility|
| `is_cah`          | byte   | %8.0g      | Critical Access inpatient facility|
| `is_psychhosp`    | byte   | %8.0g      | Psych inpatient facility|
| `is_rehabhosp`    | byte   | %8.0g      | Rehab inpatient facility|
| `prvstate`        | byte   | %8.0g      | Institution provider identifier state|
| `prvnum3`         | str1   | %1s        | Institution provider type number|
| `prvdrsrl`        | str4   | %4s        | Institution provider serial number|
| `is_snf`          | byte   | %8.0g      | Skilled nursing facility flag|
