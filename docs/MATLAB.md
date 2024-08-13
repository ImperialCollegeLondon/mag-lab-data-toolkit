# Deploying MATLAB code

The recommended way to deploy MATLAB code for the MAG data pipeline is to compile the MATLAB into an executable, that can then be run in standard ways in Python (e.g. `subprocess`).

This requires the Python code to run in an environment with the MATLAB Runtime installed - it is freely available [here](https://uk.mathworks.com/products/compiler/matlab-runtime.html).

## Recommended steps to deploy

1) Build a MATLAB image to compile the code in a standard environment (using `matlab-compiler-image-build.sh`). The code can also be compiled into an executable locally on any machine with MATLAB installed, but that executable will only be able to run on a compatible operating system.

2) Build an image with the MATLAB Runtime installed, using [`build-base-matlab-runtime.sh`](/deploy-matlab/build-scripts/build-base-matlab-runtime.sh)

3) Build an executable of your MATLAB code (see [`build-executable.sh`](/deploy-matlab/build-scripts/build-executable.sh))

4) Build a docker image based on the MATLAB Runtime image, that contains your executable and the Python code used to run it (see [`build-docker-executable.sh`](/deploy-matlab/build-scripts/build-docker-executable.sh))

Steps 1 and 2 do not need to be repeated if the MATLAB or Python code changes.

The output of this process will be a Docker image that contains the MATLAB Runtime, the Python code, and the compiled MATLAB executable.

## Alternative Approaches

MATLAB can also be purely run on it's own in a container - see [`run-matlab-in-container.sh`](/deploy-matlab/build-scripts/run-matlab-in-container.sh)

## Requirements

Compiling the MATLAB code into an executable requires a known Network License Manager, stored as an environment variable `LICENSE_FILE`.


