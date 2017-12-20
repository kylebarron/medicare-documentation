
## Harmonized Files

### Denom_bene

#### `pop01_demo_bene_idcharvar1996`
pop01_demo_bene_idcharvar1996

| variable name | storage type | display format | variable label
|-|-|-|-|
| `sdod` | long | %tdD_m_Y | Date of death |
| `sdob` | long | %tdD_m_Y | Date of birth |
| `sex` | str1 | %1s | Sex |
| `race` | str1 | %1s | Race code |
| `v_dod_sw` | str1 | %1s | Valid Day of Death |
| `bene_id` | str15 | %15s | Encrypted beneficiary identifier (individual unique identifier) |

#### `pop01_demovars_long`
`desc using pop01_demovars_long.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| sdod            | long |  %tdD_m_Y | Date of Death |
| zipcode_de      | str9 |  %9s      | Zip Code |
| sdob            | long |  %tdD_m_Y | Date of Birth |
| ehic            | str11 | %11s     |  |
| fileyear        | int |   %8.0g    |   |
| state_de        | str2 |  %2s      | State |
| county_de       | str3 |  %3s      | County |
| sex             | str1 |  %1s      | Sex(1=M,2=F,0=Unknown) |
| race            | str1 |  %1s      | Race |
| v_dod_sw        | str1 |  %1s      | Valid Day of Death |
| bene_id         | str15 | %15s     | Encrypted CCW BENE_ID |
| bene_idinbene   | byte |  %8.0g    |             |
| bene_zipnob     | str9 |  %9s      |             |
| benezip_num     | long |  %12.0g   |             |
| benezip5        | str5 |  %5s      |             |
| benezip5_num    | long |  %12.0g   |             |


#### `pop01_demo_bene_id`
`desc using pop01_demo_bene_id.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `sdod`     | long  | %tdD_m_Y | Date of Death |
| `sdob`     | long  | %tdD_m_Y | Date of Birth |
| `fileyear` | int   | %8.0g | |
| `sex`      | str1  | %1s | Sex(1=M,2=F,0=Unknown) |
| `race`     | str1  | %1s   |                Race |
| `bene_id`  | str15 | %15s   |               Encrypted CCW BENE_ID |
| `ehic`     | str11 | %11s | |
| `hsex`     | str1  | %1s     |              Sex(1=M,2=F,0=Unknown) |
| `hrace`    | str1  | %1s      |             Race |
| `hddate`   | long  | %tdD_m_Y  |            Date of Death |
| `hbdate`   | long  | %tdD_m_Y   |           Date of Birth |
| `buyin1984m1`-`buyin2013m12` | str1 | %1s | |
| `hmoind1992m1`-`hmoind2013m12` | str1 | %1s | |

#### `popPCT_demo_bene_idYEAR`
`popPCT_demo_bene_idYEAR.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `bene_id`   | str15  | %15s  |   Encrypted CCW BENE_ID  |
| `buyin2011m1`-`buyin2011m12` | str1 | %1s |  |
| `hmoind2011m1`-`hmoind2011m12` | str1 | %1s |  |


#### `pop01_demovars_wide`
`desc using pop01_demovars_wide.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| `ehic`            | str11   | %11s | |
| `county_de`       | str3    | %3s | County |
| `v_dod_sw`        | str1    | %1s | Valid Day of Death |
| `bene_id`         | str15   | %15s | Encrypted CCW BENE_ID |
| `bene_idinbene`   | byte    | %8.0g | |
| `sex1992`-`sex2013` |         str1 |    %1s | |
| `race1992`-`race2013` |        str1 |    %1s | |
| `sdob1992`-`sdob2013` |        long |    %12.0g | |
| `sdod1992`-`sdod2013` |        int |     %8.0g | |
| `county1992`-`county2013` |      str3 |    %3s | |
| `benezip1992`-`benezip2013` |     str9 |    %9s | |
| `benestate1992`-`benestate2013` |   str2 |    %2s | |

