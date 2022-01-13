import pandas
import turtle

screen = turtle.Screen()
screen.title("Latvia Major City Game")
image = "image/latvia_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data/Latvian_Major_Cities.csv")
all_cities = data.city.to_list()
guessed_cities = []

while len(guessed_cities) < 28:
    answer_cities = screen.textinput(title=f"{len(guessed_cities)}/27 Cities correct",
                                     prompt="What's another city's name?").title()
    if answer_cities == "Exit":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("data/cities to learn.csv")
        break

    if answer_cities in all_cities:
        guessed_cities.append(answer_cities)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer_cities]
        t.goto(int(city_data.x), int(city_data.y))
        t.write(answer_cities)

screen.exitonclick()
