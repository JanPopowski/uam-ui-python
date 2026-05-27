# Testy automatyczne UI — Python + Playwright (pytest-playwright)

---

## Spis treści

1. [Wymagania](#wymagania)
2. [Instalacja](#instalacja)
3. [Uruchamianie testów](#uruchamianie-testów)
4. [Proponowana struktura katalogów](#proponowana-struktura-katalogów)
5. [Dobre Praktyki](#dobre-praktyki-pom--stabilność-testów)
6. [Zadania (5)](#zadania-5)
   - [Zadanie 1: Add/Remove Elements](#zadanie-1-addremove-elements--dodawanie-i-usuwanie-elementów)
   - [Zadanie 2: Logowanie](#zadanie-2-logowanie--pozytywny-i-negatywny-scenariusz)
   - [Zadanie 3: Dynamic Loading](#zadanie-3-dynamic-loading--waits-zamiast-sleep)
   - [Zadanie 4: File Upload](#zadanie-4-file-upload--upload-i-walidacja)
   - [Zadanie 5: Alerts](#zadanie-5-alerts--obsługa-alertconfirmprompt)

---

## Wymagania

- Python **3.10+** (rekomendowane 3.11+)
- `pip`
- Dostęp do Internetu (testy używają publicznych stron demo)

---

## Instalacja

```bash
python -m pip install --upgrade pip
pip install pytest pytest-playwright pytest-html
playwright install
```

---

## Uruchamianie testów

Uruchomienie wszystkich testów:

```bash
pytest -q
```

Komenda do uruchomienia wszystkich testów z generowaniem raportu:
```
pytest -q --browser chromium --html=artifacts/report.html --self-contained-html --junitxml=artifacts/junit.xml --tracing retain-on-failure --video retain-on-failure --screenshot only-on-failure     
```

Przydatne parametry:

```bash
pytest --headed
pytest --headed --slowmo 200
pytest --tracing on
pytest --video on
pytest --screenshot only-on-failure
pytest --browser-channel chrome  
```



---

## Proponowana struktura katalogów

Minimalna struktura — jeden plik = jedno zadanie:

```
ui_tests/
  pages/
    __init__.py
    base_page.py
    add_remove_elements_page.py
    login_page.py
    dynamic_loading_page.py
    upload_page.py
    alerts_page.py

  tests/
    test_01_add_remove_elements.py
    test_01_add_remove_elements_pom.py
    test_02_login.py
    test_02_login_pom.py
    test_03_dynamic_loading.py
    test_03_dynamic_loading_pom.py
    test_04_upload.py
    test_04_upload_pom.py
    test_05_alerts.py
    test_05_alerts_pom.py

  conftest.py
  pytest.ini
  artifacts/
```

---

## Dobre praktyki (POM + stabilność testów)

1. **Zero selektorów w testach** — selektory żyją w POM.
2. **Akcje i asercje rozdzielone metodami** — np. `add_elements()` oraz `expect_delete_count()`.
3. **Brak `sleep()`** — używamy `expect(...)` i automatycznych waitów Playwright.
4. **Stabilne selektory** — preferuj `data-testid` / `get_by_role()` / `get_by_label()` gdy to możliwe.
5. **Artefakty na fail** — screenshot/trace/wideo znacznie skracają diagnostykę.

---

## Zadania (5)

### Zadanie 1: Add/Remove Elements — dodawanie i usuwanie elementów

**Strona:** https://the-internet.herokuapp.com/add_remove_elements/

**Kryteria zaliczenia:**
1. Kliknij **Add Element** 3 razy.
2. Zweryfikuj, że są 3 przyciski **Delete**.
3. Usuń 1 element i sprawdź, że zostały 2.
4. Usuń pozostałe i potwierdź, że nie ma żadnych **Delete**.

---

### Zadanie 2: Logowanie — pozytywny i negatywny scenariusz

**Strona:** https://the-internet.herokuapp.com/login

**Dane poprawne (na stronie):**
- username: `tomsmith`
- password: `SuperSecretPassword!`

**Kryteria zaliczenia:**
1. Dla błędnych danych pojawia się błąd.
2. Dla poprawnych danych pojawia się sukces.
3. Po wylogowaniu wraca ekran logowania.

---

### Zadanie 3: Dynamic Loading — waits zamiast sleep

**Strona:** https://the-internet.herokuapp.com/dynamic_loading/1

**Kryteria zaliczenia:**
1. Kliknij Start.
2. Poczekaj aż pojawi się tekst `Hello World!` bez `sleep`.
3. Zweryfikuj widoczność i treść.

---

### Zadanie 4: File Upload — upload i walidacja

**Strona:** https://the-internet.herokuapp.com/upload

**Kryteria zaliczenia:**
1. Wgraj plik (np. `example.txt`).
2. Kliknij Upload.
3. Zweryfikuj, że strona pokazuje nazwę pliku.

---

### Zadanie 5: Alerts — obsługa alert/confirm/prompt

**Strona:** https://the-internet.herokuapp.com/javascript_alerts

**Kryteria zaliczenia:**
1. Obsłuż JS Alert (accept).
2. Obsłuż JS Confirm (dismiss) i zweryfikuj wynik.
3. Obsłuż JS Prompt (wpisz tekst), zaakceptuj i zweryfikuj wynik.

---

### Zadanie 6: POM - Page Object Model

**Kryteria zaliczenia:**
1. Wszystkie testy powinny mieć utworzony swój odpowiednik z zastosowaniem wzorca POM
2. Obie wersje testów zachowane w repozytorium

---

### Zadanie 7: Pipeline - Github Actions

**Kryteria zaliczenia:**
1. Przygotuj pipeline składający się z kroków:
   1. Uruchomienie testów bez POM
   2. Uruchomienie testów z POM
   3. Zebranie obu raportów z testów i udostępnienie ich do pobrania w Github
   4. Pipeline można uruchamiać ręcznie
