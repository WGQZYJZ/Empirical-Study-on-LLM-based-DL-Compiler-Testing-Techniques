'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
data = torch.tensor([[1, 2, 3], [4, 5, 6]])
embedding = nn.Embedding(num_embeddings=10, embedding_dim=2)
embedding_output = embedding(data)
print(embedding_output)
print(embedding_output.shape)