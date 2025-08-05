import psutil


def is_exe(file:str):
    """
    Checks if the file is an .exe file
    
    Returns True if it's exe file, False otherwise
    """
    split = file.rsplit(".", 1)
    if split[-1] == "exe":
        return True
    else:
        return False

def write_to_file(file_name, name):
    """
    Writes to a file

    First argument: Path/name of a file to write into
    Second argument: Item to be written into a file
    """
    with open(file_name, "a") as fle:
        fle.write(name+"\n")



def register_running_processes():
    """
    Writes all the currently running exe files into a txt file

    Returns a list of running processes
    """
    open("Processes.txt", "w").close()
    running_processes=[]
    for process in psutil.process_iter(["name"]):
        name = process.info["name"]
        if is_exe(name):
            file = str(name).rsplit(".", 1)
            file_name = file[0]
            if file_name not in running_processes:
                running_processes.append(file_name)
                write_to_file("Processes.txt", file_name)
            else:
                pass
    return sorted(running_processes)




def find_monitored_processes(running_file):
    """
    Reads names of running processes from a file (register_running_processes), writes into a new file all the present processes that are being monitored

    Argument: path/name of the file containing process names
    
    Returns a list of all monitored procecsses present in the given file
    """
    monitored_processes = ["discord", "spotify", "firefox", "steam"]
    monitored_present = []
    with open(running_file, "r") as fle:
        content = fle.readlines()
        print(content)
    open("Monitored.txt", "w").close()
    with open("Monitored.txt", "a"):
        for name in content:
            name = name.strip()
            if name.lower() in monitored_processes:
                write_to_file("Monitored.txt", name.lower())
                monitored_present.append(name.lower)
            else:
                pass
    return monitored_present


def monitored_present(process_list:list):
    monitored_processes = ["discord", "spotify", "firefox", "steam", "winstore.app", "chrome", "hitman3"]
    mon_present = []
    for name in process_list:
        if name.lower() in monitored_processes:
            mon_present.append(name.lower())
        else:
            pass
    return mon_present