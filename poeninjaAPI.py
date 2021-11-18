import requests
import json

OrbUrl = 'https://poe.ninja/api/data/CurrencyOverview?league=Scourge&type=Currency&language=en'
CardUrl = 'https://poe.ninja/api/data/ItemOverview?league=Scourge&type=DivinationCard&language=en'
AccessoriesUrl = 'https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueAccessory&language=en'
session_requests = requests.Session()

def get_orb_price(str):
    OrbName = str

    NinjaPrice = session_requests.get(OrbUrl).text   #get ninjaURL the OrbPriceData
    NinjaPrice = json.loads(NinjaPrice)           #Convert strData to json
    for i in range(79):
        if NinjaPrice["lines"][i]["currencyTypeName"] == OrbName:    #judge the OrbName in the OrbPriceData

            print(NinjaPrice["lines"][i]["currencyTypeName"])
            print(" Buy 1 {} for {} Chaos Orb".format(OrbName,NinjaPrice["lines"][i]["chaosEquivalent"]))
            print("Sell 1 {} for {} Chaos Orb".format(OrbName,NinjaPrice["lines"][i]["receive"]["value"]))
            return " [Buy] 1 [{}] for [{}] Chaos Orb || [Sell] 1 [{}] for [{}] Chaos Orb".format(OrbName,NinjaPrice["lines"][i]["chaosEquivalent"],OrbName,NinjaPrice["lines"][i]["receive"]["value"])

def get_divination_cards_price(str):
    CardName = str

    NinjaPrice = session_requests.get(OrbUrl).text   #get ninjaURL the OrbPriceData 
    NinjaPrice = json.loads(NinjaPrice)
    for i in range(79):
        if NinjaPrice["lines"][i]["currencyTypeName"] == "Exalted Orb":
            OrbPrice = NinjaPrice["lines"][i]["chaosEquivalent"]
    CardPrice = session_requests.get(CardUrl).text
    CardPrice = json.loads(CardPrice)
    for i in range(375):
        if CardPrice["lines"][i]["artFilename"] == CardName:
            print(CardPrice["lines"][i]["artFilename"])
            print("Buy 1 {} for {} Chaos Orb".format(CardName,CardPrice["lines"][i]["chaosValue"]))
            return "Buy 1 {} for {} Chaos Orb || Buy a Exalted Orb = {}".format(CardName,CardPrice["lines"][i]["chaosValue"],OrbPrice)

def get_Unique_Accessories(str):
    AccessoriesName = str

    NinjaPrice = session_requests.get(AccessoriesUrl).text   #get ninjaURL the OrbPriceData 
    NinjaPrice = json.loads(NinjaPrice)

    for i in range(214):
        if NinjaPrice["lines"][i]["name"] == AccessoriesName:

            print(NinjaPrice["lines"][i]["name"])
            print("Buy 1 {} for {} Chaos Orb".format(AccessoriesName,NinjaPrice["lines"][i]["chaosValue"]))
            return "[Buy] a [{}] for [{}] Chaos Orb".format(AccessoriesName,NinjaPrice["lines"][i]["chaosValue"])

  