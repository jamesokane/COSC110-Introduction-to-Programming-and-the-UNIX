# Fi: Financially Independent

![Static](https://img.shields.io/badge/Python-3.x-blue.svg)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## What is Fi?
Fi is a simple python application to help you plan for your retirement by estimating your level of financial independence.

There is no need to provide Fi with all your financial information, Fi is able to compute your level of financial independence by asking you 5 simple questions:

* How much did you spend last year to support your current lifestyle.
* What is the expected inflation rate.
* How much do you currently have saved for investment.
* What is the expected average annual interest rate.
* How many years do you want to test.

Once you have answered these questions Fi will display your expected savings balance each year up to the total number of years you want to test for and let you know whether you are `Financially independent` or `Not financially independent`.     

## Installing Fi

### Requirements  
Fi requires **Python 3.x**.
If you need Python 3 the latest information and versions are available at
  https://www.python.org/downloads/

### Quick start
Use the Python interpreter to run Fi:

    $ python3 fi.py

## Using Fi

Fi will first ask you to enter how much money you spent last year to support your current lifestyle. The amount you enter must be a whole number that is equal to or greater than zero, for example `50000`. The amount can not be negative or contain decimals, for example `-50000` or `50000.25`. If an invalid value is entered you will be asked to re-enter the amount.  

    $ How much did you spend last year to support your current lifestyle?

You will than be asked to enter the inflation rate. The inflation rate must be entered as a decimal number and not a percentage. For example 5% should be entered as `0.05`. If an invalid value is entered you will be asked to re-enter the amount.   

    $ Please enter the expected inflation rate as a decimal number(e.g. 5% = 0.05):

Fi will then ask you to enter your current savings balance. The amount you enter must be a whole number and can not be negative. If an invalid value is entered you will be asked to re-enter the amount.

    $ How much do you currently have saved for investment?

You will than be asked to enter the annual interest rate that you expect to earn on your savings. The annual interest rate must be entered as a decimal number and not a percentage. If an invalid value is entered you will be asked to re-enter the amount.

    $ Please enter the expected interest rate as a decimal number(e.g. 3% = 0.03):

Finally Fi will ask you to enter the number of years that you would like to test for. The amount you enter must be a whole number that is equal to or greater than zero. The amount can not be negative or contain decimals. If an invalid value is entered you will be asked to re-enter the amount.

    $ How many years do you want to test?



### Fi example

For each year, up to the total number of years you want to test for, Fi will display the year number and the estimated savings balance for that year. If the savings balance remains positive for each year Fi will display all the years and let you know that you are `Financially independent`.  

    $ How much did you spend last year to support your current lifestyle? 50000
    $ Please enter the expected inflation rate as a decimal number(e.g. 5% = 0.05): 0.02
    $ How much do you currently have saved for investment? 1000000
    $ Please enter the expected interest rate as a decimal number(e.g. 3% = 0.03): 0.05
    $ How many years do you want to test? 20
      Year    Remaining balance
         1    $996450.00
         2    $991651.50
         3    $985520.66
         4    $977969.00
         5    $968903.21
         6    $958224.84
         7    $945830.08
         8    $931609.47
         9    $915447.59
        10    $897222.76
        11    $876806.74
        12    $854064.39
        13    $828853.26
        14    $801023.29
        15    $770416.36
        16    $736865.93
        17    $700196.55
        18    $660223.45
        19    $616752.04
        20    $569577.40
      Financially independent

However if the savings balance becomes negative for any year Fi will only display up to the year where the savings balance becomes negative and let you know that you are `Not financially independent`.

    $ How much did you spend last year to support your current lifestyle? 100000
    $ Please enter the expected inflation rate as a decimal number(e.g. 5% = 0.05): 0.025
    $ How much do you currently have saved for investment? 1500000
    $ Please enter the expected interest rate as a decimal number(e.g. 3% = 0.03): 0.04
    $ How many years do you want to test? 20
      Year    Remaining balance
         1    $1453400.00
         2    $1402271.00
         3    $1346365.22
         4    $1285423.28
         5    $1219173.76
         6    $1147332.60
         7    $1069602.58
         8    $985672.78
         9    $895217.94
        10    $797897.87
        11    $693356.77
        12    $581222.61
        13    $461106.36
        14    $332601.34
        15    $195282.38
        16    $48705.09
        17    $-107595.00
      Not financially independent

## Support
If you find a bug, or have a feature suggestion, please email me at jokane2@myune.edu.au

## License
Fi is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) License.
