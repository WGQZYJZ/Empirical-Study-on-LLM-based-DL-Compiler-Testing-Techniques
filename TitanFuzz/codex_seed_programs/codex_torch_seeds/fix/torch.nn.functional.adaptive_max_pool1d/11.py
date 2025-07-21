'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 3)
output = F.adaptive_max_pool1d(input, output_size=2)
print(output)
output_with_indices = F.adaptive_max_pool1d(input, output_size=2, return_indices=True)
print(output_with_indices)