-- CREATE EXTENSION postgis;

-- SELECT * FROM geometry_columns;

-- CREATE TABLE geometries (name varchar, geom geometry);

-- INSERT INTO geometries VALUES
--   ('Point', 'POINT(0 0)'),
--   ('Linestring', 'LINESTRING(0 0, 1 1, 2 1, 2 2)'),
--   ('Polygon', 'POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))'),
--   ('PolygonWithHole', 'POLYGON((0 0, 10 0, 10 10, 0 10, 0 0),(1 1, 1 2, 2 2, 2 1, 1 1))'),
--   ('Collection', 'GEOMETRYCOLLECTION(POINT(2 0),POLYGON((0 0, 1 0, 1 1, 0 1, 0 0)))');

-- SELECT name, ST_AsText(geom) FROM geometries;

-- SELECT * FROM geometries;

-- SELECT name, ST_GeometryType(geom), ST_NDims(geom), ST_SRID(geom)
--   FROM geometries;

-- SELECT ST_AsText(geom)
--   FROM geometries
--   WHERE name = 'Point';
  
--   SELECT ST_X(geom), ST_Y(geom)
--   FROM geometries
--   WHERE name = 'Point';

-- SELECT * FROM spatial_ref_sys;

--------------------------------------------------

select * FROM locations;

-- DELETE FROM locations;

-- ALTER TABLE locations
-- DROP COLUMN name;

-- ALTER TABLE locations
-- ADD COLUMN coffee_shop VARCHAR(255);