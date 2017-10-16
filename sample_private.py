#Google Maps API Key
API_KEY='<API_KEY>'

logFileName = 'duration.tsv'

homeAddress = '789 Abcd St, San Jose, CA 12345'
officeAddress = '123 Xyz Avenue, Mountain View, CA 98765'

#Pick way points that would make sense when reversed, e.g., at the median of the
#road, instead of a specific side of the road
homeToOfficeWaypoints = {
        'routeA': [
            '37.378326,-121.949739', 
            '37.392721,-122.001146'
            ],
        'routeB': [
            '37.328521,-122.010308',
            '37.337848,-122.084284'
            ],
        # Google Maps' best route
        'google': [
            ]
        }
