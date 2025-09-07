The last line is the same as the first one. It does not change at all.


# Usage
We do not recommend running this model on a GPU, because PyTorch implements dynamic memory allocation in C++, and so we can not allocate all of our data on the GPU by default. However, if you are training an LSTM to classify images, it is recommended to run your model on a CPU instead.

1. You need to download the weights of the pre-trained model from [here](https://s3.amazonaws.com/open_source_datasets/transformers/bert/multilingual_BertForSequenceClassification_L-2_H-128_A-8.0.zip).
2. You need to download the `tokenizer.pt` file from [here](https://s3.amazonaws.com/open_source_datasets/transformers/bert/multilingual_BertTokenizer.tar.gz).
3. Uncompress the pre-trained weights of the model, and put all files in a folder named `BERT_MLM`.
4. Put the tokenizer file into `./BERT_MLM/tokenizer.pt`
5. Change the `PATH_TO_WEIGHTS`, `TOKENIZER_FILE`, and `OUTPUT_DIR` variables to match your setups.
6. Run: python src/run.py \
    --model-name bert \
    --output-dir ./BERT_MLM \
    --overwrite \
    --do-train \
    --gradient-accumulation-steps 20 \
    --do-eval \
    --learning-rate 1e-5 \
    --weight-decay 0.01 \
    --max-position-embeddings 16384 \
    --num-train-epochs 3.0 \
    --per-device-train-batch-size 32 \
    --gradient-accumulation-steps 1
7. Open `BERT_MLM/predictions.csv` to see the predictions.


# Notes
* We have not tested the pre-trained models for general applications other than language classification.

