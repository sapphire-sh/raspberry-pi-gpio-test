#!/bin/bash

set -ex

docker run --rm -it -v /dev/mem:/dev/mem --privileged raspberry-pi-gpio-test /bin/bash
