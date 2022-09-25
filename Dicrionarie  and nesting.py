#the dictionar have key and value
# programming_dectionary = {"Bug": "Abdiladiif saaalax Axmed",
#                           "function": "shaqada"}
# print(programming_dectionary)
#
# accesing
# print(programming_dectionary["function"])
#
# Adding new item a dictionarie
#
# programming_dectionary["dadda"] = 22
# print(programming_dectionary)
#
# empty dictioanire
#
# empl_list = {}
#
# Deleting dictioantei
#
# programming_dectionary = {}
# print(programming_dectionary)
#
# Edit a item of dictioanrie
#
# programming_dectionary["Bug"] = "saalax"
# print(programming_dectionary)
#
# loopring the dictioanire
#
# for key in programming_dectionary:
#     print(key)
#     print(programming_dectionary[key])

#003 Grad programmming
#
# student_score = {
#     "Harry": 81,
#     "Ran": 78,
#     "Hermiane": 99,
#     "Drac": 74,
#     "Nerville": 62,
# }
#
# student_grades = {}
#
# for student in student_score:
#     score = student_score[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Exceptaions"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#     print(student_grades)

#Nesting List and dictionariers

capitals = {
    "France": "paris",
    "German": "Berlin",
}
travel_log = {
    "france": {"cities_visited": ["paris", "Lille","Dijon"], "total_visits":12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
# Nesting Dic in list

travel_log = [
    { "Country": "france",
      "cities_visited": ["paris", "Lille","Dijon"],
      "total_visits":12
      },

    {
     "Country": "German",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
    },
]

#005 Dic list code challenge

travel_log = [
    {
        "country": "france",
        "Visits": 12,
        "cities": ["paris","lille","Dijon"]
    },
    {

        "country": "Germany",
        "Visits": 12,
        "cities": ["Berlin", "Hambury", "Stuttrgart"]
    }


]
# Write the function that will allow new country
def add_new_coutry(country_visited,time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_coutry("Russia", 2,["moscow", "sain perterburg"])
print(travel_log)

# 006  The secret Auction program instructions and flow chart

