import requests
request=requests.get("http://api.open-notify.org/astros.json")
location=requests.get("http://api.open-notify.org/iss-now")
data=request.json()
place=location.json()
loc=place["iss_position"]
astrodata=data["people"]
ask=input("what you want to know(people and craft,location)")
while ask.lower()!="done":
      if ask.lower()=="people&data":
        for astronaut in astrodata:
            print(f"name:{astronaut['name']},craft:{astronaut['craft']}")
      elif ask.lower()=="location":
                print(f"latitude:{loc['latitude']},longitude:{loc['longitude']}")
      else:
            print("sorry,can't provide further infomation")
      ask=input("what you want to know(people and craft,location)")
print("thanks for using the astofind")                