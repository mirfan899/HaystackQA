### QA with Haystack


Clone and install
```shell
git clone https://github.com/deepset-ai/haystack.git
cd haystack
docker compose up

docker compose up -d haystack-api
docker compose up -d elasticsearch
```

upload text book.
```shell
curl -X POST -H 'Accept: application/json' -F files='@code-of-conduct.txt' http://127.0.0.1:8000/file-upload
curl -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"query": "Permanent Ban?"}' http://127.0.0.1:8000/query
```