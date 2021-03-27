import re

HOUR_IN_SEC = 3600
MIN_IN_SEC = 60
START_TIME_IN_SEC = 12000
END_TIME_IN_SEC = 40620


def count_total_size_of_files(name_of_file: str):
    total_size = 0
    with open(f'{name_of_file}.txt', 'r') as reader:
        for line in reader:
            result = re.findall(r'\d+:(\d+):(\d+):(\d+).*GET.*\.css.*200 (\d+) "', line)
            for hour, min, sec, size in result:
                total_time_in_sec = int(hour) * HOUR_IN_SEC + int(min) * MIN_IN_SEC + int(sec)
                if START_TIME_IN_SEC <= total_time_in_sec <= END_TIME_IN_SEC:
                    total_size += int(size)
    return total_size


print("Total size of css files that were successfully returned (request type - GET) between 03:20 and 11:17: ",
      count_total_size_of_files("test"))
