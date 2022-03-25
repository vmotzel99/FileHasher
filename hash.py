import os
import hashlib
from datetime import datetime

nohashlist = [/dev, /proc, /run, /sys, tmp, /var/lib, /var/run]

st = open("hashstored.txt", "a")

for root, dirs, files in os.walk("/"):
  for filename in files:
    if root not in nohashlist:
      print(os.path.join(root, filename))
      with open(filename, "rb") as f:
        bytes = f.read()
        readfhash = hashlib.sha256(bytes).hexdigest();
        st.write(filename, readfhash, datetime.now())
      
    
        

