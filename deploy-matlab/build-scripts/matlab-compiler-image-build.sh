docker build \
    --build-arg MATLAB_RELEASE=r2024a \
    --build-arg MATLAB_PRODUCT_LIST="MATLAB MATLAB_Compiler MATLAB_Compiler_SDK Statistics_and_Machine_Learning_Toolbox" \
    --build-arg MATLAB_INSTALL_LOCATION="/opt/matlab/R2024a" \
    --build-arg LICENSE_SERVER=${LICENSE_FILE} -t matlab-compiler .