
## Usage

```
$ git clone 
$ django-admin startproject --template=django-project-template --extension py,md,Dockerfile {{ project_name }}
```

or

```
$ django-admin startproject --template=https://github.com/pkucmus/django-project-template/archive/master.zip --extension py,md,Dockerfile {{ project_name }}
```

### No Docker

```
(your_virtual_env) $ cd /path/to/project
(your_virtual_env) $ pip install -e .
```

### Docker

```
$ cd /path/to/project
$ docker build -t {{ project_name }} -f devel.Dockerfile .
$ docker run -it --name {{ project_name }}_run_1 -p 8000:8000 -v $(pwd)/src/{{ project_name }}:/srv/app/{{ project_name }} {{ project_name }}
```
