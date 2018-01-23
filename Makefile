default: clean install copy zip

install: dirs
	pip install numpy -t build

dirs:
	mkdir build

copy: dirs
	cp *.py build/

zip: copy
	cd build && zip -r ../lambda.zip .

clean:
	rm -rf build
	rm lambda.zip
