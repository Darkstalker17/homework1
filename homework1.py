'''
Rohan is bored wearing the jacket and pullover now. He wants to wear something light and soft. But he also doesn't
want to get the cold by not wearing weather-appropriate clothes.
So he will design a program and check what temperature is suitable for wearing light clothes.
'''
print("What is the weather?")
print("Rainy")
print("Sunny")
print("Snowy")
print("Cloudy")
print("Windy")
print("Foggy")
print("Stormy")
print("Hurricane")
Weather = input("Enter the weather: ")
if Weather == "Rainy":
    print("Take an umbrella")
    print("Wear a raincoat")
elif Weather == "Sunny":
    print("Wear a hat")
    print("Wear sunglasses")
    print("Wear a cotton t-shirt")
elif Weather == "Snowy":
    print("Wear a warm coat")
    print("Wear a hat")
    print("Wear a scarf")
elif Weather == "Cloudy":
    print("Wear a raincoat")
    print("Wear a hat")
elif Weather == "Windy":
    print("Wear a Shirt")
    print("Wear a scarf")
elif Weather == "Foggy":
    print("Wear a vest")
    print("Wear a cap")