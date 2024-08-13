# For more information, please refer to https://aka.ms/vscode-docker-python
ARG MATLAB_RUNTIME_ZIP="MATLAB_Runtime_R2024a_Update_5_glnxa64.zip"
ARG MCRROOT="/opt/matlab_runtime"

FROM debian:12-slim AS dev

ARG MATLAB_RUNTIME_ZIP
ARG MCRROOT

RUN adduser -u 9999 --disabled-password --gecos "" matlabuser

COPY dist/${MATLAB_RUNTIME_ZIP} /opt/matlab_zip/

RUN mkdir -p /opt/matlab_runtime

RUN apt-get update && \
    apt-get install unzip && \
    apt-get install libxt6 -y

WORKDIR /opt/matlab_zip

RUN unzip ${MATLAB_RUNTIME_ZIP} && \
    chmod +x install && \
    ./install -agreeToLicense yes -destinationFolder ${MCRROOT} && \
    rm -rf /opt/matlab_zip

WORKDIR ${MCRROOT}

USER matlabuser

FROM python:3.12-slim AS final

ARG MCRROOT

COPY --from=dev / /

ENV LD_LIBRARY_PATH=.:${MCRROOT}/R2024a/runtime/glnxa64:${MCRROOT}/R2024a/bin/glnxa64:${MCRROOT}/R2024a/sys/os/glnxa64:${MCRROOT}/R2024a/sys/opengl/lib/glnxa64

CMD ["/bin/bash"]
