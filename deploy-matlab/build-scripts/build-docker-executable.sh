IMAGE_NAME="matlab-executable"

docker build --build-arg="EXECUTABLE_DIR=executable/" --build-arg="EXECUTABLE=exampleFunction" -f deploy-matlab/docker-builds/deploy-executable/Dockerfile-on-runtime-base -t $IMAGE_NAME .