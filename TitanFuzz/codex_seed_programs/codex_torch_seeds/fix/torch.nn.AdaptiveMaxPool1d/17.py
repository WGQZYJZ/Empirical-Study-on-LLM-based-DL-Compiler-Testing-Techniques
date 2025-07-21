'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 10)
pool = nn.AdaptiveMaxPool1d(3)
output = pool(input)
print(output)
print(output.shape)
pool = nn.AdaptiveMaxPool1d(3, return_indices=True)
(output, indices) = pool(input)
print(output)
print(output.shape)
print(indices)
print(indices.shape)