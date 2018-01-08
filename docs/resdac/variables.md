# Variable Definitions


#### [Beneficiary LRD Used Count](http://www.resdac.org/cms-data/variables/Beneficiary-LRD-Used-Count)

The number of lifetime reserve days that the beneficiary has elected to use during the period covered by the institutional claim. Under Medicare, each beneficiary has a one-time reserve of sixty additional days of inpatient hospital coverage that can be used after 90 days of inpatient care have been provided in a single benefit period. This count is used to subtract from the total number of lifetime reserve days that a beneficiary has available.

#### [Beneficiary Total Coinsurance Days Count](http://www.resdac.org/cms-data/variables/Beneficiary-Total-Coinsurance-Days-Count)

The count of the total number of coinsurance days involved with the beneficiary's stay in a facility.

#### [Beneficiary's Hospice Period Count](http://www.resdac.org/cms-data/variables/Beneficiarys-Hospice-Period-Count)

The count of the number of hospice period trailers present for the beneficiary's record. Prior to BBA a beneficiary was entitled to a maximum of 4 hospice benefit periods that may be elected in lieu of standard Part A hospital benefits. The BBA changed the hospice benefit to the following: 2 initial 90 day periods followed by an unlimited number of 60 day periods (effective 8/5/97).

NOTE: CWF stopped populating the hospice period count field in October 2008 and then in December 2011 began populating it again.

#### [Carrier Claim Cash Deductible Applied Amount*](http://www.resdac.org/cms-data/variables/Carrier-Claim-Cash-Deductible-Applied-Amount)

Effective with Version H, the amount of the cash deductible as submitted on the claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.

#### [Carrier Claim Entry Code](http://www.resdac.org/cms-data/variables/Carrier-Claim-Entry-Code)

Carrier-generated code describing whether the Part B claim is an original debit, full credit, or replacement debit.

#### [Carrier Claim HCPCS Year Code](http://www.resdac.org/cms-data/variables/Carrier-Claim-HCPCS-Year-Code)

Effective with Version H, the terminal digit of HCPCS version used to code the claim.

NOTE: Beginning with NCH weekly process date 10/3/97 this field was populated with data. Claims processed prior to 10/3/97 will contain zeroes in this field.

#### [Carrier Claim Payment Denial Code](http://www.resdac.org/cms-data/variables/Carrier-Claim-Payment-Denial-Code)

The code on a noninstitutional claim indicating to whom payment was made or if the claim was denied.

NOTE1: Effective with Version 'J', the field has been expanded on the NCH record to 2 bytes, With this expansion, the NCH will no longer use the character values to represent the official two byte values sent in by CWF since 4/2002. During the Version J conversion, all character values were converted to the two byte values.

NOTE2: Effective 4/1/02, this field was expanded to two bytes to accommodate new values. The NCH Nearline file did not expand the current 1-byte field but instituted a crosswalk of the 2-byte field to the 1-byte character value. See table of code for the crosswalk.

#### [Carrier Claim Primary Payer Paid Amount*](http://www.resdac.org/cms-data/variables/Carrier-Claim-Primary-Payer-Paid-Amount)

Effective with Version H, the amount of a payment made on behalf of a Medicare bene- ficiary by a primary payer other than Medicare, that the provider is applying to covered Medicare charges on a non-institutional claim.

NOTE: During the Version H conversion, this field was populated with data throughout history (back to service year 1991) by summing up the line item primary payer amounts.

#### [Carrier Claim Provider Assignment Indicator Switch](http://www.resdac.org/cms-data/variables/Carrier-Claim-Provider-Assignment-Indicator-Switch)

A switch indicating whether or not the provider accepts assignment for the noninstitutional claim.

#### [Carrier Claim Referring PIN Number](http://www.resdac.org/cms-data/variables/Carrier-Claim-Referring-PIN-Number)

Carrier-assigned identification (profiling) number of the physician who referred the beneficiary to the physician that performed the Part B services.

#### [Carrier Claim Referring Physician NPI Number](http://www.resdac.org/cms-data/variables/Carrier-Claim-Referring-Physician-NPI-Number)

The national provider identifier (NPI) number of the physician who referred the beneficiary to the physician who performed the Part B services.

NOTE: Effective May 2007, the NPI will be- come the national standard identifier for covered health care providers. NPIs will replace current OSCAR provider number, UPINs, NSC numbers, and local contractor provider identification numbers (PINs) on standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number (UPIN, PIN, OSCAR provider number, etc.)).

NOTE1: CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available on the NCH. After the 5/07 NPI implementation, the standard system main- tainers will add the legacy number to the claim when it is adjudicated. We will continue to re- ceive any currently issued UPINs. Effective May 2007, no new UPINs (legacy number) will be generated for new physicians (Part B and Outpatient claims) so there will only be NPIs sent in to the NCH for those physicians.

#### [Carrier Claim Referring Physician UPIN Number](http://www.resdac.org/cms-data/variables/Carrier-Claim-Referring-Physician-UPIN-Number)

The unique physician identification number (UPIN) of the physician who referred the beneficiary to the physician who performed the Part B services.

#### [Carrier Line Anesthesia Unit Count](http://www.resdac.org/cms-data/variables/Carrier-Line-Anesthesia-Unit-Count)

The base number of units assigned to the line item anesthesia procedure on the carrier claim (non-DMERC).

#### [Carrier Line HPSA/Scarcity Indicator Code](http://www.resdac.org/cms-data/variables/Carrier-Line-HPSAScarcity-Indicator-Code)

