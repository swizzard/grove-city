build: get_mdbook
	mdbook build

get_mdbook: 
	which mdbook || cargo install mdbook \
		--no-default-features \
		--features search \
		--vers "^0.5" \
		--locked

clean: 
	rm -rf book
