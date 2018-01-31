# Twitch-chat-bot---IRC---Python

Python 3.6.4

Prosty bot nadzorujący użytkowników chatu na portalu twitch.tv.

System upomnień:
Użytkownik może dostać 2 upomnienia. Trzecie upomnienie skutkuje uruchomieniem systemu banów.

System banów:
Ban nr.1 - 60 sec
Ban nr.2 - 600 sec
Ban nr.1 - 3600 sec

Oprócz tego funkcjonuje system słów zakazanych. Po użyciu takiego słowa użytkownik dostanie timeout na 20 minut

Do zrobienia:

    -Pobieranie i wczytywanie danych z pliku json
    
    -Dokończenie systemu punktów (Aktualnie są funkcje sprawdzające ilość punktów oraz wysyłające kod gry jako prywatną wiadomość do użytkownika. Do zrobienia dodawanie punktów w zależności od tego czy użytkownik jest subksrybentem kanału czy nie. Okreslona ilość punktów pozwoli na wylosowanie kodu na gre w platformie Steam)
    
    -Nauczyć bota prowadzić luźne rozmowy z użytkownikami (Sieć neuronowa)


Komendy dla właściciela kanału:
!addcommand - dodawanie własnej komendy:
    np. !addcommand !napis Jakiś napis
    
    Lee_Sek: !addcommand !napis Jakiś napis
    April_1_: Command added: !napis
    Lee_Sek: !napis
    April_1_: Jakiś napis
    
!removecommand - usuwanie komendy:
    np. !removecommand !napis
    
    Lee_Sek: !removecommand !napis
    April_1_: Command removed: !napis
    Lee_Sek: !napis
    -----Brak odpowiedzi-----
    
!addbadword - dodawanie wyrazów do tablicy upomnień/banów
    np. !addbadword fag warrning
    
    Lee_Sek: !addbadword fag warrning
    April_1_: Word added to warrning list
    
    lub
    
    Lee_Sek: !addbadword fag timeout
    ModeratorApril_1_: Word added to timeout list
    
!removebadword - usuwanie wyrazów z tablicy upomnień/banów

    Lee_Sek: !removebadword fag warrning
    April_1_: Word removed from warrning list

    lub
    
    Lee_Sek: !removebadword fag timeout
    April_1_: Word removed from timeout list
    
Komendy dla użytkowników:

!uptime - czas działania bota
    np !uptime
    
    Lee_Sek: !uptime
    April_1_: 0h 13m 42s
    
!command - wyświetlenie jednej z komend ustalonych przez właściciela kanału
    np. !opgg
    
    Lee_Sek: !opgg
    April_1_: http://eune.op.gg/summoner/userName=lee+sek
    
!bans - ilość banów posiadanych przez użytkownika 
 
!points - ilość punktów posiadanych przez użytkownika 
 
!warrnings - ilość upomnień posiadanych przez użytkownika 
 
!game - losowanie gry
    
!elo - połączenie z Riot Api w celu pobrania informacji na temat dywizji streamera
    np. !elo
    
    Lee_Sek: !elo
    April_1_: Current elo: CHALLENGER I 690 LP
