nazwa = input("Podaj nazwę pliku, wraz z rozszerzeniem: ")

if nazwa.endswith(".xls") or nazwa.endswith(".xlsx"):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik arkusza Excel.")
