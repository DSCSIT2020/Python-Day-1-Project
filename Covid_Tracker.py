# Python-Day-1-Project
# Developer Student Clubs - Siliguri Institute Of Technology
# Prasun Roy - https://github.com/PRASUNR0Y

import matplotlib.patches as mpatches
from covid import *
from matplotlib import pyplot as plt

covid = Covid(source="worldometers")
case = []
confirmed = []
active = []
deaths = []
recovered = []
print("Enter all countries names for whom you want to get COVID-19 data")
print("------------------------------------------------------------------")
print("Seperate country names using comma or space")
countries = input("Enter Countries Name :")

countries_name = countries.strip()
countries_name = countries_name.replace(" ",",")
countries_name = countries_name.split(",")
for x in countries_name:
    case.append(covid.get_status_by_country_name(x))

for y in case:
    confirmed.append(y["confirmed"])
    active.append(y["active"])
    deaths.append(y["deaths"])
    recovered.append(y["recovered"])
confirmed_patch = mpatches.Patch(color='red',label='Confirmed')
recovered_patch = mpatches.Patch(color='green',label='Recovered')
active_patch = mpatches.Patch(color='blue',label='Active')
deaths_patch = mpatches.Patch(color='yellow',label='Deaths')
plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch])

for x in range(len(countries_name)):
    plt.bar(countries_name[x],confirmed[x],color='red')
    if recovered[x] > active[x]:
        plt.bar(countries_name[x],recovered[x],color='green')
        plt.bar(countries_name[x], active[x], color='blue')
    else:
        plt.bar(countries_name[x], active[x], color='blue')
        plt.bar(countries_name[x], recovered[x], color='green')
    plt.bar(countries_name[x], deaths[x], color='yellow')

plt.title('Current COVID-19 Cases')
plt.xlabel('Country Name')
plt.ylabel('Cases(in millions)')
plt.show()