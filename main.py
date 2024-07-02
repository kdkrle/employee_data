from radnici import *
from tkcalendar import DateEntry
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()
root.title("Podaci o zaposlenima i radnim mestima")
root.resizable(False, False)
root.iconbitmap("pics/logo_icon.ico")


def len_char_limit(inp):
    """Ograničavanje broja i vrste karaktera (samo brojevi)."""
    
    if inp.isdigit() and len(inp) <= 10:
        return True
    elif inp == "":
        return True
    else:
        return False


def zatvaranje_aplickacije():
    """Pitanje o zatvaranju aplikacije."""
    
    msg = cmb.CTkMessagebox(
        title="Zatvaranje aplikacije",
        message="Da li želite da izađete iz aplikacije?",
        icon="warning",
        option_1="Ne",
        option_2="Da",
        button_width=50
    )
    
    odgovor = msg.get()
    
    if odgovor == "Da":
        root.destroy()


def novi_radnici():
    """Forma za unošenje podataka o novim radnicima."""
    
    def novi_radnik_unos_podataka():
        """Unos podataka o novom radniku u tabelu 'radnici'."""
        
        if not ime_unos_ent.get():
            cmb.CTkMessagebox(
                title="Nedostaje ime",
                message="Niste uneli ime novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        elif not prezime_unos_ent.get():
            cmb.CTkMessagebox(
                title="Nedostaje prezime",
                message="Niste uneli prezime novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        elif not adresa_unos_ent.get():
            cmb.CTkMessagebox(
                title="Nedostaje adresa",
                message="Niste uneli adresu novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        elif not telefon_unos_ent.get():
            cmb.CTkMessagebox(
                title="Nedostaje telefon",
                message="Niste uneli telefon novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        elif not pozicija_combo.get():
            cmb.CTkMessagebox(
                title="Nedostaje pozicija",
                message="Niste izabrali naziv pozicije novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        elif not lokacija_combo.get():
            cmb.CTkMessagebox(
                title="Nedostaje lokacija",
                message="Niste uneli radno mesto novog radnika.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
        else:
            radno_mesto = lokacije.lokacije_df.sifra[
                lokacije.lokacije_df.pun_naziv == lokacija_combo.get()
            ].to_string(index=False)
            
            # Dodavanje teksta o datumu zapošljavanja u kolonu 'istorija'.
            istorija_txt = f"Zaposlen: {datum_zaposljavanja_de.get()};"
            
            podaci_za_unos = [
                id_vrednost.cget("text"),
                ime_unos_ent.get(),
                prezime_unos_ent.get(),
                adresa_unos_ent.get(),
                telefon_unos_ent.get(),
                email_unos_ent.get(),
                pozicija_combo.get(),
                radno_mesto,
                datum_zaposljavanja_de.get_date(),
                istorija_txt
            ]
            
            radnici.novi_radnik(podaci_za_unos)
            
            cmb.CTkMessagebox(
                title="Uspešan unos",
                message="Podaci o novom radniku su uspešno uneseni.",
                icon="info",
                button_width=50,
                font=("Calibri", 18)
            )
            
            # Brisanje unetih podataka.
            ime_unos_ent.delete(0, "end")
            prezime_unos_ent.delete(0, "end")
            adresa_unos_ent.delete(0, "end")
            telefon_unos_ent.delete(0, "end")
            email_unos_ent.delete(0, "end")
            pozicija_combo.set("")
            lokacija_combo.set("")
            
            # Generisanje novog ID broja radnika.
            novi_id_broj = radnici.id_broj_radnika()
            id_vrednost.configure(text=novi_id_broj)
    
    # Nova forma za unos podataka o novim radnicima.
    novi_radnici_tl = ctk.CTkToplevel(root)
    novi_radnici_tl.title("Podaci o novom radniku")
    novi_radnici_tl.resizable(False, False)
    novi_radnici_tl.attributes("-topmost", "true")
    novi_radnici_tl.grab_set()
    
    # CustomTkinter ima bag kada je u pitanju postavljanje ikone na Toplevel
    # formu, pa zbog toga ne može da se koristi samo 'iconbitmap' komanda.
    novi_radnici_tl.after(200, lambda: novi_radnici_tl.iconbitmap(
        "pics/logo_icon.ico"))
    
    # Okviri za određene grupe podataka.
    nr_logo_naslov_frm = ctk.CTkFrame(novi_radnici_tl, fg_color="transparent")
    sifra_frm = ctk.CTkFrame(
        novi_radnici_tl,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    licni_podaci_frm = ctk.CTkFrame(
        novi_radnici_tl,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    zaposlenje_frm = ctk.CTkFrame(
        novi_radnici_tl,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    info_frm = ctk.CTkFrame(novi_radnici_tl, fg_color="transparent")
    unos_dugmad_frm = ctk.CTkFrame(novi_radnici_tl, fg_color="transparent")

    nr_logo_naslov_frm.pack(expand=True, fill= "x", pady=10)
    sifra_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    licni_podaci_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    zaposlenje_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    info_frm.pack(expand=True, fill="x", padx=40, pady=10)
    unos_dugmad_frm.pack(expand=True, fill="x", padx=20, pady=20)
    
    # Logo i naslov.
    nr_logo_naslov_frm.grid_columnconfigure((0, 1), weight=1)
    logo_nr_lbl = ctk.CTkLabel(
        nr_logo_naslov_frm,
        image=logo_manja,
        text="",
        fg_color="transparent"
    )
    logo_nr_lbl.grid(column=0, row=0)
    
    naslov_nr_lbl = ctk.CTkLabel(
        nr_logo_naslov_frm,
        text="UNOS PODATAKA O\nNOVOM RADNIKU",
        fg_color="transparent",
        text_color="khaki",
        font=("Calibri", 40, "bold")
    )
    naslov_nr_lbl.grid(column=1, row=0, padx=20)
    
    # Šifra.
    sifra_frm.grid_columnconfigure(0, weight=1)
    id_lbl = ctk.CTkLabel(
        sifra_frm,
        fg_color="black",
        text="ID radnika",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    id_lbl.grid(column=0, row=0, sticky="ew", padx=2, pady=2)
    
    id_broj = radnici.id_broj_radnika()
    id_vrednost = ctk.CTkLabel(
        sifra_frm,
        fg_color="transparent",
        text=id_broj,
        font=("Calibri", 20, "bold")
    )
    id_vrednost.grid(column=0, row=1, sticky="ew", padx=2, pady=10)
    
    # Lični podaci.
    licni_podaci_frm.grid_columnconfigure((0, 1), weight=1)
    licni_podaci_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="black",
        text="Lični podaci",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    licni_podaci_lbl.grid(column=0, row=0, columnspan= 2, sticky="ew",
                          padx=2, pady=2)
    
    ime_unos_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="transparent",
        text="Ime*",
        font=("Calibri", 16),
        anchor="w"
    )
    ime_unos_lbl.grid(column=0, row=1, sticky="ew", padx=20, pady=(10, 0))
    
    ime_unos_ent = ctk.CTkEntry(
        licni_podaci_frm,
        width=200,
        font=("Calibri", 16)
    )
    ime_unos_ent.grid(column=0, row=2, sticky="w", padx=20, pady=(0, 10))

    prezime_unos_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="transparent",
        text="Prezime*",
        font=("Calibri", 16),
        anchor="w"
    )
    prezime_unos_lbl.grid(column=1, row=1, sticky="ew", padx=20, pady=(10, 0))

    prezime_unos_ent = ctk.CTkEntry(
        licni_podaci_frm,
        width=200,
        font=("Calibri", 16)
    )
    prezime_unos_ent.grid(column=1, row=2, sticky="w", padx=20, pady=(0, 10))

    adresa_unos_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="transparent",
        text="Adresa*",
        font=("Calibri", 16),
        anchor="w"
    )
    adresa_unos_lbl.grid(column=0, row=3, sticky="ew", padx=20, pady=(10, 0))

    adresa_unos_ent = ctk.CTkEntry(
        licni_podaci_frm,
        width=200,
        font=("Calibri", 16)
    )
    adresa_unos_ent.grid(column=0, row=4, sticky="w", padx=20, pady=(0, 10))

    telefon_unos_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="transparent",
        text="Telefon*",
        font=("Calibri", 16),
        anchor="w"
    )
    telefon_unos_lbl.grid(column=1, row=3, sticky="ew", padx=20, pady=(10, 0))

    tel_reg = licni_podaci_frm.register(len_char_limit)
    telefon_unos_ent = ctk.CTkEntry(
        licni_podaci_frm,
        width=200,
        font=("Calibri", 16),
        validate="key",
        validatecommand=(tel_reg, "%P")
    )
    telefon_unos_ent.grid(column=1, row=4, sticky="w", padx=20, pady=(0, 10))

    email_unos_lbl = ctk.CTkLabel(
        licni_podaci_frm,
        fg_color="transparent",
        text="Email",
        font=("Calibri", 16),
        anchor="w"
    )
    email_unos_lbl.grid(column=0, row=5, sticky="ew", padx=20, pady=(10, 0))

    email_unos_ent = ctk.CTkEntry(
        licni_podaci_frm,
        width=200,
        font=("Calibri", 16)
    )
    email_unos_ent.grid(column=0, row=6, sticky="w", padx=20, pady=(0, 20))
    
    # Podaci o zaposlenju.
    zaposlenje_frm.grid_columnconfigure((0, 1), weight=1)
    podaci_zaposlenje_lbl = ctk.CTkLabel(
        zaposlenje_frm,
        fg_color="black",
        text="Podaci o zaposlenju",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    podaci_zaposlenje_lbl.grid(column=0, row=0, columnspan= 2, sticky="ew",
                               padx=2, pady=2)

    pozicija_lbl = ctk.CTkLabel(
        zaposlenje_frm,
        fg_color="transparent",
        text="Pozicija*",
        font=("Calibri", 16),
        anchor="w"
    )
    pozicija_lbl.grid(column=0, row=1, sticky="ew", padx=20, pady=(10, 0))

    spisak_pozicija = pozicije.pozicije_df.naziv.to_list()
    spisak_pozicija.sort()
    pozicija_combo = ctk.CTkComboBox(
        zaposlenje_frm,
        width=200,
        dropdown_font=("Calibri", 16),
        state="readonly",
        values=spisak_pozicija
    )
    pozicija_combo.grid(column=0, row=2, sticky="w", padx=20, pady=(0, 10))

    lokacija_lbl = ctk.CTkLabel(
        zaposlenje_frm,
        fg_color="transparent",
        text="Radno mesto*",
        font=("Calibri", 16),
        anchor="w"
    )
    lokacija_lbl.grid(column=1, row=1, sticky="ew", padx=20, pady=(10, 0))

    spisak_radnih_mesta = lokacije.lokacije_df.pun_naziv.to_list()
    lokacija_combo = ctk.CTkComboBox(
        zaposlenje_frm,
        width=200,
        dropdown_font=("Calibri", 16),
        state="readonly",
        values=spisak_radnih_mesta
    )
    lokacija_combo.grid(column=1, row=2, sticky="w", padx=20, pady=(0, 10))

    datum_zaposljavanja_lbl = ctk.CTkLabel(
        zaposlenje_frm,
        fg_color="transparent",
        text="Datum zapošljavanja*",
        font=("Calibri", 16),
        anchor="w"
    )
    datum_zaposljavanja_lbl.grid(column=0, row=3, sticky="ew", padx=20,
                                 pady=(10, 0))

    datum_zaposljavanja_de = DateEntry(
        zaposlenje_frm,
        width=22,
        font=("Calibri", 12),
        date_pattern='dd. mm. y.'
    )
    datum_zaposljavanja_de.grid(column=0, row=4, sticky="w", padx=20,
                                pady=(0, 20))
    
    # Informacija o popunjavanju polja.
    info_lbl = ctk.CTkLabel(
        info_frm,
        fg_color="transparent",
        text="Obavezno je popunjavanje polja iza kojih stoji znak *",
        text_color="khaki",
        font=("Calibri", 16)
    )
    info_lbl.pack(side="left")
    
    # Dugme za izlazak i dugme za unos podataka o novom radniku.
    odustani_btn = ctk.CTkButton(
        unos_dugmad_frm,
        text="Odustani",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=lambda: [novi_radnici_tl.destroy(), radnici.con.close()]
    )
    odustani_btn.pack(side="right", padx=10)
    
    unesi_btn = ctk.CTkButton(
        unos_dugmad_frm,
        text="Unesi",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=novi_radnik_unos_podataka
    )
    unesi_btn.pack(side="right", padx=10)


def pregled_podataka():
    """Uvid u podatke o pojedinačnim radnicima."""
    
    def izabrani_radnik(event):
        """Promene koje se dešavaju prilikom izbora radnika."""
        
        radnikov_id = izbor_combo.get()[-10:]
        radnikovi_podaci = radnici.radnici_df[
            radnici.radnici_df.id_radnika == radnikov_id
        ].values.flatten().tolist()
        
        lista_polja_za_popunjavanje = [
            ime_i_prezime_val,
            id_zaposlenog_val,
            adresa_val,
            telefon_val,
            email_val,
            pozicija_val,
            radno_mesto_val,
            istorija_zaposlenog_val,
            zaposlen_val,
            datum_zaposlavanja_val,
            prestanak_odnosa_val
        ]
        
        for label in lista_polja_za_popunjavanje:
            label.configure(text="")
        
        # Ime i prezime
        ime_i_prezime_str = f"{radnikovi_podaci[2]} {radnikovi_podaci[1]}"
        ime_i_prezime_val.configure(text=ime_i_prezime_str)
        
        # ID
        id_zaposlenog_val.configure(text=radnikovi_podaci[0])
        
        # Adresa
        adresa_val.configure(text=radnikovi_podaci[3])
        
        # Telefon
        telefon_val.configure(text=radnikovi_podaci[4])
        
        # Email
        email_val.configure(text=radnikovi_podaci[5])
        
        # Pozicija
        pozicija_val.configure(text=radnikovi_podaci[6])
        
        # Radno mesto
        radno_mesto_str = lokacije.lokacije_df.pun_naziv[
            lokacije.lokacije_df.sifra == radnikovi_podaci[7]
        ].to_string(index=False)
        radno_mesto_val.configure(text=radno_mesto_str)
        
        # Istorija radnika
        istorija_sredjeno = radnikovi_podaci[8].replace(";", "\n")
        istorija_zaposlenog_val.configure(text=istorija_sredjeno)
        
        # Zaposlen
        if radnikovi_podaci[9]:
            zaposlen = "Da"
        else:
            zaposlen = "Ne"
        
        zaposlen_val.configure(text=zaposlen)
        
        # Datum zapošljavanja
        datum_zaposljavanja_str = radnikovi_podaci[10].strftime("%d. %m. %Y.")
        datum_zaposlavanja_val.configure(text=datum_zaposljavanja_str)
        
        # Datum prestanka radnog odnosa
        if radnikovi_podaci[11]:
            prekid_odnosa_str = radnikovi_podaci[11].strftime("%d. %m. %Y.")
            prestanak_odnosa_val.configure(text=prekid_odnosa_str)

    pregled_tl = ctk.CTkToplevel(root)
    pregled_tl.title("Podaci o novom radniku")
    pregled_tl.resizable(False, False)
    pregled_tl.attributes("-topmost", "true")
    pregled_tl.grab_set()
    pregled_tl.after(200, lambda: pregled_tl.iconbitmap(
        "pics/logo_icon.ico"))

    # Okvir za logo i naslov i okvir za podatke.
    pregled_logo_naslov_frm = ctk.CTkFrame(pregled_tl, fg_color="transparent")
    izbor_frm = ctk.CTkFrame(pregled_tl, fg_color="transparent")
    podaci_frm = ctk.CTkFrame(pregled_tl, fg_color="transparent")
    
    pregled_logo_naslov_frm.pack(expand=True, fill="x", pady=10)
    izbor_frm.pack(expand=True, fill="x", pady=10)
    podaci_frm.pack(expand=True, fill="x", pady=10)
    zatvori_pregled_btn = ctk.CTkButton(
        pregled_tl,
        text="Zatvori",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=pregled_tl.destroy
    )
    zatvori_pregled_btn.pack(padx=40, pady=40, anchor="e")
    
    # Logo i naslov.
    pregled_logo_naslov_frm.grid_columnconfigure((0, 1), weight=1)
    logo_pregled_lbl = ctk.CTkLabel(
        pregled_logo_naslov_frm,
        image=logo_manja,
        text="",
        fg_color="transparent"
    )
    logo_pregled_lbl.grid(column=0, row=0)

    naslov_pregled_lbl = ctk.CTkLabel(
        pregled_logo_naslov_frm,
        text="PREGLED PODATAKA O TRENUTNIM I BIVŠIM RADNICIMA",
        fg_color="transparent",
        text_color="khaki",
        font=("Calibri", 40, "bold")
    )
    naslov_pregled_lbl.grid(column=1, row=0, padx=20)
    
    # Izbor radnika (Label + ComboBox).
    izbor_lbl = ctk.CTkLabel(
        izbor_frm,
        text="Izbor radnika:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="w"
    )
    izbor_lbl.grid(column=0, row=0, padx=30, pady=(20, 0), sticky="w")
    
    prezime_ime_id = radnici.df_sortiranje(radnici.radnici_df)
    izbor_combo = ctk.CTkComboBox(
        izbor_frm,
        dropdown_font=("Calibri", 20),
        state="readonly",
        values=prezime_ime_id,
        width=250,
        command=izabrani_radnik
    )
    izbor_combo.grid(column=0, row=1, padx=30, pady=(0, 20), sticky="w")
    
    # Podaci o radniku.
    ime_i_prezime_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Ime i prezime:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    ime_i_prezime_lbl.grid(column=0, row=0, padx=(30, 15), pady=10)
    ime_i_prezime_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    ime_i_prezime_val.grid(column=1, row=0, padx=(15, 30), pady=10)


    id_zaposlenog_lbl = ctk.CTkLabel(
        podaci_frm,
        text="ID radnika:",
        text_color="khaki",
        font=("Calibri", 24),
        width=150,
        anchor="e"
    )
    id_zaposlenog_lbl.grid(column=2, row=0, padx=(30, 15), pady=10)
    id_zaposlenog_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    id_zaposlenog_val.grid(column=3, row=0, padx=(15, 30), pady=10)
    
    adresa_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Adresa:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    adresa_lbl.grid(column=0, row=1, padx=(30, 15), pady=10)
    adresa_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    adresa_val.grid(column=1, row=1, padx=(15, 30), pady=10)
    
    telefon_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Telefon:",
        text_color="khaki",
        font=("Calibri", 24),
        width=150,
        anchor="e"
    )
    telefon_lbl.grid(column=2, row=1, padx=(30, 15), pady=10)
    telefon_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    telefon_val.grid(column=3, row=1, padx=(15, 30), pady=10)
    
    email_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Email:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    email_lbl.grid(column=0, row=2, padx=(30, 15), pady=10)
    email_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    email_val.grid(column=1, row=2, padx=(15, 30), pady=10)
    
    pozicija_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Pozicija:",
        text_color="khaki",
        font=("Calibri", 24),
        width=150,
        anchor="e"
    )
    pozicija_lbl.grid(column=2, row=2, padx=(30, 15), pady=10)
    pozicija_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    pozicija_val.grid(column=3, row=2, padx=(15, 30), pady=10)
    
    radno_mesto_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Radno mesto:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    radno_mesto_lbl.grid(column=0, row=3, padx=(30, 15), pady=10)
    radno_mesto_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    radno_mesto_val.grid(column=1, row=3, padx=(15, 30), pady=10)
    
    istorija_zaposlenog_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Istorija radnika:",
        text_color="khaki",
        font=("Calibri", 24),
        width=150,
        anchor="e"
    )
    istorija_zaposlenog_lbl.grid(column=2, row=3, padx=(30, 15), pady=10)
    istorija_zaposlenog_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="nw",
        justify="left"
    )
    istorija_zaposlenog_val.grid(column=3, row=3, rowspan=4, padx=(15, 30),
                                 pady=10, sticky="nsew")
    
    zaposlen_lbl = ctk.CTkLabel(
        podaci_frm,
        text="U radnom odnosu:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    zaposlen_lbl.grid(column=0, row=4, padx=(30, 15), pady=10)
    zaposlen_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    zaposlen_val.grid(column=1, row=4, padx=(15, 30), pady=10)
    
    datum_zaposlavanja_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Datum zapošljavanja:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    datum_zaposlavanja_lbl.grid(column=0, row=5, padx=(30, 15), pady=10)
    datum_zaposlavanja_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    datum_zaposlavanja_val.grid(column=1, row=5, padx=(15, 30), pady=10)
    
    prestanak_odnosa_lbl = ctk.CTkLabel(
        podaci_frm,
        text="Prekid radnog odnosa:",
        text_color="khaki",
        font=("Calibri", 24),
        width=250,
        anchor="e"
    )
    prestanak_odnosa_lbl.grid(column=0, row=6, padx=(30, 15), pady=10)
    prestanak_odnosa_val = ctk.CTkLabel(
        podaci_frm,
        text="",
        fg_color="grey20",
        corner_radius=5,
        font=("Calibri", 22),
        width=350,
        anchor="w"
    )
    prestanak_odnosa_val.grid(column=1, row=6, padx=(15, 30), pady=10)


def azuriranje_podataka():
    """Ažuriranje postojećih podataka u tabeli 'radnici'."""
    
    def kriterijum_pozicija(event):
        """Promene koje se dešavaju kada se izabere bilo koja vrednost iz
        padajućeg menija 'Pozicija'."""
        krit_lokacija_combo.set("")
        krit_zaposlen_combo.set("")
        azur_izbor_radnika_combo.set("")
        resetovanje_podataka()
        
        df = radnici.radnici_df[
            radnici.radnici_df.pozicija == krit_pozicija_combo.get()]
        azur_izbor_radnika_combo.configure(values=radnici.df_sortiranje(df))
    
    def kriterijum_radno_mesto(event):
        """Promene koje se dešavaju kada se izabere bilo koja vrednost iz
        padajućeg menija 'Radno mesto'."""
        krit_pozicija_combo.set("")
        krit_zaposlen_combo.set("")
        azur_izbor_radnika_combo.set("")
        resetovanje_podataka()

        pozicija_sifra = lokacije.lokacije_df.sifra[
            lokacije.lokacije_df.pun_naziv == krit_lokacija_combo.get()
        ].to_string(index=False)
        
        df = radnici.radnici_df[
            radnici.radnici_df.lokacija == pozicija_sifra]
        azur_izbor_radnika_combo.configure(values=radnici.df_sortiranje(df))
    
    def kriterijum_zaposlen(event):
        """Promene koje se dešavaju kada se izabere bilo koja vrednost iz
        padajućeg menija 'U radnom odnosu'."""
        krit_lokacija_combo.set("")
        krit_pozicija_combo.set("")
        azur_izbor_radnika_combo.set("")
        resetovanje_podataka()
        
        if krit_zaposlen_combo.get() == "Da":
            zaposlen_bool = True
        else:
            zaposlen_bool = False
        
        df = radnici.radnici_df[
            radnici.radnici_df.zaposlen == zaposlen_bool]
        azur_izbor_radnika_combo.configure(values=radnici.df_sortiranje(df))
    
    def resetovanje_podataka():
        """Resetovanje podatka prethodno izabranog radnika."""
        
        labels = [
            azur_id_radnika_val,
            azur_zaposlen_val,
            azur_ime_staro_lbl,
            azur_prezime_staro_lbl,
            azur_adresa_stara_lbl,
            azur_telefon_stari_lbl,
            azur_email_stari_lbl,
            azur_pozicija_stara_lbl,
            azur_rmesto_staro_lbl,
            azur_datum_zapos_stari_lbl,
            azur_datum_prekid_stari_lbl
        ]
        entries = [
            azur_ime_novo_ent,
            azur_prezime_novo_ent,
            azur_adresa_nova_ent,
            azur_telefon_novi_ent,
            azur_email_novi_ent,
        ]
        combos = [azur_pozicija_nova_combo, azur_rmesto_novo_combo]
        date_entries = [azur_datum_zapos_novi_de, azur_datum_prekid_novi_de]
        
        # Resetovanje svih Label widgeta.
        for label in labels:
            label.configure(text="")
        
        # Resetovanje svih Entry widgeta.
        for entry in entries:
            entry.delete(0, "end")
        
        # Resetovanje Combobox widgeta.
        for combo in combos:
            combo.set("")
        
        # Onespobljavanje DateEntry widgeta.
        for de in date_entries:
            de.delete(0, "end")
            de.configure(state="disabled")

    def resetovanje_kriterijuma():
        """Resetovanje svih vrednosti."""
    
        combos = [krit_pozicija_combo, krit_lokacija_combo,
            krit_zaposlen_combo, azur_izbor_radnika_combo]
        
        # Resetovanje svih Combobox widgeta.
        for combo in combos:
            combo.set("")
        azur_izbor_radnika_combo.configure(
            values=radnici.df_sortiranje(radnici.radnici_df))
        
        resetovanje_podataka()

    def izbor_radnik(event):
        """Promene koje se dešavaju prilikom izbora radnika."""
        
        # Tekući podaci radnika.
        id_izabranog_radnika = azur_izbor_radnika_combo.get()[-10:]
        tekuci_podaci = radnici.radnici_df[
            radnici.radnici_df.id_radnika == id_izabranog_radnika
        ].values.flatten().tolist()

        # ID
        azur_id_radnika_val.configure(text=id_izabranog_radnika)
        
        # Da li je radnik u radnom odnosu.
        if tekuci_podaci[9]:
            azur_zaposlen_val.configure(text="Da")
            azur_datum_zapos_novi_de.delete(0, "end")
            azur_datum_zapos_novi_de.configure(state="disabled")
            azur_datum_prekid_novi_de.configure(state="normal")
        else:
            azur_zaposlen_val.configure(text="Ne")
            azur_datum_zapos_novi_de.configure(state="normal")
            azur_datum_prekid_novi_de.delete(0, "end")
            azur_datum_prekid_novi_de.configure(state="disabled")
        
        # Unos ostalih podataka.
        azur_ime_staro_lbl.configure(text=tekuci_podaci[1])
        azur_prezime_staro_lbl.configure(text=tekuci_podaci[2])
        azur_adresa_stara_lbl.configure(text=tekuci_podaci[3])
        azur_telefon_stari_lbl.configure(text=tekuci_podaci[4])
        azur_email_stari_lbl.configure(text=tekuci_podaci[5])
        azur_pozicija_stara_lbl.configure(text=tekuci_podaci[6])
        
        radno_mesto_str = lokacije.lokacije_df.pun_naziv[
            lokacije.lokacije_df.sifra == tekuci_podaci[7]
        ].to_string(index=False)
        azur_rmesto_staro_lbl.configure(text=radno_mesto_str)
        
        datum_zaposljavanja_str = tekuci_podaci[10].strftime("%d. %m. %Y.")
        azur_datum_zapos_stari_lbl.configure(text=datum_zaposljavanja_str)
        if tekuci_podaci[11]:
            prekid_odnosa_str = tekuci_podaci[11].strftime("%d. %m. %Y.")
            azur_datum_prekid_stari_lbl.configure(text=prekid_odnosa_str)
        else:
            azur_datum_prekid_stari_lbl.configure(text="")
    
    def primena_azuriranja():
        """Ubacivanje novih podataka pritiskom na dugme 'Ažuriraj'."""
        
        # Ako radnik nije izabran, ažuriranje ne može da se izvrši.
        if azur_izbor_radnika_combo.get():
            if azur_rmesto_novo_combo.get():
                radno_mesto_value = lokacije.lokacije_df.sifra[
                    lokacije.lokacije_df.pun_naziv == azur_rmesto_novo_combo.get()
                ].to_string(index=False)
            else:
                radno_mesto_value = ""
            
            # Dodatak teksta u koloni 'istorija', ukoliko se prekine radni
            # odnos ili se radnik ponovo zaposli.
            istorija_dodatak = ""
            radni_odnos = radnici.radnici_df.zaposlen[
                radnici.radnici_df.id_radnika == azur_id_radnika_val.cget(
                    "text")]
            if azur_datum_zapos_novi_de.get():
                zapos_datum = azur_datum_zapos_novi_de.get_date().strftime(
                    "%d. %m. %Y.")
                istorija_dodatak = f";Zaposlen: {zapos_datum}"
                radni_odnos = True
            elif azur_datum_prekid_novi_de.get():
                prekid_datum = azur_datum_prekid_novi_de.get_date().strftime(
                    "%d. %m. %Y.")
                istorija_dodatak = f";Prekid radnog odnosa: {prekid_datum}"
                radni_odnos = False
            
            if azur_datum_zapos_novi_de.get():
                zaposljavanje_datum = azur_datum_zapos_novi_de.get_date()
            else:
                zaposljavanje_datum = ""
            
            if azur_datum_prekid_novi_de.get():
                prekid_odnosa_datum = azur_datum_prekid_novi_de.get_date()
            else:
                prekid_odnosa_datum = ""
            
            azuriranje_dict = {
                "ime": azur_ime_novo_ent.get(),
                "prezime": azur_prezime_novo_ent.get(),
                "adresa": azur_adresa_nova_ent.get(),
                "telefon": azur_telefon_novi_ent.get(),
                "email": azur_email_novi_ent.get(),
                "pozicija": azur_pozicija_nova_combo.get(),
                "lokacija": radno_mesto_value,
                "datum_zaposljavanja": zaposljavanje_datum,
                "prestanak_radnog_odnosa": prekid_odnosa_datum
            }
            
            radnici.azuriranje(
                azuriranje_dict,
                azur_id_radnika_val.cget("text"),
                istorija_dodatak,
                radni_odnos
            )
        else:
            cmb.CTkMessagebox(
                title="Radnik nije izabran",
                message="Da bi se ažuriranje izvršilo mora biti izabran "
                        "radnik čije podatke treba ažurirati.",
                icon="info",
                width=450,
                button_width=50,
                font=("Calibri", 18)
            )
    
    
    # Nova forma za ažuriranje podataka.
    azuriranje_tl = ctk.CTkToplevel(root)
    azuriranje_tl.title("Ažuriranje podataka")
    azuriranje_tl.resizable(False, False)
    azuriranje_tl.attributes("-topmost", "true")
    azuriranje_tl.grab_set()
    azuriranje_tl.after(200, lambda: azuriranje_tl.iconbitmap(
        "pics/logo_icon.ico"))
    
    # Okvir za ostale okvire.
    azuriranje_frm = ctk.CTkScrollableFrame(
        azuriranje_tl,
        fg_color="transparent",
        width=1200,
        height=800
    )
    azuriranje_frm.pack(expand=True, fill="both")
    
    # Okviri za određene grupe podataka.
    azur_logo_naslov_frm = ctk.CTkFrame(azuriranje_frm, fg_color="transparent")
    azur_kriterijumi_frm = ctk.CTkFrame(
        azuriranje_frm,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    azur_izbor_frm = ctk.CTkFrame(
        azuriranje_frm,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    azur_podaci_frm = ctk.CTkFrame(
        azuriranje_frm,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    azur_dugmad_frm = ctk.CTkFrame(azuriranje_frm, fg_color="transparent")
    
    azur_logo_naslov_frm.pack(expand=True, fill= "x", pady=10)
    azur_kriterijumi_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    azur_izbor_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    azur_podaci_frm.pack(expand=True, fill= "x", padx=20, pady=10)
    azur_dugmad_frm.pack(expand=True, fill="x", padx=20, pady=20)
    
    # Logo i naslov.
    azur_logo_naslov_frm.grid_columnconfigure((0, 1), weight=1)
    logo_azur_lbl = ctk.CTkLabel(
        azur_logo_naslov_frm,
        image=logo_manja,
        text="",
        fg_color="transparent"
    )
    logo_azur_lbl.grid(column=0, row=0)
    
    naslov_azur_lbl = ctk.CTkLabel(
        azur_logo_naslov_frm,
        text="AŽURIRANJE PODATAKA O RADNICIMA",
        fg_color="transparent",
        text_color="khaki",
        font=("Calibri", 40, "bold")
    )
    naslov_azur_lbl.grid(column=1, row=0, padx=20)
    
    # Kriterijumi.
    azur_kriterijumi_frm.grid_columnconfigure((0, 1, 2), weight=1)
    kriterijumi_lbl = ctk.CTkLabel(
        azur_kriterijumi_frm,
        fg_color="black",
        text="Kriterijumi",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    kriterijumi_lbl.grid(column=0, row=0, columnspan=3, sticky="ew", padx=2,
                         pady=2)
    
    krit_tekst_lbl = ctk.CTkLabel(
        azur_kriterijumi_frm,
        fg_color="transparent",
        text="Izaberite jedan od kriterijuma za izbor "
             "radnika.\nUkoliko ne izaberete nijedan kriterijum, imaćete "
             "izbor svih radnika.\nPritiskom na dugme \"Resetuj\" poništava "
             "se izbor kriterijuma i brišu prethodni podaci.",
        text_color="khaki",
        font=("Calibri", 18),
        anchor="nw",
        justify="left"
    )
    krit_tekst_lbl.grid(column=0, row=1, columnspan=3, padx=40, pady=10,
                        sticky="ew")

    krit_pozicija_lbl = ctk.CTkLabel(
        azur_kriterijumi_frm,
        fg_color="transparent",
        text="Pozicija",
        font=("Calibri", 16),
        anchor="w"
    )
    krit_pozicija_lbl.grid(column=0, row=2, sticky="ew", padx=(50, 20),
                           pady=(10, 0))

    pozicije_sortirano = pozicije.pozicije_df.naziv.to_list()
    pozicije_sortirano.sort()
    pozicija_var = ctk.StringVar()
    
    krit_pozicija_combo = ctk.CTkComboBox(
        azur_kriterijumi_frm,
        width=250,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=pozicije_sortirano,
        variable=pozicija_var,
        command=kriterijum_pozicija
    )
    krit_pozicija_combo.grid(column=0, row=3, sticky="w", padx=(50, 20),
                             pady=(0, 20))

    krit_lokacija_lbl = ctk.CTkLabel(
        azur_kriterijumi_frm,
        fg_color="transparent",
        text="Radno mesto",
        font=("Calibri", 16),
        anchor="w"
    )
    krit_lokacija_lbl.grid(column=1, row=2, sticky="ew", padx=20, pady=(10, 0))

    lokacije_sortirano = lokacije.lokacije_df.pun_naziv.to_list()
    lokacije_sortirano.sort()

    krit_lokacija_combo = ctk.CTkComboBox(
        azur_kriterijumi_frm,
        width=250,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=lokacije_sortirano,
        command=kriterijum_radno_mesto
    )
    krit_lokacija_combo.grid(column=1, row=3, sticky="w", padx=20,
                             pady=(0, 20))

    krit_zaposlen_lbl = ctk.CTkLabel(
        azur_kriterijumi_frm,
        fg_color="transparent",
        text="U radnom odnosu",
        font=("Calibri", 16),
        anchor="w"
    )
    krit_zaposlen_lbl.grid(column=2, row=2, sticky="ew", padx=20, pady=(10, 0))

    zaposlen_vrednosti = ["Da", "Ne"]
    
    krit_zaposlen_combo = ctk.CTkComboBox(
        azur_kriterijumi_frm,
        width=250,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=zaposlen_vrednosti,
        command=kriterijum_zaposlen
    )
    krit_zaposlen_combo.grid(column=2, row=3, sticky="w", padx=20,
                             pady=(0, 20))
    
    # Izbor radnika.
    azur_izbor_frm.grid_columnconfigure((0, 1, 2), weight=1)
    izbor_azur_lbl = ctk.CTkLabel(
        azur_izbor_frm,
        fg_color="black",
        text="Izbor radnika",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    izbor_azur_lbl.grid(column=0, row=0, columnspan=3, sticky="ew", padx=2,
                         pady=2)

    azur_izbor_radnika_lbl = ctk.CTkLabel(
        azur_izbor_frm,
        fg_color="transparent",
        text="Izbor Radnika",
        font=("Calibri", 16),
        anchor="w"
    )
    azur_izbor_radnika_lbl.grid(column=0, row=1, sticky="ew", padx=50,
                                pady=(10,0))

    azur_izbor_vrednosti = radnici.df_sortiranje(radnici.radnici_df)
    azur_izbor_radnika_combo = ctk.CTkComboBox(
        azur_izbor_frm,
        width=250,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=azur_izbor_vrednosti,
        command=izbor_radnik
    )
    azur_izbor_radnika_combo.grid(column=0, row=2, sticky="w", padx=50,
                                  pady=(0, 20))

    azur_id_radnika_lbl = ctk.CTkLabel(
        azur_izbor_frm,
        fg_color="transparent",
        text="ID radnika",
        font=("Calibri", 16),
        anchor="w"
    )
    azur_id_radnika_lbl.grid(column=1, row=1, sticky="ew", padx=50,
                                pady=(10, 0))

    azur_id_radnika_val = ctk.CTkLabel(
        azur_izbor_frm,
        text="",
        font=("Calibri", 18, "bold"),
        width=250,
        anchor="w"
    )
    azur_id_radnika_val.grid(column=1, row=2, sticky="ew", padx=50,
                               pady=(0, 20))
    
    azur_zaposlen_lbl = ctk.CTkLabel(
        azur_izbor_frm,
        fg_color="transparent",
        text="Zaposlen",
        font=("Calibri", 16),
        anchor="w"
    )
    azur_zaposlen_lbl.grid(column=2, row=1, sticky="ew", padx=50,
                                pady=(10, 0))

    azur_zaposlen_val = ctk.CTkLabel(
        azur_izbor_frm,
        text="",
        font=("Calibri", 18, "bold"),
        width=250,
        anchor="w"
    )
    azur_zaposlen_val.grid(column=2, row=2, sticky="ew", padx=50,
                               pady=(0, 20))
    
    # Podaci koji mogu da se menjaju.
    azur_podaci_frm.grid_columnconfigure((0, 1, 2), weight=1)
    azur_menjanje_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="black",
        text="Podaci za menjanje",
        text_color="khaki",
        font=("Calibri", 16),
        anchor="center"
    )
    azur_menjanje_lbl.grid(column=0, row=0, columnspan=3, sticky="ew",
                           padx=2, pady=2)
    
    azur_naziv_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="NAZIV PODATKA",
        font=("Calibri", 18, "bold"),
        text_color="khaki",
        width=300,
        anchor="e"
    )
    azur_naziv_lbl.grid(column=0, row=1, sticky="ew", padx=50, pady=10)
    
    azur_stari_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="STARI PODATAK",
        font=("Calibri", 18, "bold"),
        text_color="khaki",
        width=300,
        anchor="w"
    )
    azur_stari_lbl.grid(column=1, row=1, sticky="ew", padx=50, pady=10)
    
    azur_novi_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="NOVI PODATAK",
        font=("Calibri", 18, "bold"),
        text_color="khaki",
        width=300,
        anchor="w"
    )
    azur_novi_lbl.grid(column=2, row=1, sticky="ew", padx=50, pady=10)
    
    azur_ime_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Ime radnika:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_ime_lbl.grid(column=0, row=2, sticky="ew", padx=50, pady=(20, 10))
    
    azur_ime_staro_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_ime_staro_lbl.grid(column=1, row=2, sticky="ew", padx=50,
                            pady=(20, 10))
    
    azur_ime_novo_ent = ctk.CTkEntry(
        azur_podaci_frm,
        font=("Calibri", 18)
    )
    azur_ime_novo_ent.grid(column=2, row=2, sticky="ew", padx=50,
                           pady=(20, 10))
    
    azur_prezime_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Prezime radnika:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_prezime_lbl.grid(column=0, row=3, sticky="ew", padx=50, pady=10)
    
    azur_prezime_staro_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_prezime_staro_lbl.grid(column=1, row=3, sticky="ew", padx=50, pady=10)
    
    azur_prezime_novo_ent = ctk.CTkEntry(
        azur_podaci_frm,
        font=("Calibri", 18)
    )
    azur_prezime_novo_ent.grid(column=2, row=3, sticky="ew", padx=50, pady=10)
    
    azur_adresa_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Adresa:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_adresa_lbl.grid(column=0, row=4, sticky="ew", padx=50, pady=10)
    
    azur_adresa_stara_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_adresa_stara_lbl.grid(column=1, row=4, sticky="ew", padx=50, pady=10)
    
    azur_adresa_nova_ent = ctk.CTkEntry(
        azur_podaci_frm,
        font=("Calibri", 18)
    )
    azur_adresa_nova_ent.grid(column=2, row=4, sticky="ew", padx=50, pady=10)
    
    azur_telefon_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Telefon:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_telefon_lbl.grid(column=0, row=5, sticky="ew", padx=50, pady=10)
    
    azur_telefon_stari_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_telefon_stari_lbl.grid(column=1, row=5, sticky="ew", padx=50, pady=10)
    
    azur_tel_reg = azur_podaci_frm.register(len_char_limit)
    azur_telefon_novi_ent = ctk.CTkEntry(
        azur_podaci_frm,
        font=("Calibri", 18),
        validate="key",
        validatecommand=(azur_tel_reg, "%P")
    )
    azur_telefon_novi_ent.grid(column=2, row=5, sticky="ew", padx=50, pady=10)
    
    azur_email_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Email:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_email_lbl.grid(column=0, row=6, sticky="ew", padx=50, pady=10)
    
    azur_email_stari_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_email_stari_lbl.grid(column=1, row=6, sticky="ew", padx=50, pady=10)
    
    azur_email_novi_ent = ctk.CTkEntry(
        azur_podaci_frm,
        font=("Calibri", 18)
    )
    azur_email_novi_ent.grid(column=2, row=6, sticky="ew", padx=50, pady=10)
    
    azur_pozicija_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Pozicija:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_pozicija_lbl.grid(column=0, row=7, sticky="ew", padx=50, pady=10)
    
    azur_pozicija_stara_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_pozicija_stara_lbl.grid(column=1, row=7, sticky="ew", padx=50,
                                 pady=10)
    
    azur_pozicija_nova_combo = ctk.CTkComboBox(
        azur_podaci_frm,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=pozicije_sortirano
    )
    azur_pozicija_nova_combo.grid(column=2, row=7, sticky="ew", padx=50, pady=10)
    
    azur_rmesto_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Radno mesto:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_rmesto_lbl.grid(column=0, row=8, sticky="ew", padx=50, pady=10)
    
    azur_rmesto_staro_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_rmesto_staro_lbl.grid(column=1, row=8, sticky="ew", padx=50, pady=10)
    
    azur_rmesto_novo_combo = ctk.CTkComboBox(
        azur_podaci_frm,
        dropdown_font=("Calibri", 18),
        state="readonly",
        values=lokacije_sortirano
    )
    azur_rmesto_novo_combo.grid(column=2, row=8, sticky="ew", padx=50, pady=10)
    
    azur_datum_zapos_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Datum zapošljavanja:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_datum_zapos_lbl.grid(column=0, row=9, sticky="ew", padx=50, pady=10)
    
    azur_datum_zapos_stari_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_datum_zapos_stari_lbl.grid(column=1, row=9, sticky="ew", padx=50,
                                    pady=10)
    
    azur_datum_zapos_novi_de = DateEntry(
        azur_podaci_frm,
        font=("Calibri", 12),
        date_pattern='dd. mm. y.',
        state="disabled"
    )
    azur_datum_zapos_novi_de.grid(column=2, row=9, sticky="ew", padx=50,
                                   pady=10)
    
    azur_datum_zapos_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="Datum prekida radnog odnosa:",
        font=("Calibri", 18),
        anchor="e"
    )
    azur_datum_zapos_lbl.grid(column=0, row=10, sticky="ew", padx=50,
                              pady=(10, 20))
    
    azur_datum_prekid_stari_lbl = ctk.CTkLabel(
        azur_podaci_frm,
        fg_color="transparent",
        text="",
        font=("Calibri", 18, "bold"),
        anchor="w"
    )
    azur_datum_prekid_stari_lbl.grid(column=1, row=10, sticky="ew", padx=50,
                                    pady=(10, 20))
    
    azur_datum_prekid_novi_de = DateEntry(
        azur_podaci_frm,
        font=("Calibri", 12),
        date_pattern='dd. mm. y.',
        state="disabled"
    )
    azur_datum_prekid_novi_de.grid(column=2, row=10, sticky="ew", padx=50,
                                   pady=(10, 20))
    
    # Dugmad za ažuriranje, resetovanje kriterijuma i zatvaranje prozora.
    azur_zatvori_btn = ctk.CTkButton(
        azur_dugmad_frm,
        text="Zatvori",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=lambda: [azuriranje_tl.destroy(), radnici.con.close()]
    )
    azur_zatvori_btn.pack(side="right", padx=10, pady=20)

    resetuj_btn = ctk.CTkButton(
        azur_dugmad_frm,
        text="Resetuj",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=resetovanje_kriterijuma
    )
    resetuj_btn.pack(side="right", padx=10, pady=20)

    azuriraj_btn = ctk.CTkButton(
        azur_dugmad_frm,
        text="Ažuriraj",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=lambda: [primena_azuriranja(), resetovanje_kriterijuma()]
    )
    azuriraj_btn.pack(side="right", padx=10, pady=20)


def izvestaji():
    """Prikaz raznih podataka."""
    
    def hijerarhija():
        """Vizuelni prikaz hijerarhije firme, uz objašnjenja."""
        
        hijerarhija_tl = ctk.CTkToplevel(izvestaji_tl)
        hijerarhija_tl.title("Hijerarhija firme")
        hijerarhija_tl.attributes("-topmost", "true")
        hijerarhija_tl.resizable(False, False),
        hijerarhija_tl.grab_set()
        hijerarhija_tl.after(200, lambda: hijerarhija_tl.iconbitmap(
            "pics/logo_icon.ico"))
        
        # ScrollableFrame za ostale okvire.
        glavni_sf = ctk.CTkScrollableFrame(
            hijerarhija_tl,
            fg_color="transparent",
            width=800,
            height=900
        )
        glavni_sf.pack(expand=True, fill="both")
        
        # Okviri unutar glavno, za svaku grupu widgeta na formi.
        hij_naslov_frm = ctk.CTkFrame(glavni_sf, fg_color="transparent")
        hij_info_frm = ctk.CTkFrame(
            glavni_sf,
            fg_color="transparent",
            border_width=1,
            border_color="khaki",
            corner_radius=5
        )
        hij_pozicije_frm = ctk.CTkFrame(
            glavni_sf,
            fg_color="transparent",
            border_width=1,
            border_color="khaki",
            corner_radius=5
        )
        hij_zatvori_frm = ctk.CTkFrame(glavni_sf, fg_color="transparent")
        
        hij_naslov_frm.pack(expand=True, fill="x", pady=(0, 10))
        hij_info_frm.pack(expand=True, fill="x", pady=10, padx=20)
        hij_pozicije_frm.pack(expand=True, fill="x", pady=10, padx=20)
        hij_zatvori_frm.pack(expand=True, fill="x", pady=(10, 20))
        
        # Naslov.
        hij_naslov_lbl = ctk.CTkLabel(
            hij_naslov_frm,
            text="HIJERARHIJA FIRME",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 36, "bold")
        )
        hij_naslov_lbl.pack(expand=True, fill="x", ipady=5)
        hij_naslov_lbl = ctk.CTkLabel(
            hij_naslov_frm,
            text="Nivoi nadređenosti i direktno podređeni",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 32)
        )
        hij_naslov_lbl.pack(expand=True, fill="x", ipady=10)
        
        # Informacije i legenda.
        hij_info_frm.grid_columnconfigure((0, 1), weight=1)
        hij_info_zaglavlje_lbl = ctk.CTkLabel(
            hij_info_frm,
            text="Informacije o hijerarhiji",
            fg_color="black",
            font=("Calibri", 16),
            text_color="khaki",
            anchor="center"
        )
        hij_info_zaglavlje_lbl.grid(column=0, row=0, padx=2, pady=(2, 20),
                                    columnspan=2, sticky="ew")
        
        hij_info_legenda_frm = ctk.CTkFrame(hij_info_frm,
                                            fg_color="transparent")
        hij_info_objasnjenja_frm = ctk.CTkFrame(hij_info_frm,
                                                fg_color="transparent")
        hij_info_legenda_frm.grid(column=0, row=1, sticky="nsew", padx=5,
                                  pady=5)
        hij_info_objasnjenja_frm.grid(column=1, row=1, sticky="nsew",
                                      padx=5, pady=5)
        
        hij_info_legenda_frm.grid_columnconfigure((0, 1), weight=1)
        hij_info_nivo1_color = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="",
            fg_color="darkred",
            width=50,
            corner_radius=10
        )
        hij_info_nivo1_color.grid(column=0, row=0, padx=20, pady=10,
                                  sticky="e")
        hij_info_nivo2_color = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="",
            fg_color="indigo",
            width=50,
            corner_radius=10
        )
        hij_info_nivo2_color.grid(column=0, row=1, padx=20, pady=10,
                                  sticky="e")
        hij_info_nivo3_color = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="",
            fg_color="navy",
            width=50,
            corner_radius=10
        )
        hij_info_nivo3_color.grid(column=0, row=2, padx=20, pady=10,
                                  sticky="e")
        hij_info_nivo4_color = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="",
            fg_color="darkgreen",
            width=50,
            corner_radius=10
        )
        hij_info_nivo4_color.grid(column=0, row=3, padx=20, pady=10,
                                  sticky="e")
        hij_info_nivo5_color = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="",
            fg_color="olive",
            width=50,
            corner_radius=10
        )
        hij_info_nivo5_color.grid(column=0, row=4, padx=20, pady=(10, 30),
                                  sticky="e")
        hij_info_nivo1_txt = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="1. nivo nadređenosti",
            font=("Calibri", 18)
        )
        hij_info_nivo1_txt.grid(column=1, row=0, padx=(0, 20), pady=10,
                                sticky="w")
        hij_info_nivo2_txt = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="2. nivo nadređenosti",
            font=("Calibri", 18)
        )
        hij_info_nivo2_txt.grid(column=1, row=1, padx=(0, 20), pady=10,
                                sticky="w")
        hij_info_nivo3_txt = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="3. nivo nadređenosti",
            font=("Calibri", 18)
        )
        hij_info_nivo3_txt.grid(column=1, row=2, padx=(0, 20), pady=10,
                                sticky="w")
        hij_info_nivo4_txt = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="4. nivo nadređenosti",
            font=("Calibri", 18)
        )
        hij_info_nivo4_txt.grid(column=1, row=3, padx=(0, 20), pady=10,
                                sticky="w")
        hij_info_nivo5_txt = ctk.CTkLabel(
            hij_info_legenda_frm,
            text="5. nivo nadređenosti",
            font=("Calibri", 18)
        )
        hij_info_nivo5_txt.grid(column=1, row=4, padx=(0, 20),
                                pady=(10, 30), sticky="w")
        
        hij_info_objasnjenje1_txt = ctk.CTkLabel(
            hij_info_objasnjenja_frm,
            text="Nivoi nadređenosti su obeleženi različitim bojama.",
            text_color="khaki",
            font=("Calibri", 18),
            justify="left"
        )
        hij_info_objasnjenje1_txt.grid(row=0, padx=20, pady=(25, 5),
                                       sticky="w")
        hij_info_objasnjenje2_txt = ctk.CTkLabel(
            hij_info_objasnjenja_frm,
            text="Direktno podređeni, kojima viši nivo upravlja,\nnalaze "
                 "se odmah ispod njih, malo pomereni udesno.",
            text_color="khaki",
            font=("Calibri", 18),
            justify="left"
        )
        hij_info_objasnjenje2_txt.grid(row=1, padx=20, pady=5,
                                       sticky="w")
        hij_info_objasnjenje3_txt = ctk.CTkLabel(
            hij_info_objasnjenja_frm,
            text="Viši nivo ne mora ispod sebe da ima podređene\nnarednog"
                 " nivoa ili ne mora uopšte da ih ima.",
            text_color="khaki",
            font=("Calibri", 18),
            justify="left"
        )
        hij_info_objasnjenje3_txt.grid(row=2, padx=20, pady=5,
                                       sticky="w")
        hij_info_objasnjenje4_txt = ctk.CTkLabel(
            hij_info_objasnjenja_frm,
            text="U određenim situacijama, viši nivo može da upravlja\n"
                 "nižim, iako nad njim nema direktnu nadležnost.",
            text_color="khaki",
            font=("Calibri", 18),
            justify="left"
        )
        hij_info_objasnjenje4_txt.grid(row=3, padx=20, pady=5,
                                       sticky="w")

        # Hijerarhija (nadređenost) pozicija u firmi.
        hij_pozicije_frm.grid_columnconfigure(0, weight=1)
        hij_poz_zaglavlje_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Hijerarhija pozicija u firmi",
            fg_color="black",
            font=("Calibri", 16),
            text_color="khaki",
            anchor="center"
        )
        hij_poz_zaglavlje_lbl.grid(row=0, padx=2, pady=(2, 20),
                                   sticky="ew")
        hij_generalni_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Generalni direktor",
            fg_color="darkred",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_generalni_lbl.grid(row=1, padx=50, pady=(40, 0), ipadx=10,
                               ipady=5, sticky="w")

        hij_dir_prodaje_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor prodaje",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_prodaje_lbl.grid(row=2, padx=(150, 50), pady=10, ipadx=10,
                                 ipady=5, sticky="w")
        hij_prodavac_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Radnik prodavac",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_prodavac_lbl.grid(row=3, padx=(250, 50), pady=(0, 10),
                              ipadx=10, ipady=5, sticky="w")
        hij_dir_pravne_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor pravne službe",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_pravne_lbl.grid(row=4, padx=(150, 50), pady=10,
                                ipadx=10, ipady=5, sticky="w")
        hij_pravnik_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Pravnik",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_pravnik_lbl.grid(row=5, padx=(250, 50), pady=(0, 10),
                              ipadx=10, ipady=5, sticky="w")
        hij_dir_ljudskih_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor za ljudske resurse",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_ljudskih_lbl.grid(row=6, padx=(150, 50), pady=10,
                                  ipadx=10, ipady=5, sticky="w")
        hij_dir_finansija_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor finansija",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_finansija_lbl.grid(row=7, padx=(150, 50), pady=10,
                                   ipadx=10, ipady=5, sticky="w")
        hij_knjigovodja_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Knjigovođa",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_knjigovodja_lbl.grid(row=8, padx=(250, 50), pady=(0, 10),
                                 ipadx=10, ipady=5, sticky="w")
        hij_dir_magacina_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor magacina",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_magacina_lbl.grid(row=9, padx=(150, 50), pady=10, ipadx=10,
                                 ipady=5, sticky="w")
        hij_upravnik_magacina_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Upravnik magacina",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_upravnik_magacina_lbl.grid(row=10, padx=(250, 50),
                                       pady=(0, 10), ipadx=10, ipady=5,
                                       sticky="w")
        hij_magacioner_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Magacioner",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_magacioner_lbl.grid(row=11, padx=(350, 50), pady=(0, 10),
                                ipadx=10, ipady=5, sticky="w")
        hij_voz_teretnog_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Vozač teretnog vozila",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_voz_teretnog_lbl.grid(row=12, padx=(350, 50), pady=(0, 10),
                                ipadx=10, ipady=5, sticky="w")
        hij_istovarivac_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Radnik na istovaru robe",
            fg_color="olive",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_istovarivac_lbl.grid(row=13, padx=(450, 50), pady=(0, 10),
                                  ipadx=10, ipady=5, sticky="w")
        hij_dir_admin_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor administracije",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_admin_lbl.grid(row=14, padx=(150, 50), pady=10, ipadx=10,
                                 ipady=5, sticky="w")
        hij_koordinator_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Koordinator",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_koordinator_lbl.grid(row=15, padx=(250, 50), pady=(0, 10),
                                  ipadx=10, ipady=5, sticky="w")
        hij_voz_putnickog_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Vozač putničkog vozila",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_voz_putnickog_lbl.grid(row=16, padx=(250, 50), pady=(0, 10),
                                  ipadx=10, ipady=5, sticky="w")
        hij_dir_logistike_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Direktor logistike",
            fg_color="indigo",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_dir_logistike_lbl.grid(row=17, padx=(150, 50), pady=10,
                                   ipadx=10, ipady=5, sticky="w")
        hij_it_upravnik_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Upravnik IT sektora",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_it_upravnik_lbl.grid(row=18, padx=(250, 50), pady=(0, 10),
                                  ipadx=10, ipady=5, sticky="w")
        hij_programer_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Programer",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_programer_lbl.grid(row=19, padx=(350, 50), pady=(0, 10),
                               ipadx=10, ipady=5, sticky="w")
        hij_serviser_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Serviser IT opreme",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_serviser_lbl.grid(row=20, padx=(350, 50), pady=(0, 10),
                              ipadx=10, ipady=5, sticky="w")
        hij_upravnik_vp_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Upravnik voznog parka",
            fg_color="navy",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_upravnik_vp_lbl.grid(row=21, padx=(250, 50), pady=(0, 10),
                                 ipadx=10, ipady=5, sticky="w")
        hij_odrzavanje_voz_lbl = ctk.CTkLabel(
            hij_pozicije_frm,
            text="Radnik na održavanju vozila",
            fg_color="darkgreen",
            corner_radius=10,
            font=("Calibri", 20, "bold")
        )
        hij_odrzavanje_voz_lbl.grid(row=22, padx=(350, 50), pady=(0, 50),
                                    ipadx=10, ipady=5, sticky="w")
        
        # Dugme za zatvaranje prozora.
        hij_zatvori_btn = ctk.CTkButton(
            hij_zatvori_frm,
            text="Zatvori",
            corner_radius=5,
            hover_color="slategrey",
            font=("Calibri", 28, "bold"),
            command=hijerarhija_tl.destroy
        )
        hij_zatvori_btn.pack(side="right", padx=30, pady=(20, 10))

    def spisak_pozicija():
        """Spisak pozicija u firmi i njihove odgovornosti."""
        
        pozicije_tl = ctk.CTkToplevel(izvestaji_tl)
        pozicije_tl.title("Pozicije u firmi")
        pozicije_tl.attributes("-topmost", "true")
        pozicije_tl.resizable(False, False),
        pozicije_tl.grab_set()
        pozicije_tl.after(200, lambda: pozicije_tl.iconbitmap(
            "pics/logo_icon.ico"))
        
        # Potrebni podaci.
        poz_spisak = pozicije.pozicije_df.naziv.to_list()
        odgovornosti_spisak = pozicije.pozicije_df.opis.to_list()
        
        odgovornosti_uredjeno = []
        for odgovornosti in odgovornosti_spisak:
            odgovornosti_spisak = odgovornosti.split(", ")
            
            odgovornosti_string = ""
            for stavka in odgovornosti_spisak:
                odgovornosti_string += f"{stavka}\n"
            odgovornosti_uredjeno.append(odgovornosti_string)
        
        # ScrollableFrame.
        poz_sf = ctk.CTkScrollableFrame(
            pozicije_tl,
            fg_color="transparent",
            width=800,
            height=800
        )
        poz_sf.pack(expand=True, fill="both")
        
        # Okviri za podatke i za dugme za zatvranje forme.
        poz_naslov_frm = ctk.CTkFrame(poz_sf, fg_color="transparent")
        poz_podaci_frm = ctk.CTkFrame(poz_sf, fg_color="transparent")
        poz_zatvori_frm = ctk.CTkFrame(poz_sf, fg_color="transparent")

        poz_naslov_frm.pack(expand=True, fill="x", pady=(0, 20))
        poz_podaci_frm.pack(expand=True, fill="x", pady=10, padx=20)
        poz_zatvori_frm.pack(expand=True, fill="x", pady=10, padx=20)
        
        # Naslov.
        poz_naslov_lbl = ctk.CTkLabel(
            poz_naslov_frm,
            text="POZICIJE I ODGOVORNOSTI",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 36, "bold")
        )
        poz_naslov_lbl.pack(expand=True, fill="x", ipady=10)
        
        # Pozicije i odgovornosti.
        for i in range(len(poz_spisak)):
            ctk.CTkLabel(
                poz_podaci_frm,
                text=f"{poz_spisak[i]}:",
                text_color="khaki",
                font=("Calibri", 20)
            ).grid(column=0, row=i, padx=10, pady=20, sticky="ne")
            
            ctk.CTkLabel(
                poz_podaci_frm,
                text=odgovornosti_uredjeno[i],
                font=("Calibri", 18),
                justify="left"
            ).grid(column=1, row=i, padx=10, pady=20, sticky="nw")
        
        # Dugme za zatvaranje.
        poz_zatvori_btn = ctk.CTkButton(
            poz_zatvori_frm,
            text="Zatvori",
            corner_radius=5,
            hover_color="slategrey",
            font=("Calibri", 28, "bold"),
            command=pozicije_tl.destroy
        )
        poz_zatvori_btn.pack(side="right", padx=30, pady=20)
    
    def radna_mesta():
        """Spisak radnih mesta sa šiframa i adresama."""
        
        r_mesta_tl = ctk.CTkToplevel(izvestaji_tl)
        r_mesta_tl.title("Radna mesta")
        r_mesta_tl.attributes("-topmost", "true")
        r_mesta_tl.resizable(False, False),
        r_mesta_tl.grab_set()
        r_mesta_tl.after(200, lambda: r_mesta_tl.iconbitmap(
            "pics/logo_icon.ico"))
        
        # Potrebni podaci.
        lok_sortirano_df = lokacije.lokacije_df.sort_values(by=["pun_naziv"])
        
        nazivi_lst = lok_sortirano_df.pun_naziv.to_list()
        sifre_lst = lok_sortirano_df.sifra.to_list()
        adrese_lst = lok_sortirano_df.adresa.to_list()

        # ScrollableFrame.
        radna_mesta_sf = ctk.CTkScrollableFrame(
            r_mesta_tl,
            fg_color="transparent",
            width=800,
            height=800
        )
        radna_mesta_sf.pack(expand=True, fill="both")

        # Okviri za određene elemente prozora.
        rm_naslov_frm = ctk.CTkFrame(radna_mesta_sf, fg_color="transparent")
        rm_podaci_frm = ctk.CTkFrame(
            radna_mesta_sf,
            fg_color="transparent",
            border_width=1,
            border_color="khaki"
        )
        rm_zatvori_frm = ctk.CTkFrame(radna_mesta_sf, fg_color="transparent")
        
        rm_naslov_frm.pack(expand=True, fill= "x", pady=(0, 20))
        rm_podaci_frm.pack(expand=True, fill= "x", padx= 20, pady=20)
        rm_zatvori_frm.pack(expand=True, fill= "x", padx= 20, pady=10)
        
        # Naslov.
        rm_naslov_lbl = ctk.CTkLabel(
            rm_naslov_frm,
            text="RADNA MESTA I NJIHOVE ADRESE",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 36,"bold")
        )
        rm_naslov_lbl.pack(expand=True, fill="x", ipady=10, ipadx=20)
        
        # Radna mesta, njihove šifre i adrese.
        rm_podaci_frm.grid_columnconfigure((0, 1, 2), weight=1)
        rm_sifre_lbl = ctk.CTkLabel(
            rm_podaci_frm,
            text="Šifre",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 20),
            anchor="center"
        )
        rm_sifre_lbl.grid(column=0, row=0, padx=(2, 0), pady=(2, 20),
                          sticky="ew")
        
        rm_nazivi_lbl = ctk.CTkLabel(
            rm_podaci_frm,
            text="Nazivi",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 20),
            anchor="center"
        )
        rm_nazivi_lbl.grid(column=1, row=0, pady=(2, 20), sticky="ew")
        rm_adrese_lbl = ctk.CTkLabel(
            rm_podaci_frm,
            text="Adrese",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 20),
            anchor="center"
            )
        rm_adrese_lbl.grid(column=2, row=0, padx=(0, 2), pady=(2, 20),
                           sticky="ew")
        
        for i in range(len(nazivi_lst)):
            ctk.CTkLabel(
                rm_podaci_frm,
                text=sifre_lst[i],
                font=("Calibri", 20),
                anchor="center"
            ).grid(column=0, row=i+1, pady=10)
        
            ctk.CTkLabel(
                rm_podaci_frm,
                text=nazivi_lst[i],
                font=("Calibri", 20)
            ).grid(column=1, row=i+1, pady=10, padx=(100, 0), sticky="w")
        
            ctk.CTkLabel(
                rm_podaci_frm,
                text=adrese_lst[i],
                font=("Calibri", 20)
            ).grid(column=2, row=i+1, pady=10, padx=(100, 0), sticky="w")
        
        # Dugme za zatvaranje.
        rm_zatvori_btn = ctk.CTkButton(
            rm_zatvori_frm,
            text="Zatvori",
            corner_radius=5,
            hover_color="slategrey",
            font=("Calibri", 28, "bold"),
            command=r_mesta_tl.destroy
        )
        rm_zatvori_btn.pack(side="right", padx=30, pady=20)
    
    def delokrug_sektora():
        """Sektori firme i radna mesta koja im pripadaju."""

        sektori_tl = ctk.CTkToplevel(izvestaji_tl)
        sektori_tl.title("Delokrug sektora")
        sektori_tl.attributes("-topmost", "true")
        sektori_tl.resizable(False, False),
        sektori_tl.grab_set()
        sektori_tl.after(200, lambda: sektori_tl.iconbitmap(
            "pics/logo_icon.ico"))

        # Potrebni podaci.
        sektori_firme = set(pozicije.pozicije_df.sektor.to_list())
        sektori_sortirano = sorted(list(sektori_firme))
        
        rm_svih_sektora = []
        for sek in sektori_sortirano:
            rm_jednog_sektora = pozicije.pozicije_df.naziv[
                pozicije.pozicije_df.sektor == sek].to_list()
            rm_string = ""
            for r_mesto in rm_jednog_sektora:
                rm_string += f"{r_mesto}\n"
            rm_svih_sektora.append(rm_string)
        
        # ScrollableFrame.
        sektori_sf = ctk.CTkScrollableFrame(
            sektori_tl,
            fg_color="transparent",
            width=600,
            height=800
        )
        sektori_sf.pack(expand=True, fill="both")
        
        # Okviri za određene elemente prozora.
        sek_naslov_frm = ctk.CTkFrame(sektori_sf, fg_color="transparent")
        sek_podaci_frm = ctk.CTkFrame(
            sektori_sf,
            fg_color="transparent",
            border_width=1,
            border_color="khaki"
        )
        sek_zatvori_frm = ctk.CTkFrame(sektori_sf, fg_color="transparent")
        
        sek_naslov_frm.pack(expand=True, fill="x", pady=(0, 20))
        sek_podaci_frm.pack(expand=True, fill="x", padx=20, pady=20)
        sek_zatvori_frm.pack(expand=True, fill="x", padx=20, pady=10)
        
        # Naslov.
        sek_naslov_lbl = ctk.CTkLabel(
            sek_naslov_frm,
            text="PRIPADNOST RADNIH MESTA\nODREĐENIM SEKTORIMA",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 36, "bold")
        )
        sek_naslov_lbl.pack(expand=True, fill="x", ipady=10, ipadx=20)
        
        # Sektori i radna mesta.
        sek_podaci_frm.grid_columnconfigure((0, 1), weight=1)
        sek_sektori_lbl = ctk.CTkLabel(
            sek_podaci_frm,
            text="Sektori",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 20),
            anchor="center"
        )
        sek_sektori_lbl.grid(column=0, row=0, padx=(2, 0), pady=(2, 20),
                             sticky="ew")
        sek_radna_mesta_lbl = ctk.CTkLabel(
            sek_podaci_frm,
            text="Pozicije",
            text_color="khaki",
            fg_color="black",
            font=("Calibri", 20),
            anchor="center"
        )
        sek_radna_mesta_lbl.grid(column=1, row=0, padx=(0, 2), pady=(2, 20),
                                 sticky="ew")
        
        for i in range(len(sektori_sortirano)):
            ctk.CTkLabel(
                sek_podaci_frm,
                text=sektori_sortirano[i],
                text_color="khaki",
                fg_color="transparent",
                font=("Calibri", 20, "bold")
            ).grid(column=0, row=i+1, padx=(30, 50), pady=10, sticky="ne")
            
            ctk.CTkLabel(
                sek_podaci_frm,
                text=rm_svih_sektora[i],
                fg_color="transparent",
                font=("Calibri", 20),
                justify="left"
            ).grid(column=1, row=i+1, padx=(50, 30), pady=10, sticky="nw")
            
        # Dugme za zatvaranje.
        sek_zatvori_btn = ctk.CTkButton(
            sek_zatvori_frm,
            text="Zatvori",
            corner_radius=5,
            hover_color="slategrey",
            font=("Calibri", 28, "bold"),
            command=sektori_tl.destroy
        )
        sek_zatvori_btn.pack(side="right", padx=30, pady=20)
    
    def izbor_izvestaja(var_get):
        """Biranje izveštaja i njegov prikaz."""

        if var_get == "1":
            hijerarhija()
        elif var_get == "2":
            spisak_pozicija()
        elif var_get == "3":
            radna_mesta()
        else:
            delokrug_sektora()
    
    
    # Forma za izbor izvštaja.
    izvestaji_tl = ctk.CTkToplevel(root)
    izvestaji_tl.title("Izveštaji")
    izvestaji_tl.resizable(False, False)
    izvestaji_tl.grab_set()
    izvestaji_tl.after(200, lambda: izvestaji_tl.iconbitmap(
        "pics/logo_icon.ico"))
    
    # Okviri za određene grupe podataka.
    izv_logo_naslov_frm = ctk.CTkFrame(izvestaji_tl, fg_color="transparent")
    izv_radio_frm = ctk.CTkFrame(
        izvestaji_tl,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    izv_dugmad_frm = ctk.CTkFrame(izvestaji_tl, fg_color="transparent")
    
    izv_logo_naslov_frm.pack(expand=True, fill= "x", padx=20, pady=20)
    izv_radio_frm.pack(expand=True, fill= "x", padx=50, pady=20)
    izv_dugmad_frm.pack(expand=True, fill= "x", padx= 30, pady=20)
    
    # Logo i naslov.
    izv_logo_naslov_frm.grid_columnconfigure((0, 1), weight=1)
    logo_izv_lbl = ctk.CTkLabel(
        izv_logo_naslov_frm,
        image=logo_manja,
        text="",
        fg_color="transparent"
    )
    logo_izv_lbl.grid(column=0, row=0)
    
    naslov_izv_lbl = ctk.CTkLabel(
        izv_logo_naslov_frm,
        text="RAZNI IZVEŠTAJI",
        fg_color="transparent",
        text_color="khaki",
        font=("Calibri", 40, "bold")
    )
    naslov_izv_lbl.grid(column=1, row=0, padx=20)
    
    # Radiobuttons.
    izvestaji_opcije = {
        "Hijerarhija firme": "1",
        "Spisak pozicija s odgovornostima": "2",
        "informacije o radnim mestima": "3",
        "Delokrug sektora": "4"
    }
    
    izv_var = ctk.StringVar(izv_radio_frm)
    for (tekst, vrednost) in izvestaji_opcije.items():
        ctk.CTkRadioButton(
            izv_radio_frm,
            radiobutton_width=15,
            radiobutton_height=15,
            border_width_unchecked=2,
            border_width_checked=4,
            text=tekst,
            variable=izv_var,
            value=vrednost,
            font=("Calibri", 24)
        ).pack(expand=True, padx=50, pady = 15, anchor="w")
    izv_var.set("1")
    
    izv_zatvori_btn = ctk.CTkButton(
        izv_dugmad_frm,
        text="Zatvori",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=izvestaji_tl.destroy
    )
    izv_zatvori_btn.pack(side="right", padx=(10, 30), pady=20)
    
    izv_primeni_btn = ctk.CTkButton(
        izv_dugmad_frm,
        text="Primeni",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=lambda: izbor_izvestaja(izv_var.get())
    )
    izv_primeni_btn.pack(side="right", padx=10, pady=20)


def grafici():
    """Grafički prikaz različitih podataka."""
    
    def izbor_grafika(var_get):
        """Izbor grafika koji želimo da prikažemo."""
        
        if var_get == "1":
            pozicije.broj_pozicija_po_sektorima()
        elif var_get == "2":
            radnici.broj_po_godini_zaposljavanja()
        elif var_get == "3":
            radnici.broj_zaposlenih_po_pozicijama()
        elif var_get == "4":
            radnici.broj_zaposlenih_po_radnim_mestima()
        elif var_get == "5":
            radnici.broj_zaposlenih_po_sektorima()
        elif var_get == "6":
            radnici.odnos_zaposleni_bivsi()
        elif var_get == "7":
            radnici.odnos_mobilni_fiksni()
        elif var_get == "8":
            radnici.email_odnos()
        elif var_get == "9":
            radnici.odnos_po_radnom_mestu()
        else:
            radnici.odnos_po_poziciji()
    
    # Forma za izbor grafika.
    grafici_tl = ctk.CTkToplevel(root)
    grafici_tl.title("Grafički prikazi podatka")
    grafici_tl.resizable(False, False)
    grafici_tl.grab_set()
    grafici_tl.after(200, lambda: grafici_tl.iconbitmap(
        "pics/logo_icon.ico"))
    
    # Okviri za određene grupe podatka.
    graf_logo_naslov_frm = ctk.CTkFrame(grafici_tl, fg_color="transparent")
    graf_radio_frm = ctk.CTkFrame(
        grafici_tl,
        fg_color="transparent",
        border_width=1,
        border_color="khaki"
    )
    graf_dugmad_frm = ctk.CTkFrame(grafici_tl, fg_color="transparent")
    
    graf_logo_naslov_frm.pack(expand=True, fill="x", padx=20, pady=20)
    graf_radio_frm.pack(expand=True, fill="x", padx=50, pady=20)
    graf_dugmad_frm.pack(expand=True, fill="x", padx=30, pady=20)
    
    # Logo i naslov.
    graf_logo_naslov_frm.grid_columnconfigure((0, 1), weight=1)
    logo_graf_lbl = ctk.CTkLabel(
        graf_logo_naslov_frm,
        image=logo_manja,
        text="",
        fg_color="transparent"
    )
    logo_graf_lbl.grid(column=0, row=0)

    naslov_graf_lbl = ctk.CTkLabel(
        graf_logo_naslov_frm,
        text="GRAFIČKI PRIKAZI PODATAKA",
        fg_color="transparent",
        text_color="khaki",
        font=("Calibri", 40, "bold")
    )
    naslov_graf_lbl.grid(column=1, row=0, padx=20)
    
    # Radiobuttons.
    grafici_opcije = {
        "Broj pozicija po sektorima": "1",
        "Broj zaposlenih po godini zapošljavanja": "2",
        "Broj zaposlenih po pozicijama": "3",
        "Broj zaposlenih po radnim mestima": "4",
        "Procenat zaposlenih po sektorima": "5",
        "Odnos trenutno i ranije zaposlenih": "6",
        "Odnos zaposlenih s mobilnim i fiksnim telefonom": "7",
        "Odnos zaposlenih sa i bez emaila": "8",
        "Odnos ranije i trenutno zaposlenih po radnom mestu": "9",
        "Odnos ranije i trenutno zaposlenih po poziciji": "10"
    }
    
    graf_var = ctk.StringVar(graf_radio_frm)
    for (tekst, vrednost) in grafici_opcije.items():
        ctk.CTkRadioButton(
            graf_radio_frm,
            radiobutton_width=15,
            radiobutton_height=15,
            border_width_unchecked=2,
            border_width_checked=4,
            text=tekst,
            variable=graf_var,
            value=vrednost,
            font=("Calibri", 24)
        ).pack(expand=True, padx=50, pady=15, anchor="w")
    graf_var.set("1")

    graf_zatvori_btn = ctk.CTkButton(
        graf_dugmad_frm,
        text="Zatvori",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=grafici_tl.destroy
    )
    graf_zatvori_btn.pack(side="right", padx=(10, 30), pady=20)

    graf_primeni_btn = ctk.CTkButton(
        graf_dugmad_frm,
        text="Primeni",
        corner_radius=5,
        hover_color="slategrey",
        font=("Calibri", 28, "bold"),
        command=lambda: izbor_grafika(graf_var.get())
    )
    graf_primeni_btn.pack(side="right", padx=10, pady=20)


# Frame za logo i naslov.
naslovni_frm = ctk.CTkFrame(root, fg_color="transparent")
naslovni_frm.pack(pady=(20, 0))

# Logo.
slika = Image.open("pics/lisica.png")

logo = ctk.CTkImage(slika, size=(200, 249))
logo_manja = ctk.CTkImage(slika, size=(100, 125))

logo_lbl = ctk.CTkLabel(
    naslovni_frm,
    image=logo,
    text="",
    fg_color="transparent"
)
logo_lbl.grid(column=0, row=0)

# Naslov.
glavni_naslov_lbl = ctk.CTkLabel(
    naslovni_frm,
    text="SISTEM PODATAKA\nO ZAPOSLENIMA",
    fg_color="transparent",
    text_color="khaki",
    font=("Calibri", 40, "bold")
)
glavni_naslov_lbl.grid(column=1, row=0, padx=20)

# Frame za dugmad i objašnjenja.
izbor_frm = ctk.CTkFrame(root, fg_color="transparent")
izbor_frm.pack(pady=(40, 20))

# Izbor opcije (pritiskom na dugme).
novi_radnici_btn = ctk.CTkButton(
    izbor_frm,
    text="Novi radnici",
    width=250,
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=novi_radnici
)
novi_radnici_btn.grid(column=0, row=0, padx=20, pady=10, sticky="w")

pregled_podataka_btn = ctk.CTkButton(
    izbor_frm,
    text="Pregled podataka",
    width=250,
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=pregled_podataka
)
pregled_podataka_btn.grid(column=0, row=1, padx=20, pady=10, sticky="w")

azuriranje_btn = ctk.CTkButton(
    izbor_frm,
    text="Ažuriranje",
    width=250,
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=azuriranje_podataka
)
azuriranje_btn.grid(column=0, row=2, padx=20, pady=10, sticky="w")

izvestaji_btn = ctk.CTkButton(
    izbor_frm,
    text="Izveštaji",
    width=250,
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=izvestaji
)
izvestaji_btn.grid(column=0, row=3, padx=20, pady=10, sticky="w")

grafici_btn = ctk.CTkButton(
    izbor_frm,
    text="Grafici",
    width=250,
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=grafici
)
grafici_btn.grid(column=0, row=4, padx=20, pady=10, sticky="w")

# Objašenje opcija.
novi_radnici_lbl = ctk.CTkLabel(
    izbor_frm,
    text="Unos podataka o novim radnicima.",
    font=("Calibri", 24)
)
novi_radnici_lbl.grid(column=1, row=0, padx=20, pady=10, sticky="w")

pregled_podataka_lbl = ctk.CTkLabel(
    izbor_frm,
    text="Pregled podataka o zaposlenima.",
    font=("Calibri", 24)
)
pregled_podataka_lbl.grid(column=1, row=1, padx=20, pady=10, sticky="w")

azuriranje_lbl = ctk.CTkLabel(
    izbor_frm,
    text="Ažuriranje postojećih podataka.",
    font=("Calibri", 24)
)
azuriranje_lbl.grid(column=1, row=2, padx=20, pady=10, sticky="w")

izvestaji_lbl = ctk.CTkLabel(
    izbor_frm,
    text="Razni izveštaji o zaposlenima.",
    font=("Calibri", 24)
)
izvestaji_lbl.grid(column=1, row=3, padx=20, pady=10, sticky="w")

grafici_lbl = ctk.CTkLabel(
    izbor_frm,
    text="Grafički prikazi podataka.",
    font=("Calibri", 24)
)
grafici_lbl.grid(column=1, row=4, padx=20, pady=10, sticky="w")

# Dugme za zatvaranje aplikacije.
izlazak_btn = ctk.CTkButton(
    root,
    text="Izađi",
    corner_radius=5,
    hover_color="slategrey",
    font=("Calibri", 28, "bold"),
    command=zatvaranje_aplickacije
)
izlazak_btn.pack(padx=40, pady=(40, 40), anchor="e")

ctk.set_appearance_mode("dark")

root.mainloop()
