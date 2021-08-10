"""
An python CLI application to generate strong passwords.
"""

import random

char_domain = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

for i in range(int(input("Enter the number of passwords to be generated: "))):
    password = ""

    for j in range(int(input("Enter password length: "))):
        password += random.choice(char_domain)
    
    print(f"Password {i+1} : ",password)

"""
# Output:

    Enter the number of passwords to be generated: 10
    Enter password length: 8
    Password 1 :  5+/FF{zx 
    Enter password length: 10
    Password 2 :  ;THY%cq}6`
    Enter password length: 15
    Password 3 :  |I=I*s}g%L~:ul>
    Enter password length: 25
    Password 4 :  z4lX/DtM8SI::hIH4`M6:tS'o
    Enter password length: 40
    Enter password length: 50
    Password 6 :  N?@Q*$SJJ<Yrbb%'_?<DE~QJ_^@j^h->tW p`]B/q+qHK((eN'
    Enter password length: 100
    Password 7 :  vm2*I,;u0t SdA<}CI>FD,&aj;sEuId}M0UynjolNs(;7dP`^oQSH^&ls'p)hSL[~t|G-j_w@`"3Pkkx$u6RFI!-)c1F?,hYA+yl
    Enter password length: 20
    Password 8 :  FcY6pJ?<S2|*#DJ1~$=I
    Enter password length: 35
    Password 9 :  Ih8.$vZP@!ha)_Kdxnn5=wC^oW&l@I#d+q7
    Enter password length: 69
    Password 10 :  xy6|+Bk?*`v,95-Z%rRxS}I>e#!IMf?4&:/;Z<u]j|?2;c;U4Y?-T}1[!=9L$R/8,U6xr

"""