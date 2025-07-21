'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.nn.functional import adaptive_max_pool3d
input = torch.randn(1, 10, 10, 10, 10)
output = adaptive_max_pool3d(input, (1, 1, 1))
print(output)