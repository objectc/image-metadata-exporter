import json
import sys
import generator                # for export image meta into a dict

import os
if len(sys.argv)<2:
    print("no image resource dir!")
else:
    output = open('meta.data','w')
    metalist = []
    for filename in os.listdir(sys.argv[1]):
        filepath = os.path.join(sys.argv[1],filename)
        if os.path.isfile(filepath):
            print (filepath)
            subdata = generator.export(filepath)
            metalist.append(subdata)
    json.dump(metalist,output)
    output.close


