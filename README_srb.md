# 1. Naslov projekta
    SISTEM ZA UNOS PODATAKA O ZAPOSLENIMA

# 2. Kratak opis projekta
Projekat je urađen kao sastavni deo prakse kursa "Python Developer - 
Advanced" u kompaniji **ITOiP** (IT Obuka i Praksa - https://itoip.rs).

Sistem za upravljanje i unos osnovnih podataka o bivšim i zaposlenim 
radnicima.

Aplikacija je urađena u Pythonu, uz pomoć PostgreSQL sistema za upravljanje 
bazama podataka. Za kreiranje korisničkog interfejsa upotrebljena je 
biblioteka 'CustomTkinter'.

Tabele koje su urađene kao primer nalaze se u arhivi 'tables.zip'.

# 3. Sadržaj README.md fajla
#### 1. Naslov projekta
#### 2. Kratak opis projekta
#### 3. Sadržaj README.md fajla
#### 4. Baza podataka i struktura tabela
#### 5. Opis i korišćenje aplikacije

# 4. Baza podataka i struktura tabela
Naziv baze podataka: "zaposleni"

Tabele:

    radnici
        id_radnika          (varchar (10), primary key, not null)
                                                        # ID radnika
        ime                 (varchar (20), not null),   # ime radnika
        prezime             (varchar (20), not null),   # prezime radnika
        adresa              (varchar (40), not null),   # adresa stanovanja
        telefon             (varchar (10), not null),   # telefon radnika
        email               (varchar (40)),             # email radnika
        pozicija            (varchar (30), not null),   # pozicija radnika
        lokacija            (varchar (4), not null),    # radno mesto radnika
        istorija            (text, not null),           # promena radnog odnosa
        zaposlen            (boolean, not null),        # zaposlen ili ne
        datum_zaposljavanja (date not, null),           # datum zapošljavanja
        prestanak_radnog_odnosa     
                            (date)      # datum prekida radnog odnosa

    pozicije
        naziv               (varchar (30), primary key, not null)
                                                        # naziv pozicije
        opis                (text, not null)            # odgovornisti pozicije
        sektor              (varchar (15), not null)    # oblast rada pozicije

    lokacije
        sifra               (varchar (4), primary key, not null)
                                                        # skraćeni naziv
        pun_naziv           (varchar (25), not null)    # pun naziv lokacije
        adresa              (varchar (40), not null)    # adresa radnog mesta

# 5. Opis i korišćenje aplikacije

## 5.1. Glavni ekran

Glavni ekran sadrži logo i naziv firme, naslov aplikacije i dugmad za izbor 
akcije u aplikaciji. Svako dugme pored sebe ima i kratko objašnjenje, osim 
dugmeta 'Izađi' na dnu ekrana, koje služi za zatvaranje aplikacije.

## 5.2 Novi radnici

Pritiskom na dugme 'Novi radnici' na glavnom ekranu, otvara se novi prozor u 
kojem se nalazi forma za unos podataka o novom radniku.

Na vrhu prozora nalaze manji logo i naziv firme, pored kojeg je naslov ovog 
prozora.

Ispod toga je okvir naziva 'ID radnika' u kojem se generiše novi 
desetocifreni ID koji ne postoji u bazi.

Nakon toga sledi deo s nazivom 'Lični podaci' u kojem su polja za unos 
imena, prezimena, adrese, telefona i emaila, ukoliko ovaj poslednji postoji.
Prva četiri polja za unos su obavezna, jer, ukoliko se ona ne popune, 
iskaču obaveštenja o nepopunjenim poljima.

Zatim sledi okvir s nazivom 'Podaci o zaposlenju' u koja se unose pozicija 
novog radnika u firmi, naziv lokacije njegovog radnog mesta i datum 
zapošljavanja.

Ispod je obavaštenje o oznaci koja stoji nakon naziva obaveznih polja.

Na dnu ovog ekrana postoji dugme 'Unesi', koje ubacuje unesene vrednosti u 
bazu podataka i dugme 'Odustani' koje zatvara ekran.

## 5.3 Pregled podataka

