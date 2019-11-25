## Build an image

```
docker build -t micropython-notebook .
```
or
```
docker build --no-cache -t micropython-notebook .
```

## Run container in detached mode

```
docker run --rm -t -d --name micropython-notebook micropython-notebook
```

## Open micropython REPL

```
docker run --rm -it --name micropython-notebook micropython-notebook
```

## How to execute the code

```
docker exec -it micropython-notebook micropython -c "import upip; upip.install('urequests')"
```

## Stop running container

```
docker stop micropython-notebook
```

## Run jupyter lab in the container

```
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes --name micropython-notebook micropython-notebook
```
