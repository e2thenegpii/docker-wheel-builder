# docker-wheel-builder

This project is to create a tool that will natively build arbitrary python wheels are architecture dependent.  I recently ran into a situation where I wanted to have a python wheel for ARM64 in an alpine container.  The wheel developers didn't distribute an ARM64 wheel and nor could I get it to build in alpine, but I could get it to build in ubuntu.  This project intends to solve that problem.

# To Use
    docker build docker-wheel-builder -t builder
    docker run -v ${PWD}/dist:/builder/dist -v ${PWD}/specfile.yaml:/builder/specfile.yaml builder
