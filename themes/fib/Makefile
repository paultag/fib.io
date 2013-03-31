
all: clean build
	@echo "built theme fib"

clean:
	@echo "removing static"
	@rm -vrf static

build: mkstatic less

mkstatic:
	mkdir -p static/css

less:
	make -C less
	mv less/fib.css static/css


.PHONY: build clean mkstatic less
