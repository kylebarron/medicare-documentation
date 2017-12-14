Lag and Post Event Spending
===========================

Lagged and post utilization $l$-days before and since day $t$ is
complicated because of overlaps in time periods. Consider

```
        |---------------|
        |       x       |
        |---------------|
```

Where `x` marks an event during an admission, for instance. Say
we want to get inpatient charges 30 days before this event and
30 days after. Then

```
      30 days
  [-------------)
        |---------------|
        |       x       |
        |---------------|
                (-------------]
                    30 days
```

We already have a complication: How do we count spending during the
admission? We can't count all of it because some of it occurred after
the event and some after. In this case we count
- For lag, take the charges during the admission and multiply by the
  portion of the admission that occurred from the admission until the event.
- For the post, take the charges during the admission and multiply by the
  portion of the admission that occurred from the event until discharge.

We apply a similar rule admissions pre and post:

```
    A
  |----|
  [-------------)
        |---------------|
        |       x       |
        |---------------|
                (-------------]
                          |---------|
                               B
```

We could all charges in A, as they occurred completely within the 30-day
window before the event. However, we only cound the charges in B times
the proportion of days from the first date of B until x + 30 that are in
B. This is easy to visualize but a bit difficult to write down precisely.
You can see Maurice's code for guidance in
- `2SecondaryManipPrgms/completecostmetric/CumulativeCostsPrePost.sas`

In particular, see macro `CreateCostVariables`.

Code Example
------------

The example I have is for carrier pre/post utilization in the carrier
project:

```sas
%macro getCarrier( /* Outputs: &outlib..car&prefix_lag&lag */
        outlib,    /* Output library                       */
        prefix,    /* Base data prefix (ip or med)         */
        basedata,  /* Base data to use (ip or med)         */
        lag = 0    /* Compute utilization l days pre/post  */
    );

    /*  If &lag = 0, simply add up utilization within admit/disch.
        Otherwise add utilization &lag days pre/post event date.
    */
    %if &lag. = 0 %then %goto nolag; %else %goto lagn;

    * If no lag, then simply sum all carrier expenditures during admission;
    %nolag:
    proc sql &sqlopts;
    create table &outlib..car&prefix._tot as
        select a.bene_id,
            b.admission_date,
            b.discharge_date,
            sum(a.car_tot) as car20_index     label = "20% Carrier Util During Stay",
            sum(a.car_pmt) as car20_index_pmt label = "20% Carrier Paid by Medicare During Stay"
        from &outlib..car_tot a,
             &basedata.(keep = bene_id admission_date discharge_date) b
        where a.bene_id = b.bene_id and
            (b.admission_date <= a.expnsdt1 and
             a.expnsdt2 <= b.discharge_date)
        group by a.bene_id, b.admission_date, discharge_date;
    quit;
    %goto exit;

    %lagn:
    proc sql &sqlopts;
    create table &outlib..car&prefix._lag&lag. as
        select a.bene_id,
            dgn_date,
            sum(case
                /* event in [t - lag, t - 1] */
                /* Hence we count all of it */
                when expnsdt1 <  dgn_date and
                     expnsdt1 >= dgn_date - &lag. and
                     expnsdt2 <  dgn_date
                     then car_tot * 1
                /* event starts in [t - lag, t - 1], ends >= t */
                /* Hence we count portion from start to t */
                when expnsdt1 <  dgn_date and
                     expnsdt1 >= dgn_date - &lag. and
                     expnsdt2 >  dgn_date
                     then car_tot * (dgn_date - expnsdt1) / (expnsdt2 - expnsdt1 + 1)
                /* event ends in [t - lag, t - 1], starts < t - lag */
                /* Hence we count portion from t - lag to end */
                when expnsdt2 <  dgn_date and
                     expnsdt2 >= dgn_date - &lag. and
                     expnsdt1 <  dgn_date - &lag.
                     then car_tot * (expnsdt2 - (dgn_date - &lag.) + 1) / (expnsdt2 - expnsdt1 + 1)
                end) as car20_lag&lag. label = "Lagged &lag.-day 20% Carrier Util",
            sum(case
                /* event in [t - lag, t - 1] */
                /* Hence we count all of it */
                when expnsdt1 <  dgn_date and
                     expnsdt1 >= dgn_date - &lag. and
                     expnsdt2 <  dgn_date
                     then car_pmt * 1
                /* event starts in [t - lag, t - 1], ends >= t */
                /* Hence we count portion from start to t */
                when expnsdt1 <  dgn_date and
                     expnsdt1 >= dgn_date - &lag. and
                     expnsdt2 >  dgn_date
                     then car_pmt * (dgn_date - expnsdt1) / (expnsdt2 - expnsdt1 + 1)
                /* event ends in [t - lag, t - 1], starts < t - lag */
                /* Hence we count portion from t - lag to end */
                when expnsdt2 <  dgn_date and
                     expnsdt2 >= dgn_date - &lag. and
                     expnsdt1 <  dgn_date - &lag.
                     then car_pmt * (expnsdt2 - (dgn_date - &lag.) + 1) / (expnsdt2 - expnsdt1 + 1)
                end) as car20_lagpmt&lag. label = "Lagged &lag.-day 20% Carrier Paid by Medicare"
        from &outlib..car_tot a, &basedata.(keep = bene_id dgn_date) b
        where a.bene_id = b.bene_id and
            (expnsdt1 <  dgn_date and expnsdt1 >= dgn_date - &lag. or
             expnsdt2 <  dgn_date and expnsdt2 >= dgn_date - &lag.)
        group by a.bene_id, dgn_date;

    create table &outlib..car&prefix._post&lag. as
        select a.bene_id,
            dgn_date,
            sum(case
                /* event in [t, t + lag - 1] */
                /* Hence we count all of it */
                when expnsdt2 >  dgn_date and
                     expnsdt2 <  dgn_date + &lag. and
                     expnsdt1 >= dgn_date
                     then car_tot * 1
                /* event ends in [t, t + lag - 1], starts < t */
                /* Hence we count portion from t to end */
                when expnsdt2 >= dgn_date and
                     expnsdt2 <  dgn_date + &lag. and
                     expnsdt1 <  dgn_date
                     then car_tot * (expnsdt2 - dgn_date + 1) / (expnsdt2 - expnsdt1 + 1)
                /* event starts in [t, t + lag - 1], ends >= t + lag */
                when expnsdt1 >= dgn_date and
                     expnsdt1 <  dgn_date + &lag. and
                     expnsdt2 >= dgn_date + &lag.
                     then car_tot * (dgn_date + &lag. - expnsdt1) / (expnsdt2 - expnsdt1 + 1)
                end) as car20_post&lag. label = "Post &lag.-day 20% Carrier Util",
            sum(case
                /* event in [t, t + lag - 1] */
                /* Hence we count all of it */
                when expnsdt2 >  dgn_date and
                     expnsdt2 <  dgn_date + &lag. and
                     expnsdt1 >= dgn_date
                     then car_pmt * 1
                /* event ends in [t, t + lag - 1], starts < t */
                /* Hence we count portion from t to end */
                when expnsdt2 >= dgn_date and
                     expnsdt2 <  dgn_date + &lag. and
                     expnsdt1 <  dgn_date
                     then car_pmt * (expnsdt2 - dgn_date + 1) / (expnsdt2 - expnsdt1 + 1)
                /* event starts in [t, t + lag - 1], ends >= t + lag */
                /* Hence we count portion from start to t */
                when expnsdt1 >= dgn_date and
                     expnsdt1 <  dgn_date + &lag. and
                     expnsdt2 >= dgn_date + &lag.
                     then car_pmt * (dgn_date + &lag. - expnsdt1) / (expnsdt2 - expnsdt1 + 1)
                end) as car20_postpmt&lag. label = "Post &lag.-day 20% Carrier Paid by Medicare"
        from &outlib..car_tot a, &basedata.(keep = bene_id dgn_date) b
        where a.bene_id = b.bene_id and
            (expnsdt1 >  dgn_date and expnsdt1 <= dgn_date + &lag. or
             expnsdt2 >  dgn_date and expnsdt2 <= dgn_date + &lag.)
        group by a.bene_id, dgn_date;
    quit;
    %goto exit;
%exit: %mend getCarrier;
```

