#import libraries
from django.core.files import File
import subprocess
from pathlib import Path


#converter for pcap files to csv files
def PcapConverter(file):
    filename = file.replace('pcap', 'csv')
    command = ['cicflowmeter', '-f', file, '-c', filename]
    process = subprocess.run(command)
    return print(filename)

#handles uploaded files
def handle_uploaded_file(f):
    cwd = Path.cwd() / Path("NetworkTraffic")
    file_name = f.name
    if file_name.endswith('csv'):
        path = str(Path(cwd)/ Path(file_name))
        with open(path, "wb+") as file:
            file = File(file)
            for chunk in f.chunks():
                file.write(chunk)
    elif file_name.endswith('pcap'):
        #file = PcapConverter(f)
        print("error here!!!")
    else:
        print("no error")




