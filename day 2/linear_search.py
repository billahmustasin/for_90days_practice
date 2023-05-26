list_of_env = ["dev","stg","prd","test","qa"]

key = "er"
is_found = False
for env in list_of_env:
    if env == key:
        is_found = True

if is_found:
    print("found")
else:
    print("not found")