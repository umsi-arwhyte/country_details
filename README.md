# country_details

Test the Python country details package

## Runtime exceptions

The `country` module is broken.

```python
from Countrydetails import countries
from Countrydetails import country


def main():
    """..."""

    data = countries.all_countries()

    # First three elements
    print(f"\n countries (n={len(data.countries())}) = {data.countries()[:3]}")

    # Look up South Africa (ZAF)
    country_name = data.countries()[data.countries().index("South Africa")]

    print(f"\n South Africa (idx={data.countries().index(country_name)}) = {country_name}")

    # Country details
    zaf = country.country_details(country_name)

    print(f"\n ZAF name = {zaf.name()}")  # Triggers AttributeError

    print(f"\n south_africa info = {zaf.info()}")  # Triggers AttributeError


if __name__ == "__main__":
    main()
```

```shell
(country_details) *[main][~/Development/github/umsi-arwhyte/country_details/src]$ /Users/arwhyte/Development
/github/umsi-arwhyte/country_details/.venv/bin/python /Users/arwhyte/Development/github/umsi-arwhyte/country
_details/src/country.py

 countries (n=247) = ['Afghanistan', 'Aland Islands', 'Albania']

 South Africa (idx=203) = South Africa
/Users/arwhyte/Development/github/umsi-arwhyte/country_details/.venv/lib/python3.13/site-packages/Countrydetails/data/countries
Traceback (most recent call last):
  File "/Users/arwhyte/Development/github/umsi-arwhyte/country_details/src/country.py", line 34, in <module>
    main()
    ~~~~^^
  File "/Users/arwhyte/Development/github/umsi-arwhyte/country_details/src/country.py", line 26, in main
    zaf = country.country_details(country_name)
  File "/Users/arwhyte/Development/github/umsi-arwhyte/country_details/.venv/lib/python3.13/site-packages/Countrydetails/country.py", line 39, in __init__
    if country_info.get('name', None):
       ^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'
```
