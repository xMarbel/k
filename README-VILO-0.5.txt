VILO 0.5 — porządek w nawigacji i kontach
==========================================

ZMIANY
- Zakładka Wiadomości pokazuje tylko prywatne rozmowy, nie grupy i serwery.
- Rejestracja oddziela unikatową @nazwę użytkownika od nicku.
- Wyszukiwanie znajomych i identyfikacja używają @username.
- Profile zachowują zdjęcia, banery, bio i status; nick można zmieniać.
- Aktualizacja bazy jest zgodna ze starymi kontami (domyślnie nick = stara nazwa użytkownika).
- To jest kod źródłowy, a nie gotowy instalator.
- Eksperymentalne audio 1:1 w prywatnych rozmowach: mikrofon, odbierz, rozłącz, wycisz.
- Signaling przez zalogowane WebSockety, szyfrowanie mediów WebRTC.
- Bez TURN i serwera online: połączenia przez Internet mogą nie działać.
- Kanały głosowe i wideo NIE są jeszcze funkcjonalne.

INSTALATOR WINDOWS
Wgraj zawartość tego projektu do repozytorium i uruchom istniejący
workflow instalatora. Jeśli workflow używa polecenia npm run dist:win,
dodaj -- --publish never żeby zapobiec błędowi GH_TOKEN.
Nie usuwaj folderu data starego VILO. Zachowaj jego kopię.
