'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 4, 8, 8, 8)
output = F.adaptive_max_pool3d(input, (1, 1, 1))
print(output)
(output, indices) = F.adaptive_max_pool3d(input, (1, 1, 1), return_indices=True)
print(output)
print(indices)