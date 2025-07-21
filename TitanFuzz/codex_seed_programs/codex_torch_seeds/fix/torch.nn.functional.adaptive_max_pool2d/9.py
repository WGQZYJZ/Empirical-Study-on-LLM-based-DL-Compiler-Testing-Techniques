'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
input = torch.arange(0, 20, dtype=torch.float).view(1, 1, 4, 5)
print('Input: ', input)
output = F.adaptive_max_pool2d(input, output_size=3)
print('Output: ', output)