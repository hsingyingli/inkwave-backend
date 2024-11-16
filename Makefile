postgres:
	docker run --name inkwave -p 5432:5432 -e POSTGRES_USER=test -e POSTGRES_PASSWORD=testsecret -e POSTGRES_DB=inkwave -d postgres:14-alpine


new_migration:
	@read -p "migration name: " name;\
		dbmate  new $$name


migrateup:
	dbmate --url postgres://test:testsecret@localhost:5432/inkwave?sslmode=disable up
