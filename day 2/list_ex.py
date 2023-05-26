list_of_cloud_env = list(["aws","azure","gcp"])

list_of_envs = ["dev","stg","prd","tst","qa"]
list_of_envs.append("client")
for i in list_of_envs:
    print("deploying")
    print(i)


list_of_envs.insert(1,"testing")
print(list_of_envs)
a = 2
print(dir(a))