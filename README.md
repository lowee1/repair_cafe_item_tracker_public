# repair_cafe_item_tracker

### Commands used
```
hupper -w repair_cafe_item_tracker/ -v -m waitress --port=8083 repair_cafe_item_tracker.wsgi:application

docker build --rm -t repair_cafe_item_tracker_image .

docker container run -dp 8083:8083 --name repair_cafe_item_tracker repair_cafe_item_tracker_image

docker stop repair_cafe_item_tracker

docker start repair_cafe_item_tracker

docker rm repair_cafe_item_tracker
```