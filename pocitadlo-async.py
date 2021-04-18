import asyncio
import time


async def pocitaj():
    print("zacinam pocitat")
    await asyncio.sleep(1)
    print("hotovo")


async def main():
    await asyncio.gather(*[pocitaj() for _ in range(5)])

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"doba pocitania {elapsed:0.2f}.")
    s = time.perf_counter()

