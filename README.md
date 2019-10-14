# UNIT C-3: Exercise: Processing bag files.
## URL for repository:
https://github.com/mistermzx/rh3_bagfile_processor
## Instructions to reproduce result
1. Place .bag files in /data folder
  * amod19-rh3-ex-record-MartinZiranXu.bag
2. Build:
```shell
dts devel build -f --arch amd64
```
3. Run:
```shell
docker run -it --rm  -v ~/Documents/rh3_bagfile_processor:/home -e BAGFILE_PATH=/home/data/amod19-rh3-ex-record-MartinZiranXu.bag -e OUTPUT_PATH=/home/data/amod19-rh3-ex-process-MartinZiranXu.bag duckietown/rh3_bagfile_processor:v1-amd64
```
## Upload to dropbox:
amod19-rh3-ex-process-MartinZiranXu.bag
