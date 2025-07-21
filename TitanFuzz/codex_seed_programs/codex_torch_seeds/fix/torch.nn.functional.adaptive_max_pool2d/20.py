'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(1, 1, 10, 10)
output = torch.nn.functional.adaptive_max_pool2d(input, (4, 4))
print(output)
(output, indices) = torch.nn.functional.adaptive_max_pool2d(input, (4, 4), return_indices=True)
print(output)
print(indices)