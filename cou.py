# Install the countryinfo library
# You can do this by adding the following line to your code or installing it separately in the terminal 
# pip install countryinfo

from countryinfo import CountryInfo

def get_country_info():
    # Get user input for the country name
    country_name = input("Enter the name of the country: ")

    try:
        # Fetch country information
        country_info = CountryInfo(country_name)

        # Display information
        print("「Country Info」❄")
        print("- - - - - - - - - - - - - - - - - - - ")
        print("\nCountry Information:")
        print(f"Name: {country_info.name()}")
        print(f"Capital: {country_info.capital()}")
        print(f"Population: {country_info.population()}")
        print(f"Region: {country_info.region()}")
        print(f"Subregion: {country_info.subregion()}")
        print(f"Currencies: {', '.join(country_info.currencies())}")
        print(f"Languages: {', '.join(country_info.languages())}")

    except Exception as e:
        print(f"Error: {e}")

# Coded By @a_d_w_a
# Run the function
get_country_info()
