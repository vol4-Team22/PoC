.PHONY: up up2 down rm rm-image
up1:
	docker image build -t sample/test:latest .
up2:
	docker container run -d -p 8000:8000 --name test -v ${PWD}/backend:/app sample/test:latest
down:
	docker container stop test

rm:
	docker container rm test

rm-image:
	docker image rm sample/test:latest