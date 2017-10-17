# OpenFlights data converter

## What be this?
This script fetches [OpenFlights Data](https://openflights.org/data.html) and converts the databases (airports-extended.dat, arilines.dat and routes.dat) into JSON files.

## How to use it?
Just run the script. _Don't want to?_ Then go to the releases and get the files.

## What now?
Do what you whant couse a pirte is free.

Use in web project?
```javascript
var data = require('./airports-extended.json');
```
Import to MongoDB?
```bash
mongoimport --db openFlights --collection airports --file airports-extended.dat.json --jsonArray
mongoimport --db openFlights --collection airlines --file airlines.dat.json --jsonArray
mongoimport --db openFlights --collection routes --file routes.dat.json --jsonArray
```






