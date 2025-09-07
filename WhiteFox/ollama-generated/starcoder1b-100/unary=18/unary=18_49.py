
# Requirements for evaluation
- The model can be evaluated on several public PyTorch models. The results of all these models are shown in [this Table](#Model_Evaluation).
- The data for evaluation has already been extracted in the following format:
  - Input tensors
  - Labels


## Model Evaluation
|model name     |loss        |accuracy%  |runtime (s)|
|--------------|------------|------------|------------|
|[Bert](https://huggingface.co/transformers/model_doc/bert.html)           |     0.874359 | 82.14%   | 2.265       |
|[DistilBERT](https://github.com/microsoft/distilbert-pytorch)|     0.885375|80.96%     | 12          |
|[RoBERTa](https://huggingface.co/transformers/model_doc/roberta.html)         |    0.853443  | 78.85%    |  13         |
|[XLM-RoBERTa](https://github.com/huggingface/transformers#xlm)|     0.857976  | 81.24%    |  14         |
|[DistilX LM RoBERTa](https://github.com/huggingface/transformers#xlm-roberta)|  0.839621|79.46%    |  20         |

