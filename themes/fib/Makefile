#
#


all: clean build
	@echo "built theme fib"


clean:
	@echo "removing static"
	@rm -vrf static


build: less resources


resources: less
	mkdir -p static/imgs static/font
	cp resources/imgs/* static/imgs
	cp resources/font/* static/font
	cp resources/css/* static/css


less:
	make -C less
	mkdir -p static/css
	mv less/fib.css static/css


.PHONY: build clean resources less
