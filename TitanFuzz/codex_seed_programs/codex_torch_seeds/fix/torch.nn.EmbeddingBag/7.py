"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, include_last_offset=False, padding_idx=None, device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.long)
embedding = nn.EmbeddingBag(num_embeddings=10, embedding_dim=4, sparse=True)
output = embedding(input_data)
print(output)