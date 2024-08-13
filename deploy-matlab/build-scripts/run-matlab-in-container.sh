docker run --volume "$(pwd):/external" \
    -e MLM_LICENSE_FILE=${LICENSE_FILE} \
    mathworks/matlab:r2024a -batch "cd('/external/examples/matlab'); exampleFunction(5)"