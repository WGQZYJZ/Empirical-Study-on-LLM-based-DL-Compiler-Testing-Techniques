'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding\ntorch.nn.functional.embedding(input, weight, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False)\n'
import torch
input_data = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
embedding_layer = torch.nn.Embedding(10, 3)
embedding_result = embedding_layer(input_data)
print(embedding_result)