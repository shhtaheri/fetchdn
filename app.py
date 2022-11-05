import re

def fetch_domain_name(url):
    return re.sub(".+\/\/|www.|\..+", "", url)

dn = fetch_domain_name("https://github.com")
print(dn)