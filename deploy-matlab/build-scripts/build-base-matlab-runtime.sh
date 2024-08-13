IMAGE_NAME="matlab-runtime"

docker build -f examples/docker-builds/base-matlab-runtime/Dockerfile -t $IMAGE_NAME .