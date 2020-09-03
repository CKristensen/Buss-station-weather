create table if not exists public.test_pyth1 (
	row_id serial,
	lat float,
	lon float
);

create table if not exists public.test_pyth2 (
	row_id serial,
	lat float,
	lon float
);

insert into public.test_pyth1 (lat, lon) values (1, 1);
insert into public.test_pyth1 (lat, lon) values (0, 2);
insert into public.test_pyth1 (lat, lon) values (1, 3);

insert into public.test_pyth2 (lat, lon) values (2, 1);
insert into public.test_pyth2 (lat, lon) values (2, 2);
insert into public.test_pyth2 (lat, lon) values (2, 3);

	with min_distance as (
		select  buss_stop.row_id bid, MIN(POWER(buss_stop.lat-t.lat, 2) + POWER(buss_stop.lon-t.lon, 2)) mdistance
		from public.test_pyth1 buss_stop
		cross join public.test_pyth2 t
		group by buss_stop.row_id
	),
	distances as (
		select  buss_stop.row_id bid, t.row_id sid, POWER(buss_stop.lat-t.lat, 2) + POWER(buss_stop.lon-t.lon, 2) distance
		from public.test_pyth1 buss_stop
		cross join public.test_pyth2 t
	) 
	select * 
	from distances d 
	join min_distance md 
	using(bid)
	where md.mdistance = d.distance;

	
