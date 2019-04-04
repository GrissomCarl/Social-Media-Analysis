#   Author: Carl Grissom
#   Date: 03/29/2019
#   File name: locations.py
#   Description: location variables for twitter geo searches. 
#       Coordinates for a city were determined by a google search    
#           "city name coordinates" i.e. Saint Louis coordinates.
#     
#       Radius is set to 100 miles from the coordinate point.
#   NOTE: When updating locations need to update LOCATIONS to reflected change      
#
#   All rights reserved.

# locations
# city = [longitude, latitude, "radius"]

CHICAGO = ("41.8781", "-87.6298", "100mi")
KANSAS = ("39.0997", "-94.5786", "100mi")
NEWYORK = ("40.7128", "-74.0060", "100mi")
REDMOND = ("47.6740", "-122.121513", "100mi")
LOSANGELES = ("34.0522", "-118.2437", "100mi")
SANFRANSICO = ("37.7749", "-122.4194", "100mi")
SAINTLOUIS = ("38.6270", "-90.1994", "100mi")


LOCATIONS = ("CHICAGO", 
             "KANSAS", 
             "NEWYORK", 
             "REDMOND", 
             "LOSANGELES", 
             "SANFRANSICO", 
             "SAINTLOUIS"
            )