Mathematical Formulae
---------------------

Mathematically, the rules are as follows:

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: {
      equationNumbers: {
        autoNumber: "AMS"
      }
    },
    tex2jax: {
      inlineMath: [ ['$','$'], ['\(', '\)'] ],
      displayMath: [ ['$$','$$'] ],
      processEscapes: true,
    }
  });
</script>
<script
  type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

$$
\begin{aligned}
  \text{(pre)}
  \quad\quad
  \text{weight}^{t^* - l}_{idht}
  & =
  \begin{cases}
    1
    & t^* - l \le \text{admit}_{idht}, \text{disch}_{idht} < t^* \\[15pt]
        \dfrac{\text{disch}_{idht} - (t^* -l) + 1}{\text{disch}_{idht} - \text{admit}_{idht} + 1}
    & \text{admit}_{idht} < t^* - l \le \text{disch}_{idht} < t^* \\[15pt]
        \dfrac{t^* - \text{admit}_{idht}}{\text{disch}_{idht} - \text{admit}_{idht} + 1}
    & t^* - l \le \text{admit}_{idht} < t^* \le \text{disch}_{idht} \\[15pt]
        0
    & \text{otherwise}
  \end{cases} \\
  \text{(post)}
  \quad\quad
  \text{weight}^{t^* + l}_{idht}
  & =
  \begin{cases}
    1
    & t^* \le \text{admit}_{idht}, \text{disch}_{idht} < t^* + l \\[15pt]
        \dfrac{t^* + l - \text{admit}_{idht}}{\text{disch}_{idht} - \text{admit}_{idht} + 1}
    & t^* \le \text{admit}_{idht} < t^* + l \le \text{disch}_{idht} \\[15pt]
        \dfrac{\text{disch}_{idht} - t^* + 1}{\text{disch}_{idht} - \text{admit}_{idht} + 1}
    & \text{admit}_{idht} < t^* \le \text{disch}_{idht} < t^* + l \\[15pt]
        0
    & \text{otherwise}
  \end{cases}
\end{aligned}
$$

And now define lag/lead utilization:

$$
\begin{aligned}
  y_{idh, t^* - l}
  & = \sum^{}_{t \ne t^*} \text{weight}^{t^* - l}_{idht} \cdot y_{idht} \\
  y_{idh, t^* + l}
  & = \sum^{}_{t \ne t^*} \text{weight}^{t^* + l}_{idht} \cdot y_{idht} \\
\end{aligned}
$$

Though in our example all lag and post periods are admissions, it can be
anything with start and an endpoints.

