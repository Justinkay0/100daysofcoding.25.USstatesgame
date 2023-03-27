with open('weather_data.csv', mode='r') as f:
    data = f.readlines()

data.str.strip()

print(data)