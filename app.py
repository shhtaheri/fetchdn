import re

def fetch_domain_name(url):
    return re.sub(".+\/\/|www.|\..+", "", url)

# Second Solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
    
dn = fetch_domain_name("https://github.com")
print(dn)