import subprocess

def performimportdata():
    # print("here")
    command = "osm2pgsql -d osm2pgsqldb -U postgres -W -H localhost -P 5432 -S default.style osmdata_geofabrik/malaysia-singapore-brunei-latest.osm.pbf"
    directory = "C:\\Users\\Gareth Thong\\FYP\\osm2pgsql\\osm2pgsql-bin"
    # result = subprocess.run(command, cwd=directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = subprocess.run(command, cwd=directory, shell=True, text=True)
    return("Data import was successful")
    # print("over here")
    # Check if the command was successful
    # if result.returncode == 0:
    #     # Command was successful, print the output
    #     return("Data import was successful")
    # else:
    #     # Command failed, print the error
    #     return("Data import unsuccessful")