# Figui: financially independent graphical user interface

![Static](https://img.shields.io/badge/Python-3.x-blue.svg)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)

## What is Figui?
Figui is a python application with a simple user interface which helps you to easily analyse the important data from your finacially independent Monte Carlo simulation.

Figui gives you the ability to select and open the `output.txt` file created by your Monte Carlo simulation. This file is than analysed and the maximum, minimum, and average balance for the final year of the simulation are displayed in the main window.   

## Installing Figui
### Requirements  
Figui requires **Python 3.x**.
If you need Python 3 the latest information and versions are available at
  https://www.python.org/downloads/

### Quick start
Use the Python interpreter to run Fimc:

    $ python3 figui.py

Or alternatively if you are using Linux:

    $ ./figui.py

## Using Figui
Figui has a simple user interface which allows you to click on the `Open...` button and select the file which you want to analyse. Once you have selected the file you will be returned to the main window where the Maximum balance, Minimum balance and Average balance will be shown.

If there are any problems opening or analysing the selected file an error message window will appear and you will be asked to review the selected file and try again.    

If you want to analyse another file simply click on the `Open...` button again and select a new file.
### Fimc example
Consider the following output from the financial independence Monte Carlo simulation:

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

A potential interface presenting the required information from that file may look like the following:

<img width="400" alt="figui" src="https://user-images.githubusercontent.com/17037177/40883287-0df45764-673c-11e8-828a-814b3fc2cb18.png">

## Support
If you find a bug, or have a feature suggestion, please email me at jokane2@myune.edu.au

## License
Figui is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) License.
