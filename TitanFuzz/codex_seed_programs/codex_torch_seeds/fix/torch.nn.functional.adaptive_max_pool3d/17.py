'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
input = torch.randn(1, 1, 6, 6, 6)
output = torch.nn.functional.adaptive_max_pool3d(input, output_size=(2, 2, 2))
print('input: ', input)
print('output: ', output)