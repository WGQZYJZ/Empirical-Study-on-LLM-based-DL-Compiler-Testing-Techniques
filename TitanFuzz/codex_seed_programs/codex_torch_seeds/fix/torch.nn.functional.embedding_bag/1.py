"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding_bag\ntorch.nn.functional.embedding_bag(input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode='mean', sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None)\n"
import torch
import torch.nn.functional as F
import numpy as np
import torch
input = torch.tensor([[0, 1, 2, 0], [0, 1, 2, 0]])
weight = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
output = F.embedding_bag(input, weight, mode='sum')
print(output)
output = F.embedding_bag(input, weight, mode='mean')
print(output)