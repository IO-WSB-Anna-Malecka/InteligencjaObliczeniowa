print("    ^    ")
print("   ^^^   ")
print("  ^^^^^  ")
print(" ^^^^^^^ ")
print("  ^^^^^  ")
print(" ^^^^^^^ ")
print("^^^^^^^^^")
print("   ###   ")




def holidaybush(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print('^',end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()

#holidaybush(5)