import random

# Seznamy o 25 slovech ve třech obtížnostech
lehka = [
    "pes", "les", "výr", "věk", "dům", "nor", "oči", "páv", "tuk", "brk", 
    "čaj", "čas", "gól", "dub", "hra", "čip", "jez", "sob", "jas", "hák", 
    "gel", "prd", "ufo", "šíp", "puk"
]
stredni = [
    "atlas", "autor", "apríl", "chleba", "chemie", "chodba", "chodec", "garáž", "gyros", "granát", 
    "losos", "lovec", "látka", "lopuch", "lesba", "lustr", "lejno", "louže", "zebra", "zánět", 
    "zdivo", "zrzek", "západ", "zápas", "nemoc"
]
tezka = [
    "akvárium", "adaptace", "akademik", "bumerang", "bylinkář", "dusičnan", "drobeček", "harlekýn", "harmonie", "federace", 
    "farmářka", "formička", "impérium", "instinkt", "konečník", "kontrakt", "letectvo", "nadšenec", "myšlenka", "nevýhoda", 
    "ošetření", "pohrůžka", "rýmování", "služebná", "vláknina"
]

gratulace = "Tentokrát jsi vyvázl a tvůj bídný život zůstal ušetřen!"
konec = "Už se houpeš ve větru! Snad příště cizinče."

# Počet pokusů. 11 je smrt
spatne_pokusy = 0
dobre_pokusy = 0
spatna_pismena = []

# Uvítání a volba obtížnosti
print("Vítám tě cizinče ve hře ’Obešenec v konzoli’. Dokážeš uhádnout celé slovo?\nNebo se budeš bezvládně houpat na kusu dřeva?")
input("Pokud se nebojíš, stiskni klávesu.")
print("Zvol si obtížnost:")
print("1)lehká - slovo o třech písmenech\n2)střední - slovo o pěti písmenech\n3)těžká - slovo o osmi písmenech")
obtiznost = int(input("Tak kterou?: "))

# Lehká obtížnost
if obtiznost == 1:
    print("Začínáš zlehka. Uvidíme co dokážeš.\nJaké písmeno tipuješ?")
    slovo = list(random.choice(lehka))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        pismeno = input("")
        if pismeno in spatna_pismena:
                print("Tohle už jsi zkoušel a neprošlo ti to červe!")
        if pismeno in slovo:
            pozice_pismene = slovo.index(pismeno)    
            sablona[pozice_pismene] = pismeno
            print(" ".join(sablona)) 
            dobre_pokusy += 1
            if dobre_pokusy == 3:   # Když odhalíme všechny tři písmena
                print(gratulace)
                break    
        else:
            print("Tohle není dobře")
            if pismeno in spatna_pismena:
                print("Tohle už jsi zkoušel a neprošlo ti to červe!")
            spatna_pismena.append(pismeno)
            spatne_pokusy += 1
            if spatne_pokusy == 11:
                print(konec)
                print("Slovo které tě zabilo je", "".join(slovo),".")
                break
            print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")
# Střední obtiznost
elif obtiznost == 2:
    print("Dobrá volba, ale máš na to?.\nJaké písmeno tipuješ?")
    slovo = list(random.choice(stredni))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        pismeno = input("")
        if pismeno in slovo:
            pozice_pismene = slovo.index(pismeno)    
            sablona[pozice_pismene] = pismeno
            print(" ".join(sablona)) 
            dobre_pokusy += 1
            if dobre_pokusy == 5:   # Když odhalíme všech pět písmen
                print(gratulace)
                break
        else:
            print("Tohle není dobře")
            if pismeno in spatna_pismena:
                print("Tohle už jsi zkoušel a neprošlo ti to červe!")
            spatna_pismena.append(pismeno)
            spatne_pokusy += 1
            if spatne_pokusy == 11:
                print(konec)
                print("Slovo které tě zabilo je", "".join(slovo),".")
                break
            print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")
# Těžká obtížnost
elif obtiznost == 3:
    print("HAHA. Ty si myslíš že mě porazíš? Tak se ukaž!.\nJaké písmeno tipuješ?")
    slovo = list(random.choice(tezka))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_", "_", "_", "_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        pismeno = input("")
        if pismeno in slovo:
            pozice_pismene = slovo.index(pismeno)    
            sablona[pozice_pismene] = pismeno
            print(" ".join(sablona)) 
            dobre_pokusy += 1
            if dobre_pokusy == 8:   # Když odhalíme všech osm písmen
                print(gratulace)
                break    
        else:
            print("Tohle není dobře")
            if pismeno in spatna_pismena:
                print("Tohle už jsi zkoušel a neprošlo ti to červe!")
            spatna_pismena.append(pismeno)
            spatne_pokusy += 1
            if spatne_pokusy == 11:
                print(konec)
                print("Slovo které tě zabilo je", "".join(slovo),".")
                break
            print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")
else:
    print("Tahle možnost není možná. Čti pořádně cizinče")
input()