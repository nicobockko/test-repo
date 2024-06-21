
import concurrent.futures


def create_files(n=10000):
    import random
    """Creates four sample text files."""
    file_contents = [
        "apple banana apricot avocado\n" *n,
        "cat bat rat mat\n"*n,
        "aardvark antelope armadillo\n"*n,
        "anaconda anglerfish alligator\n"*n
    ]
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    for file_name, content in zip(file_names, file_contents):
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Created {file_name} with content:")

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
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(count_a_in_file, file_list)
    for filename, count in zip(file_list, results):
        print(f"File {filename} has {count} 'a' characters.")


if __name__ == '__main__':
    # create_files(10000000)
    import time
    t = time.time()
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    # main(files)
    for i in files:
        print(count_a_in_file(i))
    print(time.time() - t)