Pritiskom na dugme 'Pregled podataka' na glavnom ekranu otvaramo novi 
prozor u kojem vršimo pregled podata svih radnika koji su zaposleni u firmi 
ili su to nekada bili.

Određeni radnik se bira iz padajućeg menija 'Izbor radnika'. Radnici su 
sortirani po prezimenu, a iza prezimena i imena stoji i njihov ID broj, jer 
je moguće da postoje radnici s istim imenom i prezimenom.

Izborom radnika automatski se ispisuju podaci u odgovarajuća polja.

Na dnu je dugme 'Zatvori' koje zatvara ovaj prozor.

## 5.4. Ažuriranje

Dugme 'Ažuriranje' na glavnom ekranu vodi nas u formu za ažuriranje 
postojećih podataka. Na vrhu se ponovo nalazi logo s nazivom firme, kao i 
naslov ove forme.

Sledi okvir s nazivom 'Kriterijumi' u kojem možemo koristiti kriterijume 
(filtere), kako bismo suzili listu za izbor radnika. Na vrhu okvira su 
osnovne informacije za korišćenje ovih filtera, a nakon toga slede padajući 
meniji sa izborom radnika na određenoj poziciji, na određenom mestu ili po 
tome da li je radnik još uvek zaposlen ili nije.

Izborom nekog od filtera menja se i lista za izbor radnika. Ukoliko nijedan 
filter nije odabran, lista padajućeg menija 'Izbor radnika' sadrži sve 
radnike iz baze podataka.

Ispod filtera je okvir 'Izbor radnika' u kojem biramo radnika kojem treba 
ažurirati podatke. Izborom nekog radnika iz padajućeg menija automatski se 
ispisuju podaci u ovom i narednom okviru. U ovom okviru još postoji ID 
radnika, koji ne može da se menja i informacija o tome da li je radnik još 
zaposlen ili nije.

Sledeći okvir 'Podaci za menjanje' ima tri kolone. Prva kolona sadrži 
nazive podataka, druga tekuće podatke iz baze podataka, a treća polja za 
unos, padajuće menije i polja za izbor datuma. Podaci se mogu ažurirati 
zbog njihove promene ili lošeg unosa u bazu podataka. Mogu se menjati svi, 
nekoliko podataka ili samo jedan od njih.

Dugme 'Ažuriraj' ubacuje nove podatke u pripadajuće tabele. Dugme 'Resetuj' 
uklanja filtere, izbor radnika i sve podatke, tako da sve možemo birati i 
upisivati ispočetka. Dugme 'Zatvori', naravno, zatvara ovaj prozor.

## 5.5. Izveštaji

Pritiskom na dugme 'Izveštaji' na glavnom ekranu otvara se novi prozor. U 
tom prozoru na vrhu imamo logo i naziv firme, uz koje stoji naslov prozora.

Ispod stoji okvir za izbor jedne od više opcija, koje su ujedno i kratak 
opis izeštaja koji ćemo dobiti otvaranjem nove forme.

'Hijerarhija firme' je slikoviti prikaz nivoa nadređenosti u firmi. Ispod 
naslova i podnaslova nalazi se kratka legenda i informacije za tumačenje 
ovog prikaza. Sam prikaz je ispod toga u posebnom okviru 'Hijerarhija 
pozicija u firmi'.

Opcija 'Spisak pozicija s odgovornostima' daje nam uvid u odgovornosti koje 
zaposleni ima na odgovarajućoj pozicji.

Opcijom 'Informacije o radnim mestima' otvara se novi prozor s 
informacijama u tri kolone. Prva je kratka oznaka za radno mesto, druga je 
pun naziv radnog mesta, a treća je lokacija, tj. adresa, na kojoj se to 
radno mesto nalazi.

Poslednja opcija 'Delokrug sektora' vodi nas u formu koja prikazuje koji 
sektori u firmi postoje i koje radne pozicije pripadaju kojim sektorima.

## 5.6 Grafici

Pritiskanjem poslednjeg dugmeta na glavnoj formi otvara se prozor za izbor 
nekog od grafika ili dijagrama. Postoji izbor za deset različitih vrsta 
grafičkog prikaza odnosa među podacima koje imamo.
