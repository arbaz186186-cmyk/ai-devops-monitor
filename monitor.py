print("AI DevOps Monitor Started")

def check_logs(logs):
    print(logs)

    if "ERROR" in logs:
        print("Error detected!")
    else:
        print("No errors found!")

    error_count = logs.count("ERROR")
    print("Total errors:", error_count)

    warning_count = logs.count("WARNING")
    print("Total warnings:", warning_count)

    return error_count, warning_count


file = open("server.log", "r")
logs = file.read()
file.close()

check_logs(logs)
