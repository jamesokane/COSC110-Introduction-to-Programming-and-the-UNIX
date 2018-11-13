# Fimc: financially independent monte carlo

![Static](https://img.shields.io/badge/Python-3.x-blue.svg)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## What is Fimc?
Fimc is a simple python application to help you plan for your retirement by estimating your level of financial independence utilising the Monte Carlo experiement (https://en.wikipedia.org/wiki/Monte_Carlo_method).

There is no need to provide Fimc with all your financial information, Fimc is able to compute your level of financial independence by asking you 8 simple questions:

* How much did you spend last year to support your current lifestyle.
* What is the expected inflation rate.
* How much do you currently have saved for investment.
* What is the expected average annual interest rate.
* How many years do you want to test for.
* The maximum amount the inflation rate can change in a single year
* The maximum amount the interest rate can change in a single year
* How many simulations do you want to run.

Once you have answered these questions Fimc will output the number of simulations that were `successful`, meaning those that the final savings balance is greater than or equal to zero. A detailed output of the results of the simulations will be written to a new file, output.txt. Within this file each simulation will be shown on a new line, with your expected savings balance shown for each test year. If the final savings balance is greater than or equal to zero the line will end with `successful`, or else it will end with `unsuccessful`.        

## Installing Fimc

### Requirements  
Fimc requires **Python 3.x**.
If you need Python 3 the latest information and versions are available at
  https://www.python.org/downloads/

### Quick start
Use the Python interpreter to run Fimc:

    $ python3 fimc.py

Or alternatively if you are using Linux:

    $ ./fimc.py

## Using Fimc

Fimc will first ask you to enter how much money you spent last year to support your current lifestyle. The amount you enter must be a whole number that is equal to or greater than zero, for example `50000`. The amount can not be negative or contain decimals, for example `-50000` or `50000.25`. If an invalid value is entered you will be asked to re-enter the amount.  

    $ How much did you spend last year to support your current lifestyle?

You will than be asked to enter the inflation rate. The inflation rate must be entered as a decimal number and not a percentage. For example `5%` should be entered as `0.05`. If an invalid value is entered you will be asked to re-enter the amount.   

    $ Please enter the expected inflation rate:

You will than be asked to enter the maximum amount the inflation rate can change in a single year. The expected inflation rate change must be entered as a decimal number and not a percentage. If an invalid value is entered you will be asked to re-enter the amount.   

    $ Please enter the expected maximum change for inflation in a given year:    

Fimc will then ask you to enter your current savings balance. The amount you enter must be a whole number and can not be negative. If an invalid value is entered you will be asked to re-enter the amount.

    $ How much do you currently have saved for investment?

You will than be asked to enter the annual interest rate that you expect to earn on your savings. The annual interest rate must be entered as a decimal number and not a percentage. If an invalid value is entered you will be asked to re-enter the amount.

    $ Please enter the base annual interest rate:

You will than be asked to enter the maximum amount the interest rate can change in a single year. The expected interest rate change must be entered as a decimal number and not a percentage. If an invalid value is entered you will be asked to re-enter the amount.

    $ Please enter the expected maximum change for interest in a given year:    

Fimc will then ask you to enter the number of years that you would like to test for. The amount you enter must be a whole number that is greater than zero, and cannot contain decimals. If an invalid value is entered you will be asked to re-enter the amount.

    $ How many years do you want to test?

Finally you will be asked to enter the number of simulations that you would like to run. The amount you enter must be a whole number that is greater than zero, and cannot contain decimals. If an invalid value is entered you will be asked to re-enter the amount.

    $ How many simulations do you want to run?

### Fimc example

A possible interaction with Fimc could look like:

    $ How much did you spend last year to support your current lifestyle? 50000
    $ Please enter the expected inflation rate: 0.02
    $ Please enter the expected maximum change for inflation in a given year: 0.005
    $ How much do you currently have saved for investment? 1000000
    $ Please enter the base annual interest rate: 0.05
    $ Please enter the expected maximum change for interest in a given year: 0.01
    $ How many years do you want to test? 20
    $ How many simulations should be run? 10
    Simulation was successful in 10/10 runs (100.00%)

Which could result in the following being written to output.txt:

    996450.00 997127.57 991738.31 991570.19 998556.25 1000484.89 997192.45 990387.97 975623.83 958100.54 942007.60 929704.62 918233.23 900004.58 887633.66 870515.07 847598.11 818308.90 789771.25 758229.52 successful
    996450.00 990742.82 990672.72 985749.77 975074.53 968791.87 957437.07 939607.47 913168.46 879636.30 848867.03 821970.21 788351.47 747336.70 697057.29 645413.23 584250.92 516481.62 443916.83 366322.98 successful
    996450.00 984864.56 966349.06 946290.65 930039.13 906929.30 889398.10 869435.43 846839.11 825558.81 801240.47 772569.28 744955.97 719052.12 684296.49 648650.32 608710.95 563139.21 514628.47 459006.28 successful
    996450.00 991021.06 987994.35 990566.15 999510.05 1001476.72 999795.91 989668.45 978468.37 974108.38 964150.93 951465.49 930572.62 900426.75 874582.85 850496.38 822418.99 793876.87 761754.89 722025.21 successful
    996450.00 988315.40 971097.67 953592.83 928254.94 897432.03 858915.51 819282.51 774480.58 733599.88 690442.87 649415.01 608173.95 560050.88 507090.65 449033.86 391749.60 330482.33 267064.66 200467.62 successful
    996450.00 995583.14 990118.07 986506.97 976976.67 959630.10 941217.41 920010.23 889482.94 863641.31 828430.79 792768.97 758749.57 716961.68 669008.56 618751.16 567777.90 514683.54 460895.87 404014.99 successful
    996450.00 1001025.26 1004000.64 1006275.12 1005355.03 1001912.09 994816.68 990644.97 978347.15 964815.09 956917.20 938870.90 922686.48 898394.32 877677.78 860909.80 842507.64 822149.32 805462.05 789396.32 successful
    996450.00 983440.51 974691.77 959623.50 942173.09 915875.19 885931.86 853122.84 813300.26 772777.32 731838.06 682693.23 635092.66 580649.62 520025.10 452890.62 378359.38 302885.26 221603.17 135806.35 successful
    996450.00 982870.36 962530.78 938946.45 918506.32 895509.32 868759.74 835849.95 799066.21 763733.44 726344.68 686079.46 638342.18 594013.99 546518.85 497866.11 448964.84 398676.51 344741.56 288125.35 successful
    996450.00 989554.74 986020.89 987178.50 991353.62 999140.09 1003679.71 1015112.14 1021784.56 1024498.81 1028085.23 1031613.11 1034157.27 1041985.32 1057072.05 1068082.57 1076359.21 1093909.70 1115623.15 1130307.06 successful

Note that, because of the random nature of these results, the exact values in output.txt could differ even for the same input.

## Support
If you find a bug, or have a feature suggestion, please email me at jokane2@myune.edu.au

## License
Fimc is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) License.
