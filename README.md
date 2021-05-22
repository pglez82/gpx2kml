# GPX2KML

Converts a to a kml in the simplest and smallest version possible without losing any points. It doesn't store the altitude, only latitude and longitude per point (see example in test_files). I made this program to use it with the Bangle.js smartwatch which does not have a lot of memory and it is unable to handle GPX files.

## Usage
Install the dependencies with `pip install -r requirements`. Run the program:

```python
python gpx2kml.py -f test_files/pena-careses-siero.gpx
```