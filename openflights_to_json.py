import csv
import requests
import json

#OpenFlights data converter (csv -> json)
#https://openflights.org/data.html

# fetch data from URLs
class Urls(object):
    airlines = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat"
    airports_extended = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports-extended.dat"
    routes = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"

# data fields
class Fields(object):
    get = dict()
    get['airlines.dat'] = ['id', 'name', 'alias', 'IATA', 'ICAO', 'callsign', 'country', 'active']
    get['airports-extended.dat'] = ['id', 'name', 'city', 'country', 'IATA', 'ICAO', 'latitude', 'longitude', 'altitude', 'timezone',' dst', 'tzdata', 'type', 'source']
    get['routes.dat'] = ['airline', 'airline_id', 'source_airport', 'source_airport_id', 'destination_airport', 'destination_airport_id', 'codeshare', 'stops', 'equipment']

# url based parser
def parse_and_save(url):
    filename = url[url.rfind('/')+1:]
    filename_json = filename + ".json"
    fields = Fields.get[filename]
    print("Processing "+filename+":")
    try:        
        print("[+] Fetching "+filename+"...")
        r = requests.get(url, stream=True)
        if(r.status_code == requests.codes.ok):
            print("[+] Reading "+filename+"...")
            csv_reader = csv.DictReader(r.text.splitlines(), fields, delimiter=',')
            print("[+] Parsing "+filename+"...")
            data = list(csv_reader)
            for r in data:
                for f in r:
                    if r[f] == "\\\\N":
                        print(f, r[f])
                        r[f] == ""
            print("[+] Writing "+filename_json+"...")
            with open(filename_json, 'w') as output_json:
                json.dump(data, output_json)                    
            print("[+] Done: {} records.".format(len(data)))
        else:
            raise ConnectionError("[x] Unable to get "+filename+" from: "+url)
    except Exception  as e:
        print('[x] Error '+str(e))        

def get_airlines():
    parse_and_save(Urls.airlines)
 
def get_airports():    
    parse_and_save(Urls.airports_extended)

def get_routes():    
    parse_and_save(Urls.routes)

def main():
    get_airlines()
    get_airports()
    get_routes()

if __name__ == "__main__":
    main()
