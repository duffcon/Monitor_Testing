from subprocess import Popen, PIPE
import re
import math
import os.path
import sys


hw_info_patterns = dict ({
    "Vendor": dict({ "Pattern": 'Vendor: (\w+)"*.*"*' , "Group": 1  }), 
    "Model": dict({ "Pattern": 'Model: "(.*)"', "Group": 1  }),
    "Serial": dict({ "Pattern": 'Serial ID: "(.*)"', "Group": 1  }),
    "Year": dict({ "Pattern": 'Year of Manufacture: (\d+)', "Group": 1  }),
    "HorizontalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 1  }),
    "VerticalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 2  }),
    "RefreshRate": dict({ "Pattern": '(?s:.*)Resolution: .*@(\d+)Hz' , "Group": 1  }),
    "Length": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 1  }),
    "Width": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 2 })
        })
monitor_data = dict()


# call and return output of subprocess
def sendCommand(c):
    p = Popen(c, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"")
    rc = p.returncode
    if p.returncode != 0:
        print(err)
        return 0
    output = str(output, 'utf-8')
    return output

# return a list of strings, one for each connected monitor
def getHwInfo():
    m = sendCommand(['hwinfo', '--monitor'])
    m = m.split("\n\n")
    return m

# parse the data for the first monitor, simple example
info_strings = getHwInfo()
info_string = info_strings[0]
for key in hw_info_patterns.keys():
    match = re.search(hw_info_patterns[key]["Pattern"],info_string)
    if match == None:
        continue
    monitor_data[key] = match.group(hw_info_patterns[key]["Group"])

print(monitor_data)
