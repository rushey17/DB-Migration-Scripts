import re

# Read the local exported collection file as SQL format
with open('grants.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Remove ObjectId strings using regular expressions
modified_script = re.sub(r'ObjectId\("([a-fA-F0-9]+)"\)', r'\1', sql_script)

# Write the modified SQL file
with open('grants_stage1.sql', 'w') as file:
    file.write(modified_script)

