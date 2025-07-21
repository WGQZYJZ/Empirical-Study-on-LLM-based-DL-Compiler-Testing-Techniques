'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
input = torch.randn(1, 1, 3, 3)
print(input)
output = torch.nn.functional.adaptive_max_pool2d(input, (1, 1))
print(output)
(output, indices) = torch.nn.functional.adaptive_max_pool2d(input, (1, 1), return_indices=True)
print(output)
print(indices)
output = torch.nn.functional.adaptive_max_pool2d(input, (3, 3))
print(output)