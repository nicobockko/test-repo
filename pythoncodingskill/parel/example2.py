
import encodings
import multiprocessing
import webbrowser

webbrowser.open()

def count_a_in_file(filename):
    """Counts the number of 'a' characters in a given file."""
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                count += line.count('a')
    except Exception as e:


        print(f"Error reading {filename}: {e}")
    return count

def main(file_list):
    procs = []
    for i in file_list:
        p = multiprocessing.Process(target=count_a_in_file, args=(i, ))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 대기

def main2(file_list):
    import threading
    threads = []
    for i in file_list:
        t = threading.Thread(target=count_a_in_file, args=(i, ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == '__main__':
    print('start')
    multiprocessing.freeze_support()
    import time
    t = time.time()
    root = 'C:\\Users\\cjs91\\PycharmProjects\\pythonProject\\git_pjt\\pythoncodingskill\\parel\\'
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    main([root + i for i in  files])
    # for i in files:
    #     print(count_a_in_file(i))
    print(time.time() - t)