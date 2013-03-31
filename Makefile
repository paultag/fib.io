all: build


build: render


render:
	make -C notes


upload: build
	cd output; \
	rsync -vr --delete \
		. \
		tag@pault.ag:/srv/www/nginx/fib