Effective 10/3/2005 with the implementation of NCH/ NMUD CR#2, the code used to track health professional shortage area (HPSA) and physician scarcity bonus payments on carrier claims.

NOTE: Prior to 10/3/2005, claims contained a modifier code to indicate the bonus payment. A 'QU' represented a HPSA bonus payment and an 'AR' represented a scarcity bonus payment. As of 1/1/2005, the modifiers were no longer being reported by the provider. NCH & NMUD were not ready to accept the new field until 10/3/2005.

#### [Carrier Line Miles/Time/Units/Services Count](http://www.resdac.org/cms-data/variables/Carrier-Line-MilesTimeUnitsServices-Count)

The count of the total units associated with services needing unit reporting such as transportation, miles, anesthesia time units, number of services, volume of oxygen or blood units. This is a line item field on the carrier claim (non-DMERC) and is used for both allowed and denied services.

NOTE: For anesthesia (MTUS Indicator = 2) this field should be reported in time unit intervals, i.e. 15 minute interals or fraction thereof. It appears that some carriers are reporting minutes instead of time units.

#### [Carrier Line Miles/Time/Units/Services Indicator Code](http://www.resdac.org/cms-data/variables/Carrier-Line-MilesTimeUnitsServices-Indicator-Code)

Code indicating the units associated with services needing unit reporting on the line item for the carrier claim (non-DMERC).

#### [Carrier Line Performing Group NPI Number](http://www.resdac.org/cms-data/variables/Carrier-Line-Performing-Group-NPI-Number)

The National Provider Identifier (NPI) of the group practice, where the performing physician is part of that group.

NOTE: Effective May 2007, the NPI will become the national standard identifier for covered health care providers. NPIs will replace the current legacy numbers (UPINs, PINs, etc.) on the standard HIPPA claim transactions. (During the NPI transition phase (4/3/06 - 5/23/07) the capability was there for the NCH to receive NPIs along with an existing legacy number.

CMS has determined that dual provider identifiers (old legacy numbers and new NPI) must be available in the NCH. After the 5/07 NPI implementation, the standard system maintainers will add the legacy number to the claim when it is adjudicated. We will continue to receive the OSCAR provider number and any currently issued UPINs. Effective May 2007, no NEW UPINs (legacy number) will be generated for NEW physicians (Part B and Outpatient claims), so there will only be NPIs sent in to the NCH for those physicians.

#### [Carrier Line Performing NPI Number](http://www.resdac.org/cms-data/variables/Carrier-Line-Performing-NPI-Number)

A placeholder field (effective with Version H) for storing the NPI assigned to the performing provider.

#### [Carrier Line Performing PIN Number](http://www.resdac.org/cms-data/variables/Carrier-Line-Performing-PIN-Number)

The profiling identification number (PIN) of the physician\supplier (assigned by the carrier) who performed the service for this line item on the carrier claim (non-DMERC).

#### [Carrier Line Performing Provider ZIP Code](http://www.resdac.org/cms-data/variables/Carrier-Line-Performing-Provider-ZIP-Code)

The ZIP code of the physician/supplier who performed the Part B service for this line item on the carrier claim (non-DMERC).

#### [Carrier Line Performing UPIN Number](http://www.resdac.org/cms-data/variables/Carrier-Line-Performing-UPIN-Number)

The unique physician identification number (UPIN) of the physician who performed the service for this line item on the carrier claim (non-DMERC).

#### [Carrier Line Pricing Locality Code](http://www.resdac.org/cms-data/variables/Carrier-Line-Pricing-Locality-Code)

Code denoting the carrier-specific locality used for pricing the service for this line item on the carrier claim (non-DMERC).

#### [Carrier Line Provider Type Code](http://www.resdac.org/cms-data/variables/Carrier-Line-Provider-Type-Code)

Code identifying the type of provider furnishing the service for this line item on the carrier claim (non-DMERC).

#### [Carrier Line RX Number](http://www.resdac.org/cms-data/variables/Carrier-Line-RX-Number)

The number used to identify the prescrip- tion order number for drugs and biologicals purchased through the competitive acquisition program (CAP).

NOTE1: MMA required the implementation of a competative acquisition program (CAP) for Part B drugs and biologicals not paid on a cost or PPS basis. Physicians will be given a choice between buying and billing these drugs under the average sales price (ASP) or obtaining these drugs from an approved CAP vendor. The prescription number is needed to identify which claims were submitted for CAP drugs and their administration.

NOTE2: Eventhough this field was implemented with NCH/NMUD CR#2, data will not be coming in until 1/1/2006.The number used to identify the prescrip- tion order number for drugs and biologicals purchased through the competitive acquisition program (CAP). NOTE1: MMA required the implementation of a competative acquisition program (CAP) for Part B drugs and biologicals not paid on a cost or PPS basis. Physicians will be given a choice between buying and billing these drugs under the average sales price (ASP) or obtaining these drugs from an approved CAP vendor. The prescription number is needed to identify which claims were submitted for CAP drugs and their administration. NOTE2: Eventhough this field was implemented with NCH/NMUD CR#2, data will not be coming in until 1/1/2006.

#### [Carrier Line Reduced Payment Physician Assistant Code](http://www.resdac.org/cms-data/variables/Carrier-Line-Reduced-Payment-Physician-Assistant-Code)

Effective 1/92, the code on the carrier (non-DMERC) line item that identifies claims that have been paid a reduced fee schedule amount (65%, 75% or 85%) because a physician's assistant performed the services.