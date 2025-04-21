# Data for lab03

## `la-fatal-traffic-accidents-2019-2021.csv`

The file `la-fatal-traffic-accidents-2019-2021.csv` comes from 
this source:

https://data.lacity.org/Public-Safety/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w/about_data

The data was filtered to include:
* Only rows where the Date Occurred Field is between 2019 and 2021 inclusive
* Only rows where one of the MO code is 3027, "T/C - (K) Fatal Injury"

A full list of MO code used by the LAPD can be found here in the file `LAPD-MO-Codes.csv`
in the same directory.

The codes used in the `Victim Sex` column are M: Male, F: Female; X: Unknown

The codes used in the `Victim Descent` column are, according to [this source](https://medium.com/analytics-vidhya/los-angeles-crime-data-analysis-using-pandas-a68780d80a83) as follows:

```
A	Other Asian
B	Black
C	Chinese
D	Cambodian
F	Filipino
G	Guamanian
H	Hispanic/Latin/Mexican
I	American Indian/Alaskan Native
J	Japanese
K	Korean
L	Laotian
O	Other
P	Pacific Islander
S	Samoan
U	Hawaiian
V	Vietnamese
W	White
X	Unknown
Z	Asian Indian
```

## `LAPD-MO-Codes.csv`

This list of codes was taken from this PDF file:
file:///Users/pconrad/Downloads/MO_CODES_Numerical_20180627-1.pdf


