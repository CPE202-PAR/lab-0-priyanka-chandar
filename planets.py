# Given earth weight  and planet, returns weight on provided planet
# If string does not match a planet, raise ValueError
def weight_on_planets(pounds: float, planet: str) -> float:
    """calculates weight on a different planet
    Args:
       pounds (float): weight on Earth
       planet (str): planet at which weight should be calculated (either Mars or Jupiter)
    Returns:
       float: the converted weight on the different planet
    """
    # write your code here
    # Sample Run:
    # What do you weigh on earth? 136
    # On Mars you would weigh 51.68 pounds.
    # On Jupiter you would weigh 318.24 pounds.
    if planet == "Mars":
        conversion_rate = 0.38
    elif planet == "Jupiter":
        conversion_rate = 2.34
    elif planet == "Venus":
        conversion_rate = 0.91
    else:
        raise ValueError
    new_weight = pounds * conversion_rate
    return new_weight

def main():    # pragma: no cover
    pounds = float(input("What do you weigh on earth? "))
    #planet = str(input("Would you like to calculate weight on Mars or Jupiter? "))
    #weight_on_planets(pounds, planet)
    print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.\n" +
          "On Venus you would weigh", weight_on_planets(pounds, 'Venus'), "pounds.")

    #except ValueError:
       #print("Error: Check inputted weight and planet.")
       #sys.exit()


if __name__ == '__main__':    # pragma: no cover
    main()
