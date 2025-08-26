#list -> data structure which can hold multiple value of multiple type
#list -> data structure which can hold multiple valure of same type
list_of_cloud = ["aws","gcp","azure","digital","ocean","utho","alibaba","oracle"]
cloud = "gcp" #variable

print(list_of_cloud)

# add a new cloud saleforce

list_of_cloud.append("salesforce")   

# add a new cloud IBM

list_of_cloud.append("IBM")    # add to the end of list

print(list_of_cloud)

list_of_cloud.insert(2,"heroku")

print(list_of_cloud)

list_of_cloud.insert(1,"kashif")

print(list_of_cloud)

print(len(list_of_cloud))

list_of_cloud.insert(0,"HELLO CLOUD")

print(list_of_cloud)

# iteration of a list
for cloud in list_of_cloud:

    print(cloud)

for i in range(0,11):

    print("hello friends")
