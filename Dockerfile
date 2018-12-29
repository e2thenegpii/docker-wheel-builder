FROM python
ARG outdir=/builder/dist
COPY . /builder
WORKDIR /builder
RUN pip install --no-cache -r requirements.txt
CMD python -m wheel-builder specfile.yaml -- -w dist
