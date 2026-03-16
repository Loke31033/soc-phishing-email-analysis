import re

with open("email_samples/phishing_email.txt","r") as file:
    content = file.read()

urls = re.findall(r'https?://[^\s]+', content)

print("\nDetected URLs:\n")

for url in urls:
    print(url)
