-- select name, ST_X(ST_Centroid(way)), way_area from planet_osm_polygon where name = 'National Cancer Centre Singapore' or name = 'Tekka Centre';
-- SELECT
--     (SELECT ST_X(ST_Centroid(way))
--      FROM planet_osm_polygon
--      WHERE name = 'National Cancer Centre Singapore'
--      ORDER BY way_area DESC
--      LIMIT 1)
--     <
--     (SELECT ST_X(ST_Centroid(way))
--      FROM planet_osm_polygon
--      WHERE name = 'Tekka Centre'
--      ORDER BY way_area DESC
--      LIMIT 1) AS isWest;
-- select building, name, way from planet_osm_polygon where building != 'null' and name like '%Tiong Bahru%';
-- select building, name, way from planet_osm_point where building != 'null' and name like '%Tiong Bahru%';
-- select building, name, way from planet_osm_roads where building != 'null' and name like '%Tiong Bahru%';
-- select building, name, way from planet_osm_line where building != 'null' and name like '%Tiong Bahru%';
-- select ST_AsText(way) from planet_osm_polygon;
-- select ST_AsText(way) from planet_osm_point;
-- select * from planet_osm_point;
-- select name from planet_osm_polygon where name != 'null';
-- SELECT name, ST_AsText(way) as coordinates
-- FROM planet_osm_polygon AS outer_poly
-- WHERE ST_Contains(outer_poly.way, (
--     SELECT way
--     FROM planet_osm_point
--     WHERE name = 'ERP'
--     ORDER BY way_area DESC
--     LIMIT 1
-- ));
-- SELECT name, ST_AsText(way) as coordinates FROM planet_osm_polygon WHERE name = 'Tekka Centre' ORDER BY way_area DESC LIMIT 1;
-- select * from planet_osm_polygon where name != 'null' and military != 'null';
-- select * from planet_osm_line where name != 'null';
-- select * from planet_osm_polygon where name = 'National Cancer Centre Singapore';
-- select name,ST_AsText(way) from planet_osm_polygon where name = 'National Cancer Centre Singapore';
-- SELECT name, way
-- FROM planet_osm_polygon AS outer_poly
-- WHERE ST_Contains(outer_poly.way, (
--     SELECT way 
--     FROM planet_osm_polygon 
--     WHERE name = 'National Cancer Centre Singapore' 
--     ORDER BY way_area DESC :
--     LIMIT 1
-- ));
-- select * from planet_osm_point where name != 'null';
-- select ST_AsText(way) from planet_osm_point;
-- select name from planet_osm_polygon 
-- where name != 'null' 
-- and leisure = 'park' 
-- order by ST_Area(way) ?
-- desc limit 1;
-- WITH erp AS (
--   SELECT * 
--   FROM planet_osm_point 
--   WHERE name = 'ERP'
-- ), 
-- foodcenter AS (
--   SELECT * 
--   FROM planet_osm_polygon 
--   WHERE name = 'Maxwell Food Center'
-- )

-- select * from planet_osm_polygon where name != 'null';
-- select * from planet_osm_point where name != 'null';
-- SELECT *
-- FROM planet_osm_polygon AS outer_poly
-- WHERE ST_Contains(outer_poly.way, (
-- 	WITH erp AS (
-- 	  SELECT * 
-- 	  FROM planet_osm_point 
-- 	  WHERE name = 'ERP'
-- 	), 
-- 	foodcenter AS (
-- 	  SELECT * 
-- 	  FROM planet_osm_polygon 
-- 	  WHERE name = 'Maxwell Food Center'
-- 	)
-- 	select erp.way
-- 	FROM erp, foodcenter
-- 	ORDER BY ST_Distance(erp.way, foodcenter.way) ASC
-- 	LIMIT 1
-- ));

	WITH erp AS (
	  SELECT * 
	  FROM planet_osm_point 
	  WHERE name = 'ERP'
	), 
	foodcenter AS (
	  SELECT * 
	  FROM planet_osm_polygon 
	  WHERE name = 'Maxwell Food Center'
	)
	select *
	FROM erp, foodcenter
	ORDER BY ST_Distance(erp.way, foodcenter.way) ASC
	LIMIT 1;

-- SELECT name, ST_AsText(way) as coordinates
-- FROM planet_osm_polygon AS outer_poly
-- WHERE ST_Contains(outer_poly.way, (
--     SELECT way
--     FROM planet_osm_polygon
--     WHERE name = 'Tekka Centre'
--     ORDER BY way_area DESC
--     LIMIT 1
-- ));
-- select * from planet_osm_point where name = 'ERP';
-- select * from planet_osm_polygon where name = 'Maxwell Food Center';
-- SELECT a.*
-- FROM planet_osm_point a
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM planet_osm_polygon b
--     WHERE a.name = b.name
-- ) and a.name != 'null';
-- select * from planet_osm_polygon where name = '7-Eleven';
-- select name from planet_osm_polygon where name != 'null' and leisure = 'park' order by way_area desc limit 1;
-- select name, ST_AsText(way) from planet_osm_line where name = 'Bishan Street 13';
-- SELECT SUM(ST_Length(way)) AS total_distance
-- FROM (
--     select way from planet_osm_line where name = 'Bishan Street 13'
-- ) AS linestrings;
-- select * from spatial_ref_sys;