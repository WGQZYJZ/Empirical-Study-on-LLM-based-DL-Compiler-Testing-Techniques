'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 10)
output = F.adaptive_max_pool1d(input, 3)
print('input.size() = ', input.size())
print('output.size() = ', output.size())