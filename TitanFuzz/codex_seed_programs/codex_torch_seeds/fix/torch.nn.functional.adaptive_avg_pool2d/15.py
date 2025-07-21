'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
from torch.nn.functional import adaptive_avg_pool2d
input = torch.randn(1, 1, 5, 5, requires_grad=True)
output = adaptive_avg_pool2d(input, (3, 3))
print('input: ', input)
print('output: ', output)