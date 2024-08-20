FROM fedora

MAINTAINER Kumar Vipin Yadav <kumarvipinyadav369@gmail.com>

RUN ls

WORKDIR /tmp/api_tests

ENTRYPOINT ["/bin/bash"]
