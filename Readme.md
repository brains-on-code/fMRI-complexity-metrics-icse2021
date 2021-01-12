# Program Comprehension and Code Complexity Metrics: An fMRI Study

![Python analysis pipeline](https://github.com/brains-on-code/fMRI-complexity-metrics-icse2021/workflows/Python%20analysis%20pipeline/badge.svg)
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4434423.svg)](https://doi.org/10.5281/zenodo.4434423)

This repository contains the replication package, analysis scripts, and additional information on our paper accepted at ICSE 2021.

Publication: Norman Peitek, Sven Apel, Chris Parnin, André Brechmann, and Janet Siegmund. *Program Comprehension and Code Complexity Metrics: An fMRI Study*. In Proceedings of the International Conference of Software Engineering (ICSE), 2021

# Replication Package

In `/replication`, we provide:

- all used stimuli for the comprehension, control condition, and distractor tasks (`/tasks-*`) either as image and/or text file. We used our [CodeImageGenerator](https://github.com/peitek/CodeImageGenerator) to create image files for our Java code snippets.
- experiment protocol for the fMRI session
- the meta protocol for the post-session interview

# Data

In `/data`, we share all raw and preprocessed data that we can. Due to our local privacy law, we cannot publicly provide the fMRI data at this time. Please contact us for individual solutions.

# Analysis

In `/analysis`, we share our analysis scripts that process the input data, compute the results, create plots, and run statistics.

To run the script yourself, you will need:

- Python 3.x
- numpy
- pandas
- scipy
- seaborn
- statsmodels

Once your system is ready, start the `/analysis/main.py`.

# Results

For convenience, we provide all output that the analysis script yields for our data in `/output`.

## Experiment Data: fMRI Correlations

In addition to the selected plots presented in the paper, we added all correlation plots in `/output/plots`.

## Experiment Data: Additional Metrics

We explored overall 41 additional metrics. In `/data/metrics/Metrics.md`, we provide a description of each metric.

In the paper, we provide a shortened overview. Here is the full correlation table:

| Metric      | BA21_ken  | BA39_ken  | Broca_ken | BA6_ken   | BA21_r2  | BA39_r2  | Broca_r2 | BA6_r2   | Maximum  |
|-------------|-----------|-----------|-----------|-----------|----------|----------|----------|----------|----------|
| BRANCH      | 0.557773  | 0.292167  | 0.159364  | 0.504652  | 0.415799 | 0.103552 | 0.078938 | 0.207715 | 0.557773 |
| CALL        | 0.370328  | 0.205738  | 0.164590  | 0.267459  | 0.204753 | 0.071783 | 0.051056 | 0.073125 | 0.370328 |
| CALLED      | -0.208656 | 0.000000  | 0.130410  | -0.182574 | 0.056715 | 0.017678 | 0.106936 | 0.001090 | 0.130410 |
| CALLEDp     | -0.208656 | 0.000000  | 0.130410  | -0.182574 | 0.056715 | 0.017678 | 0.106936 | 0.001090 | 0.130410 |
| CAST        | -0.104328 | -0.156492 | 0.000000  | -0.052164 | 0.026899 | 0.015624 | 0.003773 | 0.001346 | 0.026899 |
| CDENS       | 0.010120  | -0.070837 | -0.050598 | 0.091077  | 0.011646 | 0.000051 | 0.010224 | 0.030627 | 0.091077 |
| CONTROL     | 0.214834  | 0.132993  | 0.010230  | 0.296676  | 0.197186 | 0.039313 | 0.001442 | 0.119085 | 0.296676 |
| D           | 0.409878  | 0.448914  | 0.409878  | 0.507468  | 0.349998 | 0.188200 | 0.212085 | 0.260151 | 0.507468 |
| E           | -0.066667 | -0.009524 | 0.028571  | -0.066667 | 0.273073 | 0.184345 | 0.050303 | 0.307943 | 0.307943 |
| ev(G)       | 0.273608  | 0.189421  | 0.084187  | 0.231515  | 0.143175 | 0.047072 | 0.032334 | 0.049483 | 0.273608 |
| EXEC        | 0.144016  | 0.185164  | 0.020574  | 0.164590  | 0.118612 | 0.071181 | 0.000121 | 0.060093 | 0.185164 |
| EXP         | 0.336554  | 0.317322  | 0.163469  | 0.451944  | 0.368432 | 0.187518 | 0.068906 | 0.312163 | 0.451944 |
| IF_NEST     | 0.267946  | 0.306224  | 0.267946  | 0.306224  | 0.148737 | 0.100819 | 0.084406 | 0.090501 | 0.306224 |
| iv(G)       | 0.382200  | 0.104236  | 0.057909  | 0.335872  | 0.208681 | 0.019524 | 0.007082 | 0.077722 | 0.382200 |
| LOC_one     | 0.374607  | 0.394323  | 0.236594  | 0.374607  | 0.270407 | 0.216431 | 0.053383 | 0.135601 | 0.394323 |
| LOOP        | 0.480500  | 0.216225  | 0.120125  | 0.360375  | 0.324037 | 0.046773 | 0.016582 | 0.109620 | 0.480500 |
| LOOP_NEST   | 0.480500  | 0.216225  | 0.120125  | 0.360375  | 0.324037 | 0.046773 | 0.016582 | 0.109620 | 0.480500 |
| N           | 0.355786  | 0.336554  | 0.182701  | 0.413481  | 0.284907 | 0.172197 | 0.047551 | 0.265963 | 0.413481 |
| n           | 0.354891  | 0.177445  | 0.118297  | 0.374607  | 0.198826 | 0.029716 | 0.011963 | 0.174860 | 0.374607 |
| NBD         | 0.544541  | 0.294960  | 0.204203  | 0.363027  | 0.421860 | 0.128777 | 0.084884 | 0.138806 | 0.544541 |
| NCLOC       | 0.374607  | 0.394323  | 0.236594  | 0.374607  | 0.270407 | 0.216431 | 0.053383 | 0.135601 | 0.394323 |
| NP          | 0.265606  | 0.557773  | 0.504652  | 0.398410  | 0.082558 | 0.318665 | 0.198942 | 0.118455 | 0.557773 |
| QCP_CRCT    | 0.347863  | 0.309211  | 0.154606  | 0.405840  | 0.326370 | 0.149337 | 0.068916 | 0.224625 | 0.405840 |
| QCP_MAINT   | 0.325363  | 0.325363  | 0.172251  | 0.401918  | 0.273295 | 0.150278 | 0.033830 | 0.236500 | 0.401918 |
| QCP_RLBTY   | 0.267946  | 0.267946  | 0.114834  | 0.344502  | 0.254133 | 0.116341 | 0.017404 | 0.193501 | 0.344502 |
| RETURN      | -0.326823 | -0.181568 | -0.084732 | -0.326823 | 0.135191 | 0.029161 | 0.022666 | 0.108289 | 0.135191 |
| RLOC        | 0.374607  | 0.315459  | 0.157729  | 0.374607  | 0.323820 | 0.102057 | 0.004763 | 0.135061 | 0.374607 |
| STAT        | 0.230288  | 0.250313  | 0.070088  | 0.290363  | 0.170580 | 0.070865 | 0.000483 | 0.092828 | 0.290363 |
| V           | 0.355786  | 0.259627  | 0.144237  | 0.413481  | 0.329236 | 0.136128 | 0.040358 | 0.302362 | 0.413481 |
| v(G)        | 0.102869  | 0.123443  | 0.000000  | 0.205738  | 0.051420 | 0.022982 | 0.000800 | 0.046978 | 0.205738 |
| DepDegree   | 0.398133  | 0.378712  | 0.262185  | 0.436976  | 0.278511 | 0.236720 | 0.090076 | 0.173922 | 0.436976 |
| LOC_two     | 0.419439  | 0.235295  | 0.153453  | 0.337597  | 0.382308 | 0.096456 | 0.027058 | 0.181027 | 0.419439 |
| McCabe      | 0.102869  | 0.123443  | 0.000000  | 0.205738  | 0.051420 | 0.022982 | 0.000800 | 0.046978 | 0.205738 |
| Halstead    | 0.485714  | 0.542857  | 0.428571  | 0.600000  | 0.393218 | 0.209351 | 0.213938 | 0.288564 | 0.600000 |
| Sonar_Cog   | 0.239046  | 0.139443  | 0.039841  | 0.298807  | 0.237528 | 0.057054 | 0.016282 | 0.131811 | 0.298807 |
| Sonar_Cyclo | 0.102869  | 0.123443  | 0.000000  | 0.205738  | 0.051420 | 0.022982 | 0.000800 | 0.046978 | 0.205738 |

# License

This repository is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# Contact

If you have questions, please contact me directly: `norman.peitek@lin-magdeburg.de`. Thank you!
