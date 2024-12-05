import socket
import threading

# Константы
HOST = '127.0.0.1'  # Адрес сервера
PORT = 10001  # Порт сервера

clients = []
messages = []


# создаем сокет
# подключемся к серверному сокету

# 2 задание
'''def primary(start, end):
    for n in range(start, end + 1):
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n)


def main():
    threadings = []
    start = 1
    end = 200
    n = end - start
    for i in range(start, end, (end - start) // 200 + 1):
        start_s = i
        end_s = i + (end - start) // 200 if i + (end - start) // 200 < n else end
        threadings.append(threading.Thread(target=primary, args=(start_s, end_s,)))

    for t in threadings:
        t.start()
        t.join()'''


#######################################


# 3 задание
'''def fact(start, end, a):
    f = 1
    for n in range(start, end + 1):
        f *= n

    a.append(f)


def main():
    a = []
    s = []
    n = 5
    for i in range(1, (n + 1), n // 5):
        l_start = i
        l_end = i + n // 5 if i + n // 5 < n + 1 else n + 1

        s.append(threading.Thread(target=fact, args=(l_start, l_end - 1, a,)))

    for t in s:
        t.start()
        t.join()

    result = 1
    for n in a:
        result *= n

    print(result)'''


################################


#4 задание
'''def fact(start, end, a):
    f = 1
    for n in range(start, end + 1):
        f *= n

    a.append(f)


def main():
    a = []
    s = []
    c_r = int(input("Введите количество потоков: "))
    n = int(input("Введите число, для которого хотите вычислить факториал: "))
    step = c_r if c_r < n else n

    for i in range(1, (n + 1), n // step):
        start_s = i
        end_s = i + n // step if i + n // step < n + 1 else n + 1

        s.append(threading.Thread(target=fact, args=(start_s, end_s - 1, a,)))

    for t in s:
        t.start()
        t.join()

    result = 1
    for n in a:
        result *= n

    print(result)'''


################################


#5 задание
'''
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_array(arr):
    return sorted(arr)


def threaded_sort(arr, result, index):
    result[index] = sort_array(arr)


def parallel_sort(arr, num_threads=4):
    chunk_size = len(arr) // num_threads
    threads = []
    result = [None] * num_threads

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = None if i == num_threads - 1 else (i + 1) * chunk_size
        sub_array = arr[start_index:end_index]

        thread = threading.Thread(target=threaded_sort, args=(sub_array, result, i))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


    sorted_array = result[0]
    for i in range(1, len(result)):
        sorted_array = merge(sorted_array, result[i])

    return sorted_array


if __name__ == "__main__":
    import random

    large_array = [random.randint(0, 10000) for _ in range(100)]

    sorted_array = parallel_sort(large_array, num_threads=8)

    print(sorted_array)'''


##############################################


#6 задание

import time
import random

class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if amount <= self.balance:
                print(f"Снимаем {amount} рублей. Остаток до снятия: {self.balance} рублей.")
                time.sleep(random.uniform(0.1, 1))
                self.balance -= amount
                print(f"Снято {amount} рублей. Остаток после снятия: {self.balance} рублей.")
            else:
                print(f"Недостаточно средств для снятия {amount} рублей. Остаток: {self.balance} рублей.")

def client(atm, amount):
    atm.withdraw(amount)

if __name__ == "__main__":
    initial_balance = 1000
    atm = ATM(initial_balance)


    clients = []
    for i in range(5):
        amount_to_withdraw = random.randint(100, 300)
        client_thread = threading.Thread(target=client, args=(atm, amount_to_withdraw))
        clients.append(client_thread)
        client_thread.start()


    for client_thread in clients:
        client_thread.join()

    print(f"Конечный баланс: {atm.balance} рублей.")

'''
if __name__ == '__main__':
    main()'''