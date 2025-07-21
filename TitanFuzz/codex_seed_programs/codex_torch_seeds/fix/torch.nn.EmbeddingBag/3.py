"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, include_last_offset=False, padding_idx=None, device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.tensor([[1, 2, 0, 3, 2], [1, 0, 0, 0, 0]])
embedding_bag = nn.EmbeddingBag(5, 8)
output_data = embedding_bag(input_data)
print(output_data)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, include_last_offset=False, padding_idx=None, device=None, dtype=None)\n"