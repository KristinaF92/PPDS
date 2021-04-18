import time


def pocitaj():
    print("zacinam pocitat")
    time.sleep(1)
    print("hotovo")


def main():
    for _ in range(5):
        pocitaj()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"doba pocitania {elapsed:0.2f}.")
