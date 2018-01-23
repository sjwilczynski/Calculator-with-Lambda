default: clean copy zip

build_dist:
	mkdir dist

copy: build_dist
	cp *.py dist/

zip: build_dist
	cd dist && zip -r lambda.zip .

clean:
	rm -rf dist
