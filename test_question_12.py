import re
text = "Contact us at john@gmail.com or support@example.com. You can also email admin@school.org."
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
print("Emails found:", emails) 