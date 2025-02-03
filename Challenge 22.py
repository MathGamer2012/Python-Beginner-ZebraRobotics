tempValue = ['Toronto', 21]
cityTemp = []
cityTemp.append(tempValue)
tempValue = ['Mumbai', 24]
cityTemp.append(tempValue)
tempValue = ['Yellowknife', 16]
cityTemp.append(tempValue)
cityTemp = sorted(cityTemp, key=lambda x: x[1])
print(cityTemp)
