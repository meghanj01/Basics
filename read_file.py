import resource
import sys


def read_file(file_name):
    text_file = open(file_name, "r")
    line_list = text_file.readlines()
    text_file.close()
    return line_list


file_lines = read_file(sys.argv[1])

print(type(file_lines))

print(len(file_lines))

for line in file_lines:
    print(line)

print("Peak Memory Usage =", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print("User Mode Time =", resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print("System Mode Time =", resource.getrusage(resource.RUSAGE_SELF).ru_stime)
