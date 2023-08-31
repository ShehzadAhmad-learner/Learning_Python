dictionary = {
    "shehzad":"An industrial engineering student trying to learn machine learning",
    "majeed":"A minning engineering student who is Hafiz e Quran",
    "Ehtisham":"A chemical engineering student passionate about football",
    "Farhan": "mechatronics engineering student who loves playing pubg ",
    "Kamran":"also a chemical engineering student who loves playing pubg",


}
print(dictionary["shehzad"])
dictionary["fawad"]= "BS Software student in Awkum and leaning Quran too"
print(dictionary)
for key in dictionary:
    print(key)
    print(dictionary[key])
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}
travel_log = {
    "France":{
        "Paris":5,
        "Lille":3,
        "Dijon":6,

    },
    "Germany":["Berlin", "hamburg","Stuttgart"]
}
print(travel_log["France"])