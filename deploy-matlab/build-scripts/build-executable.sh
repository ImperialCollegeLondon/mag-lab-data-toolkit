
mkdir -p dist

docker run --rm --volume "$(pwd):/external" \
    -e MLM_LICENSE_FILE=${LICENSE_FILE} \
    matlab-compiler -batch \
    "mcc -m -R -nojvm -R -nodisplay /external/deploy-matlab/example-code/matlab/exampleFunction.m -d /external/executable"