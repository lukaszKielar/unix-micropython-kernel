# Jupyter kernel for MicroPython's UNIX port

## How to start

### Clone git repository

```
git clone https://github.com/lukaszKielar/unix-micropython-kernel
cd unix-micropython-kernel
```

### Create dedicated environment

```
conda create --name <env> --file requirements.txt
conda activate <env>
```

### Install package in develop mode

```
python setup.py develop
```

## Register kernel

```
jupyter kernelspec install --user unix_micropython_kernel
```

## Remove kernel

```
jupyter kernelspec remove unix_micropython_kernel
```
