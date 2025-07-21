'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.long)
embedding = torch.nn.Embedding(10, 3)
output_data = embedding(input_data)
print(output_data)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, per_sample_weights=False, include_last_offset=False, device=None, dtype=None)\n"
import torch
import numpy as np