'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 2, 5, 5, 5)
output_size = (2, 2, 2)
output = F.adaptive_max_pool3d(input, output_size)
print(output)