from validate_email import validate_email

is_valid = validate_email(
    email_address="james@onlyhauling.com",
    smtp_helo_host="mohsinrazzaq.dev",
    smtp_from_address="mohsin@mohsinrazzaq.dev",
)
print(is_valid)

