'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5)
print(input)
pool = nn.AdaptiveMaxPool1d(1)
output = pool(input)
print(output)