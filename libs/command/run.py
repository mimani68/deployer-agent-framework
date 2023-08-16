import os

def run_command(command):
    osResult = os.popen(command).readlines()
    result = []
    for item in osResult:
        lines = item.split("\n")
        result.append("".join(line.rstrip() for line in lines))
    return result