#### `pop01_hsahrr_long`
`desc using pop01_hsahrr_long.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| sdod       | long  | %tdD_m_Y | Date of death |
| zipcode_de | str9  | %9s      | Zip Code |
| sdob       | long  | %tdD_m_Y | Date of birth |
| ehic       | str11 | %11s     | NBER Encrypted health insurance claim number (individual unique identifier) |
| fileyear      | int   | %8.0g | Year raw file if inindx |
| state_de      | str2  | %2s   | State |
| county_de     | str3  | %3s   | County |
| sex           | str1  | %1s   | Sex |
| race          | str1  | %1s   | Race code |
| v_dod_sw      | str1  | %1s   | valid date of death |
| bene_id       | str15 | %15s  | Encrypted beneficiary identifier |
| bene_idinbene | byte  | %8.0g | |
| bene_zipnob   | str9  | %9s   | Zipcode number for beneficiary in the denominator files(character) |
| benezip_num   | long  | %12.0g | |
| benezip5      | str5  | %5s | |
| benezip5_num  | long  | %12.0g | Zipcode number, first five digits |
| bene_hsanum   | long  | %12.0g | Dartmouth HSA Num, matched on bene zip code |
| bene_hsacity  | str24 | %24s   | Dartmouth HSA city, matched on bene zip code |
| bene_hsastate | str2  | %2s    | Dartmouth HSA state, matched on bene zip code |
| bene_hrrnum   | int   | %8.0g  | Dartmouth HRR Num, matched on bene zip code |
| bene_hrrcity  | str24 | %24s   | Dartmouth HRR city, matched on bene zip code |
| bene_hrrstate | str2  | %2s    | Dartmouth HRR state, matched on bene zip code |
| rawyear       | int   | %8.0g  | HRR data used in current year -- 1995 is used before 1995 |

#### `pop01_hsahrr_long_dupes`
This data is the deduplicated version of `pop01_hsahrr_long`. At the 1% sample, it has 580,000 observations instead of 9,700,000.

`desc using pop01_hsahrr_long_dupes.dta`

| variable name | storage type | display format | variable label
|-|-|-|-|
| sdod       | long  | %tdD_m_Y | Date of death |
| zipcode_de | str9  | %9s      | Zip Code |
| sdob       | long  | %tdD_m_Y | Date of birth |
| ehic       | str11 | %11s     | NBER Encrypted health insurance claim number (individual unique identifier) |
| fileyear      | int   | %8.0g | Year raw file if inindx |
| state_de      | str2  | %2s   | State |
| county_de     | str3  | %3s   | County |
| sex           | str1  | %1s   | Sex |
| race          | str1  | %1s   | Race code |
| v_dod_sw      | str1  | %1s   | valid date of death |
| bene_id       | str15 | %15s  | Encrypted beneficiary identifier |
| bene_idinbene | byte  | %8.0g | |
| bene_zipnob   | str9  | %9s   | Zipcode number for beneficiary in the denominator files(character) |
| benezip_num   | long  | %12.0g | |
| benezip5      | str5  | %5s | |
| benezip5_num  | long  | %12.0g | Zipcode number, first five digits |
| bene_hsanum   | long  | %12.0g | Dartmouth HSA Num, matched on bene zip code |
| bene_hsacity  | str24 | %24s   | Dartmouth HSA city, matched on bene zip code |
| bene_hsastate | str2  | %2s    | Dartmouth HSA state, matched on bene zip code |
| bene_hrrnum   | int   | %8.0g  | Dartmouth HRR Num, matched on bene zip code |
| bene_hrrcity  | str24 | %24s   | Dartmouth HRR city, matched on bene zip code |
| bene_hrrstate | str2  | %2s    | Dartmouth HRR state, matched on bene zip code |
| rawyear       | int   | %8.0g  | HRR data used in current year -- 1995 is used before 1995 |
