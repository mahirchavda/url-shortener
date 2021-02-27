build:
	docker build -t mahirchavda/url-shortener .

build_nocache:
	docker build -t mahirchavda/url-shortener . --no-cache=true

dclean:
	docker stop `docker ps -q`; docker system prune -f; docker volume prune -f;

ddclean:
	docker stop `docker ps -q`; docker system prune -af; docker volume prune -f;

pyclean:
	find -iname ".pytest_cache" -exec rm -rf {} \;
	find -iname "__pycache__" -exec rm -rf {} \;
	find -iname "*.pyc" -exec rm -rf {} \;