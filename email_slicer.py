# Get user email address
email = input("Cual es tu direccion de correo?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = "Tu nombre de usuario es '{}' y tu dominio es '{}'".format(user_name,domain_name)

# Display output message
print(output)