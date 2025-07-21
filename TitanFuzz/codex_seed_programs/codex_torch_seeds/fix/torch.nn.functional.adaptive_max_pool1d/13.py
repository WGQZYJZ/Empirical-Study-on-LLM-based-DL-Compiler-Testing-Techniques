'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
input = torch.arange(1, 5, dtype=torch.float32).reshape(1, 1, 4)
output = F.adaptive_max_pool1d(input, 2)
print('input:', input)
print('output:', output)