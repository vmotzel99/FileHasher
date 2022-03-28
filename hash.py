import os
import sys
import hashlib
from datetime import datetime

nohashlist = ['dev', 'proc', 'run', 'sys', 'tmp', 'var/lib', 'var/run', 'boot', 'mnt', 'var', 'opt', 'etc']

def main():
    st = open("hashstored.txt", "a")
    for root, dirs, filen in os.walk('/'):
        for fils in filen:
            addpath = (os.path.join(root, fils))
            if ".cache" in str(addpath) or ".vscode" in str(addpath) or ".mozilla" in str(addpath):
                break
            else:
                for i in nohashlist:
                    if i not in addpath:
                        with open(addpath, "rb") as f:
                            bytes = f.read()
                            readfhash = hashlib.sha256(bytes).hexdigest()
                            st.write(fils)
                            st.write(readfhash)
                            st.write(str(datetime.now()) + "\n") 
    st.close()

if __name__=="__main__":
    main()
      
    
        

