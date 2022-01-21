import pandas as pd
import  matplotlib.pyplot as plt
import csv

df = pd.read_csv("star_with_gravity.csv")
planet_data_rows=[]

planet_masses = []
planet_distance = []
planet_names = []
planet_gravity=[]

for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_distance.append(planet_data[2])
  planet_names.append(planet_data[1])
  planet_gravity.append(planet_data[5])


gravity_planets = []
for index, Gravity in enumerate(planet_gravity):
  if Gravity>150<350:
    gravity_planets.append(planet_data_rows[index])

print(len(gravity_planets))

dist_planets = []
for index,Distance  in enumerate(dist_planets):
  if Distance<=100:
    dist_planets.append(planet_data_rows[index])

print(len(dist_planets))

df.to_csv("suitable_planets.csv")