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

print("""
  ___  _                                            
 / _ \| |__   ___  ___  ___ _ __   ___  ___  __   __
| | | | '_ \ / _ \/ __|/ _ \ '_ \ / _ \/ __| \ \ / /
| |_| | |_) |  __/\__ \  __/ | | |  __/ (__   \ V / 
 \___/|_.__/ \___||___/\___|_| |_|\___|\___|   \_/  
                                                    
 _                        _ _ 
| | _____  _ __  _______ | (_)
| |/ / _ \| '_ \|_  / _ \| | |
|   < (_) | | | |/ / (_) | | |
|_|\_\___/|_| |_/___\___/|_|_|v1
                              
""")

# Počet pokusů. 11 je smrt
spatne_pokusy = 0
dobre_pokusy = 0
tipovana_pismena = []

def hadani():
    """smyčka hádání písmen"""
    global pismeno
    global dobre_pokusy
    global spatne_pokusy
    global tipovana_pismena
    pismeno = input("Jaké písmeno tipuješ?\n")
    if pismeno in slovo:
        pozice_pismene = slovo.index(pismeno)    
        sablona[pozice_pismene] = pismeno
        print(" ".join(sablona)) 
        dobre_pokusy += 1
        tipovana_pismena.append(pismeno)
    else:
        print("Tohle není dobře")
        if pismeno in tipovana_pismena:
            print("Tohle už jsi zkoušel a neprošlo ti to červe!")
        tipovana_pismena.append(pismeno)
        spatne_pokusy += 1
        if spatne_pokusy < 11:
            print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")                    

# Uvítání a volba obtížnosti
print("Vítám tě cizinče ve hře ’Obešenec v konzoli’. Dokážeš uhádnout celé slovo?\nNebo se budeš bezvládně houpat na kusu dřeva?")
input("Pokud se nebojíš, stiskni klávesu.")
print("Zvol si obtížnost:")
print("1)lehká - slovo o třech písmenech\n2)střední - slovo o pěti písmenech\n3)těžká - slovo o osmi písmenech")
obtiznost = int(input("Tak kterou?: "))

# Lehká obtížnost
if obtiznost == 1:
    print("Začínáš zlehka. Uvidíme co dokážeš.")
    slovo = list(random.choice(lehka))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        hadani()
        if dobre_pokusy == 3:   # Když odhalíme všechny tři písmena
            print(gratulace)
            break
        if spatne_pokusy == 11:
            print("Slovo které tě zabilo je", "".join(slovo),".")
            break
# Střední obtiznost
elif obtiznost == 2:
    print("Dobrá volba, ale máš na to?.")
    slovo = list(random.choice(stredni))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        hadani()
        if dobre_pokusy == 5:   # Když odhalíme všech pět písmen
            print(gratulace)
            break
        if spatne_pokusy == 11:
            print("Slovo které tě zabilo je", "".join(slovo),".")
            break
        print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")
# Těžká obtížnost
elif obtiznost == 3:
    print("HAHA. Ty si myslíš že mě porazíš? Tak se ukaž!.")
    slovo = list(random.choice(tezka))    # Náhodný výběr slova a přiřazení do seznamu
    sablona = ["_", "_", "_", "_", "_", "_", "_", "_"]   # Šablona slova. Podrtžítka budeme nahrazovat písmeny
    znovu = True
    while znovu:
        hadani()
        if dobre_pokusy == 8:   # Když odhalíme všech osm písmen
            print(gratulace)
            break    
        if spatne_pokusy == 11:
            print(konec)
            print("\nSlovo které tě zabilo je", "".join(slovo),".")
            break
        print("Jetě", 11 - spatne_pokusy, "x špatně, a je po tobě.")
else:
    print("Tahle možnost není možná. Čti pořádně cizinče")
print("\n***Hacker Ninjas North 2022***")
input()
