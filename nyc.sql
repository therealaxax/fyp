-- SELECT * FROM nyc_subway_stations;

-- SELECT nghbhd FROM nyc_subway_stations WHERE name = 'Broad St';

-- SELECT * FROM nyc_homicides;

-- SELECT * FROM nyc_streets;
-- SELECT AVG(ST_Length(geom))
-- FROM nyc_streets
-- WHERE type = 'residential'

-- SELECT * FROM geometry_columns;

-- SELECT * FROM spatial_ref_sys;

-- SELECT * FROM geometries;

-- SELECT name, ST_AsText(geom)
--   FROM nyc_subway_stations
--   LIMIT 1;

-- SELECT name, ST_AsGeoJSON(geom)
-- FROM nyc_subway_stations

-- SELECT ST_AsText(geom)
--   FROM geometries
--   WHERE name = 'Linestring';
  
--   SELECT ST_Length(geom)
--   FROM geometries
--   WHERE name = 'Linestring';

-- SELECT name, ST_AsGeoJSON(geom)
--   FROM geometries
--   WHERE name = 'Collection';

-- SELECT nyc_neighborhoods.name, ST_AsText(nyc_neighborhoods.geom)
-- FROM nyc_neighborhoods
-- INNER JOIN nyc_subway_stations
-- ON ST_Contains(nyc_neighborhoods.geom, nyc_subway_stations.geom)
-- WHERE nyc_subway_stations.name = 'Broad St';

-- SELECT nyc_subway_stations.name, ST_AsText(nyc_subway_stations.geom)
-- FROM nyc_neighborhoods
-- INNER JOIN nyc_subway_stations
-- ON ST_Contains(nyc_neighborhoods.geom, nyc_subway_stations.geom)
-- WHERE nyc_subway_stations.name = 'Broad St';

SELECT nyc_neighborhoods.name
FROM nyc_neighborhoods
INNER JOIN nyc_subway_stations
ON nyc_neighborhoods.boroname = nyc_subway_stations.borough
WHERE nyc_subway_stations.name = 'Broad St';
-- LIMIT 5;