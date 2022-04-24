import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
  print("Bot is currently online!")


@client.command()
async def AirbusInfo(ctx):
  await ctx.send("Airbus is a European multinational aerospace corporation.")
  await ctx.send("To know more about the company, follow this link: https://en.wikipedia.org/wiki/Airbus")


@client.command()
async def A300(ctx):
  embed=discord.Embed(title="Airbus A300",color=discord.Colour.green())
  embed.add_field(name="Basic Info: ",value="The Airbus A300 was the company's first aircraft ever built. It is a twin engined, medium range aircraft.",inline=False)
  embed.add_field(name="Produced: ",value="1971-2007",inline=False)
  embed.add_field(name="Engines: ",value="Pratt & Whitney PW4000 (A300-600)",inline=False)
  embed.add_field(name="First Operator: ",value="Air France",inline=True)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/61/Airbus_A300B2-1C%2C_Air_France_AN1091113.jpg")
  await ctx.send(embed=embed)


@client.command()
async def A310(ctx):
  embed=discord.Embed(title="Airbus A310",color=discord.Colour.orange())
  embed.add_field(name="Basic Info: ",value="The Airbus A310 is a twin engined long range aircraft developed by Airbus Industrie.",inline=False)
  embed.add_field(name="Produced: ",value="1981-1998",inline=False)
  embed.add_field(name="Engines: ",value="Pratt & Whitney JT9D",inline=False)
  embed.add_field(name="First Operator: ",value="Swissair",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Swissair_Airbus_A310-322%3B_HB-IPK%40ZRH%3B11.08.1994_%284847642397%29.jpg")
  await ctx.send(embed=embed)



@client.command()
async def A320(ctx):
  embed=discord.Embed(title="Airbus A320",color=discord.Colour.red())
  embed.add_field(name="Basic Info: ",value="The Airbus A320 family is family a twin engined short to medium haul aircraft developed by Airbus Industrie.",inline=False)
  embed.add_field(name="Produced: ",value="1986-Present",inline=False)
  embed.add_field(name="Engines: ",value="CFM56",inline=False)
  embed.add_field(name="First Operator: ",value="Air France")
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Jetstar_Airbus_A320_in_flight_%286768081241%29_crop.jpg/300px-Jetstar_Airbus_A320_in_flight_%286768081241%29_crop.jpg")
  await ctx.send(embed=embed)


@client.command()
async def A330(ctx):
  embed=discord.Embed(title="Airbus A330",color=discord.Colour.blue())
  embed.add_field(name="Basic Info: ",value="The Airbus A330 is a twin engined long haul aircraft developed by Airbus Industrie.",inline="False")
  embed.add_field(name="Produced: ",value="1992-Present",inline=False)
  embed.add_field(name="Engines: ",value="Rolls Royce Trent 7000",inline=False)
  embed.add_field(name="First Operator: ",value="Air Inter",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Turkish_Airlines%2C_Airbus_A330-300_TC-JNL_NRT_%2823708073592%29.jpg/300px-Turkish_Airlines%2C_Airbus_A330-300_TC-JNL_NRT_%2823708073592%29.jpg")
  await ctx.send(embed=embed)

  

@client.command()
async def A340(ctx):
  embed=discord.Embed(title="Airbus A340",color=discord.Colour.yellow())
  embed.add_field(name="Basic Info: ",value="The Airbus A340 is a four engined long haul aircraft developed by Airbus Industrie.",inline=False)
  embed.add_field(name="Produced: ",value="1991-2012",inline=False)
  embed.add_field(name="Engines: ",value="Rolls Royce Trent 500",inline=False)
  embed.add_field(name="First Operator: ",value="Lufthansa",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Airbus_A340-311%2C_Lufthansa_AN1936774.jpg/300px-Airbus_A340-311%2C_Lufthansa_AN1936774.jpg")
  await ctx.send(embed=embed)

  

@client.command()
async def A350(ctx):
  embed=discord.Embed(title="Airbus A350",color=discord.Colour.purple())
  embed.add_field(name="Basic Info: ",value="The Airbus A350 is an ultra long haul twin engined aircraft developed by Airbus Industrie.",inline=False)
  embed.add_field(name="Produced: ",value="2010-Present",inline=False)
  embed.add_field(name="Engines: ",value="Rolls Royce Trent XWB",inline=False)
  embed.add_field(name="First Operator: ",value="Qatar Airways",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Qatar_Airways_A350-941_%28A7-ALA%29_landing_at_Frankfurt_Airport.jpg/300px-Qatar_Airways_A350-941_%28A7-ALA%29_landing_at_Frankfurt_Airport.jpg")
  await ctx.send(embed=embed)
  


@client.command()
async def A380(ctx):
  embed=discord.Embed(title="Airbus A380",color=discord.Colour.red())
  embed.add_field(name="Basic Info: ",value="The Airbus A380 is a long range four engined aircraft developed by Airbus Industrie. It is the largest Passenger Aircraft.",inline=False)
  embed.add_field(name="Produced: ",value="2003-2021",inline=False)
  embed.add_field(name="Engines: ",value="Rolls Royce Trent 900",inline=False)
  embed.add_field(name="First Operator: ",value="Singapore Airlines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg/300px-A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg")
  await ctx.send(embed=embed)
  


@client.command()
async def A220(ctx):
  embed=discord.Embed(title="Airbus A220",color=discord.Colour.red())
  embed.add_field(name="Basic Info: ",value="The Airbus A220 is a short to medium haul twin engined airliner developed by Airbus Industrie, along with the Canadian firm Bombardier Aviation.",inline=False)
  embed.add_field(name="Produced: ",value="2012-Present",inline=False)
  embed.add_field(name="Engines: ",value="Pratt & Whitney PW1500G",inline=False)
  embed.add_field(name="First Operator: ",value="Swiss International Air Lines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/YL-CSD_Bombardier_BD-500-1A100_CS300_BCS3_Airbus_A220-300_A223_c_n_55006_-_BTI_%2831100301167%29.jpg/300px-YL-CSD_Bombardier_BD-500-1A100_CS300_BCS3_Airbus_A220-300_A223_c_n_55006_-_BTI_%2831100301167%29.jpg")
  await ctx.send(embed=embed)
  


@client.command()
async def A330neo(ctx):
  embed=discord.Embed(title="Airbus A330neo",color=discord.Colour.orange())
  embed.add_field(name="Basic Info: ",value="The Airbus A330neo is a long haul twin engined aircraft developed by Airbus Industrie, as a modern replacement to the original Airbus A330ceo.",inline=False)
  embed.add_field(name="Produced: ",value="2015-Present",inline=False)
  embed.add_field(name="Engines: ",value="Rolls Royce Trent 7000",inline=False)
  embed.add_field(name="First Operator: ",value="TAP Air Portugal",inline=False)
  embed.set_thumbnail(url="https://samchui.com/wp-content/uploads/2019/02/IMG_0666-800x500.jpg")
  await ctx.send(embed=embed)



@client.command()
async def A320neo(ctx):
  embed=discord.Embed(title="Airbus A320neo",color=discord.Colour.red())
  embed.add_field(name="Basic Info: ",value="The Airbus A320neo family is a family of aircraft developed by Airbus Industrie, as a modern replacement to the A320ceo family.",inline=False)
  embed.add_field(name="Produced: ",value="2012-Present",inline=False)
  embed.add_field(name="Engines: ",value="Pratt & Whitney PW1000G",inline=False)
  embed.add_field(name="First Operator: ",value="Lufthansa",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg/300px-IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg")
  await ctx.send(embed=embed)
  


@client.command()
async def A400M(ctx):
  embed=discord.Embed(title="Airbus A400M",color=discord.Colour.orange())
  embed.add_field(name="Basic Info: ",value="The Airbus A400M is a European Four Engined Turboprop Military Aircraft by Airbus Industrie.",inline=False)
  embed.add_field(name="Produced: ",value="2007-Present",inline=False)
  embed.add_field(name="Engines:",value="Ratier-Figeac FH385 & FH386",inline=False)
  embed.add_field(name="First Operator: ",value="French Air Force")
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Airbus_A400M_Atlas_of_the_Spanish_Air_Force_%28code_EC-400%29_arrives_RIAT_Fairford_18July2019_arp.jpg/220px-Airbus_A400M_Atlas_of_the_Spanish_Air_Force_%28code_EC-400%29_arrives_RIAT_Fairford_18July2019_arp.jpg")
  await ctx.send(embed=embed)
  
keep_alive()
  
client.run("TOKEN")
