from Countrydetails import countries
from Countrydetails import country

def main():
    """Entry point. Orchestrates flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    data = countries.all_countries()

    # First three elements
    print(f"\n countries (n={len(data.countries())}) = {data.countries()[:3]}")

    # Look up South Africa (ZAF)
    country_name = data.countries()[data.countries().index("South Africa")]

    print(f"\n South Africa (idx={data.countries().index(country_name)}) = {country_name}")

    # Country details
    zaf = country.country_details(country_name)

    print(f"\n ZAF name = {zaf.name()}")

    # print(f"\n south_africa info = {zaf.info()}")









if __name__ == '__main__':
    main()
