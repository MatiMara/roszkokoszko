import time
from colorama import Fore, Style, init

init()

blocks = ["Klient", "Sterownik", "Kuchnia", "Robot"]

def highlight_block(block_name):
    for b in blocks:
        if b == block_name:
            print(f"{Fore.GREEN}{block_name}{Style.RESET_ALL}", end=" ")
        else:
            print(f"{Fore.RED}{b}{Style.RESET_ALL}", end=" ")
    print()

def klient():
    highlight_block("Klient")
    time.sleep(2)

def sterownik():
    highlight_block("Sterownik")
    time.sleep(1)

def kuchnia():
    highlight_block("Kuchnia")
    time.sleep(3)

def robot():
    highlight_block("Robot")
    time.sleep(1)

def wait_for_path_completion():
    for block in blocks:
        highlight_block(block)
        time.sleep(1)

def main():
    for _ in range(4):
        klient()
        sterownik()
        kuchnia()
        sterownik()
        kuchnia()
        sterownik()
        robot()
        sterownik()
        kuchnia()
        sterownik()
        robot()
        sterownik()
        klient()
        sterownik()
        robot()
        sterownik()

    # Czekaj na zakończenie wszystkich bloków po przejściu ścieżki
    wait_for_path_completion()

if __name__ == "__main__":
    main()
