'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 5)
output = F.adaptive_max_pool1d(input, output_size=3)
print(output)
'\nTask 4: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=True)\n'
(output, indices) = F.adaptive_max_pool1d(input, output_size=3, return_indices=True)
print(output)
print(indices)