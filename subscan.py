#example of code : subscan.py wordlistfile.txt example.com
import requests 
import sys 

sub_list = open(sys.argv[1]).read()  
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ", sub_domains)   
    
