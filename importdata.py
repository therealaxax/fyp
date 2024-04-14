import subprocess

def performimportdata():
    command = "osm2pgsql -d osm2pgsqldb -U postgres -W -H localhost -P 5432 -S default.style osmdata_geofabrik/malaysia-singapore-brunei-latest.osm.pbf"
    directory = "C:\\Users\\Gareth Thong\\FYP\\osm2pgsql\\osm2pgsql-bin"
    result = subprocess.run(command, cwd=directory, shell=True, text=True)
    return("Data import was successful")