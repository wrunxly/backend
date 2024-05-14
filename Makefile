runimg:
		@docker run --rm --name backend -it -p 8080:8080 -v $$(pwd):/app/ --env-file dot-env-template backend
buildimg:
		@docker build -t backend .
