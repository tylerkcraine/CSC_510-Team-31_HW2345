
# Data 
File small.csv has a sample containing a small portion of the Data.

File auto93.csv is a full sized test file for this project. 

## Theory
The  function _Y=F(X)_ computes dependent variables _Y_ from independent variables _X_. 
Some variables are `Num`eric (which we denote with a leading upper case letter) and some
are `Sym`bolic. Some `dependent` variables need to maximized (denoted with a trailing `-` sign)
and other need to be maximized (denoted with a trailing `+`).

Line one of the file has a name showing the column
name and types. E.g. in the small.csv
the dependent variables are columns 4,5 and 8. 
```
Clndrs,Volume,Hp:,Lbs-,Acc+,Model,origin,Mpg+
8,304.0,193,4732,18.5,70,1,10
8,360,215,4615,14,70,1,10
8,307,200,4376,15,70,1,10
8,318,210,4382,13.5,70,1,10
8,429,208,4633,11,72,1,10
```
The ":" header on `Hp:` (above). This denotes a column that we skipped.

We report middle and diversity of each non-skipped column.

For numbers:
- mid = median = sort numbers seen so far, return the middle value
- div = standard deviation = sort numbers, find 90th, 10th percentile, return (90th-10th)/2.56
  - Since 1 or 2 standard deviations captures 66 to 95\% of the mass. So somewhere in-between
    1 and 2 is some point where you catch 90\% (that point is 1.28 standard deviations, so we used
    plus or minus 1.28=2.56)

For symbols:
- mid = mode = most common symbol
- div = entropy = for symbols occurring at probability p1,p2,... then   
     entropy= <em>&sum; -p<sub>i</sub> \* log2(p<sub>i</sub>)</em>.
  - Entropy can be viewed as the effort required to recreate a signal. 
  - If a signal has parts
    that occur a probability p1,p2,... 
  - then the probability that we want to search for a signal is:
    p1 + p2,.... 
  - And the effort to find the signal is _log2(p)_ (assuming a binary chop)
  - The probability of that search effort is  <em>-p<sub>i</sub> \* log2(p<sub>i</sub>)</em>
    
