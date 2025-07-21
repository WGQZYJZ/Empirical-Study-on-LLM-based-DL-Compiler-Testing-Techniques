"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, include_last_offset=False, padding_idx=None, device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
data = torch.randint(low=0, high=10, size=(5,), dtype=torch.long)
offsets = torch.tensor([0, 1, 2, 3, 4], dtype=torch.long)
embedding_bag = nn.EmbeddingBag(10, 3, mode='mean')
output = embedding_bag(data, offsets)
print(output)