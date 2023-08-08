insert_statement = ''  #update this based on different table schema
#for grants collection eg., INSERT INTO "grants_v" ("_id", "donor_id", "npo_id", "grant_year", "grant_amount", "grant_description", "grant_desc_and_grantee_mission") VALUES\n'
items = []
i = 1
with open('grants_stage1.sql', 'r') as sql_file:  #read stage1 transformed file
   for item in sql_file:
    if i%3 == 0:  
       items.append(item.strip())  #only getting the actual insert values record for eg., ('638cbb4e89755d0b6ced87c2', '638cbaa589755d0b6cd126e5', '638cba7889755d0b6ccec22d', 2016, ....)
       i = i+1

with open('grants_stage2.sql', 'a') as output_file:
    for i, j in enumerate(items):
        if (i + 1) % 4000 == 1:  #batch insert of only 4000 records
            output_file.write(insert_statement)
        modified_item = j[:-1] + ',' if (i + 1) % 4000 != 0 else j
        output_file.write(modified_item + '\n')

print('completed!')
