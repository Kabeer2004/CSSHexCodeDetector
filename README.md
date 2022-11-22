# CSSHexCodeDetector
detects valid hex codes in CSS files using Python (Hackerrank Question)

this is the question "Hex Color Code" from Hackerrank. took me an ungodly time to solve (and for a very dumb reason)

CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E and F).
■ A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).

the program accepts your CSS Code as input and prints all the valid hexcode values in the code (it is smart enough to ignore Selectors which also begin with a '#')

■ sample input:
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

■ sample output:
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

note how it ignores #BED and #Cab even though they satisfy the conditions for hexcode.
the number '11' in the first line of sample input indicates how many lines you are entering. so, enter that accordingly and then enter your code line by line.
