from multiprocessing import Pool, cpu_count
import time


def sync_factorize(*number):
    total_result = []
    for num in number:
        result = []
        for i in filter(lambda x: num % x == 0, range(1, num+1)):
            result.append(i)
        total_result.append(result)
    return total_result


def async_factorize(number):
    result = []
    for i in filter(lambda x: number % x == 0, range(1, number+1)):
        result.append(i)
    return result


if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)
    start_time = time.time()
    sync_res = sync_factorize(*numbers)
    print(f"Sync function executed time: {time.time() - start_time}")

    print(f"Count CPU: {cpu_count()}")
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        async_res = pool.map(async_factorize, numbers)
        pool.close()
        pool.join()
    print(f"Async function executed time:{time.time() - start_time}")


