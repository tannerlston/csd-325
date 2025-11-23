# Tanner Elston, 11/19/25, Assignment Test Cases 7.2

# Outline necessary parameters, capitalize places, define base output
def city_country(city, country, population=None, language=None):
    formatted_city = city.title()
    formatted_country = country.title()
    base = f"{formatted_city}, {formatted_country}"

# Includes value in output if argument is present
# Utilizing string concatenation
    if population is not None:
        base += f" - population {population}"

    if language is not None:
        if population is None:
            base += f" - population unknown, {language.title()}"
        else:
            base += f", {language.title()}"

    return base




if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("buenos aires", "argentina", 3000000)) 
    print(city_country("lima", "peru", 2000000, "spanish"))    
