import psutil

def get_process_info() -> dict:
    processes = {}
    for proc in psutil.process_iter(['name', 'status']):
        name = proc.info['name']
        status = proc.info['status']
        if name and name.endswith('.exe'):
            processes[name] = status
    return processes

def print_to_file(dict: dict, filepath: str = "processes.txt") -> None:
    with open(filepath, 'w') as fle:
        for name, status in dict.items():
            fle.write(f"{name} -- {status}\n")
        print("Finished writing to file")
    

def get_monitored(dict: dict) -> dict:
    mn_prcs = {}
    mntr = ["firefox", "spotify"]
    for name, status in dict.items():
        if status == "running" and name.lower()[:-4] in mntr:
            mn_prcs[name[:-4]] = status
    return mn_prcs
        
    

if __name__ == "__main__":
    processses = get_process_info()
    print(processses)
    print_to_file(processses)
    mon = get_monitored(processses)
    print(mon)