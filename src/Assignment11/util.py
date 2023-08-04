import re

def validateemail():
    def validemail(email):
        p = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
        return re.match(p, email)


n = int(input())
emails = [input().strip() for _ in range(n)]
valid_emails = list(filter(validateemail(), emails))
valid_emails.sort()
print(valid_emails)