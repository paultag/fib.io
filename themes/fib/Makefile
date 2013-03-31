#
#


all: clean build
	@echo "built theme fib"


clean:
	@echo "removing static"
	@rm -vrf static


build: less resources


resources:
	mkdir -p static/imgs
	cp resources/imgs/* static/imgs


less:
	make -C less
	mkdir -p static/css
	mv less/fib.css static/css


.PHONY: build clean resources less
