"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding_bag\ntorch.nn.functional.embedding_bag(input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode='mean', sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.tensor([[1, 2, 3, 0, 0], [4, 5, 0, 0, 0]])
weight = torch.rand(10, 5)
output = F.embedding_bag(input, weight, mode='sum')
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding_bag\ntorch.nn.functional.embedding_bag(input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode='mean', sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None)\n"
import torch
import torch.nn as nn