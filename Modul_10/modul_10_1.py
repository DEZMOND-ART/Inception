import threading
from time import sleep,time

def wite_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'слово № {i} \n')
            sleep(0.1)
    print(f'Запись в фаил {file_name} завершена')

start_time = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time()
print(f'Время выполнения функций: {end_time - start_time}')

start_time_threads = time()

threads = []
threads.append(threading.Thread(target=wite_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=wite_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=wite_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=wite_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f'Время выполнения потоков: {end_time_threads - start_time_threads} секунд')