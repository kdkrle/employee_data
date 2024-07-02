import psycopg2 as pg
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import CTkMessagebox as cmb
import numpy as np


class Radnici:
    """Manipulacija podacima iz tabele 'radnici'."""
    
    def __init__(self):
        self.con = pg.connect(
            database="zaposleni",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.radnici_df = None
    
    def radnici_ucitavanje(self):
        """Osvežavanje podataka tabele 'radnici'."""
        
        self.radnici_df = pd.read_sql_query("SELECT * FROM radnici", self.con)
    
    def id_broj_radnika(self):
        """Generisanje jedinstvenog ID broja (šifre) radnika."""
        
        id_spisak = self.radnici_df.id_radnika.to_list()
        
        id_zaposlenog = ""
        for _ in range(10):
            id_zaposlenog += str(randint(0,9))
        
        if id_zaposlenog in id_spisak:
            self.id_broj_radnika()
        else:
            return id_zaposlenog
    
    def novi_radnik(self, podaci):
        """Unos podataka o novom radniku u tabelu 'radnici' baze podataka."""
        
        novi_radnik_sql = f"""
        INSERT INTO radnici (id_radnika, ime, prezime, adresa, telefon,
        email, pozicija, lokacija, zaposlen, datum_zaposljavanja, istorija)
        VALUES ('{podaci[0]}', '{podaci[1]}', '{podaci[2]}', '{podaci[3]}',
        '{podaci[4]}', '{podaci[5]}', '{podaci[6]}', '{podaci[7]}', 'True',
        '{podaci[8]}', '{podaci[9]}')
        """
        
        kursor = self.con.cursor()
        kursor.execute(novi_radnik_sql)
        self.con.commit()
        # Kursor se zatvara ovde, a konekcija pritiskom na dugme 'Odustani',
        # inače, posle unosa podtaka o prvom radniku, sledeći podaci ne mogu da
        # se unesu dok se forma ne zatvori i ponovo otvori.
        kursor.close()
        
        self.radnici_ucitavanje()

    def df_sortiranje(self, df):
        """Sortiranje Dataframe podataka po prezimenima i vraćanje soritirane
        liste imena i prezimena, s id brojem."""
        
        prezime_ime_sort_df = df.sort_values(by=["prezime", "ime"])
        
        lista_imena = prezime_ime_sort_df.ime.to_list()
        lista_prezimena = prezime_ime_sort_df.prezime.to_list()
        id_lista = prezime_ime_sort_df.id_radnika.to_list()
        
        lista_radnika = []
        for i in range(len(id_lista)):
            # Sortiranje se vrši po prezmenu/imenu, ali, budući da je moguće
            # da postoje ista imena i prezimena, potrebno je da postoji i ID
            # koji će ih razlikovati.
            id_prezime_ime = f"{lista_prezimena[i]} {lista_imena[i]} - " \
                             f"{id_lista[i]}"
            
            lista_radnika.append(id_prezime_ime)
            
        return lista_radnika

    def azuriranje(self, dict, id, dodatak, zaposlen):
        """Ažuriranje podataka tabele 'radnici' novim podacima."""
        
        try:
            kursor = self.con.cursor()
    
            for key, value in dict.items():
                if value:
                    if key == "datum_zaposljavanja":
                        # Ukoliko se bivši radnik ponovo zapošljava,
                        # potrebno je izbrisati datum prestanka radnog odnosa.
                        azuriranje_sql = f"""
                        UPDATE radnici
                        SET prestanak_radnog_odnosa = null
                        WHERE id_radnika = '{id}';
                        UPDATE radnici
                        SET {key} = '{value}'
                        WHERE id_radnika = '{id}';
                        """
                    else:
                        azuriranje_sql = f"""
                        UPDATE radnici
                        SET {key} = '{value}'
                        WHERE id_radnika = '{id}'
                        """
                    
                    kursor.execute(azuriranje_sql)
                    self.con.commit()
            
            if dodatak:
                istorija_sql = f"""
                UPDATE radnici
                SET istorija = istorija || '{dodatak}',
                    zaposlen = '{zaposlen}'
                WHERE id_radnika = '{id}'
                """
                
                kursor.execute(istorija_sql)
                self.con.commit()
            # Kursor se zatvara ovde, a konekcija se zatvara pritiskom na
            # dugme 'Zatvori' prozora za ažuriranje.
            kursor.close()
            
        except:
            cmb.CTkMessagebox(
                title="Greška",
                message="Greška prilikom ažuriranja",
                icon="warning",
                button_width=50,
                font=("Calbri", 18)
            )
        else:
            cmb.CTkMessagebox(
                title="Uspešno ažuriranje",
                message="Ažuriranje podataka uspešno izvršeno",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        finally:
            self.radnici_ucitavanje()
    
    def broj_po_godini_zaposljavanja(self):
        """Broj trenutno zaposlenih po godini u kojoj su zaposleni."""
        
        # Potrebni podaci.
        zaposleni_df = self.radnici_df[self.radnici_df.zaposlen == True]
        
        datumi_zaposljavanja = zaposleni_df.datum_zaposljavanja.to_list()
        godine_zaposljavanja = []
        for datum in datumi_zaposljavanja:
            year = datum.year
            godine_zaposljavanja.append(year)
        
        godine_sortirano = sorted(list(set(godine_zaposljavanja)))
        
        lista_br_zaposlenih_po_godini = []
        for god in godine_sortirano:
            br_zaposlenih = godine_zaposljavanja.count(god)
            lista_br_zaposlenih_po_godini.append(br_zaposlenih)
        
        # Grafik.
        plt.figure(figsize=(12, 8))
        
        plt.plot(
            godine_sortirano,
            lista_br_zaposlenih_po_godini,
            marker="o",
            color="tab:green",
            markerfacecolor="tab:olive",
            linestyle="-."
        )
        plt.title(
            "BROJ ZAPOSLENIH PO GODNI ZAPOŠLJAVANJA",
            fontdict={"family": "Calibri", "color": "darkolivegreen",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        plt.xlabel(
            "Godine",
            fontdict={"family": "Calibri", "color": "darkolivegreen",
                      "size": 16, "weight": "bold"},
            labelpad=30
        )
        plt.ylabel(
            "Broj zaposlenih",
            fontdict={"family": "Calibri", "color": "darkolivegreen",
                      "size": 16, "weight": "bold"},
            labelpad=30
        )
        plt.xticks(rotation=80)
        plt.xticks(np.arange(1997, 2025, step=1))
        plt.grid()
        plt.subplots_adjust(bottom=0.2)
        
        plt.show()
    
    def broj_zaposlenih_po_pozicijama(self):
        """Stubični prikaz broja zaposlenih po pozicijama."""
        
        # Potrebni podaci.
        pozicije_u_firmi = set(self.radnici_df.pozicija.to_list())
        pozicije_sortirano = sorted(list(pozicije_u_firmi), reverse=True)
        
        broj_zaposlenih_lista = []
        for poz in pozicije_sortirano:
            br_po_jednoj_poziciji = self.radnici_df.pozicija[
                (self.radnici_df.pozicija == poz) &
                (self.radnici_df.zaposlen == True)
            ].count()
            broj_zaposlenih_lista.append(br_po_jednoj_poziciji)
            
        # Grafik.
        plt.figure(figsize=(10, 8))
        
        plt.barh(pozicije_sortirano, broj_zaposlenih_lista, color="olivedrab")
        plt.title(
            "Broj zaposlenih po pozicijama".upper(),
            fontdict={"family": "Calibri", "color": "darkolivegreen", "size":
                22, "weight": "bold"},
            pad=30
        )
        plt.xlabel(
            "Broj zaposlenih",
            fontdict={"family": "Calibri", "color": "darkolivegreen", "size":
                16, "weight": "bold"},
            labelpad=10
        )
        plt.ylabel(
            "Pozicije",
            fontdict={"family": "Calibri", "color": "darkolivegreen",
                      "size": 16, "weight": "bold"},
            labelpad=20
        )
        plt.grid()
        plt.subplots_adjust(left=0.3, right=0.95)
        
        plt.show()
    
    def broj_zaposlenih_po_radnim_mestima(self):
        """Stubični prikaz broja zaposlenih po radnim mestima."""
        
        # Potrebni podaci.
        radna_mesta_nazivi = sorted(lokacije.lokacije_df.pun_naziv.to_list(),
                                    reverse=True)
        radna_mesta_sifre = []
        for naziv in radna_mesta_nazivi:
            sifra_rm = lokacije.lokacije_df.sifra[
                lokacije.lokacije_df.pun_naziv == naziv].to_string(index=False)
            radna_mesta_sifre.append(sifra_rm)
        
        broj_zaposlenih_lista = []
        for sfr in radna_mesta_sifre:
            br_po_radnom_mestu = self.radnici_df.lokacija[
                (self.radnici_df.lokacija == sfr) &
                (self.radnici_df.zaposlen == True)
            ].count()
            broj_zaposlenih_lista.append(br_po_radnom_mestu)
        
        # Grafik.
        plt.figure(figsize=(12, 8))

        plt.barh(radna_mesta_nazivi, broj_zaposlenih_lista,
                 color="mediumorchid")
        plt.title("Broj zaposlenih po radnim mestima".upper(),
            fontdict={"family": "Calibri", "color": "indigo",
                      "size": 22, "weight": "bold"}, pad=30)
        plt.xlabel("Broj zaposlenih",
            fontdict={"family": "Calibri", "color": "indigo",
                      "size": 16, "weight": "bold"}, labelpad=10)
        plt.ylabel("Radna mesta",
            fontdict={"family": "Calibri", "color": "indigo",
                      "size": 16, "weight": "bold"}, labelpad=20)
        plt.grid()
        plt.subplots_adjust(left=0.2, right=0.95)

        plt.show()
        
    def broj_zaposlenih_po_sektorima(self):
        """Dijagram broja zaposlenih po sektorima."""
        
        # Potrebni podaci.
        sektori_firme = set(pozicije.pozicije_df.sektor.to_list())
        sektori_sortirano = sorted(list(sektori_firme))
        
        rm_svih_sektora = []
        for sek in sektori_sortirano:
            rm_jednog_sektora = pozicije.pozicije_df.naziv[
                pozicije.pozicije_df.sektor == sek].to_list()
            rm_svih_sektora.append(rm_jednog_sektora)
        
        zaposleni_df = self.radnici_df[self.radnici_df.zaposlen == True]
        
        br_po_sektorima_lista = []
        for rm in rm_svih_sektora:
            br_po_radnim_mestima = 0
            for i in range(len(rm)):
                broj_na_jednom_rm = zaposleni_df.pozicija[
                    self.radnici_df.pozicija == rm[i]].count()
                br_po_radnim_mestima += broj_na_jednom_rm
            
            br_po_sektorima_lista.append(br_po_radnim_mestima)
        
        # Grafik.
        plt.figure(figsize=(8, 8))
        
        plt.pie(
            br_po_sektorima_lista,
            labels=sektori_sortirano,
            autopct="%.1f%%",
            colors=["tomato", "cornflowerblue", "yellowgreen", "orchid",
                    "gold", "burlywood"],
            startangle=90
        )
        plt.title(
            label="Procenat zaposlenih u svakom sektoru".upper(),
            fontdict={"family": "Calibri", "color": "darkgoldenrod",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        
        plt.show()
        
    def odnos_zaposleni_bivsi(self):
        """Dijagram odnosa trenutno zaposlenih i onih koji su ranije
        radili u firmi."""
        
        # Potrebni podaci.
        status_zaposlenja = ["Trenutno zaposleni", "Ranije zaposleni"]
        
        br_trenutno_zaposlenih = self.radnici_df.zaposlen[
            self.radnici_df.zaposlen == True].count()
        br_ranije_zaposlenih = self.radnici_df.zaposlen[
            self.radnici_df.zaposlen == False].count()
        trenutno_ranije_zaposleni = [br_trenutno_zaposlenih,
                                     br_ranije_zaposlenih]
        
        # Grafik.
        plt.figure(figsize=(8, 8))
        
        plt.pie(
            trenutno_ranije_zaposleni,
            labels=status_zaposlenja,
            autopct="%.1f%%",
            colors=["tab:blue", "tab:cyan"],
            startangle=90
        )
        plt.title(
            label="Odnos trenutno i ranije zaposlenih".upper(),
            fontdict={"family": "Calibri", "color": "tab:gray",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        
        plt.show()
    
    def odnos_mobilni_fiksni(self):
        """Odnos zaposlenih koji imaju mobilni telefon i onih koji koriste
        fiksni telefon."""
        
        # Potrebni podaci.
        zaposleni_df = self.radnici_df[self.radnici_df.zaposlen == True]
        telefoni_lista = zaposleni_df.telefon.to_list()
        
        ukupno_mobilnih = 0
        ukupno_fiksnih = 0
        for telefon in telefoni_lista:
            if telefon[:3] == "011":
                ukupno_fiksnih += 1
            else:
                ukupno_mobilnih += 1
        
        broj_mobilnih_i_fiksnih = [ukupno_mobilnih, ukupno_fiksnih]
        tel_status = ["Mobilni telefoni", "Fiksni telefoni"]
        
        # Grafik.
        plt.figure(figsize=(8, 8))
        
        plt.pie(
            broj_mobilnih_i_fiksnih,
            labels=tel_status,
            autopct="%.1f%%",
            colors=["tab:red", "tab:orange"],
            startangle=90
        )
        plt.title(
            label="Odnos zaposlenih s mobilnim i fiksnim telefonom".upper(),
            fontdict={"family": "Calibri", "color": "tab:brown",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        
        plt.show()
    
    def email_odnos(self):
        """Odnos zaposlenih koji imaju email i onih koji ga nemaju."""
        
        # Potrebni podaci.
        zaposleni_df = self.radnici_df[self.radnici_df.zaposlen == True]
        
        bez_emaila = len(zaposleni_df.email[(zaposleni_df.email.isnull()) | (
            zaposleni_df.email == "")])
        sa_emailom = len(zaposleni_df.email) - bez_emaila
        broj_sa_i_bez_email = [sa_emailom, bez_emaila]
        email_status = ["Sa emailom", "Bez emaila"]
        
        # Grafik.
        plt.figure(figsize=(8, 8))

        plt.pie(
            broj_sa_i_bez_email,
            labels=email_status,
            autopct="%.1f%%",
            colors=["tab:purple", "tab:pink"],
            startangle=90
        )
        plt.title(
            label="Odnos zaposlenih sa i bez emaila".upper(),
            fontdict={"family": "Calibri", "color": "indigo", "size": 22,
                      "weight": "bold"},
            pad=20
        )

        plt.show()
    
    def odnos_po_radnom_mestu(self):
        """Odnos ranije i trenutno zaposlenih po radnom mestu."""
        
        # Potrebni podaci.
        spisak_rm_sifri = set(self.radnici_df.lokacija.to_list())
        sifre_rm_sortirano = sorted(list(spisak_rm_sifri), reverse=True)
        
        rm_sortirano = []
        for sfr in sifre_rm_sortirano:
            radno_mesto = lokacije.lokacije_df.pun_naziv[
                lokacije.lokacije_df.sifra == sfr].to_string(index=False)
            rm_sortirano.append(radno_mesto)
            
        trenutno_zaposleni_df = self.radnici_df[
            self.radnici_df.zaposlen == True]
        ranije_zaposleni_df = self.radnici_df[
            self.radnici_df.zaposlen == False]
        
        br_trenutno_zaposlenih = []
        for rm in sifre_rm_sortirano:
            trenutno_zaposleni_po_rm = trenutno_zaposleni_df.lokacija[
                trenutno_zaposleni_df.lokacija == rm].count()
            br_trenutno_zaposlenih.append(trenutno_zaposleni_po_rm)

        br_ranije_zaposlenih = []
        for rm in sifre_rm_sortirano:
            ranije_zaposleni_po_rm = ranije_zaposleni_df.lokacija[
                ranije_zaposleni_df.lokacija == rm].count()
            br_ranije_zaposlenih.append(ranije_zaposleni_po_rm)
        
        odnosi_ranije_trenutno = []
        for i in range(len(br_trenutno_zaposlenih)):
            odnos = round(br_ranije_zaposlenih[i]/br_trenutno_zaposlenih[i], 3)
            odnosi_ranije_trenutno.append(odnos)
        
        # Grafik.
        plt.figure(figsize=(12, 8))

        plt.plot(
            odnosi_ranije_trenutno,
            rm_sortirano,
            marker="o",
            color="tab:red",
            markerfacecolor="tab:orange",
            linestyle="--"
        )
        plt.title(
            "ODNOS RANIJE I TRENUTNO ZAPOSLENIH PO RADNOM MESTU\nveći "
            "odnos - veći procenat ranije u odnosu na trenutno zaposlene",
            fontdict={"family": "Calibri", "color": "tab:brown",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        plt.xlabel(
            "Odnos ranije i trenutno zaposlenih",
            fontdict={"family": "Calibri", "color": "tab:brown",
                      "size": 16, "weight": "bold"},
            labelpad=20
        )
        plt.ylabel(
            "Radna mesta",
            fontdict={"family": "Calibri", "color": "tab:brown",
                      "size": 16, "weight": "bold"}
        )
        plt.xticks(np.arange(0, 1.1, step=0.1))
        plt.grid()
        plt.subplots_adjust(right=0.95, left=0.18, bottom=0.15, top=0.85)

        plt.show()

    def odnos_po_poziciji(self):
        """Odnos ranije i trenutno zaposlenih po poziciji."""
    
        # Potrebni podaci.
        spisak_pozicija = set(self.radnici_df.pozicija.to_list())
        pozicije_sortirano = sorted(list(spisak_pozicija), reverse=True)

        trenutno_zaposleni_df = self.radnici_df[
            self.radnici_df.zaposlen == True]
        ranije_zaposleni_df = self.radnici_df[
            self.radnici_df.zaposlen == False]

        br_trenutno_zaposlenih = []
        for poz in pozicije_sortirano:
            trenutno_zaposleni_po_poz = trenutno_zaposleni_df.pozicija[
                trenutno_zaposleni_df.pozicija == poz].count()
            br_trenutno_zaposlenih.append(trenutno_zaposleni_po_poz)

        br_ranije_zaposlenih = []
        for poz in pozicije_sortirano:
            ranije_zaposleni_po_poz = ranije_zaposleni_df.pozicija[
                ranije_zaposleni_df.pozicija == poz].count()
            br_ranije_zaposlenih.append(ranije_zaposleni_po_poz)
        
        odnosi_ranije_trenutno = []
        for i in range(len(br_trenutno_zaposlenih)):
            odnos = round(br_ranije_zaposlenih[i]/br_trenutno_zaposlenih[i], 3)
            odnosi_ranije_trenutno.append(odnos)

        # Grafik.
        plt.figure(figsize=(12, 8))

        plt.plot(
            odnosi_ranije_trenutno,
            pozicije_sortirano,
            marker="o",
            color="tab:blue",
            markerfacecolor="tab:cyan",
            linestyle=":")
        plt.title(
            "ODNOS RANIJE I TRENUTNO ZAPOSLENIH PO POZICIJI\nveći "
            "odnos - veći procenat ranije u odnosu na trenutno zaposlene",
            fontdict={"family": "Calibri", "color": "tab:gray",
                      "size": 22, "weight": "bold"},
            pad=20
        )
        plt.xlabel(
            "Odnos ranije i trenutno zaposlenih",
            fontdict={"family": "Calibri", "color": "tab:gray",
                      "size": 16, "weight": "bold"},
            labelpad=20
        )
        plt.ylabel(
            "Pozicije",
            fontdict={"family": "Calibri", "color": "tab:gray",
                      "size": 16, "weight": "bold"},
            labelpad=20
        )
        plt.xticks(np.arange(0, 1.1, step=0.1))
        plt.grid()
        plt.subplots_adjust(right=0.95, left=0.24, bottom=0.15, top=0.85)

        plt.show()


class Pozicije:
    """Manipulacija podacima iz tabele 'pozicije'."""
    
    def __init__(self):
        self.con = pg.connect(
            database="zaposleni",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.pozicije_df = None
    
    def pozicije_ucitavanje(self):
        """Osvežavanje podataka tabele 'pozicije'."""
        
        self.pozicije_df = pd.read_sql_query("SELECT * FROM pozicije",
                                                self.con)


    def broj_pozicija_po_sektorima(self):
        """Grafik broja radnih pozicija po svakom sektoru."""
        
        # Potrebni podaci.
        sektori_firme = set(self.pozicije_df.sektor.to_list())
        sektori_sortirano = sorted(list(sektori_firme))
        
        broj_pozicija_lista = []
        for sek in sektori_sortirano:
            br_jednog_sektora = self.pozicije_df.naziv[
                self.pozicije_df.sektor == sek].count()
            broj_pozicija_lista.append(br_jednog_sektora)
        
        # Grafik.
        plt.figure(figsize=(10, 7))
        
        plt.bar(sektori_sortirano, broj_pozicija_lista, color="orange")
        plt.title(
            "Broj pozicija po sektorima".upper(),
            fontdict={"family": "Calibri", "color": "darkgoldenrod", "size":
                22, "weight": "bold"},
            pad=30
        )
        plt.xlabel(
            "Sektori",
            fontdict={"family": "Calibri", "color": "darkgoldenrod", "size":
                16, "weight": "bold"},
            labelpad=10
        )
        plt.ylabel(
            "Broj pozicija",
            fontdict={"family": "Calibri", "color": "darkgoldenrod", "size":
                16, "weight": "bold"},
            labelpad=20
        )
        plt.xticks(rotation=60)
        plt.grid()
        plt.subplots_adjust(bottom=0.25)
        
        plt.show()


class Lokacije:
    """Manipulacija podacima iz tabele 'lokacije'."""
    
    def __init__(self):
        self.con = pg.connect(
            database="zaposleni",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.lokacije_df = None
    
    def lokacije_ucitavanje(self):
        """Osvežavanje podataka tabele 'lokacije'."""
        
        self.lokacije_df = pd.read_sql_query("SELECT * FROM lokacije",
                                             self.con)


radnici = Radnici()
radnici.radnici_ucitavanje()
pozicije = Pozicije()
pozicije.pozicije_ucitavanje()
lokacije = Lokacije()
lokacije.lokacije_ucitavanje()
