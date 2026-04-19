import multiprocessing
import time

def oshirish(hisoblagich, qiymat):
    for _ in range(100000):
        hisoblagich.value += qiymat

if __name__ == "__main__":
    hisoblagich = multiprocessing.Value('i', 0)  # 'i' - integer, 0 - default qiymat

    processlar_soni = 5
    qiymat = 1

    processlar = []
    for _ in range(processlar_soni):
        p = multiprocessing.Process(target=oshirish, args=(hisoblagich, qiymat))
        processlar.append(p)
        p.start()

    for p in processlar:
        p.join()

    print(hisoblagich.value)
```

Kodda biz `multiprocessing.Value` yordamida umumiy hisoblagichni yaratib, keyin 5 ta jarayonni yaratib, har bir jarayon umumiy hisoblagichni 100 000 marta oshiradi. Natija hisoblagichni qiymati bo'ladi.
