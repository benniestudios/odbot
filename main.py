import os
from os import path
import discord
import requests
from requests.structures import CaseInsensitiveDict
import json
from keep_alive import keep_alive
from discord.ext import commands

intents = discord.Intents.default()
bot = discord.Bot()

url = "https://www.nationsatrisk.com/api/alliance/members?page=1"

headers = CaseInsensitiveDict()
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

resp = requests.post(url, headers=headers)
x1 = resp.text
y1 = json.loads(x1)
nations = "**name:** " + y1['data'][0]['name'] + " | **nation:** " + y1["data"][
    0]["country_name"] + " | **Last Login:**" + str(y1['data'][0]['login_date'])

for i in range(1, 10):
    nations += "\n**name:** " + y1['data'][i]['name'] + " | **nation:** " + y1[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y1["data"][i]["login_date"])

url = "https://www.nationsatrisk.com/api/alliance/members?page=2"

headers = CaseInsensitiveDict()
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

resp = requests.post(url, headers=headers)
x2 = resp.text
y2 = json.loads(x2)

for i in range(1, 10):
    nations += "\n**name:** " + y2['data'][i]['name'] + " | **nation:** " + y2[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y2["data"][i]["login_date"])

url = "https://www.nationsatrisk.com/api/alliance/members?page=3"

headers = CaseInsensitiveDict()
headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

resp = requests.post(url, headers=headers)
x3 = resp.text
y3 = json.loads(x3)

for i in range(1, 10):
    nations += "\n**name:** " + y3['data'][i]['name'] + " | **nation:** " + y3[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y3["data"][i]["login_date"])



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def listnations(ctx):
    embed = discord.Embed(title="Nations",
                          url="https://nationsatrisk.com/",
                          description=nations,
                          color=0x00008B)
    await ctx.respond(embed=embed)


@bot.slash_command()
async def link(ctx, username):
    author = ctx.author.id
    user = username

    filename = './users.json'
    listObj = []

    #check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)

    # Verify existing list
    print(listObj)
    print(type(listObj))

    listObj.append({
        "username": user,
        "id": author,
    })

    # Verify updated list
    print(listObj)

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',', ': '))

    embed = discord.Embed(title=user + " " + str(author),
                          url="https://nationsatrisk.com/",
                          description="Successfully linked account",
                          color=0x00008B)
    await ctx.respond(embed=embed)


def convert_mention_to_id(mention):
    return int(mention[1:][:len(mention)-2].replace("@","").replace("!",""))

@bot.slash_command()
async def nation(ctx, mention):

  url = "https://www.nationsatrisk.com/api/alliance/members?page=1"

  headers = CaseInsensitiveDict()
  headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
  headers["Content-Type"] = "application/json"
  headers["Content-Length"] = "0"

  resp = requests.post(url, headers=headers)
  x1 = resp.text
  y1 = json.loads(x1)
  nations = "**name:** " + y1['data'][0]['name'] + " | **nation:** " + y1["data"][
    0]["country_name"] + " | **Last Login:**" + str(y1['data'][0]['login_date'])

  for i in range(1, 10):
    nations += "\n**name:** " + y1['data'][i]['name'] + " | **nation:** " + y1[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y1["data"][i]["login_date"])

  url = "https://www.nationsatrisk.com/api/alliance/members?page=2"

  headers = CaseInsensitiveDict()
  headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
  headers["Content-Type"] = "application/json"
  headers["Content-Length"] = "0"

  resp = requests.post(url, headers=headers)
  x2 = resp.text
  y2 = json.loads(x2)

  for i in range(1, 10):
    nations += "\n**name:** " + y2['data'][i]['name'] + " | **nation:** " + y2[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y2["data"][i]["login_date"])

  url = "https://www.nationsatrisk.com/api/alliance/members?page=3"

  headers = CaseInsensitiveDict()
  headers[
    "Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uYXRpb25zYXRyaXNrLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTY2NTU2OTM4NiwiZXhwIjoxNjY1NjU1Nzg2LCJuYmYiOjE2NjU1NjkzODYsImp0aSI6IkI1UTB3VWZBU0hJdUJkMEEiLCJzdWIiOjI0MDQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.y4EEYC4z0OWwd8GHEvocaxaXeZuqoiaO_0eaXxDGOb0"
  headers["Content-Type"] = "application/json"
  headers["Content-Length"] = "0"

  resp = requests.post(url, headers=headers)
  x3 = resp.text
  y3 = json.loads(x3)

  for i in range(1, 10):
    nations += "\n**name:** " + y3['data'][i]['name'] + " | **nation:** " + y3[
        "data"][i]["country_name"] + " | **Last Login:** " + str(
            y3["data"][i]["login_date"])

  if not mention:
    await ctx.send(ctx.author.id)
  else:
    try:
      user = convert_mention_to_id(mention) 
    except ValueError:
      await ctx.send("Invalid ID")

  f = open('./users.json')
  data = json.load(f)

  name = y1["data"][0]["name"]
  nation = y1["data"][0]["country_name"]
  rank = str(y1["data"][0]["rank"])
  alliance_rank = y1["data"][0]["alliance_rank"]
  ll = str(y1["data"][0]["login_date"])
  flag = str(y1["data"][0]["flag"])
  score = str("{:,}".format(y1["data"][0]["points"]))

  for item in data:
    if item['id'] == user:
      print(item['username'] + str(item['id']))
      nationuser = item['username']
      for i in range(0, 100):
        name = y1["data"][i]["name"]
        if name == nationuser:
          name = y1["data"][i]["name"]
          nation = y1["data"][i]["country_name"]
          rank = str(y1["data"][i]["rank"])
          alliance_rank = y1["data"][i]["alliance_rank"]
          ll = str(y1["data"][i]["login_date"])
          flag = str(y1["data"][i]["flag"])
          score = str("{:,}".format(y1["data"][i]["points"]))
          break
        if i > 50:
          for i in range(0, 100):
            name = y2["data"][i]["name"]
            if name == nationuser:
              name = y2["data"][i]["name"]
              nation = y2["data"][i]["country_name"]
              rank = str(y2["data"][i]["rank"])
              alliance_rank = y2["data"][i]["alliance_rank"]
              ll = str(y2["data"][i]["login_date"])
              flag = str(y2["data"][i]["flag"])
              score = str("{:,}".format(y1["data"][i]["points"]))
              break
            if i > 50:
              for i in range(0, 100):
                name = y3["data"][i]["name"]
                if name == nationuser:
                  name = y3["data"][i]["name"]
                  nation = y3["data"][i]["country_name"]
                  rank = str(y3["data"][i]["rank"])
                  alliance_rank = y3["data"][i]["alliance_rank"]
                  ll = str(y3["data"][i]["login_date"])
                  flag = str(y3["data"][i]["flag"])
                  score = str("{:,}".format(y1["data"][i]["points"]))
                  break
                  

    embed = discord.Embed(title="Nation", url="https://www.nationsatrisk.com/nation/overview?user="+name, description="**Username:** " + name + "\n**Nation:** " + nation + "\n**Rank:** #" + rank + "\n**Alliance Rank:** " + alliance_rank + "\n**Score** " + score + "\n**Last Login:** " + ll, color=0x00008B)

    embed.set_thumbnail(url=flag)
    await ctx.respond(embed=embed)


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_TOKEN")
bot.run(token)  # Starts the bot
