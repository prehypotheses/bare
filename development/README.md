<br>

## Development Environment

The outlined remote environment is used build and test [https://huggingface.co](https://huggingface.co) Space `gradio` applications.

### Remote Development

The remote development environment requires

* [Dockerfile](../.devcontainer/Dockerfile)
* [requirements.txt](../.devcontainer/requirements.txt)

The image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile -t interact
```

On success, the output of

```shell
docker images
```

should include

<br>

| repository | tag    | image id | created  | size     |
|:-----------|:-------|:---------|:---------|:---------|
| interact   | latest | $\ldots$ | $\ldots$ | $\ldots$ |


<br>

Subsequently, a container, i.e., an instance, of the image `interact` is launched via variations of:

<br>

```shell
docker run --rm --gpus all --shm-size=16gb -i -t 
  -p 7860:7860 -p 8000:8000 -w /app 
    --mount type=bind,src="$(pwd)",target=/app 
      -v ~/.aws:/root/.aws interact
```

<br>

Herein, `-p 7860:7860` maps the host port `7860` to container port `7860`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  Additionally

* --rm: [automatically remove container](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* -i: [interact](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* -t: [tag](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* -p: [publish the container's port/s to the host](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s)
* --mount type=bind: [a bind mount](https://docs.docker.com/engine/storage/bind-mounts/#syntax)
* -v: [volume](https://docs.docker.com/engine/storage/volumes/)

<br>

Get the name of the running instance of ``interact`` via:

```shell
docker ps --all
```

<br>
<br>

## Devices

An auto method for device selection is

```shell
import logging
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
logging.info('Device: %s', device)
```

<br>
<br>


## Code Analysis

The GitHub Actions script [main.yml](../.github/workflows/main.yml) conducts code analysis within a Cloud GitHub Workspace.  Depending on the script, code analysis may occur `on push` to any repository branch, or `on push` to a specific branch.  The sections herein outline remote code analysis.

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Analyse a directory via the command

```shell
python -m pylint --rcfile .pylintrc {directory}
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135


<br>

### pytest & pytest coverage

The directive patterns

```shell
python -m pytest tests/{directory.name}/...py
pytest --cov-report term-missing  --cov src/{directory.name}/...py tests/{directory.name}/...py
```

for test and test coverage, respectively.

<br>

### flake8

For code & complexity analysis.  A directive of the form

```bash
python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics src/...
```

inspects issues in relation to logic (F7), syntax (Python E9, Flake F7), mathematical formulae symbols (F63), undefined variable names (F82).  Additionally

```shell
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics src/...
```

inspects complexity.


<br>
<br>


## References

Images:
* [docker hub](https://hub.docker.com)
* [NVIDIA <abbr title="Graphics Processing Unit">GPU</abbr> Cloud (NGC) Catalogue](https://catalog.ngc.nvidia.com)

Interfaces:
* [GRADIO & Docker](https://www.gradio.app/main/guides/deploying-gradio-with-docker)
* [GRADIO Documentation](https://www.gradio.app/docs/gradio/interface)
  * [Named Entity Recognition](https://www.gradio.app/guides/named-entity-recognition)
* [Generators](https://jamstack.org/generators/)
  * [11ty](https://www.11ty.dev)
* [Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker#docker-spaces)
* [Demonstration](https://huggingface.co/docs/hub/spaces-sdks-docker-first-demo)
* [Deploying a Gradio app with Docker](https://www.gradio.app/guides/deploying-gradio-with-docker)

Amazon:
* [Prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)

Engineering
* [Switching User in Docker Image or Container](https://www.baeldung.com/linux/docker-image-container-switch-user)


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
