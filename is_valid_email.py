import re

def is_valid_email(email):
    # Define a regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,63}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email) and len(email) <= 256:
        return True
    else:
        return False

# Example usage:
email_address = "sreenivas@gmail.com"
if is_valid_email(email_address):
    print(f"The email address {email_address} is valid.")
else:
    print(f"The email address {email_address} is not valid.")

The email address sreenivas@gmail.com is valid.
