import json

# this script sorts all the cemeterys by either average war or total war
# and stores it as a list of tuples in war.json

with open ("cem_dict_final.json","r") as f:
    war_dict = json.load(f)

#print(type(war_dict))
war_list = []
for keys in war_dict:
    cem_tuple=()
    sum = 0
    for el in war_dict[keys]:
        i = war_dict[keys].index(el)
        try:
            sum+= float(war_dict[keys][i][1])
        except ValueError:
            sum += 0
    cem_tuple = (keys,sum,sum/len(war_dict[keys]),len(war_dict[keys]))
    war_list.append(cem_tuple)
    
# to sort by average war set key to lambda x: x[2] to do total set to lambda x: x[1]
sorted_war_list = sorted(war_list, key=lambda x: x[2], reverse=True)
print (len(sorted_war_list))
with open("war.json", "w") as f:
    json.dump(sorted_war_list, f)
