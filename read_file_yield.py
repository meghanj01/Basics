import resource
import sys


def read_file_yield(file_name):
    text_file = open(file_name, "r")
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data


file_data = read_file_yield(sys.argv[1])
print(type(file_data))

for l in file_data:
    print(l)

print("Peak Memory Usage =", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print("User Mode Time =", resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print("System Mode Time =", resource.getrusage(resource.RUSAGE_SELF).ru_stime)
