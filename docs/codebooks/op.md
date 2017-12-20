# Outpatient data

## Claims data

`desc using op01_clms_raw_2012`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `tot_chrg` | double | %12.0g   | total charges |
| `pmt_amt`  | double | %12.0g   | total payment |
| `benepmt`  | double | %12.0g   | beneficiary payment |
| `prvdrpmt` | double | %12.0g   | provider payment |
| `ptb_ded`  | double | %12.0g   | part b deductible |
| `ptb_coin` | double | %12.0g   | part b coinsurance |
| `blddedam` | double | %12.0g   | blood deductible |
| `prpayamt` | double | %12.0g   | primary payer payment |
| `from_dt`  | long   | %tdD_m_Y | Claim start date |
| `thru_dt`  | long   | %tdD_m_Y | Claim end date |
| `state_cd`   | str2   | %2s      | beneficiary state |
| `cnty_cd`    | str3   | %3s      | beneficiary county |
| `zip_cd`     | str9   | %9s      | beneficiary zip |
| `prcdr_dt1`-`25`|  long | %tdD_m_Y | ICD9 Procedure date #1 |
| `icd_dgns_cd1`-`25`|  str5 | %5s | diagnosis codes #1 |
| `icd_dgns_vrsn_cd1`-`25`|  str1 | %1s | ICD9 or ICD10 Procedure codes #1 |
| `icd_prcdr_cd1`-`25`|  str7 | %7s | ICD9 Procedure codes #1 |
| `icd_prcdr_vrsn_cd1`-`25`|  str1 | %1s | ICD9 or ICD10 Procedure codes #1 |
| `provider`     | str6  | %6s    | Provider number |
| `prstate`      | str2  | %2s    | Provider state code |
| `at_upin`      | str6  | %6s    | Attending physician UPIN |
| `op_upin`      | str6  | %6s    | Operating physician UPIN |
| `ot_upin`      | str1  | %1s    | Other physician UPIN |
| `at_npi`       | str10 | %10s   | Attending physician NPI |
| `op_npi`       | str10 | %10s   | Operating physician NPI |
| `ot_npi`       | str10 | %10s   | Other physician NPI |
| `orgnpinm`     | str10 | %10s   | Organization physician NPI |
| `no_paycd`     | str2  | %2s    | Claim Medicare No-Pay reason code |
| `linecnt`      | byte  | %8.0g  | Number of revenue center codes |
| `bene_id`      | str15 | %15s   | Encrypted 723 Beneficiary ID |
| `clm_id`       | str15 | %15s   | Encrypted Claim ID |
| `opclmrawindx` | long  | %12.0g | OP raw obs clms: unique with fileyear part and diag_id |
| `part`         | byte  |  %8.0g | |
| `ehic`         | str1  |  %1s | |
| `fileyear`     | int  |   %8.0g | |

## Revenue Center data
`desc using op01_rev_raw_2012`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `rev_dt`    | long   | %tdD_m_Y | Revenue center date |
| `cntrindex` | int    | %8.0g    | Rev variable # obs comes from |
| `revpmt`    | double | %12.0g   | Rev Center amount reimbursed |
| `rev_chrg`  | double | %12.0g   | Rev Center charge amt |
| `revblood`  | double | %12.0g   | Rev Center blood deductible amt |
| `revdctbl`  | double | %12.0g   | Rev Center deductible amt |
| `wageadj`   | double | %12.0g   | Rev Center coin/wage adjusted coin |
| `rdcdcoin`  | byte   | %8.0g    | Rev Center reduced coin |
| `rev_msp1`  | double | %12.0g   | Rev Center secondary payer amounts #1 |
| `rev_msp2`  | double | %12.0g   | Rev Center secondary payer amounts #2 |
| `rev_unit`  | long   | %12.0g   | Rev Center unit amount |
| `rev_rate`  | double | %12.0g   | Rev Center rate |
| `rev_ncvr`  | double | %12.0g   | Revenue Center Non-Covered Charge Amount |
| `hcpcs_cd`  | str5   | %5s      | Revenue center HCPCS code |
| `mdfr_cd1`  | str2   | %2s      | Revenue center HCPCS modifier #1 |
| `mdfr_cd2`  | str2   | %2s      | Revenue center HCPCS modifier #2 |
| `rev_cntr`  | str4   | %4s      | Revenue center code |
| `apchipps`  | str5   | %5s      | Revenue center APC code |
| `pmtmthd`   | str1   | %1s      | Rev Center payment method indicator |
| `packaging` | str1   | %1s      | Rev Center packaging indicator |
| `rndrng_physn_npi` | str10 | %10s | Revenue Center physician NPI |
| `rndrng_physn_upin` | str1  | %1s | Revenue Center physician UPIN |
| `mdfr_cd3`        | str1  | %1s | Revenue center HCPCS modifier #3 |
| `mdfr_cd4`        | str1  | %1s | Revenue center HCPCS modifier #4 |
| `mdfr_cd5`        | str1  | %1s | Revenue center HCPCS modifier #5 |
| `pricng`          | str1  | %1s | Revenue center pricing indicator |
| `bene_id`         | str15 | %15s | Encrypted 723 Beneficiary ID |
| `clm_id`          | str15 | %15s | Encrypted Claim ID |
| `diag_id`         | byte  |  %8.0g | |
| `ehic`            | str1  |  %1s | |
| `oprevrawindx`    | long  |  %12.0g | OP raw obs revnue: unique with fileyear part and diag_id |
| `part`            | byte  |  %8.0g | |
| `fileyear`        | int   |  %8.0g | |

