-- SELECT
--     z.zoneid,
--     w.wastetype,
--     SUM(wastecollected) AS totalwastes
-- FROM
--     myfacttrips f
-- INNER JOIN
--     mydimzone z ON f.zoneid = z.zoneid
-- INNER JOIN
--     mydimwaste w ON f.wasteid = w.wasteid
-- GROUP BY GROUPING SETS (
--     (z.zoneid, w.wastetype),
--     z.zoneid,
--     w.wastetype,
--     ()
-- )
-- ORDER BY
--    z.zoneid,
--    w.wastetype;



-- SELECT
--     d.Year,
--     z.zonename,
--     z.zoneid,
--     SUM(wastecollected) AS totalwastes
-- FROM
--     myfacttrips f
-- INNER JOIN
--     mydimdate d ON f.dateid = d.dateid
-- INNER JOIN
--     mydimzone z ON f.zoneid = z.zoneid
-- GROUP BY ROLLUP (d.Year, z.zonename, z.zoneid)
-- ORDER BY
--     d.Year DESC,
--     z.zonename,
--     z.zoneid;



-- SELECT
--     d.Year,
--     z.zonename,
--     z.zoneid,
--     Avg(wastecollected) AS averagewastes
-- FROM
--     myfacttrips f
-- INNER JOIN
--     mydimdate d ON f.dateid = d.dateid
-- INNER JOIN
--     mydimzone z ON f.zoneid = z.zoneid
-- GROUP BY CUBE (d.Year, z.zonename, z.zoneid)
-- ORDER BY
--     d.Year DESC,
--     z.zonename,
--     z.zoneid;

CREATE MATERIALIZED VIEW max_waste_stats AS
SELECT
    z.zonename,
    z.zoneid,
    w.wastetype,
    MAX(wastecollected) AS MaxWastes
FROM
    myfacttrips f
INNER JOIN
    mydimzone z ON f.zoneid = z.zoneid
INNER JOIN
    mydimwaste w ON f.wasteid = w.wasteid
GROUP BY
    z.zonename,
    z.zoneid,
    w.wastetype
WITH DATA;


SELECT
    z.zonename,
    z.zoneid,
    w.wastetype,
    MAX(f.wastecollected) AS MaxWastes
FROM
    myfacttrips f
INNER JOIN
    mydimzone z ON f.zoneid = z.zoneid
INNER JOIN
    mydimwaste w ON f.wasteid = w.wasteid
GROUP BY
    z.zonename,
    z.zoneid,
    w.wastetype;

REFRESH MATERIALIZED VIEW max_waste_stats;