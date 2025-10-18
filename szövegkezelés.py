
szöveg_felhasználótól = input("Kérek egy szöveget: ")

szöveg_hossza = len(szöveg_felhasználótól)

if(szöveg_hossza > 0):
    előtét = "Ezt írtad be: "
    végleges_szöveg = előtét + szöveg_felhasználótól

    print(végleges_szöveg)

    utolsó_betű = szöveg_felhasználótól[-1]

    print(f"Utolsó betű: {utolsó_betű}")

    print(f"Milyen hosszú a szöveg: {szöveg_hossza}")
    print(f"Utolsó betű: {szöveg_felhasználótól[szöveg_hossza-1]}")

    if(szöveg_hossza % 2 != 0):
        középső_betű = round(szöveg_hossza/2)
        print(f"Középső betű: {szöveg_felhasználótól[középső_betű]}")

megadott_szöveg = "Helló világ!"
első_szó = megadott_szöveg[:5]
print(f"Első szó: '{első_szó}'")
első_szó_szóközök_nélkül = első_szó.strip()
print(f"Első szó: '{első_szó_szóközök_nélkül}'")

print(f"Első szó nagybetűsen: '{első_szó.upper()}'")

utolsó_szó = megadott_szöveg[6:]
print(f"Utolsó szó: '{utolsó_szó}'")

újszöveg = megadott_szöveg.replace("világ","world")
print(f"új szöveg: {újszöveg}")

darabok = megadott_szöveg.split(" ")
print(darabok)
print(darabok[0])

db = 0
for betű in megadott_szöveg:
    if betű == "l":
        db+=1

print(f"'l' betűk száma: {db}")