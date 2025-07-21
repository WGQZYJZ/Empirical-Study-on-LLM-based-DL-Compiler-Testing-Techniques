'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
embedding = nn.Embedding(10, 3)
print(embedding(input_data))