# Run Wenet Speech Training

Navigate to the directory `wenet/examples/pinyin/WenetSpeech/s0`:
```bash
cd wenet/examples/pinyin/WenetSpeech/s0
```

### Commands
*Run data preprocessing & training*
```bash
bash run.sh --stage 0 --stop-stage 4
```

*Stages*
```bash
# creates the data directory & convert to pinyin labels
bash run.sh --stage 0 --stop-stage 0 

# run bpe model & generate dictionary
bash run.sh --stage 1 --stop-stage 1

# [SKIPPED] compute cmvn
bash run.sh --stage 2 --stop-stage 2

# create shards (skipped) & prepare data format
bash run.sh --stage 3 --stop-stage 3

# run training
bash run.sh --stage 4 --stop-stage 4

# evaluation & other stuff
bash run.sh --stage 5 --stop-stage 5
bash run.sh --stage 6 --stop-stage 6
```