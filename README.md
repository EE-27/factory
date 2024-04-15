Úkol
Vytvořte webovou aplikaci s rozhraním API a panelem správce.
Vytvořte databázi pomocí migrací Django.
Požadavky na implementaci:

Potřebujete implementovat síťový model pro prodej elektroniky.
Síť by měla mít hierarchickou strukturu o třech úrovních:

Továrna;
maloobchodní síť;
individuální podnikatel.
Každý článek v síti odkazuje pouze na jednoho dodavatele zařízení (ne nutně na předchozího v hierarchii). Je důležité si uvědomit, že úroveň hierarchie není určena názvem odkazu, ale jeho vztahem k ostatním prvkům sítě, tj. továrna je vždy na úrovni 0, a pokud maloobchodní síť odkazuje přímo na továrnu a obchází ostatní odkazy, je její úroveň 1.

Každý článek sítě by měl mít následující prvky:
Název.
Kontakty:
e-mail,
země,
město,
ulice,
číslo domu.
Produkty:
název,
model,
datum uvedení výrobku na trh.
Dodavatel (předchozí objekt v hierarchii sítě).
Dluh vůči dodavateli v peněžním vyjádření, s přesností na haléře.
Čas vytvoření (vyplňuje se automaticky při vytvoření).
